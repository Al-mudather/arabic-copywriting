# arabic-copywriting

An agent skill (Claude Code, Codex, Cursor and others) for writing and editing **professional Arabic copy that readers understand on first read and feel understood** — marketing pages, brochures, UI strings, notifications, emails, meeting minutes and reports.

It is not a translator. It makes the agent write from the meaning, then check the result for correctness.

## What it does

- **Clarity first:** bans foreign metaphors, developer jargon and label-and-colon fragments; short verbal sentences; one voice per document.
- **No translationese:** WRONG → RIGHT tables for calques (تمّ + مصدر، قام بـ، من قِبَل، كلما…كلما، سوف لن…) and false friends that flip the meaning (الدافع، غير المرئية، لا يجب، تخفيض، تحميل…).
- **Correctness:** punctuation (، ؛ ؟ «»), hamza, ة/ه، ى/ي، tanween, number–noun agreement, verb + preposition pairs — grounded in Ahmad Zaki Pasha, Ahmad Mukhtar Omar and the Cairo Arabic Language Academy.
- **Persuasion without the American accent:** how to adapt frameworks like Alex Hormozi's value equation into natural Arabic, with examples from Careem, Tabby, Tamara and Talabat.
- **A failure log** that grows with every document, so the same mistake is never made twice.
- **A built-in linter** (`scripts/arabic_lint.py`, Python 3, no dependencies) for HTML, Markdown, text and JSON.

Some glossary entries are specific to Medsera (an Arabic medical-education platform); the rules apply to any Arabic product.

## Install

```bash
npx skills add Al-mudather/arabic-copywriting@arabic-copywriting -g -y
```

Or in Claude Code:

```
/plugin marketplace add Al-mudather/arabic-copywriting
```

## Use

Just ask for Arabic. The skill triggers whenever the output contains Arabic sentences, when you ask to rewrite or review Arabic, or when Arabic "sounds translated".

Check a file:

```bash
python3 skills/arabic-copywriting/scripts/arabic_lint.py page.html
```

## How it was tested

The same rejected 20-page brochure was rewritten with this skill and with `fasaha` + `humanizer-ar-msa`, then judged blind. This skill won on clarity (8 vs 6) and trust (8 vs 6); the other pipeline won on grammar (8 vs 7). The best of both was merged back into this skill.

---

# مهارة كتابة المحتوى العربي

مهارة لوكلاء الذكاء الاصطناعي تكتب نصوصًا عربية احترافية يفهمها القارئ من أول قراءة ويشعر أن كاتبها يفهمه: صفحات تسويقية، وكتيّبات، ونصوص التطبيقات، ومحاضر الاجتماعات.

لا تترجم كلمة بكلمة. تكتب من المعنى أولًا، ثم تراجع النحو والإملاء وعلامات الترقيم، ومعها أداة فحص تلقائية للنص العربي.

## التثبيت

```bash
npx skills add Al-mudather/arabic-copywriting@arabic-copywriting -g -y
```

الترخيص: MIT
