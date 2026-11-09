---
name: arabic-copywriting
description: Write, rewrite, edit or review professional Arabic (Modern Standard Arabic) so Arab readers understand it on first read and feel understood — marketing copy, landing pages, brochures, PDFs, UI microcopy, notifications, emails, meeting minutes, reports and docs. Covers natural phrasing (no translationese), register, grammar, hamza and spelling, Arabic punctuation, numbers, English terms inside RTL text, and Medsera's product glossary. Use this skill whenever the output contains Arabic sentences — even if the user writes the request in English, says "translate", asks for "Hormozi style" or a story in Arabic, sends Arabic text to fix, or produces Arabic strings for ar.json — and whenever someone complains that Arabic copy is weak, unclear, stiff or sounds translated.
---

# Arabic copywriting

The goal is not Arabic words. The goal is that a doctor in Khartoum, Cairo or Riyadh reads the text once, understands it, and feels that whoever wrote it knows their life. When readers say "what are you talking about?", the cause is almost never grammar. It is English thinking dressed in Arabic words: English metaphors, product jargon, label-and-colon fragments, and sentences built in English order.

So this skill works in two layers. First write from the **meaning** (what must the reader understand, feel and do?). Then make it **correct** (grammar, spelling, punctuation, terms).

## The core shift: you are writing, not translating

When you have an English source, an English idea, or an English framework (Hormozi, a slogan, a UI label), do this:

1. State the intent to yourself in one plain sentence: "the instructor should understand that the platform marks essays so they only review."
2. Close the English. Ask: how would an Arab doctor say this to a colleague in the doctors' room, in clean فصحى?
3. Write that. Then check it against the English only to confirm nothing important is missing — never to copy its structure.

A useful self-test: if your Arabic converts back word-for-word into fluent English, it was written in English first. Rewrite it.

## Register and voice

- **فصحى معاصرة مبسّطة** ("white Arabic"): standard Arabic in everyday words, the way a respected doctor writes a WhatsApp message to colleagues — clean, warm, no showing off. Not classical, not news-agency stiff, not dialect.
- **No dialect words in body text** (الحين، دلوقتي، هسي، كده، شغل، مصاريف، على كيفك). Dialect is allowed only inside quotation marks as a real quote (a chat screenshot, what a student said).
- **One voice per document.** Brochures and landing pages speak to the reader as «أنت». Community announcements use the plural «أنتم». Minutes and reports use the third person and never "I". Don't switch midway.
- **Gender-aware.** Address with the generic masculine singular in marketing (as Careem, Tabby, Tamara do), but avoid gendered adjectives about the reader — prefer an action or noun («جاهزيتك للامتحان» rather than «هل أنت مستعد»). Buttons use the imperative or masdar (ابدأ، نسخ الرابط). Mention «طبيب وطبيبة» from time to time in marketing.
- **Warm, not sugary.** Name real feelings plainly (قلق، تعب، خوف من الرسوب). Avoid pet names (يا بطل، يا شاطر), repeated «لا تقلق!», and stacked exclamation marks. Never explain basic medicine to doctors.
- **Honest colleague, not showman.** No «فرصة العمر»، «عرض لا يُقاوَم»، «لن تصدّق», fake urgency, or unprovable claims.

## The ten habits that made our Arabic unclear (and what to do instead)

These come from a real editorial audit of Medsera documents that readers rejected. Each one hurts comprehension more than any grammar slip.

