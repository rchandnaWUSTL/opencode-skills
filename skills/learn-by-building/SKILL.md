---
name: learn-by-building
description: Design a lean, evidence-based learning project where Claude teaches and quizzes instead of doing the work, then scaffold a repo that runs each 30-minute session itself. Use when someone wants to learn a skill or topic by building something ("teach me X while I build", "a side project that closes this gap", "make me a syllabus / learning plan", "tutor me, don't do it for me"), or wants to turn interview or performance feedback into a project that fixes it.
---

# Learn by building

Turn "I want to learn X" into a small project the learner builds while Claude teaches. The output is a repo with a tutor contract (`CLAUDE.md`), so any later session there can be started with "start the session" and runs itself.

**The main failure is the learner quitting because it doesn't feel worth it**, not a weak syllabus. Every design choice below serves that: lean scope, an early payoff, and every session ending on a question that matters to them.

## Process

### 1. Intake: ask only what you can't infer

Read what's already available first: memory, feedback notes, transcripts, the repo. Then ask for whatever is still missing, in one round:

- **The goal behind the goal.** Why learn this, and where will it get tested (an interview loop, a job, a launch)? The real test sets the depth.
- **The evidence of the gap.** What exactly went wrong, in the words of whoever said it? Quote it if you can.
- **Time.** Minutes per session (default 30) and sessions per week. Any deadline?
- **Starting point.** What they already know, so you don't teach it again.

### 2. Build backward: write the final outcomes first

Write 5–8 **questions the learner must answer cold, out loud, at the end, with one more layer ready when asked "why?"** Pull them from the real evidence: the questions they couldn't answer, and the probes coming in their next rounds. These outcomes are the whole syllabus; everything else exists to reach them. (Backward design, Wiggins & McTighe.)

### 3. Pick the project

Choose one project that forces every outcome. Good ones:

- Sit in the domain where they got tested, or right next to it.
- Have layers that match the gaps. For example, deterministic step, model step, UI and follow-up action, if the gap was systems decomposition.
- Ship as something they can show: a repo, a demo, a one-page design doc, maybe a landing page.
- Are real enough that "what did you personally build?" has a strong answer.

Give a recommendation and say why. Don't present a menu.

### 4. Draft the syllabus, then cut it

Default to **about 18 sessions of 30 minutes (about 9 hours)**. Go over 24 only if the goal really needs it, and say why.

Every session must pass the **leverage test**:

1. It feeds at least one final outcome.
2. Its exit ticket is a question someone will actually ask them. Phrase it in quotes, the way an interviewer or reviewer would.
3. It can't be merged with a neighbor without losing that question.

Cut aggressively:

- **Engineering work that produces no new understanding** goes to an "Optional extras" list: deploys, UI polish, a production integration where a drawing plus one small piece of code teaches the same concept.
- **Background theory the outcomes don't need** gets cut. Teach the categories that matter, not the whole field.
- **Ceremony** (test-first rituals, five-level scales, written unit tests) gets cut when a lighter mechanism does the same job.
- **Slow non-learning work** becomes boilerplate. Claude can generate raw material, like examples for the learner to label, while the learner does the judgment.

Put the highest-signal parts early so the payoff lands in week 2–3. Add checkpoints about every 6–7 sessions; make them **mock interviews** (see below), not written tests.

### 5. Scaffold the repo

Create a new repo where the learner keeps projects. Ask where if you don't know, and never put it inside an unrelated repo. Copy these templates and fill them in:

| File | From | What to fill in |
|---|---|---|
| `CLAUDE.md` | `templates/CLAUDE.md` | Context (the gap, in their words), what counts as core logic vs boilerplate, worked-example sessions, checkpoint personas, stack |
| `SYLLABUS.md` | `templates/SYLLABUS.md` | Sessions, exit tickets, checkpoints, optional extras, final outcomes |
| `REVIEW.md` | `templates/REVIEW.md` | Nothing; cards come from sessions |
| `LEARNING.md` | `templates/LEARNING.md` | Nothing |
| `quizzes/pretest.md` | `templates/pretest.md` | 8–10 questions drawn from the final outcomes. They're retaken at the end. |
| `PLAN.md` | (write it) | What the project is, who it's for, the architecture, part checkboxes |
| `README.md` | (write it) | Two lines and links |

Then `git init` and commit. Ask before creating a GitHub remote, and ask whether it should be public or private.

### 6. Offer a viewable page

Offer to publish the syllabus as a private artifact: session cards with progress checkboxes, the session shape, lanes, and final outcomes. Treat `SYLLABUS.md` as the source of truth; republish the page when it changes.

### 7. Tell them how to use it

Three lines: `cd` into the repo, run `claude`, say "start the session." Mention anything they need installed before session 1.

## The teaching method (what the templates encode)

Everything below is already in `templates/CLAUDE.md`. It's summarized here so you can explain it and adapt it. Sources are in `references/evidence.md`.

- **Session shape (30 min):** do now (3 review cards from memory, confidence rated first) → predict → work block (stop at minute 24) → explain back out loud → exit ticket (cold) plus new cards and a commit. Never skip the last two steps to finish the work block.
- **Three AI lanes:** *no AI* (pretest, solo reps, final retake, the start of each mock), *hints only* (all core logic), *boilerplate* (labeled setup code). Adapted from the University of Sydney's two-lane policy and the AI Assessment Scale. Students who get answers from AI do better in practice and worse unaided (Bastani et al., PNAS 2025). Hint-only tutors avoid most of that harm, and a well-designed one doubled learning in Harvard's trial (Kestin & Miller 2025).
- **Hint ladder:** a question, then a pointer to docs, then a concrete hint, and the answer only on explicit request. Help fades as they get things right and steps back up when they miss.
- **One worked example, then fading:** the first time a new kind of code comes up, Claude works a *different* case line by line, scaffolds the next one, then steps back.
- **Spaced review cards (Leitner):** 4 boxes with short intervals (1/2/4/8 sessions). Even gaps work about as well as expanding ones; what matters is retrieving each idea 4–5 times.
- **New material by part, mixing only in review:** interleaving helps you tell problems apart, less so on first exposure.
- **Checkpoints are mock interviews:** a 10-minute solo rep with no AI, then a fresh agent with a realistic persona that probes one layer deeper and runs a **code viva** on a function chosen at random. Pass bar: the rep works and the mock clears the bar.
- **Teach sessions:** in a few sessions Claude plays a confused newcomer and the learner teaches it (Mollick & Mollick's "AI as student").
- **No concessions:** "I'm not an engineer" gets "how would you reason about it from what you know?"
- **Verify before teaching:** back every factual claim with a doc link or a live experiment, noting versions. A confidently wrong tutor is the main harm.
- **Keep it worth it:** at each checkpoint, ask which session felt least worth it, then cut, merge or rework. The plan should shrink over time.
- **Resume anywhere:** "Current session" in LEARNING.md always records where they stopped and the next step.

## Don'ts

- Don't write a 40-plus-session plan because it looks thorough. Thorough plans get abandoned.
- Don't build the project for them during design. Scaffold files only.
- Don't cite research you haven't checked when the learner asks about it. Search first, and say when evidence is mixed.
- Don't pick the project for being impressive. Pick it because it forces the outcomes.
