# Grammar, spelling and punctuation for professional Arabic

## Contents
1. Punctuation (mark by mark, typography, run-on sentences)
2. Spelling (hamza, ة/ه, ى/ي, ال, tanween, numbers, typos)
3. Grammar errors that show on the page
4. Pre-publish checklist
5. Sources

Marks: **[standard]** = uniform across reference books; **[contested]** = authorities disagree; the recommended form is the one nobody objects to.

---

## 1. Punctuation (علامات الترقيم)

Ahmad Zaki Pasha introduced modern Arabic punctuation in «الترقيم وعلاماته في اللغة العربية» (1912/1913): marks placed "to fix places of separation, stopping and starting, tones of voice and speech purposes during reading". Two core rules from the Arabic Language Encyclopedia: no space before a mark; don't stack marks (except ؟!).

### 1.1 Mark by mark

| Mark | Name | Use it for | Don't |
|---|---|---|---|
| ، | الفاصلة | short connected clauses forming one idea; list items; after a vocative («يا دكتور أحمد،»); after نعم/لا; between a long condition and its answer | between subject and predicate, verb and object, noun and adjective, مضاف and مضاف إليه; before every و |
| ؛ | الفاصلة المنقوطة | between two sentences where the second is the cause/result of the first («تأجّل الامتحان؛ لأنّ القاعة غير جاهزة»); between long list items that contain commas | overuse — in marketing a full stop is usually better [contested] |
| : | النقطتان | after a quoting verb («قال المحاضر:»); before a list, example, definition | as a headline device inside prose («الخبر السار: …»); more than once per sentence |
| . | النقطة | end of every complete sentence; abbreviations (د. أحمد، أ.د.) | after headings and buttons |
| ؟ | الاستفهام | direct questions | indirect questions: «سألته عن موعد الامتحان.» |
| ! | التعجب | real exclamation, warnings, strong appeals | repeated (!!!); in minutes/docs; more than once per screen in marketing |
| « » | التنصيص | exact quotes, titles, coined terms on first use | mixing with "" in one document |
| ( ) | القوسان | short explanations, abbreviations, English term on first mention: «الأيض (Metabolism)» | whole sentences — make a new sentence |
| — | الشرطة | a parenthetical clause between two dashes (جملة معترضة) | instead of a colon or comma; more than one pair per paragraph |
| … | الحذف | omitted text in a quote; a deliberately trailing thought | four or more dots; filler at the end of slogans |

### 1.2 Typography
1. Use Arabic glyphs ، (U+060C)، ؛ (U+061B)، ؟ (U+061F). Never Latin `, ; ?` inside Arabic text.
2. No space before a mark, one after. No space inside «» or ( ): «كذا» not « كذا ». Prefixes never get a space: «وقال»، «بالمستشفى» — not «و قال»، «ب الإضافة».
3. Quotes: «» in published copy; pick one style per product.
4. Arabic lists: «أ، وب، وج» or «أ، ب، وج». Don't copy the English serial comma pattern «أ، ب، و ج».
5. English words inside Arabic: punctuation after them is Arabic punctuation. Numbers run LTR inside RTL (W3C alreq). If a mark jumps sides in the UI, it's bidi rendering — fix with markup (`<bdi>`, RLM), not by rewording. % and currency signs sit to the number's left; ° to its right.
6. Digits: one family per product. Medsera uses Western 0–9.
7. No tatweel (ـــ) stretching in body text.

### 1.3 The comma-chain run-on
The most visible weakness of machine Arabic: 40–80 words glued with commas and و. Rules: one idea per sentence; ≲25 words in marketing, ≲30 in docs. Arabic links sentences with conjunctions that show the relation (فـ، ثمّ، لكنّ، إذ، لذا) — or ends them.

- ❌ «تقدّم المنصة دورات متخصصة، وتضم نخبة من الأطباء، ويمكنك التسجيل الآن، والدفع بالبطاقة، وستحصل على شهادة، كما يمكنك…»
- ✅ «تقدّم المنصة دورات متخصصة يقدّمها أطباء ذوو خبرة. سجّل الآن وادفع بالبطاقة، واحصل على شهادتك عند الإتمام.»

---

## 2. Spelling (الإملاء)

