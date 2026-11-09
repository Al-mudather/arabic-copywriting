#!/usr/bin/env python3
"""Mechanical checks for professional Arabic copy.

Usage:
    python3 arabic_lint.py <file> [<file> ...] [--max-sentence 30] [--quiet-info]

Accepts .html/.htm (tags stripped), .md, .txt and .json (string values only).
Each hit is a prompt to look, not an automatic error. Exit code 1 if any
'error' level hit is found, else 0.
"""
import html
import json
import re
import sys
from pathlib import Path

AR = "؀-ۿ"  # Arabic block
AR_LETTER = f"[{AR}]"

# (level, code, regex, message)
RULES = [
    # --- punctuation / typography ---
    ("error", "latin-comma", re.compile(rf"(?<={AR_LETTER}),|,(?=\s*{AR_LETTER})"), "Latin comma inside Arabic -> use «،»"),
    ("error", "latin-semicolon", re.compile(rf"(?<={AR_LETTER});|;(?=\s*{AR_LETTER})"), "Latin semicolon inside Arabic -> use «؛»"),
    ("error", "latin-question", re.compile(rf"(?<={AR_LETTER})\?"), "Latin question mark after Arabic -> use «؟»"),
    ("error", "space-before-punct", re.compile(r"\s+[،؛:؟!.](?=\s|$)"), "space before punctuation"),
    ("error", "detached-waw", re.compile(rf"(?:(?<=\s)|^)و\s+(?={AR_LETTER}{{2,}})"), "detached «و » — attach it to the next word"),
    ("warn", "double-bang", re.compile(r"[!！]{2,}|؟!{2,}"), "repeated exclamation marks"),
    ("warn", "long-ellipsis", re.compile(r"\.{4,}"), "more than three dots"),
    ("warn", "mixed-quotes", re.compile(rf'"[^"\n]*{AR_LETTER}[^"\n]*"'), 'straight quotes around Arabic -> prefer «»'),
    ("warn", "space-inside-quotes", re.compile(r"«\s|\s»"), "space inside «»"),
    ("warn", "serial-comma", re.compile(r"،\s+و\s"), "«، و » — Arabic lists attach و to the word («، وكذا»)"),
    # --- spelling ---
    ("error", "hamza-on-wasl", re.compile(r"(?:^|(?<=[\s«(\"'و]))إ(?:ست|جت|خت|نت|نط|بت|شت|تص|تف|تب|تح|حت|عت|قت|كت|لت|مت|نض|زد|ضط|طر)[" + AR + r"]{2,}"), "possible همزة قطع on a همزة وصل word (إستخدام، إجتماع…)"),
    ("error", "ta-tanween", re.compile(r"(?:تاً|ةاً|ةً?ا(?=\s|$))"), "wrong tanween spelling on ة (عادتاً -> عادةً)"),
    ("error", "undotted-ya", re.compile(r"(?:^|(?<=\s))(?:فى|الذى|التى|إلى\S*ى\b)(?=\s|$)"), "undotted final ى (فى/الذى -> في/الذي)"),
    ("warn", "insha-allah", re.compile(r"إنشاء الله"), "«إنشاء الله» -> «إن شاء الله»"),
    ("warn", "masoul-mixed", re.compile(r"مسئول|شئون"), "«مسئول/شئون» — use «مسؤول/شؤون» for a pan-regional audience"),
    # --- translationese ---
    ("warn", "tamma", re.compile(r"(?:^|(?<=[\s«(]))(?:و|ف)?(?:تمّ|تم|يتمّ|يتم|سيتم|ستتم|تتم)\s+[" + AR + r"]+"), "«تمّ + مصدر» — use an active verb or true passive"),
    ("warn", "qama-bi", re.compile(r"(?:قام|قامت|يقوم|تقوم|قم|قوموا)\s+ب[" + AR + r"]+"), "«قام بـ + مصدر» — use the verb directly"),
    ("warn", "min-qibal", re.compile(r"من\s+قِ?بَ?لِ?"), "«من قِبَل» passive agent — rewrite actively"),
    ("warn", "kullama-twice", re.compile(r"كلما[^.؟!\n]{1,80}كلما"), "«كلما… كلما» — don't repeat كلما"),
    ("error", "sawfa-lan", re.compile(r"سوف\s+لن"), "«سوف لن» -> «لن»"),
    ("warn", "hamm", re.compile(r"(?:^|(?<=\s))(?:هام|هامة|هامّ|هامّة)(?=\s|[،.؟!]|$)"), "«هام» — prefer «مهمّ»"),
    ("warn", "tawajud", re.compile(r"(?:يتواجد|تتواجد|متواجد|متواجدة|متواجدون|التواجد)"), "«تواجد» — prefer يوجد/حاضر/يكون"),
    ("warn", "bittali", re.compile(r"وبالتالي|بالتالي"), "«بالتالي» — prefer لذا / ومن ثمّ / فـ"),
    ("warn", "yalab-dawr", re.compile(r"(?:يلعب|تلعب|لعب)\s+دور"), "«يلعب دورًا» — prefer يؤدّي دورًا / يُسهم"),
    ("warn", "more-than-great", re.compile(r"أكثر من رائع"), "«أكثر من رائع» calque"),
    ("info", "bishakl", re.compile(r"بشكل\s+[" + AR + r"]+|بطريقة\s+[" + AR + r"]+"), "«بشكل/بطريقة + صفة» — often better as a masdar or adverb"),
    ("warn", "laysa-faqat", re.compile(r"ليس\s+فقط"), "«ليس فقط… بل أيضًا» calque"),
    ("info", "haythu", re.compile(r"(?:^|(?<=\s))(?:و)?حيث(?=\s)"), "«حيث» as a connector — max one per ~300 words"),
    ("info", "baynama", re.compile(r"(?:^|(?<=\s))(?:و)?بينما(?=\s)"), "«بينما» — max one per ~300 words; consider أمّا… فـ / في حين"),
    ("warn", "end-of-day", re.compile(r"في نهاية اليوم"), "«في نهاية اليوم» calque"),
    ("warn", "ijabi-salbi", re.compile(r"(?:إيجابي|سلبي)(?:ة)?(?=\s|[،.]|$)"), "«إيجابي/سلبي» — often a calque (keep for test results)"),
    ("warn", "khass-bik", re.compile(r"ال[" + AR + r"]+\s+الخاص(?:ة)?\s+ب(?:ك|كم|ي|نا)\b"), "«… الخاص بك» — use an attached pronoun"),
    ("warn", "binajah", re.compile(r"بنجاح"), "«بنجاح» — usually redundant in UI/copy"),
    ("info", "ka-as", re.compile(r"(?:^|(?<=\s))ك(?:طبيب|مرشد|مسوّق|مسوق|أستاذ|مدرّس|مدرس|عضو|مشترك|طالب|مدير|قيمة|مسودة|مسودات)[" + AR + r"]*"), "«كـ» meaning 'as' — consider بصفته / بوصفه"),
    ("info", "signpost", re.compile(r"من الجدير بالذكر|تجدر الإشارة|في هذا السياق"), "signposting padding — delete and state the fact"),
    # --- prepositions and common slips (from the 2026-11-09 blind test) ---
    ("warn", "ajaba-an", re.compile(r"(?:يجيب|تجيب|أجاب|أجابت|أجب|أجبت|نجيب|يجيبون)\s+(?:ال)?(?:سؤال|أسئلة|السؤال|الأسئلة)"), "«أجاب السؤال» — the verb takes «عن»: «أجاب عن السؤال»"),
    ("info", "yahtaj-ila", re.compile(r"(?:يحتاج|تحتاج|نحتاج|يحتاجون|احتاج)\s+(?!إلى|إليه|إليها|إليك|إليهم|ل|أن|ان)[" + AR + r"]{3,}"), "«يحتاج + اسم» — usually «يحتاج إلى»"),
    ("warn", "biba3diha", re.compile(r"ببعضها|ببعضهم(?!\s+ب)"), "«ببعضها» — prefer «بعضها ببعض»"),
    ("warn", "yatafaja", re.compile(r"(?:يتفاجأ|تتفاجأ|يتفاجؤون|تفاجأ|تفاجئ)"), "«يتفاجأ» — prefer «يُفاجأ»"),
    ("info", "absolute-claim", re.compile(r"لا\s+(?:توجد|يوجد)\s+(?:أي|حتى الآن)|الوحيدة?\s+في|الأفضل\s+في\s+(?:العالم|المنطقة)"), "absolute claim — soften unless you can prove it («لم نجد بعد…»)"),
    ("info", "alawa", re.compile(r"علاوة على ذلك"), "«علاوة على ذلك» — correct, but a common AI tell when repeated; vary or cut"),
    # --- false friends ---
    ("error", "false-friend-dafi", re.compile(r"(?:العضو|الأعضاء|أعضاء|عضو)\s+(?:ال)?داف(?:ع|عين|عون)"), "«العضو الدافع» = motivating member -> «المشترك»"),
    ("error", "false-friend-invisible", re.compile(r"(?:الأسئلة|أسئلة)\s+(?:غير\s+)?المرئية"), "«الأسئلة غير المرئية» = invisible -> «التي لم يحلّها»"),
    ("warn", "false-friend-layajib", re.compile(r"لا\s+يجب"), "«لا يجب» = must not; for 'don't have to' use «لا يلزم / ليس عليك»"),
    ("warn", "false-friend-tahmil", re.compile(r"(?:تحميل|حمّل|حمل)\s+(?:ال)?(?:ملف|ملفات|كتاب|كتب|فيديو)"), "«تحميل» is read as download — for upload use «رفع»"),
    ("info", "false-friend-tahwil", re.compile(r"مسار التحويل|نسبة التحويل"), "«التحويل» reads as bank transfer — say «تحوّل المهتمين إلى مشتركين»"),
    # --- dialect ---
    ("warn", "dialect", re.compile(r"(?:^|(?<=\s))(?:الحين|دلوقتي|دلوقت|هسي|هسع|كده|كدا|عشان|علشان|إيش|ايش|ليش|مش|مو|زي|بتاع|بتاعة|شغلانة|مصاريف|على كيفك|يا بطل|يا شاطر)(?=\s|[،.؟!]|$)"), "dialect word — allowed only inside a quote"),
    # --- foreign metaphors and abstractions ---
    ("warn", "metaphor", re.compile(r"(?:جيش|الجيش|وقود|الوقود|محرّك|محرك|المجهر|مجهر|عدسة|الرافعة|بوابات|بوابة الإتقان|غرفة غرفة|خريطة البيت|مشكلة بيت)"), "foreign metaphor — say the plain meaning (unless literal)"),
    ("info", "abstract", re.compile(r"(?:رحلة|رحلتك|تمكين|مكّن|آفاق|استثنائي|استثنائية|التميّز|التميز|حلول مبتكرة|نقلة نوعية)"), "abstract word — follow it with a concrete fact or delete it"),
    ("info", "jargon", re.compile(r"(?:مفتاح تشغيل|الخادم|ثقة النموذج|وضع المعايرة|المعايرة|الإشارات متعارضة|مستحق اليوم|فلتر|داشبورد|بوست|كورس|المنتور)"), "product/developer jargon or loanword — describe what happens to the person"),
    # --- English tokens with Arabic glued on ---
    ("error", "glued-latin", re.compile(r"(?:ال|بال|لل|وال|كال)ـ?\s?(?=[A-Za-z])|(?<=[A-Za-z])(?:ك|كم|ها|نا)\b"), "Arabic article/suffix glued to a Latin word («الـOET») — rephrase («امتحان OET»)"),
]

