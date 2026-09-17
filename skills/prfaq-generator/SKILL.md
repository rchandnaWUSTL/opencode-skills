---
name: prfaq-generator
description: Generate a working-backwards PRFAQ (Press Release + FAQ) from a PRD or from raw customer evidence. Use when asked to write a PRFAQ, press release, or working-backwards document. Supports "--think" flag to run thought-partner first.
---

# Skill: PRFAQ Generator

Generate a working-backwards PRFAQ -- a press release written as if the product already shipped, followed by the questions customers and internal stakeholders would ask.

The point of the exercise is to find out whether the idea is worth building. If the press release is boring, the idea is boring. Say so.

---

## Input

**Mode A -- from a PRD.** The user provides a PRD path or pastes PRD content. Extract problem framing, requirements, personas, and evidence from it rather than re-deriving them.

**Mode B -- standalone.** The user names a topic. Gather evidence from whatever they provide: customer notes, call transcripts, support tickets, research, competitor docs.

Mode detection: if a PRD is referenced or pasted, use Mode A. Otherwise Mode B.

Before writing, ask for anything missing that materially changes the document:
- Company name and one-line company description (for the dateline)
- Product name
- Target launch timeframe (for the dateline date)
- Whether a real customer has agreed to be quoted

If the user doesn't want to answer, use placeholders and flag them.

### Thin evidence

In Mode B, if evidence is thin (fewer than 2 distinct customers or fewer than 3 total mentions), don't quietly generate a polished PRFAQ on top of nothing. Say what you found and offer either (a) a shorter signal brief capturing what's known and what's needed, or (b) proceeding with the PRFAQ clearly marked as speculative. Let the user choose.

In Mode A, the PRD is the evidence gate. Proceed.

---

## Document Structure

Sections in this order:

1. One-sentence summary
2. Problem Statement
3. Press Release
4. External FAQs
5. Internal FAQs
6. Appendix
7. Review Tracking

---

## Section Rules

### One-Sentence Summary

First line after the title, no heading. Max 30 words. What the thing does and who it's for. Executive audience -- no jargon, no internal codenames.

### Problem Statement

2-3 paragraphs:

- The customer problem, grounded in evidence
- Why it matters now -- market timing, customer urgency, competitive pressure
- The gap between what customers need and what exists today

This section must stand alone. A reader who skips straight here should understand the motivation without reading anything else.

### Press Release

Eight elements, fixed order. Write as if the feature already shipped. Past and present tense only -- "today announced", "customers can now". Future tense means you're still pitching, not announcing.

**Heading.** Max 15 words. Names the product and the capability. No version numbers.

**Subheading.** One sentence expanding the headline. Names the target audience and the key benefit.

**Dateline paragraph.** 3-5 sentences. Format: `[CITY], [Month Day, Year] -- [Company], [one-line company description], today announced...` Name the feature, state what it enables, reference the audience, mention one concrete benefit.

**Problem paragraph.** One paragraph on the problem customers faced before this existed. Customer perspective. Reference real pain points from evidence without naming specific customers.

**Solution paragraph.** One paragraph on how it works at a high level. Customer outcomes, not architecture. What can they do now that they couldn't before?

**Customer quote.** Follow the Pixar story spine:

- *Every day...* -- the status quo
- *Until one day...* -- the inciting incident
- *Because of that...* -- consequence; the customer takes action (can repeat to build tension)
- *Until finally...* -- resolution
- *And ever since that day...* -- the new normal

It shouldn't read like it follows a formula word-for-word, but the arc must be there: status quo, disruption, action, resolution, new normal. Ground the "before" beats in actual workarounds from the evidence -- that's what makes a fictional quote credible.

Use a clearly fictional persona by default (e.g. "Jane Doe, Director of Platform Engineering at Example Corp"). Only use a real customer name if the user confirms that customer has agreed to be quoted.

**Exec quote.** Lead with empathy, then announce. Structure:

