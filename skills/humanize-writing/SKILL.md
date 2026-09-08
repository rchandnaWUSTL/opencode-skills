---
name: humanize-writing
description: Remove AI-writing tells from prose, docs, UI strings, scripts, and emails so the text reads like a person wrote it. Use when asked to de-AI, humanize, "make this not sound like AI," sweep for AI tells, or polish copy before an audience that punishes AI slop.
---

# Skill: Humanize Writing

Make text read like a person wrote it. Two failure modes cause most AI-sounding text: the model performs (rhythm, reveals, significance) and the model over-explains (narrating what the reader can see). The fix is usually deletion, then plain restatement.

---

## Input

- The text (file paths or pasted)
- What kind of text it is: **UI copy** or **prose** (docs, emails, scripts, README). The rules differ.
- Who reads it and how suspicious they are of AI writing

---

## The tells

Check every one. They cluster; one hit is style, three is a diagnosis.

**Punctuation and rhythm**
- Em dashes, especially several per page doing different jobs. Replace with a period, comma, colon, or parentheses.
- Clipped fragment pairs for rhythm: "Fast. Simple." A person picks one idea and builds it out.
- Rule-of-three everywhere: "adjective, adjective, adjective" or three parallel phrases. Break the symmetry: cut one item or expand one properly.
- Balanced antithesis: "X does A, Y does B" as a closing beat. State the one fact that matters.
- Uniform sentence length. Humans write long then short.

**Constructions**
- The negation-reveal: "It's not X. It's Y." / "This isn't about X, it's about Y." State Y.
- Significance flourishes: "It's important to note," "crucially," "a testament to," "what's remarkable is." Delete; if the point matters, the content shows it.
- Register announcements that perform candor or precision: "One honest caveat," "to be honest," "let me be direct," "here's the thing," "fair question." Say the sentence, skip the label for it.
- Hedging filler: "generally speaking," "to some extent," "in many ways." Delete or commit.
- Cute metaphors doing work a plain word could do: "house rules," "north star," "secret sauce."
- Wrap-up paragraphs that restate what was just said. End on the last new fact.

**Vocabulary**
- AI-era words (kill on sight): delve, tapestry, robust, seamless, leverage (as a verb), streamline, underscore, pivotal, crucial, foster, boast, comprehensive, journey, landscape, empower, elevate, meticulous, adept, realm, swift, garner, showcase, testament, intricate, "the shift we're seeing".
- Register tics: small metaphor verbs and jargon nouns that are fine once and a tell on repeat: land, ship, surface (as a verb), unlock, unpack, double-click, lean into, crisp, tight, sharp, killer, gold, beat (for a segment), story (for an argument), moment, north star, "the ask". Detection is frequency, not presence: if a word does metaphor duty three or more times in a piece, replace most instances with the plain verb (arrives, finishes, shows, section, argument).
- Stacked adjectives: "a powerful, flexible, intuitive tool." One adjective, or a fact instead.
- Puffery instead of evidence: "significantly improves" with no number. Use the number or cut the claim.

**Structure**
- Headers as colon-subtitles: "Testing: Why It Matters." Use "Testing."
- Bold-label bullet lists where prose would do.
- Explaining things the reader obviously knows.

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

## Workflow

Copy this checklist and work through it:

```
Humanize pass:
- [ ] 1. Classify each piece: UI copy or prose
- [ ] 2. Deletion pass: remove strings/sentences that narrate, restate, or perform
- [ ] 3. Tells pass: check every item in "The tells" against what remains
- [ ] 4. Rewrite survivors as plain statements
- [ ] 5. Verify (below)
```

**Verify**
- `grep -rn "—"` on the files: zero hits in UI strings; in prose, each remaining em dash must be deliberate and rare.
- Grep for the vocabulary list and negation patterns (`isn't just`, `not only`, `it's not`, `more than just`).
- Read it aloud. Anywhere you hear a drumbeat, break the rhythm.
- Diff check: the humanized version should almost always be shorter. If it grew, you rewrote when you should have deleted.

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

---

## Boundaries

- Don't flatten voice into blandness. The goal is a person, not a robot of a different kind. Keep jokes, opinions, and specifics; cut performance.
- Don't change meaning, facts, or numbers while editing.
- Domain jargon the audience uses daily is fine; builder jargon leaking to users is not.