TAG_RE = re.compile(r"<(script|style)[^>]*>.*?</\1>|<[^>]+>", re.S | re.I)
SENT_SPLIT = re.compile(r"(?<=[.؟!])\s+|\n+")


def extract_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    suf = path.suffix.lower()
    if suf in (".html", ".htm"):
        raw = re.sub(r"</(p|li|h\d|div|td|th|tr|section|br)\s*>|<br\s*/?>", "\n", raw, flags=re.I)
        raw = html.unescape(TAG_RE.sub("", raw))
    elif suf == ".json":
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return raw
        out = []

        def walk(x):
            if isinstance(x, dict):
                for v in x.values():
                    walk(v)
            elif isinstance(x, list):
                for v in x:
                    walk(v)
            elif isinstance(x, str):
                out.append(x)

        walk(data)
        raw = "\n".join(out)
    return raw


def lint(path: Path, max_sentence: int, quiet_info: bool):
    text = extract_text(path)
    lines = [ln.strip() for ln in text.splitlines()]
    hits = []
    for i, line in enumerate(lines, 1):
        if not line or not re.search(AR_LETTER, line):
            continue
        for level, code, rx, msg in RULES:
            if quiet_info and level == "info":
                continue
            for m in rx.finditer(line):
                if code == "hamza-on-wasl" and re.match(r"إ(?:نتاج|نترنت|متاع|طار)", m.group(0).lstrip("«(\"'و")):
                    continue
                frag = line[max(0, m.start() - 18): m.end() + 18]
                hits.append((level, code, i, msg, frag))
        # sentence-level checks
        for sent in SENT_SPLIT.split(line):
            if not re.search(AR_LETTER, sent):
                continue
            words = sent.split()
            if len(words) > max_sentence:
                hits.append(("warn", "long-sentence", i, f"sentence of {len(words)} words (> {max_sentence}) — split it", sent[:70] + "…"))
            if sent.count("،") >= 4:
                hits.append(("warn", "comma-chain", i, "4+ commas in one sentence — likely a run-on", sent[:70] + "…"))
            if sent.count(":") >= 2:
                hits.append(("warn", "colon-overuse", i, "two colons in one sentence", sent[:70] + "…"))

    ar_words = len(re.findall(rf"{AR_LETTER}+", text))
    colon_lines = sum(1 for ln in lines if ":" in ln and re.search(AR_LETTER, ln))
    return hits, ar_words, colon_lines