1. Acknowledge the pain -- "We've heard from teams that..."
2. Show you understand why it's genuinely hard -- operational reality, not marketing speak
3. Announce the solution as the response to that pain -- "That's why we built..."

The reader should feel understood before they feel sold to. A quote that opens with the product has already failed.

**CTA.** One sentence pointing readers to docs or the product page.

### External FAQs

8-12 Q&A pairs for customers and prospects -- questions someone would ask after reading the press release.

- Ground answers in real evidence. If a customer asked exactly this, answer their actual concern
- Plain language, action-oriented -- "How do I..." not "What is the architecture of..."
- Cover: getting started, compatibility with existing setup, migration path, pricing (if known), limitations, timeline
- Order most-likely to least-likely
- 2-5 sentences per answer. If it runs longer, the question should be split

### Internal FAQs

Questions engineering, sales, support, and leadership would ask. Not customer-facing. This is where the PRFAQ earns its keep -- it forces the uncomfortable questions early.

Cover at minimum:

- **Demand / customer evidence** -- cite actual evidence with names and counts. Never "customers have asked for this" without a number
- **Pricing impact** -- "TBD with business planning" if undetermined. Never guess at pricing
- **Engineering scope** -- reference spikes or design docs if they exist, otherwise "TBD -- engineering spike needed to estimate"
- **Competitive landscape** -- ground in what's actually known about competitor behavior, not speculation
- **Support implications** -- what breaks, what generates tickets, what needs docs
- **Risks and dependencies** -- what has to be true for this to work

For anything unresolved: `TBD -- [what would resolve it]`. Every TBD names its own exit condition. A TBD without one is just a blank.

### Appendix

Supporting material that doesn't belong inline: related tickets or epics, engineering docs, prior art, evidence sources consulted, related PRDs.

If there's nothing, write "No appendix materials at this time." rather than dropping the section -- readers go looking for it.

### Review Tracking

Always included, always the same shape:

```markdown
## Review Tracking

| Reviewer | Role | Status | Date | Notes |
|----------|------|--------|------|-------|
| | Engineering | Not Started | | |
| | Product Design | Not Started | | |
| | Product Marketing | Not Started | | |
| | Support Enablement | Not Started | | |
| | Security | Not Started | | |
| | Partner / Alliances | Not Started | | |
```

Leave reviewer names blank unless provided. Adjust rows to fit the org if the user names different stakeholders. Status values: `Not Started`, `In Review`, `Approved`, `Changes Requested`.

---

## Voice & Style

1. **Announcement tone, not template tone.** Write like a real product announcement. No superlatives -- "revolutionary", "groundbreaking", "game-changing" all mean nothing. If the feature is good, describing it plainly is enough.
2. **Customer-centric framing.** "Customers can now choose their scanning provider," not "We built a provider abstraction layer." Every section centers on what the customer can do.
3. **Evidence-grounded.** Fictional quotes still reflect real workarounds. FAQs anticipate questions people actually asked.
4. **Honest about unknowns.** TBDs with exit conditions. Never present a guess as a decision.
5. **No filler.** If an answer is "we don't know yet", say that and say what would resolve it. Don't pad.
6. **Specific over vague.** Name the thing.

---

## Behavior

1. Detect mode; gather the PRD or the evidence
2. Ask for missing company/product/date details
3. Check the evidence threshold in Mode B; flag if thin
4. Generate the full draft
5. Display it and give the user an honest read -- if the press release is weak, say why. A boring press release is the signal the exercise exists to produce
6. Ask for approval before saving
7. On approval, save to `[topic-slug]-prfaq-[YYYY-MM-DD].md` in the current directory, or wherever the user specifies

---

## Worked Example (abbreviated)

Real PRFAQs run longer. This shows shape, not length.