1. **Foreign metaphors.** «مشكلة بيت»، «غرف المنصة»، «مجهر المنتور»، «جيش يبيع عنك»، «محرك بلا وقود»، «الرافعة»، «بوابات الإتقان». Arabic readers take these literally and stall. Default to saying it plainly. Use an image only if Arab doctors already use it (المناوبة، قاعة الامتحان، ملف الهجرة، الرسوم التي لا تريد دفعها مرتين). Never build a whole document on one metaphor.
2. **Developer and product jargon.** مفتاح تشغيل، الخادم الحقيقي، ثقة النموذج، وضع المعايرة، الإشارات متعارضة، مستحق اليوم، تحويل تلقائي للجودة. Describe what happens to the person in plain verbs: «يعرض لك مدى تأكده من كل درجة، ويجمع لك ما يشك فيه لتراجعه».
3. **Literal English phrases (calques).** «يعيش في خمسة أماكن»، «صحة المجتمع»، «مسار التحويل»، «يحمي النقد»، «افعلوا ما لا يتوسع». Rewrite from the meaning. See `references/translationese.md`.
4. **False friends that flip the meaning.** «الدافع» for paying (means "motive" → المشترك), «غير المرئية» for unseen (means invisible → التي لم يحلّها), «تخفيض» for downgrade (means discount → الانتقال إلى باقة أقل), «لا يجب» for "don't have to" (means "must not" → لا يلزمك), «مقدمًا» for "front-load" (means "in advance"), «النقد» for cash (also "criticism"), «التحويل» for conversion (reads as bank transfer). Full list in `references/translationese.md`.
5. **Label-and-colon fragments.** English slide syntax: «الأنواع: أفضل إجابة، اختيار متعدد، ...». Most bullets should be full sentences with a verb. At most one "label:" pattern per section.
6. **Noun stacks and nominalization chains.** «العمل على تحقيق تطوير عملية التقييم» → «نطوّر التقييم». Max two nouns in an إضافة chain; turn the third into a verb.
7. **English sentence order.** Arabic narrates with the verbal sentence: «أطلقت المنصة دورة» rather than «المنصة أطلقت دورة» — use the nominal sentence only for emphasis or a new topic. Cut "your/his" possessives and «هذا/هذه» that English forces.
8. **Feature catalogues instead of outcomes.** Sixty features with badges bury the story. Lead with what changes for the reader; group features under that outcome; keep the full inventory in an appendix.
9. **Internal numbers and unsourced claims.** Costs per API call, demo data, "Hormozi says..." without a source. Every number must matter to the reader, be sourced or labelled illustrative, and be recomputed (one draft said $100 ≈ 200–300 SAR; it is 375).
10. **Inconsistent terms.** المنتور/المدرّس/الأستاذ/المرشد in one document; ميدسيرا masculine on one page and feminine on another. Pick one word per concept (see `references/glossary.md`) and treat **ميدسيرا as feminine**: «ميدسيرا تجمع».

## Workflow

### 1. Before writing
- Skim `references/failure-log.md`: mistakes we already made once, so they are caught first.
- Who reads it (instructor, student, marketer, partner, internal team)? What should they understand, feel, and do after reading?
- Which document type? (See "Document types" below.)
- Pull the terms you need from `references/glossary.md` so they're consistent from the first line.

### 2. Draft from meaning
- One idea per sentence. Marketing sentences ≲ 20 words, docs ≲ 30. Use conjunctions that show the relation (فـ، ثمّ، لكنّ، لذا، إذ) or a full stop — not a chain of commas.
- Open with the reader's situation or the result, not with the product.
- A number beats an adjective: «40 سؤالًا يوميًا بشرح كامل» not «محتوى غني».
- Every abstract word (رحلة، تمكين، مستقبل، تميّز، آفاق، استثنائي، حلول) must be followed in the same sentence by a concrete fact — or deleted.

### 3. Four editing passes
Run them in order; each catches different problems.

1. **Clarity pass — the colleague test.** Read each paragraph as a busy Sudanese GP would. If they would ask «تقصد إيش؟», rewrite from the intent. Kill metaphors, jargon, and fragments.
2. **Naturalness pass — translationese hunt.** Remove تمّ + مصدر، قام بـ، من قِبَل، كلما…كلما، سوف لن، بشكل/بطريقة + adjective، كـ meaning "as"، ليس فقط… بل أيضًا، حيث as a connector، بالتالي، يلعب دورًا. Details in `references/translationese.md`.
3. **Correctness pass.** Hamza (especially همزة الوصل: استخدام، اجتماع، انطلاق), ة/ه, ى/ي, number–noun agreement, accusative endings after كان/أصبح/ليس/إنّ, tanween on visible objects. Verb + preposition pairs that English drops: «يحتاج إلى»، «أجاب عن»، «تخرّج من»، «حصل على»، «اطّلع على»، «بعضها ببعض» (not «ببعضها»), «يُفاجأ» (not «يتفاجأ»). Every pronoun (هذا، ذلك، ـه) still has its noun nearby. Check each list item and table row on its own — a single missed row is a common slip. Details in `references/grammar-punctuation.md`.
4. **Consistency pass.** Glossary terms, ميدسيرا feminine, one voice, status labels identical across body and appendix, same quote marks «» everywhere, Western digits.

