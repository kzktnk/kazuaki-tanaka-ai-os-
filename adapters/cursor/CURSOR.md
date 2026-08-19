# Kazuaki Tanaka AI OS

# Cursor Adapter

**Version:** v0.9 Bootstrap  
**Status:** Active  
**Applies to:** Cursor Desktop and repository-aware Cursor agents  
**Document role:** Tool-specific execution instructions for using the Kazuaki Tanaka AI OS in Cursor

---

## 1. Purpose

This file defines how Cursor should use the Kazuaki Tanaka AI OS.

Cursor is the primary repository-aware execution environment for:

- reading AI OS context
- creating and editing Markdown files
- reviewing repository consistency
- applying standards and frameworks
- performing knowledge migration
- maintaining cross-references
- preparing changes for Git commit

This adapter translates the model-independent AI OS into Cursor-specific operating behavior.

It does not replace:

- `AI_OPERATING_MANUAL.md`
- `CONTEXT_ROUTING.md`
- `ARCHITECTURE.md`
- files under `core/`, `standards/`, `frameworks/`, `domains/`, `technology/`, or `knowledge/`

Those files remain the source of truth.

---

## 2. Mandatory Startup Sequence

Before starting a non-trivial task, Cursor should:

1. Read `AI_OPERATING_MANUAL.md`.
2. Read `CONTEXT_ROUTING.md`.
3. Classify the task.
4. Load the minimum relevant context.
5. Confirm the intended files to read or modify.
6. Execute the task.
7. Apply the relevant quality standards.
8. Check repository consistency.
9. Summarize changes.
10. Identify whether new reusable knowledge should be migrated.

Do not begin broad repository edits before completing this sequence.

---

## 3. Default Context Loading

For significant work, load:

- `AI_OPERATING_MANUAL.md`
- `CONTEXT_ROUTING.md`
- `core/principles.md`
- `core/identity.md`
- `core/values.md`
- `core/reasoning.md`

Then load task-specific files according to `CONTEXT_ROUTING.md`.

Do not load the entire repository unless the task requires repository-wide analysis.

---

## 4. Task Execution Modes

Cursor should operate in one of the following modes.

### Ask Mode

Use for:

- repository assessment
- explaining structure
- identifying missing files
- proposing changes
- reviewing architecture
- generating commands or implementation plans

Ask Mode should not claim that files were created or modified.

### Agent Mode

Use for:

- creating files
- editing files
- restructuring directories
- updating cross-references
- applying repository-wide changes
- performing migration work
- validating consistency after changes

Before making substantial changes, provide a concise implementation plan.

After making changes, provide a summary.

### Manual Edit Mode

Use when the user prefers to:

- create a file directly
- paste approved content
- make a small controlled change
- avoid broader Agent changes

Cursor should preserve the user-provided content unless explicitly asked to improve it.

---

## 5. File Creation Rules

When creating a new file:

1. Confirm the correct directory.
2. Confirm that a similar file does not already exist.
3. Use lowercase English and hyphens for file names, except where tool conventions require otherwise.
4. Include a clear title and purpose.
5. Add version or status where useful.
6. Add cross-references where relevant.
7. Avoid client-confidential content.
8. Do not create empty directories unless needed immediately.
9. Do not duplicate source-of-truth content into adapters.

Examples:

```text
frameworks/decision-velocity.md
standards/consulting-review.md
playbooks/wbs-design.md
knowledge/patterns/organizational-memory.md
```

Tool-specific exceptions include:

```text
AI_OPERATING_MANUAL.md
CONTEXT_ROUTING.md
ARCHITECTURE.md
CURSOR.md
CLAUDE.md
```

---

## 6. Editing Rules

When editing an existing file:

- preserve the file's purpose
- avoid unnecessary rewrites
- remove duplication where possible
- maintain terminology consistency
- preserve useful nuance
- state assumptions when content is incomplete
- update cross-references when file names or responsibilities change
- do not silently change architecture

If a change affects repository structure or source-of-truth rules, update as appropriate:

- `ARCHITECTURE.md`
- `AI_OPERATING_MANUAL.md`
- `CONTEXT_ROUTING.md`
- relevant directory README files
- `CHANGELOG.md` (when present)

---

## 7. Proposal and Deliverable Review

When asked to review a proposal, presentation, steering committee document, or consulting deliverable:

Load:

- core context
- `standards/consulting-review.md`
- `standards/writing.md`
- relevant framework files
- relevant domain files
- relevant project context

Review for:

- strategic alignment
- logical consistency
- completeness
- executive readability
- decision readiness
- execution feasibility
- missing assumptions
- risks
- prioritization
- next actions

Do not limit the review to wording or formatting.

Improve the thinking.

---

## 8. Writing Tasks

When asked to create or revise:

- LinkedIn posts
- note articles
- emails
- executive messages
- presentation text
- proposals

Load:

- core identity and values
- `standards/writing.md`
- relevant framework or domain files
- related prior source content where appropriate

Adapt:

- audience
- tone
- length
- language
- structure
- evidence level
- call to action

Do not create generic content that ignores the AI OS.

---

## 9. Framework Work

When creating or updating a framework:

Load:

- the existing framework, if present
- related lessons
- related patterns
- related decisions
- relevant standards
- relevant domain or technology files

A framework should define:

- purpose
- scope
- when to use
- inputs
- structure
- method
- outputs
- limitations
- risks
- related assets

Do not convert a single project experience directly into a universal framework without stating limitations.

---

## 10. Knowledge Migration

When asked to migrate an asset:

1. Preserve the source.
2. Extract observations.
3. Identify principles.
4. Identify lessons.
5. Identify recurring patterns.
6. Identify framework implications.
7. Identify standard or playbook implications.
8. Remove confidential or project-identifying details.
9. Create or update the appropriate files.
10. Add cross-references.
11. Update `knowledge/index/master-index.md` and any domain index (`linkedin-series-index.md`, `legacy-source-index.md`).
12. Update `CONTEXT_ROUTING.md` if new assets should load for a task type.
13. Produce a migration summary.

Possible outputs include:

- `knowledge/source/...`
- `knowledge/lessons/...`
- `knowledge/patterns/...`
- `knowledge/decisions/...`
- framework updates
- standard updates
- playbook updates

Do not create every possible output automatically.

Create only assets that are genuinely supported and reusable.

---

## 11. Source Preservation

When preserving source content such as LinkedIn posts:

Preferred structure:

```text
knowledge/source/linkedin/
└── 014/
    ├── en.md
    ├── ja.md
    ├── metadata.md
    └── assets/
```

Use both English and Japanese source files when both are authoritative versions.

`metadata.md` should include, where known:

- source ID
- title
- publication date
- language
- tags
- related frameworks
- related patterns
- related lessons
- migration status

Do not treat a translation as disposable if it contains audience-specific adaptation.

---

## 12. Repository Search Behavior

Before creating new content:

1. Search file names.
2. Search headings.
3. Search key concepts and synonyms.
4. Check related framework, standard, lesson, and pattern files.
5. Reuse or extend existing assets where appropriate.

Prefer updating an existing source-of-truth file over creating overlapping files.

---

## 13. Repository-Wide Review

When asked to review the repository:

Check:

- missing files
- duplicate concepts
- conflicting guidance
- broken cross-references
- inconsistent naming
- empty placeholders
- obsolete adapters
- architecture drift
- source-of-truth violations
- confidential content risk
- missing version or status information
- files that should be promoted, merged, or archived

Report findings by priority.

Do not restructure the repository without explicit approval.

---

## 14. Confidentiality Rules

Never write the following into the repository:

- client-confidential information
- credentials
- API keys
- access tokens
- private URLs
- internal hostnames
- non-public security configurations
- personal sensitive information
- unapproved proprietary content

When deriving knowledge from project work:

- anonymize
- generalize
- preserve relevant conditions
- remove identifying details
- state limitations
- store only reusable knowledge

If uncertain, stop and flag the risk.

---

## 15. Change Summary

After file changes, provide:

### Files created

List all new files.

### Files modified

List all edited files.

### Key changes

Summarize substantive changes.

### Assumptions

State important assumptions.

### Follow-up

Identify any recommended next step.

Do not claim a file was changed unless it was actually changed.

---

## 16. Git Workflow

Cursor may prepare file changes, but Git history should remain clear.

Recommended commit message patterns:

```text
feat(core): define decision-making principles
feat(frameworks): expand AI governability framework
docs: add context routing rules
refactor(knowledge): consolidate governance patterns
fix(standards): correct review criteria
chore: update repository structure
```

Cursor should suggest a commit message after meaningful changes.

Do not commit or push unless the user explicitly requests it and the environment supports it.

---

## 17. Completion Checks

Before finishing a task, verify:

- the correct routing was used
- the relevant core files were applied
- the correct standards were applied
- file placement is correct
- duplication was avoided
- terminology is consistent
- cross-references are valid
- confidentiality is protected
- output is actionable
- new knowledge was identified where appropriate

For repository changes, also verify:

- files exist in the intended path
- Markdown is valid and readable
- headings are consistent
- no accidental placeholders remain
- architecture remains coherent

---

## 18. Failure and Escalation Rules

Stop and ask for guidance when:

- the requested change conflicts with the source-of-truth hierarchy
- a confidential detail may be persisted
- a broad restructure is required
- multiple files claim the same responsibility
- the correct project context is unavailable
- the requested result requires unsupported assumptions
- an existing file appears authoritative but outdated
- the task requires accountable human approval

Do not hide ambiguity.

---

## 19. Cursor-Specific Behavioral Rules

Cursor should:

- inspect the actual repository before proposing changes
- distinguish Ask Mode from Agent Mode
- avoid claiming execution while in Ask Mode
- use repository-aware search before generating new files
- prefer small, reviewable changes
- show implementation plans for larger tasks
- preserve user-approved content
- avoid uncontrolled repository-wide rewrites
- explain why a file should be created, changed, merged, or removed
- identify when a task creates migration candidates

---

## 20. Default Response Pattern

For a substantial Cursor task:

### Before execution

```text
Task classification:
Context to load:
Files expected to change:
Implementation plan:
```

### After execution

```text
Completed:
Files created:
Files modified:
Key decisions:
Assumptions:
Suggested commit message:
Recommended next step:
```

Keep these summaries concise.

---

## 21. Guiding Statement

> Cursor is the execution environment, not the source of truth.

The source of truth is the model-independent AI OS.

Cursor should read it, apply it, improve it carefully, and leave the repository more coherent than it found it.
