---
name: create-presentation
description: Build a HashiCorp internal presentation (pptx) from scratch using python-pptx, in the dark Helios style by default (Terraform purple, HashiCorp Sans, product-color accents). Use when asked to create a deck, build slides, or make a presentation. Supports "--think" flag to run thought-partner first.
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

## Classic style (alternate, the original ILM look)

Use only when the user asks for the classic dark deck. The default is the Helios style above.

| Role | Color | Hex |
|---|---|---|
| Background | Near-black | `#1F2023` |
| Primary text | Off-white | `#F5F7FA` |
| Body / supporting | Gray | `#B9BCC5` |
| Dividers | Dark gray | `#606060` |
| Section labels / accents | HCP purple | `#B87FFF` |
| Emphasis (1-2 moments per deck) | Brand teal | `#14B8C8` |
| tfctl only | Terraform green | `#4CAF50` |

- Logo: HCP Terraform on-dark lockup, top-right on every slide (ask the user for the file; if none is supplied, draw the mark plus text and say so)
- Font sizes: titles 22-34pt, body 14-17pt, table/fine print 11-13pt

### Color pairing (with HCP purple on dark)
- Best: Nomad green `#00CA8E` -- WCAG AAA (7.63:1), split-complementary
- Acceptable: Packer blue `#02A8EF` -- AA (6.09:1)
- Avoid: Vault gold (muddy), Consul pink (fails AA), Boundary red (error semantics)

---

## Helios style (default look for decks)

Use this unless the user asks for another style. **Assume no local files.** Do not require a logo, photos, fonts, templates or any file on disk. Use what the user supplies, fall back to drawn or default equivalents when they supply nothing, and tell the user in chat what you substituted.

A self-contained kit lives in `reference/` (needs only python-pptx and Pillow):

- `reference/helios_kit.py`: `Deck` class with every layout (title, agenda, section, cards, rows, statement, big, cascade, scorecard, shoutouts, welcome, close). It draws the Terraform mark natively, so no image file or network is needed.
- `reference/example_helios_deck.py`: runnable example with placeholder content and no files
- `reference/install_hashicorp_sans.py`: optional, installs HashiCorp Sans from the public Helios site (internal use only, never commit the font files). Without it the kit falls back to Arial.

### Visual system

| Role | Value |
|---|---|
| Background / text / muted | `#000000` / `#FFFFFF` / `#B2B6BD` |
| Hairlines, card border, card fill | `#3B3D45`, `#0C0C0E` |
| Primary | Terraform purple: `#B87FFF` for text and accents, `#7B42BC` for fills and the banner gradient start |
| Accent rotation | Nomad green `#00CA8E`, Packer blue `#02A8EF`, Waypoint teal `#14C6CB`, Vault yellow `#FFCF25`, Consul pink `#E03875` (pink and yellow for fills or sparing use) |
| Fonts | `HashiCorp Sans SemiBold` for headings, `HashiCorp Sans` for body, `Menlo` for small tags and labels. If HashiCorp Sans is not installed the kit falls back to Arial and Courier New. Fonts are not embedded in the pptx, so tell the user the look needs the font installed wherever the deck opens. |

- Top banner: 0.34in gradient strip (`#7B42BC` to `#B87FFF`) with the deck name in Title Case, centered, 11pt
- HCP Terraform logo top-right, placed below the banner (y 0.5in). Pass the official lockup if the user provides it. Otherwise the kit draws the mark plus "HCP Terraform" text; tell the user to swap in the official logo.
- Decoration: the Terraform mark alone (single-colour `#7b42bc`, no "HCP Terraform" text), drawn natively by the kit, on the right of title, section and closing slides. Never invent abstract decoration such as grids of squares.
- Slide titles 34pt semibold; body 15pt; labels 11 to 12pt; stat numbers 36pt in an accent colour
- Cards: square corners, 1pt `#3B3D45` border, 0.07in top bar in the next accent colour. Rows: label in an accent colour, description in muted grey, hairline between rows.
- Tags (Q4, Discovery): outlined, mono, purple. Size the box from the text length (mono is wide) and turn wrapping off.
- Arrows between columns are drawn shapes. Never use the arrow glyph, it renders as a dash.
- Sentence case for every label and header (no mixing with ALL CAPS). Page counter bottom-left as "n / N".

