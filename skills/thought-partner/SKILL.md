---
name: thought-partner
description: Run a structured product thinking framework before committing to a solution. Use when asked to "think through" a feature or decision, or when "--think" or "with thought partner" is appended to any request. Applies JTBD clarity, friction analysis, nudge design, satisfaction prediction, and SCAMPER to surface better alternatives.
---

# Skill: Thought Partner

An opt-in product thinking framework. Interrogates whether a proposed solution is the right one before committing to writing docs. Never runs automatically -- must be explicitly invoked.

---

## Invocation

1. **Flag on any task**: `"Write a PRD for X --think"` or `"Write a PRD for X with thought partner"` -- runs first, suspends for approval, then downstream task continues
2. **Standalone**: `"Think through whether we should build X"` or `"Run thought partner on X"`

---

## Framework

Five stages in order. Each builds on the previous.

### Stage 1: JTBD Clarity

- **Core goal**: What is the customer actually trying to accomplish? (Not what they asked for -- what they need.)
- **Urgency**: Why now? What changed?
- **Stakes**: What happens if this isn't solved?
- **Alternatives**: How are customers solving this today without you?
- **Hiring criteria**: What would make a customer choose this over their current approach?

### Stage 2: Friction Diagnosis

- **Comprehension**: Will customers understand what this is and why they need it?
- **Decision complexity**: How many choices does the customer face? Can decisions be reduced without losing value?
- **Actionability**: Can the customer start immediately, or does it require setup/migration?
- **Cognitive load**: Does this add complexity to existing workflows?
- **Consistency**: Does it work the way the rest of the product works?
- **Distractions**: Does the scope include things that don't serve the core JTBD?

### Stage 3: Motivational Nudge Design

- **Intrinsic nudges**: What makes this inherently valuable? What's the "aha moment"?
- **Extrinsic nudges**: What external factors (compliance, cost savings, mandates) push adoption?
- **Adoption barriers**: What would make a customer say "not now" or "not for us"?

### Stage 4: Satisfaction Evaluation

- **Problem solved?**: Does this fully address the core JTBD, or does it leave a gap the customer still fills manually?
- **Expectations exceeded?**: Is there anything that would pleasantly surprise customers?
- **Retention risk**: What would make a customer stop using it or revert?
- **Advocacy potential**: Would a customer tell a peer about this? What would they say?

### Stage 5: SCAMPER Alternative Challenge

- **Substitute**: What could be replaced with something simpler or more familiar?
- **Combine**: Can this be merged with an existing feature for more value with less surface area?
- **Adapt**: Is there a solution from another product or domain to adapt?
- **Modify**: What if scope changed -- bigger, smaller, more or less opinionated?
- **Put to other use**: Could this solve a different customer problem?
- **Eliminate**: What if you didn't build this? What would customers actually lose?
- **Reverse**: What if you approached this from the opposite direction?

**Creativity prompts:**
- **"Think again"**: Set aside the first answer. What's a completely different way to solve the same JTBD?
- **"Why not both?"**: Are two options being treated as mutually exclusive that could coexist?
- **"Make it unnecessary"**: What if you eliminated the condition that creates the problem?
- **"Cross-domain"**: Take a concept from a completely different industry and apply it here.

---

## Output Format

Display to the user. Save to a file only if explicitly requested.

```markdown
## Thought Partner Analysis: [topic]

### JTBD Clarity
**Core goal:** ...
**Urgency:** ...
**Stakes:** ...
**Alternatives:** ...
**Hiring criteria:** ...

### Friction Diagnosis
| Friction Type | Assessment | Severity |
|---|---|---|
| Comprehension | ... | Low / Medium / High |
| Decision complexity | ... | Low / Medium / High |
| Actionability | ... | Low / Medium / High |
| Cognitive load | ... | Low / Medium / High |
| Consistency | ... | Low / Medium / High |
| Distractions | ... | Low / Medium / High |

**Key friction risks:** [1-2 sentence summary]

### Motivational Nudge Design
**Intrinsic nudges:**
- [nudge] -- [rationale]

**Extrinsic nudges:**
- [nudge] -- [rationale]

**Adoption barriers:**
- [barrier] -- [rationale]

### Satisfaction Evaluation
- **Problem solved?** ...
- **Expectations exceeded?** ...
- **Retention risk:** ...
- **Advocacy potential:** ...

### Alternative Solution Challenge
**SCAMPER:**
- **Substitute:** ...
- **Combine:** ...
- **Adapt:** ...
- **Modify:** ...
- **Put to other use:** ...
- **Eliminate:** ...
- **Reverse:** ...

**Creativity prompts:**
- **Think again:** ...
- **Why not both?** ...
- **Make it unnecessary:** ...
- **Cross-domain:** ...

### Recommendation
**Proceed?** Yes / Yes with modifications / Explore alternative first / No
**Rationale:** ...
**Watch out for:** ...
**Alternatives worth exploring:** ...
```

---

## Behavior

1. Generate the full analysis
2. Display it to the user
3. Pause and ask how to proceed:
   - **"Proceed"**: Run the downstream task if one was queued, otherwise done
   - **"Explore [alternative]"**: Re-run on the specified alternative
   - **"Proceed with [modifications]"**: Pass modifications as context to the downstream task
   - **"Stop"**: End with no further action