### 4. Run the mechanical check
For any Arabic over a few lines, run the linter that ships in this skill's `scripts/` folder (Python 3, no dependencies) and fix or justify each hit:

```bash
python3 <this-skill-folder>/scripts/arabic_lint.py <file.html|.md|.txt|.json>
```

It flags Latin punctuation inside Arabic, spaces before punctuation, detached و, wrong همزة قطع on وصل words, تاً, فى/الذى, translationese phrases, dialect words, foreign metaphors, Arabic prefixes glued to Latin words, long sentences and colon overuse. A hit is a prompt to look, not an automatic error.

### 5. Final read-aloud
Read the text aloud (or imagine it). If you run out of breath, split the sentence. If it sounds like a dubbed film, it's still translationese. Read the last line of each section for the emotion it leaves, not only its literal meaning (an ending once read as "you'll ignore your students").

### 6. Feed the log
If you caught a mistake that isn't already in `references/failure-log.md` or `references/translationese.md`, append one entry using the log's schema. That is how the skill gets better with every document.

## Punctuation essentials

Full rules in `references/grammar-punctuation.md`. The ones that matter most:

- Use Arabic glyphs: **، ؛ ؟** — never Latin `, ; ?` inside Arabic.
- No space before a mark, one space after. No space inside «» or ( ). Prefixes attach: «وقال»، «بالمستشفى».
- **«»** for quotes and coined terms, consistently.
- **:** only after a quoting verb or before a list/explanation — not as a headline device in prose («الخبر السار: …»), and never twice in a sentence.
- **؛** only when the second clause is the cause or result of the first. In marketing a full stop is usually better.
- **!** at most once per screen in marketing; none in minutes and docs.
- No Oxford comma before the last «و» — Arabic lists read «أ، وب، وج» or «أ، ب، وج», never «أ، ب، و ج».

## Numbers, dates, English terms

- **Western digits 0–9** everywhere (Medsera house rule), including in Arabic UI.
- Digits remove the number-gender problem, but the noun form still follows the rule: 3–10 → plural («5 دورات»), 11–99 → singular with tanween («25 طبيبًا»), 100+ → singular genitive («300 سؤال»). Zero → «لا يوجد…», one → «طالب واحد», two → dual («امتحانان»).
- Dates: «12 مارس 2027» (يناير … ديسمبر, not كانون/تشرين). Currency spelled out: «2,920 دولارًا أستراليًا».
- **Keep exam names, subtests and medical terms in Latin**: AMC, OET, MCQ, AHPRA, Writing, Reading, Listening, Speaking, recalls, Grade B. Doctors studied medicine in English; transliterations («أو إي تي») read worse. Wrap them in an Arabic sentence frame: «ارفع درجتك في Writing».
- Never glue Arabic letters to Latin words: «في امتحان OET», not «بالـOET» or «الـAMC». Don't start or end a line with a Latin run if punctuation can jump; put an Arabic word first. In HTML, wrap multi-word Latin names in `<bdi style="white-space:nowrap">…</bdi>` so they don't split across lines.
- Diacritics: none in body text, except a shadda or vowel where it prevents a misreading (مسوّق، تدرّس، المعلَّم، يُفاجأ). Be consistent.
- Add the English in parentheses only on first mention, and only for terms doctors know in English: «وضع الشرح (Tutor)»، «امتحان تجريبي (Mock)». Never on buttons or notifications.

## Persuasion in Arabic (Hormozi without the American accent)

Frameworks like Hormozi's value equation, offers and guarantees work in Arabic when you translate the **logic**, not the **voice**. Full craft notes and brand examples in `references/copy-craft.md`.