### 2.1 Hamza
**همزة الوصل (no hamza drawn)** [standard]: imperative of 3-letter verbs (اكتب، اقرأ); past, imperative and masdar of 5- and 6-letter verbs (انطلق/انطلاق، اجتمع/اجتماع، استخدم/استخدام، ابتكر/ابتكار، اختبر/اختبار); the nouns اسم، ابن، ابنة، امرؤ، امرأة، اثنان، اثنتان; the article ال.
Top professional error: ❌ إستخدام، إجتماع، إنطلاق، إبتكار، إختبار، إستمرار، إنتظار ← ✅ without hamza.

**همزة القطع (hamza drawn)**: 4-letter verbs and their masdar (أرسل/إرسال، أعدّ/إعداد، أكمل/إكمال), particles (إنّ، أنّ، إلى، إذا). Test: put و before it — if the hamza is still pronounced (وَأرسل), it's قطع.

**Medial hamza**: seat follows the strongest vowel (كسرة > ضمة > فتحة > سكون): رئيس، سُئل، سؤال، مسألة، بيئة، هيئة.
[contested] Egypt writes مسئول/شئون; Gulf and Damascus write مسؤول/شؤون. For a pan-regional audience use **مسؤول/شؤون** and never mix.

**Final hamza** follows the preceding vowel: قرأ، تباطؤ، شاطئ. After sukun it's on the line: جزء، عبء، أداء، دواء. With tanween: جزءًا، شيئًا، عبئًا؛ after a long alif no extra alif: سماءً، دواءً.

### 2.2 ة vs ه
Say the word as if more text follows. If you hear «ت», write ة (مدرسة، دورة، جلسة). The pronoun "his" is always ه (كتابه). ❌ الدوره، المكتبه.

### 2.3 ى vs ي
ى: إلى، على، حتى، مستشفى، مستوى. ي: في، الذي، التي، يمشي. Egyptian typing habit of undotted final ى (فى، الذى، علي for على) is wrong in standard print — normalise it.

### 2.4 ال
The ل is always written, even when silent: الطبيب، الدواء. After لِـ the alif drops: للطبيب. If the word starts with ل, two lams remain: «لليل».

### 2.5 Tanween al-fath
Modern print puts it on the letter before the alif: كتابًا، شكرًا، أيضًا، جدًّا (older كتاباً also seen — pick one; Medsera uses ًا). No alif after ة, after ء that follows an alif, or after ى: عادةً، فرصةً، سماءً، هدًى. ❌ عادتاً، فرصتاً.

### 2.6 Numbers and dates in copy
Digits: «12 درسًا»، «9 نوفمبر 2026». Month names يناير … ديسمبر for Gulf/Egypt/Sudan. مئة preferred over مائة (be consistent). Ranges: «من 3 إلى 5 أيام», or «3–5 أيام» in tables.

### 2.7 Frequent typos
| ❌ | ✅ |
|---|---|
| لاكن، هاذا، ذالك | لكن، هذا، ذلك |
| إنشاء الله | إن شاء الله |
| مسئولية and مسؤولية mixed | one system |
| و قال، ب الإضافة | وقال، بالإضافة |

---

## 3. Grammar errors that show on the page

### 3.1 العدد والمعدود [standard]
- 1–2: agrees or is dropped: طبيب واحد، طبيبان.
- 3–10: opposite gender, plural genitive noun: ثلاثة أطباء، ثلاث طبيبات، ستة أسابيع (أسبوع is masculine → ستة).
- 11–99: singular accusative noun: أحد عشر طبيبًا، خمس وعشرون جلسةً.
- 100/1000: singular genitive: مئة طبيب، ألف مشترك.
- Numbers ending in 01/02 take the form of 1/2 for the noun after the hundreds/thousands: 1,301 → «فحصٍ», «1,302 فحصين» — or rephrase («اختبرنا النظام 1,301 مرة»).
- **With digits in copy**: 3–10 + plural («5 دورات»), 11–99 + singular with tanween («25 طبيبًا»), 100+ + singular («300 سؤال»). Ordinals agree: «الدفعة الثالثة»، «المستوى الثالث».
- Zero: rephrase («لا يوجد طلاب»). Two: dual («امتحانان»، «شهران»).

### 3.2 Agreement
- Non-human plurals take feminine singular: «الدورات متاحة»، «الملفات التي رفعتها» — not متاحون / الذين.
- Verb before a plural subject stays singular: ❌ حضروا الأطباء ← ✅ حضر الأطباء.
- Feminine subject: «قالت الطبيبة»، «تبدأ الدورة». Brand names treated as feminine stay feminine: «ميدسيرا تجمع».
- السوق is usually feminine: «السوق ما زالت».

