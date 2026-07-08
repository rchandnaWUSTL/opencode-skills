---
name: prd-generator
description: Generate a Product Requirements Document (PRD) from customer evidence and context. Use when asked to write a PRD, create product requirements, or document a feature specification. Supports "--think" flag to run thought-partner first.
---

# Skill: PRD Generator

Generate a Product Requirements Document from customer evidence and context.

---

## Input

- **Topic**: The feature or capability to write the PRD for
- **Evidence**: Customer notes, call transcripts, research -- paste directly or reference files
- **Context** (optional): Engineering docs, prior art, related specs -- include anything relevant

If evidence is thin (fewer than 2 customers or 3 mentions), say so and offer to produce a signal brief instead (a shorter doc capturing what's known and what's needed to proceed).

---

## Document Structure

### Canonical Section Order

Every PRD follows this exact order:

1. **# [Title]**
2. **One-sentence summary** (first line after title, no heading)
3. **## Overview**
4. **## Background**
5. **## Problem**
6. **## Personas**
7. **## Phases & Requirements Table**
8. **## Phase N: [Phase Title]** (repeated per phase)
9. **## User Research**
10. **## Out of Scope**

### Optional Sections (insert at specific positions)

Only include when the topic explicitly warrants it:

- **## Assumptions** -- after Problem, before Personas
- **## Rollout Plan** -- after all Phase sections, before User Research
- **## Measuring Success** -- after all Phase sections, before User Research
- **## Analytics Requirements** -- after all Phase sections, before User Research
- **## Future Possibilities** -- after Out of Scope
- **## Pricing & Packaging** -- after Out of Scope
- **## Breaking Backwards Compatibility** -- after Background, before Problem
- **## Appendix** -- always last

### Prohibited Sections

Never include these -- they don't belong in a PRD:

- Executive Summary
- Solution Overview
- Technical Considerations
- Risks & Mitigations
- Go-to-Market
- Success Metrics (use "Measuring Success" if needed)
- Open Questions (questions belong inside requirements as "Considerations")
- Dependencies
- Timeline / Milestones
- Resources Required

---

## Section Rules

### One-Sentence Summary
Max 30 words. Captures what the feature does and why it matters. Understandable without prior context.

### Overview
2-4 paragraphs: what the feature is, why it matters (grounded in evidence), how it fits the product, what's in scope.

### Background
Current state, how customers solve this today (workarounds, third-party tools), relevant industry context, any prior internal work.

### Problem
Use Jobs To Be Done (JTBD) format for each distinct problem:

```
**When** [situation],
**I want** [action],
**so that** [outcome].
```

Each JTBD should be grounded in real evidence. Aim for 3-6 JTBDs.

### Personas
For each persona:
- **Name**: Role title (e.g. "Platform Engineer", "Security Architect")
- **Description**: 2-3 sentences -- what they do, what they care about, how they interact with the product
- **Key needs**: Bullets specific to this feature

### Phases & Requirements Table

```markdown
| Phase | Requirement | Description |
|---|---|---|
| Phase 1 | [title] | [one-line description] |
```

Phase 1 = minimum viable scope addressing the core JTBD. Only add Phase 2+ if evidence supports it.

### Phase Requirements

Each requirement (`### Requirement Title`) contains:

**Narrative**: What the requirement is, why it matters, how it connects to the broader feature.

**Acceptance Criteria**: Pass/fail behavioral conditions using "must" language. 3-6 per requirement. Each must be testable.

What belongs:
- User-visible actions
- System behavior from the user's perspective
- Observable outcomes
- Non-functional requirements at a product level

What does NOT belong (these are engineering design doc concerns):
- API endpoint specs
- Database schemas
- Component names
- Architecture or data flow details
- Implementation technology choices

**Considerations**: Genuine open questions and trade-offs that need resolution. At least one per requirement. These surface risks and unknowns early -- don't fabricate them for completeness.

### User Research

For each customer:

```markdown
### [Customer / Source]

**Calls / references:** [N]

[Summary of what this customer said, with dates and paraphrased quotes]
```

Never fabricate evidence. If evidence is thin, say so explicitly.

### Out of Scope

5-10 specific items a reader might expect to be in scope but aren't. Include a brief reason for each.

---

## Voice & Style

1. **Plain language** -- write for PMs, engineers, and designers. No marketing language.
2. **Evidence-grounded** -- every major claim traces to customer evidence, engineering constraints, or industry standards.
3. **Default state off** -- any new feature, toggle, or configuration defaults to off/disabled unless there's a compelling reason otherwise.
4. **Specific over vague** -- name the thing. "Support Acme Scanning as a provider" not "support additional scanning options."
5. **Honest about unknowns** -- use "TBD -- [what's needed to resolve]" rather than guessing.
6. **No filler sections** -- if a conditional section has no real content, omit it entirely.

---

## Behavior

1. Gather evidence from whatever the user has provided (pasted notes, referenced files, context)
2. Check evidence threshold -- if thin, flag it and offer a signal brief instead
3. Generate the full PRD draft
4. Display it to the user
5. Ask for approval before saving to a file
6. On approval, save to `[topic-slug]-prd-[YYYY-MM-DD].md` in the current directory (or wherever the user specifies)