- **Result** in exam terms: «اجتز MCQ من أول محاولة»، «درجة B في Writing» — not «حياة أحلامك».
- **Likelihood** by proof, not claims: doctors who passed, real numbers, a free sample.
- **Time and effort** concretely: «خطة 12 أسبوعًا»، «نصحّح لك ونخبرك أين الخطأ».
- **Guarantee** plainly and conditionally: «إن حضرت الحصص وأكملت الامتحانات التجريبية ولم تنجح، تحصل على الدورة التالية مجانًا».
- **Headline patterns that work in Arabic:** result + number; the reader's own question («رسبت في Writing مرة؟»); short contrast («في أسابيع، لا شهور»); fear removed («بدون اشتراك سنوي»); proof up front.
- **Storytelling:** concrete scene, real details (time on the clock, the exact repeated question), a named character labelled «قصة توضيحية» if composite. One story carries more than ten features.
- Rhythm comes from short parallel clauses («اسأل، تدرّب، اعرف أين تقف»). Use rhyme (سجع) only if it falls naturally; forced saj' reads as an advertisement.

### How much rhetoric (lessons from a blind test)
On 9 Nov 2026 the same brochure was rewritten with this skill and with fasaha + humanizer-ar-msa, then judged blind. This skill won on clarity and trust; the other won on grammar and a few memorable lines. Keep both lessons:
- **Rhetoric earns its place only when it lands a story or uses an image doctors live with.** «لم يكن جاهلًا. كان واثقًا من الخطأ.» works: one short punchline at the turn of a story. «والمجهر لا يرى شيئًا بلا عيّنة» is a clinical image, so it can work once, and only if no other microscope metaphor runs through the document.
- **What doesn't work for product and business copy:** a metaphor every few hundred words, rhymed fear-of-missing-out slogans («فأول بيت يُفتح أول بيت يمتلئ»), literary allusions («تنام ملء جفونك»), archaic words («مبذولة»), rhetorical questions that force a re-read, and turning scannable lists into long paragraphs on pages people read on a phone.
- **Local touches help:** «فيدفع طالبك بعملته في الخرطوم أو القاهرة أو الخليج» says "four currencies" in a way the reader feels.
- **Keep facts the reader needs, even uncomfortable ones** (the platform's share, statuses). Cutting them costs trust.

## Document types

- **Marketing / brochure / landing page:** outcome first, one story, short verbal sentences, numbers, proof, one clear next step. Honest status labels if features are unfinished (use plain labels: «متاح الآن»، «في مرحلة التجربة»، «يتولاه فريقنا»، «قريبًا»).
- **UI microcopy and notifications:** shortest possible. Buttons = imperative verb («ابدأ التدريب»). No «تمّ … بنجاح» → «حُفظت التغييرات». No «فشل» → «تعذّر التحميل. حاول مرة أخرى». Empty states say what to do next. Match `references/glossary.md` exactly so the app speaks one language.
- **Meeting minutes and reports:** third person, past tense for what happened, clear decisions and owners. No dialect except quoted. Give every decision its context so a reader who wasn't there understands («حذف خيار "وظيفة تدريبية مهددة" من قائمة المشاعر لأننا لا نملك حلًا لصاحبه»). Keep personal details of attendees out of summaries.

## Reference files

Read the one you need — they're long so the main file stays short.

- `references/failure-log.md` — real mistakes we already made (bad → good → why), grows with every document. Read it first; append new patterns at the end of the workflow.
- `references/translationese.md` — WRONG → RIGHT tables for calques, false friends, structural translationese, plus real before/after rewrites from rejected Medsera copy. Read it during the naturalness pass, and whenever rewriting existing Arabic.
- `references/grammar-punctuation.md` — punctuation mark by mark, hamza, ة/ه, ى/ي, tanween, number agreement, كان/إنّ, الأسماء الخمسة, sources. Read it during the correctness pass or when unsure of a rule.
- `references/glossary.md` — Medsera product terms (English → recommended Arabic → avoid), English-in-RTL rules, and known inconsistencies in the app strings. Read it before writing anything about the product, and for any ar.json work.
- `references/copy-craft.md` — headline patterns, emotional vocabulary for doctors, live examples from Careem/Tabby/Tamara/Talabat and why they work, regional notes for Sudan/Egypt/Gulf, adapting Hormozi. Read it for marketing and persuasive copy.