```markdown
# Vulnerability Scanning Provider Selection -- PRFAQ

Enterprise customers can now use their preferred vulnerability scanner in the registry instead of being locked to the built-in default.

## Problem Statement

Enterprise organizations with mature security tooling don't get to choose which vulnerability scanner they use. Compliance frameworks, security team mandates, and existing vendor contracts dictate which platform is authoritative. When the registry only supports one scanner, these organizations run parallel workflows: one inside the product for registry visibility, one outside for compliance.

This isn't theoretical. Customers in financial services already run their mandated scanner's CLI at build time, then manually cross-reference results against the registry's vulnerability tab. The data lives in two places, neither complete, with no unified view for promotion decisions.

The gap is clear: the registry needs to support the scanners enterprise customers already run.

## Press Release

### Registry Now Supports Third-Party Vulnerability Scanners

Enterprise customers can use their existing scanning deployment as the vulnerability data source, eliminating parallel workflows.

SAN FRANCISCO, March 15, 2026 -- Example Corp, a provider of container supply chain tooling, today announced vulnerability scanning provider selection. Platform teams can now choose their organization's mandated scanner as the vulnerability data source alongside the existing default, bringing compliance-approved scan data directly into the registry. Teams get a single place to review vulnerability data before promoting images to production.

Organizations with existing scanner deployments have struggled with fragmented vulnerability data. Security teams require a specific tool for compliance reporting, but the registry only showed results from its built-in scanner. Platform engineers ran the mandated scanner separately and reconciled results by hand -- brittle, error-prone, and slow.

With provider selection, administrators configure their preferred scanner once at the registry level. Vulnerability data flows into the UI with full severity ratings, affected package details, and remediation guidance. Existing workflows continue unchanged for customers who don't opt in.

> "We used to joke that a new CVE meant canceling your day. Security would flag it, then we'd scramble to find which images had that package. Even after patching, we never knew what was still exposed. Now I open the registry, search the CVE, and see affected images and where they're running. I can file tickets, assign owners, and coordinate deployments with real confidence. I can't imagine going back."
>
> -- Jane Doe, Director of Platform Engineering at Example Industries

> "We've heard from platform teams that they're running two scanners and reconciling the output by hand, usually under time pressure, usually during an incident. That's a genuinely awful place to be, and it's not a problem you can document your way out of. That's why we built provider selection -- so teams use the tool their security org already approved, in the place they already work."
>
> -- Alex Rivera, VP of Product at Example Corp

To learn more, visit the product documentation.

## External FAQs

**Q: Which scanners are supported?**
A: At launch, the built-in default plus one third-party provider. Additional providers will be evaluated based on demand. The default is unchanged for existing registries.

**Q: What happens to my existing scan results if I switch?**
A: Existing results remain visible and are not deleted. New scans use the selected provider. Historical data retains its original provider attribution.

**Q: Can I run both simultaneously?**
A: Dual-provider mode is planned for a future release. At launch, one active provider per registry.

## Internal FAQs

**Q: What is the customer demand?**
A: Three named accounts have raised this directly -- one across three calls (Nov 2025, Dec 2025, Feb 2026) with an explicit request for a provider selector. Two others discussed scanning constraints without naming a specific tool.

**Q: What is the pricing impact?**
A: TBD with business planning. Key question: does provider selection gate on tier, or is it available to all paid customers? This is a bring-your-own-license integration -- we don't resell the scanner.

**Q: What is the engineering effort?**
A: TBD -- engineering spike needed to estimate. The provider abstraction layer and the third-party API integration are the primary new work.

**Q: What breaks in support?**
A: Credential misconfiguration is the likely top ticket driver. TBD -- needs a support enablement doc before GA.

## Appendix

* Related epic: [link]
* Customer evidence: [sources consulted]

## Review Tracking

| Reviewer | Role | Status | Date | Notes |
|----------|------|--------|------|-------|
| | Engineering | Not Started | | |
| | Product Design | Not Started | | |
| | Product Marketing | Not Started | | |
| | Support Enablement | Not Started | | |
| | Security | Not Started | | |
| | Partner / Alliances | Not Started | | |
```