### Do not do

- Never put the name, logo, or mark of an inspiration site (Vercel, A24, Teenage Engineering, etc.) on a slide
- No footers, footnotes, caveats, or sources on slides. The slides are presented to an audience. Put caveats, sources and "what I could not verify" in chat, and sources in the sidecar notes file.
- No audience labels on the title slide ("for engineering and design")
- No combined sentences on one line. Split into separate lines and give the first line the accent colour.
- No jargon on slides for a mixed audience (engineering plus design): replace internal service or library names, error-tracker names, spec terms and ticket slang with plain outcomes ("slow database query", not "un-indexed column")
- No wrapped bullets. Shorten the text, or shrink the font (12pt when there are 4 cards).

### Deck skeleton for team and quarterly decks

1. Title (two lines, first in purple, plus one plain subtitle)
2. Agenda as slide 2 (numbered, accent-coloured numbers), then a section divider before each section (number, name, Terraform mark)
3. A recap can open with a welcome slide for new teammates: circular photo crops with a coloured ring, name, role, one line. Ask the user to attach the photos and say where to save them; until they exist the circle shows initials.
4. Recap slides: cards for projects, rows for platform work, then a scorecard, then shoutouts
5. Why this work: priorities list, then the cascade slide (company goal, then org priority, then our work, with coloured left bars and drawn arrows), then an insight statement
6. One slide per project: tag, one-sentence description, one or two plain lines
7. For a project with several slides: hook, project slide, why (friction, then the business reason), timeline or order
8. Close with "Thank you" unless the user wants a discussion question

### Build and delivery rules (PowerPoint by default, Keynote supported)

- Default target is PowerPoint. The same `.pptx` also opens in Keynote. If the user says they use Keynote, say nothing more is needed except the notes and font points below.
- Build with `python-pptx` via `reference/helios_kit.py`; keep the build script next to the output
- Speaker notes go to a sidecar `<deck>-notes.md` by default (the kit does this). Keynote rejects the notes python-pptx writes into a pptx. Only embed notes in the pptx (`embed_notes=True`) when the user wants real PowerPoint speaker notes and does not use Keynote.
- The kit rewrites theme and master fonts so no Calibri, Arial or Helvetica remains except as the stated fallback. Check with `unzip -p deck.pptx 'ppt/slides/*.xml' 'ppt/theme/*.xml' | grep -o 'typeface="[^"]*"' | sort | uniq -c`.
- After installing fonts, fully quit and relaunch PowerPoint or Keynote
- If LibreOffice (`soffice`) and `pdftoppm` exist, render to check: `soffice --headless --convert-to pdf deck.pptx`, `pdftoppm -r 40 -png`, a contact sheet with Pillow, then look at it. Write the sheet to a new filename each time, the image viewer caches old paths. If they do not exist, ask the user to open the deck and report problems.
- Never overwrite a deck the user may be editing. If they say they are editing other slides, write the changed slide to a separate one-slide file (build to a temp path, keep one slide with python-pptx) and tell them to paste it in.
- After a rebuild, reopen the deck: `open deck.pptx` (default app), `open -a "Microsoft PowerPoint" deck.pptx` or `open -a Keynote deck.pptx` on macOS. Only rebuild the style the user is actually using.
- Keep a build script per deck so changes are reproducible. When the user asks for a small change, change the script and rebuild.

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
- Talk to the user in chat about caveats and gaps. Slides carry only what is presented.
- Check with the session organizer on specific asks before finalizing structure
- Ask what was already shared with the audience so framing aligns
