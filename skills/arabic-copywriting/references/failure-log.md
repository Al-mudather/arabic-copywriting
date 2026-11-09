# Arabic failure log (accumulating)

Real mistakes caught in Medsera copy, so the same mistake is never made twice. Idea borrowed from fasaha's `llm-failure-log.md`.

**How to use it:** read it before a correctness pass. When you catch a pattern that is genuinely new (not already here or in `translationese.md`), append one entry using the schema. One entry per new pattern, never one per run. Never delete entries; mark them RESOLVED instead.

## Entry schema

```
## YYYY-MM-DD — <short title>
- bad: <the wrong Arabic>
- good: <the corrected Arabic>
- type: metaphor | jargon | false friend | calque | grammar | preposition | punctuation | bidi | register | claim | ambiguity
- note: <why it failed / how to spot it next time>
```

## Entries

## 2026-11-09 — «الدافع» for a paying member
- bad: «رسالة لطيفة للعضو الدافع الذي انقطع»، «9 أعضاء دافعين»
- good: «رسالة تذكير للمشترك الذي انقطع»، «9 مشتركين»
- type: false friend
- note: دافع = motive / pusher. The paying member is «المشترك».

## 2026-11-09 — «غير المرئية» for unseen questions
- bad: «اختيار الأسئلة غير المرئية أولًا»
- good: «تظهر له أولًا الأسئلة التي لم يحلّها»
- type: false friend
- note: مرئي = visible. Describe the action instead.

## 2026-11-09 — «لا يجب» for "don't have to"
- bad: «أنت طبيب، لست مسوّقًا. ولا يجب أن تكون»
- good: «أنت طبيب لا مسوّق، ولا يلزمك أن تصبح مسوّقًا»
- type: false friend
- note: «لا يجب» is read as "must not".

## 2026-11-09 — «بيعة» for a sale
- bad: «أول بيعة قد تأتي هنا»
- good: «قد تأتي أول عملية بيع هنا»
- type: false friend
- note: بيعة = oath of allegiance.

## 2026-11-09 — the house metaphor
- bad: «هذه ليست مشكلة تدريس. إنها مشكلة بيت.» / «مشكلتك في البيت.»
- good: «مشكلتك ليست في التدريس، بل في أن أدواتك مبعثرة.»
- type: metaphor
- note: Read literally as a family/housing problem. A blind judge flagged it as the single most confusing line.

## 2026-11-09 — status chip glued to the sentence
- bad: «يتولاه حاليًا فريق ميدسيرا معك مع فريق ميدسيرا.» / «تقارير الإيرادات… يتولاه فريقنا»
- good: «…يعدّها فريقنا ويشاركها معك.» with the chip kept as a separate label
- type: grammar
- note: When a UI chip sits after a sentence in the PDF text, the text reads twice or the chip's verb disagrees with the plural noun. Write the sentence so it is complete without the chip.

## 2026-11-09 — «اسأل مجتمعك» for "ask about your community"
- bad: «المساعدون: اسأل مجتمعك بالعربي»
- good: «اسأل عن مجتمعك بالعربية»
- type: preposition
- note: Without «عن» it means asking the members themselves.

## 2026-11-09 — «نجح/رسب» for a single answer
- bad: «محظوظ: نجح بالصدفة، وسيرسب بالصدفة»
- good: «أصاب بالصدفة، وسيخطئ بالصدفة»
- type: ambiguity
- note: The grid is about one answer, not the exam result. Use the verb that matches the unit.

## 2026-11-09 — «تعلّم» without context
- bad: «تعلّم الإجابة الصحيحة كـ«مقبولة»»
- good: «تحدّد الإجابة المعتمدة»
- type: ambiguity
- note: Undiacritized «تعلّم» reads as "you learn". Prefer a verb with one reading.

## 2026-11-09 — closing line that reverses the meaning
- bad: «…وتنام في الثالثة فجرًا.» / «تكون نائمًا لا تردّ على الرسائل»
- good: «وفي الثالثة فجرًا تنام مطمئنًا، لأن الجواب صار في متناول طالبك.»
- type: ambiguity
- note: First version means "you go to bed at 3 a.m."; second sounds like ignoring students. Read endings for the reader's emotion, not just the literal meaning.

## 2026-11-09 — absolute market claim
- bad: «ولا توجد حتى الآن منصة عربية واحدة تجمع هذا التحضير»
- good: «لم نجد بعد منصة عربية تجمع هذا التحضير في مكان واحد»
- type: claim
- note: One reader who knows a rival stops trusting the whole document.

## 2026-11-09 — missing obligatory prepositions
- bad: «يحتاج معلومة»، «تجيب السؤال»، «ببعضها»، «يتفاجأ»
- good: «يحتاج إلى معلومة»، «تجيب عن السؤال»، «بعضها ببعض»، «يُفاجأ»
- type: preposition
- note: fasaha caught these where our first pass didn't. Check verb + preposition pairs on every pass.

## 2026-11-09 — Latin product name split across lines
- bad: a Latin name such as «Oxford Handbook» or «Open Tilawa» breaking between its words at a line end
- good: `<bdi style="white-space:nowrap">Oxford Handbook</bdi>`
- type: bidi
- note: From fasaha's log. In HTML, wrap multi-word Latin names in `<bdi>` with nowrap.

## 2026-11-09 — gendered حال/adjective left in a brochure personalised for a named reader
- bad: «إن لم تكن جاهزًا للإطلاق»، «تدخله مرشدًا وطالبًا»، «وفي الثالثة فجرًا تنام مطمئنًا»، «أنت طبيب لا مسوّق» (in a guide dedicated «إلى د. سلمى»)
- good: «وإن لم يحن وقت الإطلاق بعد»، «تدخله بحساب المرشد وبحساب الطالب»، «وفي الثالثة فجرًا يجد طالبك الجواب في دروسك دون أن يوقظك»، «مهمتك التدريس لا التسويق»
- type: register
- note: The generic «أنت» verbs pass, but accusative adjectives and nouns about the reader (جاهزًا، مطمئنًا، طبيب) visibly mark gender and clash with the dedication. When a document names its reader, grep for ًا-adjectives describing «أنت» and rewrite them as a verb, a noun phrase, or with the student as the subject. Let the name appear only in the dedication and in students' chat bubbles.
