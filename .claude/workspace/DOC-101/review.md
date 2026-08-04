# Review: DOC-101

File reviewed: `docs/api/tasks.md`

No lint script exists at `.claude/skills/doc-review/scripts/lint.py` in this repo, so Step 1 (mechanical lint) was skipped. Findings below come from the qualitative pass (Step 2) plus targeted regex checks for the deterministic rules the linter would otherwise cover (em dashes, semicolons, bare demonstrative pronouns), and the clarity sub-agent check (Step 3).

## Findings

### All headings (file-wide, including new "Comment Structure" / "9. Add a Comment" / "10. List Comments" / "11. Delete a Comment"): Heading case

Severity: Major
Confidence: Medium
Problem: CLAUDE.md states "Sentence case for all headings," but every heading in this file — including the eight pre-existing ones (`## Task Structure`, `## 1. Create a Task`, `## 7. Add Checklist Item`, etc.) and the four new ones added for this ticket — uses title case. The new headings match the file's existing (non-compliant) convention exactly, so this is not a regression introduced by this draft, but it is a real, file-wide style guide violation. Confidence is Medium rather than High because CLAUDE.md also prioritizes "Consistency with existing docs" and "Minimal diffs" above stylistic rewrites not explicitly requested — normalizing only the four new headings to sentence case would make them inconsistent with the eight surrounding ones, which arguably hurts scanability more than it helps.
Suggested rewrite: N/A for this ticket. If the writer wants this fixed, it should be a single follow-up pass across the whole file (all 12 headings), not a partial fix scoped to the new content.

### Line 320: Em dash inside a VERIFY marker

Severity: Minor
Confidence: High
Problem: `— confirm whether comments follow that pattern instead.` uses an em dash, which the style guide prohibits. This has zero reader impact since HTML comments don't render on the published site, but it's a literal style-guide violation in the source and a lint script would flag it.
Suggested rewrite: `...envelope. Confirm whether comments follow that pattern instead.`

### Lines 289 and 307: Semicolons inside GAP markers

Severity: Minor
Confidence: High
Problem: Both lines use a semicolon to join two clauses (`...per the source ticket; confirm whether...` and `...missing or empty text; the source ticket does not confirm...`), which the style guide prohibits. Same as above: invisible to readers, but present in source.
Suggested rewrite: Line 289: split into two sentences at the semicolon. Line 307: same.

## Clarity sub-agent check

A context-free sub-agent was given only the document text and asked three questions. Its answers:
1. What the doc helps you do: correctly identified it as Tasks API reference covering CRUD, progress, checklists, and comments, with request/response shapes, roles, and error codes.
2. Audience: correctly identified engineers integrating with the API programmatically.
3. First action: correctly identified checking your role (Admin/Member) and consulting the Endpoints Overview table to find the right endpoint.

All three answers match the doc's actual purpose and structure. No confusion was introduced by the new comments content — no finding here.

## Summary

The new comments content (Comment Structure section, sections 9–11, and the three added table rows) is consistent with the existing file's terminology, tone, and structural pattern, and the clarity check confirms the page still reads clearly with the addition. Every issue found here is Minor except one file-wide heading-case violation that predates this draft and isn't safe to fix in isolation without a broader normalization pass. The single most impactful change available right now is stripping the em dash (line 320) and two semicolons (lines 289, 307) from the marker comments, since those are unambiguous, zero-risk fixes. Findings: 1 Major, 2 Minor, 0 Critical.
