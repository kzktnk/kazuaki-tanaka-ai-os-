# Consulting Review Standard

Version: v0.10 Bootstrap

## Purpose

This document defines the standard review criteria for consulting deliverables.
The objective is to maximize decision quality, not simply improve document appearance.

---

# Review Principles

1. Start from the client's objective, not the document.
2. Evaluate decisions before presentation.
3. Optimize for executive understanding.
4. Prefer simplicity over complexity.
5. Every page must support a business decision.

---

# Review Dimensions

## 1. Strategic Alignment
- Is the business objective clear?
- Does every section support the objective?
- Is there a clear "so what"?

## 2. Logical Consistency
- MECE **when the job of the page is completeness**. A landscape overlay or topology map is not scored as a MECE inventory
- No contradictions
- Clear assumptions
- Clear conclusions

## 3. Completeness
Check for missing perspectives:
- Business
- Organization
- Process
- Technology
- Data
- Governance
- People
- Risk
- Financial impact
- Implementation

## 4. Executive Communication
- One key message per page
- Headings tell the story
- Minimal unnecessary text
- Visuals support the narrative

## 5. Practicality
Recommendations should be:
- Actionable
- Prioritized
- Realistic
- Sequenced

## 6. Quality of Thinking
The review should identify:
- Hidden assumptions
- Trade-offs
- Risks
- Alternatives
- Decision criteria

## 7. Artifact Job
Name the job of the page **before** scoring completeness, MECE, or hearing readiness:

| Job | Passes when | Fails when |
|-----|-------------|------------|
| Landscape / overlay | Running work is placed against the aim | Reviewed as a gap-finding or new-projectization engine |
| Topology map | Connections (and what flows) are visible | Asked to exhaust issues by itself |
| Issue log | Between-unit breaks are listed in named views | Intra-unit known problems and topology share one picture |
| Information request | Questions are locked; method (hearing / form / sponsor-answered) comes after | “Please let us hear from everyone” precedes the questions |
| Change communication | Adoption vs roadmap-formulation is named; kick conditions precede field-team dispatch | Sample stakeholder lists are the first thick artifact |

For multi-project packs, default views for the issue log are Boundary / Dependency / Interface / Consistency / Schedule (`playbooks/cross-project-program-management.md`). Patterns: `knowledge/patterns/scn-as-landscape-not-completeness.md`, `knowledge/patterns/topology-map-vs-issue-log.md`, `knowledge/patterns/formulation-comms-vs-adoption-comms.md`.

---

# Review Output Format

Every review should include:

## Executive Summary
Overall assessment in 3–5 bullets.

## Strengths
What should be preserved.

## Gaps
What is missing or weak.

## Risks
Potential issues if unchanged.

## Recommendations
Prioritized improvements:
- High
- Medium
- Low

---

# Partner-Level Checklist

Before considering a deliverable complete:

- Clear business objective
- Executive-ready storyline
- Logical flow
- Artifact job named (landscape ≠ completeness ≠ issue log ≠ hearing request)
- MECE where the job is completeness
- No unsupported claims
- Risks addressed
- Recommendations prioritized
- Client can make a decision after reading

---

# IBM-style Expectations

A strong consulting deliverable should:
- Create clarity
- Reduce decision uncertainty
- Enable action
- Demonstrate structured thinking
- Balance strategic vision with execution realism

---

# Usage

Prompt example:

> Review this document using `standards/consulting-review.md`.
Focus on artifact job, strategic alignment, logical consistency, executive communication,
completeness, and actionable recommendations.
