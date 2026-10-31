---
name: humanize-writing
description: Remove AI-writing tells from prose, docs, UI strings, scripts, and emails so the text reads like a person wrote it. Use when asked to de-AI, humanize, "make this not sound like AI," sweep for AI tells, or polish copy before an audience that punishes AI slop.
---

# Skill: Humanize Writing

Make text read like a person wrote it. Two failure modes cause most AI-sounding text: the model performs (rhythm, reveals, significance) and the model over-explains (narrating what the reader can see). A third makes it generic: no names, numbers, or things that actually happened. The fix is usually deletion, then plain restatement, then specifics.

The goal is a suspicious human reader, not a detector score. Modern detectors are trained classifiers that measure statistical sameness, so word swaps barely move them. What reads as human to people (real specifics, uneven rhythm, a writer's own opinions) is also the only thing that changes that profile.

---

## Input

- The text (file paths or pasted)
- What kind of text it is: **UI copy** or **prose** (docs, emails, scripts, README). The rules differ.
- **Edit or rewrite**: did a person write this (edit mode: minimal diff, keep their quirks) or did a model (rewrite mode: full pass)?
- Who reads it and how suspicious they are of AI writing

---

## The tells

Check every one. They cluster; one hit is style, three is a diagnosis.

**Punctuation and rhythm**
- Em dashes, especially several per page doing different jobs. Replace with a period, comma, colon, or parentheses. A spaced double hyphen ( -- ) is the same tell.
- Clipped fragment pairs for rhythm: "Fast. Simple." A person picks one idea and builds it out.
- Rule-of-three everywhere: "adjective, adjective, adjective" or three parallel phrases. Break the symmetry: cut one item or expand one properly.
- Balanced antithesis: "X does A, Y does B" as a closing beat. State the one fact that matters.
- Uniform sentence length. Humans write long then short.

**Constructions**
- The negation-reveal: "It's not X. It's Y." / "This isn't about X, it's about Y." / "not just X, but Y." State Y.
- The corrective "rather than": "Treat it as a tool rather than a replacement." State what it is.
- Copula avoidance: "serves as," "stands as," "functions as," "boasts," "features," "marks a." Use is, has, or the real verb.
- Hollow -ing tails tacked onto a finished sentence: "…, highlighting the importance of X," "…, ensuring Y," "…, underscoring Z." Delete the tail; if the point matters, make it its own sentence with a fact.
- Significance flourishes: "It's important to note," "crucially," "a testament to," "what's remarkable is," "plays a pivotal role," "setting the stage for," "enduring legacy." Delete; if the point matters, the content shows it.
- Phantom attribution: "Experts argue," "Studies show," "Industry reports suggest," "Critics say." Name the source or cut the claim.
- Register announcements that perform candor or precision: "One honest caveat," "to be honest," "let me be direct," "here's the thing," "fair question." Say the sentence, skip the label for it.
- Signposting: "Let's dive in," "Here's what you need to know," "In this post we'll cover." Start with the first real sentence.
- Hedging filler: "generally speaking," "to some extent," "in many ways." Delete or commit.
- Cute metaphors doing work a plain word could do: "house rules," "north star," "secret sauce."
- Synonym cycling: "the company… the firm… the organization" for one thing. Pick a name and repeat it.
- Wrap-up paragraphs that restate what was just said ("In summary," "Overall," "Ultimately"). End on the last new fact.

**Chatbot residue** (any one of these is close to proof; always remove)
- "Certainly!", "Great question," "I hope this helps," "Let me know if you'd like…," "Feel free to," "Happy to help."
- Source hedges: "Based on available information," "While specific details are limited."
- Placeholders left in: "[Your Name]," "[insert date]," "Company X."

**Vocabulary**
- AI-era words (kill on sight): delve, tapestry, robust, seamless, leverage (as a verb), streamline, underscore, pivotal, crucial, foster, boast, comprehensive, journey, landscape, empower, elevate, meticulous, adept, realm, swift, garner, showcase, testament, intricate, "the shift we're seeing". Newer models favor: enhance, align with, highlighting, showcasing, emphasizing, multifaceted, nuanced, holistic, prioritize, navigate (figurative), ever-evolving. The list goes stale; one word is noise, a cluster is a tell.
- Brochure tone: nestled, vibrant, rich (history, heritage), renowned, bustling, "in the heart of," "commitment to," "diverse array," world-class.
- Register tics: small metaphor verbs and jargon nouns that are fine once and a tell on repeat: land, ship, surface (as a verb), unlock, unpack, double-click, lean into, crisp, tight, sharp, killer, gold, beat (for a segment), story (for an argument), moment, north star, "the ask". Detection is frequency, not presence: if a word does metaphor duty three or more times in a piece, replace most instances with the plain verb (arrives, finishes, shows, section, argument).
- Stacked adjectives: "a powerful, flexible, intuitive tool." One adjective, or a fact instead.
- Puffery instead of evidence: "significantly improves" with no number. Use the number or cut the claim.

**Structure**
- Headers as colon-subtitles: "Testing: Why It Matters." Use "Testing."
- Title Case Headers. Use sentence case.
- Emoji at the start of headers or bullets.
- Bold-label bullet lists where prose would do, and bold scattered through paragraphs.
- Stock sections: "Despite its success, X faces several challenges…" followed by an upbeat "Future outlook." Cut both unless there's a specific challenge with a specific consequence.
- Explaining things the reader obviously knows.

---

## Specificity pass

Deletion makes text shorter; specifics make it human. Generic claims are the deepest tell because no amount of rewording fixes them.

For each sentence that survives deletion, ask: could this sentence appear unchanged in a thousand other documents? If yes, it needs one of:
- A number: "took 5 minutes and $4," not "fast and cheap"
- A name: the customer, the tool, the person, the file
- A date or sequence: "in March," "after the second outage"
- What actually happened: "the cache restore took longer than the install," not "performance issues arose"
- The writer's real opinion, stated once without hedging

**Never invent a specific.** Use facts already in the source, the codebase, or the conversation. If the fact isn't available, leave a marker for the user: `[NEEDS SPECIFIC: which customer?]`. If the sentence has no specific to give, delete it.

---

## Rules by text type

**UI copy** (labels, buttons, captions, helper text, empty states)
- Label, don't narrate. "Customer app," not "What customers see when they use the product."
- Delete any string that only explains what the UI already shows. Deletion is the strongest edit.
- Solo fragments take no trailing period. Sentence case. Skip colons after labels.
- Buttons: verb + object ("Send invoice"), not abstractions ("Submit").
- Constraints only in helper text: "At least 5 characters," not "Explain your change so it's logged."
- The test: would a bored engineer at a good product company write this label? If it has personality, cut it.

**Prose** (docs, README, emails, one-pagers, scripts to be read aloud)
- One idea per sentence, built out. No performing.
- Concrete nouns and numbers beat adjectives: "took 5 minutes and $4" beats "remarkably fast and cheap."
- Keep the writer's stakes and first person where it's honest: "I caught this in review."
- Spoken scripts get more slack: contractions, direct address, and enumerations are natural speech. The negation-reveal still sounds like AI when spoken; cut it there too.

---

## Don't overcorrect

Humanizing has its own tells. Over-editing produces a different robot.

**Leave alone** (these are not AI signs on their own):
- Correct grammar and spelling
- A single "Additionally" or "However"
- Formal register when the domain is formal (legal, academic, API reference)
- The author's own odd word choices, idioms, and repeated phrases in edit mode. Homogenizing a person's voice is exactly what AI polish does.

**Never add:**
- Deliberate typos, misspellings, or broken grammar
- Forced slang, "lol," or casualness the writer wouldn't use
- Rare synonyms swapped in for common words ("utilize" for "use," "commence" for "start"). This is what humanizer tools do; it damages meaning and doesn't fool detectors.
- Gratuitous fragments and one-line paragraphs for punch. That's the LinkedIn-post pattern, itself a tell.
- Made-up anecdotes, numbers, or quotes to sound specific

---

## Workflow

Copy this checklist and work through it:

```
Humanize pass:
- [ ] 0. Baseline: run scripts/scan.py on the original
- [ ] 1. Classify each piece: UI copy or prose; edit or rewrite mode
- [ ] 2. Deletion pass: remove strings/sentences that narrate, restate, or perform
- [ ] 3. Tells pass: check every item in "The tells" against what remains
- [ ] 4. Specificity pass: replace generic claims with facts from the source, or mark [NEEDS SPECIFIC]
- [ ] 5. Rewrite survivors as plain statements; check "Don't overcorrect"
- [ ] 6. Verify (below)
```

**Verify**
- Run `python3 scripts/scan.py <file>` (path relative to this skill's directory; pass `-` to read stdin) before and after. It reports em dashes per 1,000 words, sentence-length spread, repeated sentence openers, and every pattern hit with a line number. Hits are prompts to look, not verdicts: the scanner can't tell a quoted example from a real tell.
- Targets: zero chatbot residue; zero em dashes in UI strings, rare and deliberate in prose; sentence-length spread (cv) above about 0.4; no repeated-opener warning (one word starting 15% or more of sentences).
- Read it aloud. Anywhere you hear a drumbeat, break the rhythm.
- Diff check: the humanized version should almost always be shorter. If it grew, you rewrote when you should have deleted (specifics are the exception: a number can add words).
- Report any `[NEEDS SPECIFIC]` markers to the user rather than leaving them silently.

---

## Examples

| Before (AI) | After |
|---|---|
| Customer surface (demo) | Customer app |
| Append-only. Newest first. | Entries can't be edited or deleted |
| Flip a flag and watch it change. | A sample customer app that uses these feature flags |
| The biggest risk isn't the code — it's the thing you asked for. | The biggest risk is the thing you asked for. |
| Devin does the toil, your engineers do the judgment. | Devin builds, your engineers review. |
| It cost $4 — remarkably cheap — and took just 5 minutes. | It cost $4 and took 5 minutes. |
| The dashboard serves as a central hub, empowering teams to make data-driven decisions. | The dashboard shows each team's open incidents and deploys. |
| Experts agree that caching significantly improves performance. | Caching cut p95 latency from 800 ms to 120 ms. |
| The migration went smoothly, highlighting the team's robust processes. | The migration finished in two hours with no rollback. |
| Performance issues arose during testing. | The cache restore took longer than a clean install. [NEEDS SPECIFIC: how much longer?] |

---

## Boundaries

- Don't flatten voice into blandness. The goal is a person, not a robot of a different kind. Keep jokes, opinions, and specifics; cut performance.
- Don't change meaning, facts, or numbers while editing. Don't invent them either.
- Domain jargon the audience uses daily is fine; builder jargon leaking to users is not.
- This skill improves writing; it is not a detector-evasion tool. Don't promise that output will pass a particular AI detector.
