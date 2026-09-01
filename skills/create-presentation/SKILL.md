---
name: create-presentation
description: Build a HashiCorp internal presentation (pptx) from scratch using python-pptx. Use when asked to create a deck, build slides, or make a presentation. Supports "--think" flag to run thought-partner first.
---

# Skill: Create Presentation

Build a reproducible HashiCorp internal presentation using python-pptx.

---

## Input

- **Topic**: What the presentation is about
- **Audience**: Who will see it (peers, leadership, customers, etc.)
- **Slot**: How long is the session (e.g. 20 min)
- **Evidence**: Case studies, win stories, demo footage, customer names -- paste or reference files
- **Organizer context** (optional): What the session organizer specifically wants covered; what has already been shared with the audience beforehand

If audience or slot is unknown, ask before proceeding.

---

## Workflow

1. Clarify audience, slot length, and organizer context
2. Propose a slide outline following the canonical structure below -- get approval before building
3. Write `build_deck.py` using python-pptx, saved alongside the output
4. Run it to produce the `.pptx`
5. Report the output path and any manual steps (e.g. logo swap, demo embed)

---

## Canonical Slide Structure

Follow this order:

1. **Title** -- topic + one-line frame
2. **Opportunity / Problem** -- the customer problem they actually feel
3. **Concept bridge** -- the insight that reframes the problem
4. **Insight** -- statement slide (large type, 3 lines building to conclusion)
5. **Proof table** -- evidence table (real customers, real ARR, real outcomes)
6. **Case study section break** -- large type, customer name
7. **Case study: problem** -- what they faced, their org context, their goal (separate, don't conflate)
8. **Demo** -- single slide: just says "demo", with speaker notes for exact callout moments
9. **Timeline** -- 4 columns: Week 1 / Week 2 / Week 3 / Future
10. **Meta-tool** (if applicable) -- tool/workflow the audience can use themselves
11. **FAQ** -- questions bold on own line, answers below (not inline)
12. **Close** -- question that opens discussion; empowers audience to act

For a 20 min slot: ~10 min content, ~10 min discussion. Don't fill every minute.

---

## Slide Content Rules

- Minimal text -- short phrases, not sentences
- **No bullet wrapping** -- every bullet must fit one line. Rewrite if it wraps.
- Statement slides (full-bleed, large type) for key insights
- Two-column layout for genuine comparisons only
- Show evidence directly -- don't say "named customers", just show the table
- Don't over-explain what's on screen
- FAQ: question bold on its own line, answer on the next line below it
- Slide titles: plain and direct ("The problem" not "The real problem")
- Bottom line / callout text: prominent (teal or white), never dimmed gray

---

## Copywriting Rules

- **NO EM DASHES. EVER.** Use commas, colons, or line breaks.
- Lead with the answer in the first 2 minutes -- conclusion first, not build-up
- Story arc: customer problem -> insight that reframes -> proof -> so what
- Win stories: lead with what worked, not the problems or gaps
- Don't say "here's the proof" -- just show it
- Don't say "new motion" unless it actually is a new GTM motion
- Avoid internal jargon the audience won't recognize
- Consistent POV per slide -- don't mix "we did X" and "they did Y"
- Closing slide: empower the audience to act, don't offer to do it for them
- End with a question that opens discussion naturally

---

## Branding

| Role | Color | Hex |
|---|---|---|
| Background | Near-black | `#1F2023` |
| Primary text | Off-white | `#F5F7FA` |
| Body / supporting | Gray | `#B9BCC5` |
| Dividers | Dark gray | `#606060` |
| Section labels / accents | HCP purple | `#B87FFF` |
| Emphasis (1-2 moments per deck) | Brand teal | `#14B8C8` |
| tfctl only | Terraform green | `#4CAF50` |

- Logo: HCP Terraform on-dark lockup, top-right on every slide
- Font sizes: titles 22-34pt, body 14-17pt, table/fine print 11-13pt

### Color pairing (with HCP purple on dark)
- Best: Nomad green `#00CA8E` -- WCAG AAA (7.63:1), split-complementary
- Acceptable: Packer blue `#02A8EF` -- AA (6.09:1)
- Avoid: Vault gold (muddy), Consul pink (fails AA), Boundary red (error semantics)

---

## Demo Slides

- Recorded demo with live narration preferred over fully live
- Keep demo under 3-4 min (60s ideal for embeds)
- Demo slide: just the word "demo" on screen; all context in speaker notes
- Speaker notes: exact moments to call out during playback
- The surrounding slides carry the story; the demo carries the proof
- See `terminal-demo` skill for full recording pipeline (VHS `.tape` files, agg, ffmpeg)

---

## Process

- Build with `python-pptx`; save `build_deck.py` alongside the output
- Prefer `.pptx` over Google Slides for HashiCorp internal -- dark theme renders better
- Check with the session organizer on specific asks before finalizing structure
- Ask what was already shared with the audience so framing aligns