def main(argv):
    max_sentence = 30
    quiet_info = False
    files = []
    it = iter(argv)
    for a in it:
        if a == "--max-sentence":
            val = next(it, None)
            if val is None or not val.isdigit():
                print("--max-sentence needs a number", file=sys.stderr)
                return 2
            max_sentence = int(val)
        elif a == "--quiet-info":
            quiet_info = True
        else:
            files.append(a)
    if not files:
        print(__doc__)
        return 2
    any_error = False
    for f in files:
        p = Path(f)
        if not p.exists():
            print(f"missing: {f}", file=sys.stderr)
            any_error = True
            continue
        hits, ar_words, colon_lines = lint(p, max_sentence, quiet_info)
        counts = {}
        for h in hits:
            counts[h[0]] = counts.get(h[0], 0) + 1
        print(f"\n== {f}  ({ar_words} Arabic words, {colon_lines} lines with a colon)")
        by_code = {}
        for h in hits:
            by_code.setdefault((h[0], h[1], h[3]), []).append(h)
        order = {"error": 0, "warn": 1, "info": 2}
        for (level, code, msg), items in sorted(by_code.items(), key=lambda kv: (order[kv[0][0]], -len(kv[1]))):
            print(f"\n[{level}] {code} ×{len(items)} — {msg}")
            for _, _, ln, _, frag in items[:6]:
                print(f"   L{ln}: …{frag}…")
            if len(items) > 6:
                print(f"   (+{len(items) - 6} more)")
        per300 = lambda c: round(c / max(ar_words, 1) * 300, 1)
        tam = sum(1 for h in hits if h[1] in ("tamma", "qama-bi"))
        print(f"\nsummary: {counts.get('error', 0)} errors, {counts.get('warn', 0)} warnings, {counts.get('info', 0)} info"
              f" · تمّ/قام بـ per 300 words: {per300(tam)} (target 0)")
        if counts.get("error"):
            any_error = True
    return 1 if any_error else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
