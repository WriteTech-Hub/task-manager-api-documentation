description: Structured editorial review against the style guide, findings only.
---

Review the technical document at $ARGUMENTS against our style guide. Do not rewrite or modify the source text. Provide findings only. Do not invent product behavior.

## Review dimensions

Evaluate each dimension independently. Only flag genuine problems.

### Concision
Flag sentences using more words than necessary. Setup phrases, hedging language, and redundant qualifiers are the common culprits. Test: can the sentence be shortened without losing meaning?

### Information density
Flag sentences or paragraphs delivering little or no new information: restatements of what a heading already says, throat-clearing introductions, transition sentences describing what the next paragraph will say.

### Scanability
Flag:
* Paragraphs longer than 5 sentences that could be lists
* Sections with no visual break between dense prose blocks
* Missing or weak lead sentences that do not orient the reader

### Progressive disclosure
Flag when information appears before the reader needs it. Background and context follow actionable content, not precede it.

### Action clarity
For procedural sections, flag instructions that are ambiguous, incomplete, or missing an explicit outcome.

### AI-sounding phrasing
Flag: "delve into", "it's worth noting", "comprehensive", "robust", "leverage", "seamlessly", "empower", "streamline", "unlock", "harness", "moreover", "furthermore", "take advantage of", "this allows you to", "this enables you to."

### Style guide compliance
* No em dashes
* No semicolons
* No bare demonstrative pronouns
* Sentence case for all headings
* Consistent list marker style

## Output format

### Summary
One paragraph: what the doc covers, whether it meets its goals.

### Findings table

| Severity | Location | Issue | Rule violated | Fix |
|---|---|---|---|---|
| Critical/Major/Minor | heading or phrase | description | style rule | one-line fix |

### Top 3 changes for biggest impact
Format: Outcome → Action.

### Open questions
Clarifying questions about gaps or ambiguous content.