### 3.3 كان وأخواتها / إنّ وأخواتها
- كان، أصبح، صار، ليس، ظلّ، ما زال → predicate accusative: ❌ أصبح المحتوى متاح ← ✅ متاحًا؛ ❌ ليس الأمر سهل ← ✅ سهلًا؛ ❌ كان الأطباء حاضرون ← ✅ حاضرين.
- إنّ، أنّ، لكنّ → subject accusative, even when it comes after the predicate: ❌ إنّ لدينا خبر سار ← ✅ خبرًا سارًّا.

### 3.4 الأسماء الخمسة
ذو (nom.) / ذا (acc.) / ذي (gen.): «طبيب ذو خبرة»، «اخترنا طبيبًا ذا خبرة»، «لطبيب ذي خبرة». Plural ذوو / ذوي, feminine ذات. ❌ أطباء ذو خبرة ← ✅ ذوو خبرة.

### 3.5 جمع المذكر السالم and the dual
ون (nom.) / ين (acc./gen.): «شارك المتدربون»، «رأيت مهندسين». In إضافة the ن drops: ❌ مشرفين الدورة ← ✅ مشرفو الدورة / مشرفي الدورة. Dual: «طبيبا الطوارئ».

### 3.6 Visible accusative objects
❌ نقدّم شرح مفصل ← ✅ نقدّم شرحًا مفصّلًا. ❌ 12 درس ← ✅ 12 درسًا. A missing tanween on an object looks careless.

### 3.7 Other common slips
- «نفس الشيء» → «الشيء نفسه» (safer).
- «لا يجب» = must not. For "don't have to" use «لا يلزم»، «ليس عليك».
- «إلا أنّ» / «غير أنّ» rather than English-style «ولكن» chains.

---

## 4. Pre-publish checklist

Run `scripts/arabic_lint.py` for most of these; check the rest by eye.

**Punctuation**
1. No Latin `, ; ?` between Arabic letters.
2. No space before ، ؛ : . ؟ !
3. No detached «و » before a word.
4. No `!!` and no `....`.
5. One quote style («»).
6. No sentence over ~30 words or with 4+ commas.
7. ≤1 colon per sentence; ≤1 pair of dashes per paragraph.

**Spelling**
8. Hamza on وصل words (إستخدام، إجتماع…) removed.
9. فى/الذى/علي (for على) normalised.
10. No تاً / ةاً.
11. No ه at the end of feminine nouns (الدوره).
12. One hamza system for مسؤول/شؤون.

**Grammar**
13. Every number + noun checked (3–10 plural, 11–99 singular + ًا, 100+ singular).
14. Every كان/أصبح/ليس/ظلّ/إنّ/لكنّ: visible endings checked.
15. Non-human plurals → feminine singular agreement and «التي».
16. ذو/ذا/ذي/ذوو/ذات agree.
17. Dropped ن in إضافة (مشرفو، مدرّسي).

**Final**
18. Read aloud. Out of breath → split. Sounds dubbed → rewrite from meaning.

---

## 5. Sources
- Ahmad Zaki Pasha, «الترقيم في اللغة العربية»: https://ar.wikisource.org/wiki/الترقيم_في_اللغة_العربية
- Arabic Language Encyclopedia (punctuation): https://dorar.net/arabia/2669 · https://dorar.net/arabia/2672 · https://dorar.net/arabia/2702
- Cairo Arabic Language Academy decisions (PDF): https://www.nu.edu.ye/wp-content/uploads/2014/01/قرارات-مجمع-اللغة-العربية-بالقاهرة.pdf
- Ahmad Mukhtar Omar, «معجم الصواب اللغوي»: https://arabiclexicon.hawramani.com/ahmad-mukhtar-umar-mujam-al-sawab-al-lughawi/
- Ahmad Mukhtar Omar, «أخطاء اللغة العربية المعاصرة عند الكتّاب والإذاعيين» (عالم الكتب)
- Muhammad al-Adnani, «معجم الأخطاء الشائعة» (مكتبة لبنان); Mustafa Jawad, «قل ولا تقل»
- Hazem Alsanad, punctuation in Arabic vs English legal drafting (KSAA, 2022): https://faculty.ksu.edu.sa/ar/halsanad/publication/439562
- W3C Arabic & Persian Layout Requirements: https://www.w3.org/TR/alreq/
