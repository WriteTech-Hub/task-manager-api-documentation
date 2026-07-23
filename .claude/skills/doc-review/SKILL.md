---
name: doc-review
description: Perform a strict editorial review of a documentation file before publishing.
---

# doc-review

Perform a strict editorial review of a documentation file before publishing.

## When to use this skill

Run this on any draft before it is published, whether AI-generated or human-written. Use it as a final pass before requesting peer review, or after incorporating feedback to verify all issues are resolved.

## Inputs

* File path of the document to review

## Steps

### Step 1: Run the mechanical linter (optional)

A mechanical linter catches deterministic violations before the qualitative review: things like bare demonstrative pronouns, prohibited terms, sequential list numbering, and heading case. These are high-confidence findings that do not require judgment, so checking them programmatically first saves review time.

If your project has a lint script, run it now:

```bash
python [skills-dir]/doc-review/scripts/lint.py <file-path>
```

Include lint findings in the report as Critical or Major severity based on the rule violated.

**If you do not have a lint script yet, skip this step.** The qualitative review in Step 2 will catch most of the same issues. A lint script is worth adding once you have identified the style violations that appear most often in your project. At that point, automating them pays off. A minimal starting point:

```python
import re
import sys

def lint(filepath):
    findings = []
    with open(filepath) as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        # Em dashes
        if "—" in line or " -- " in line:
            findings.append((i, "Em dash found — use a period, colon, or restructure."))
        # Semicolons
        if ";" in line and not line.strip().startswith("```"):
            findings.append((i, "Semicolon found — split into two sentences."))
        # Bare demonstrative pronouns
        if re.search(r'\b(This|These|That|Those)\s+(prevents|allows|enables|means|makes|shows|helps)', line):
            findings.append((i, "Bare demonstrative pronoun — follow with a noun."))
        # Sequential list numbering (2., 3., etc.)
        if re.match(r'^\s*[2-9]\d*\.', line):
            findings.append((i, "Sequential list number — use '1.' for all items."))
        # Prohibited terms
        for term in ["utilize", "leverage", "seamlessly", "robust", "unlock"]:
            if term.lower() in line.lower():
                findings.append((i, f"Prohibited term: '{term}'."))

    return findings

if __name__ == "__main__":
    issues = lint(sys.argv[1])
    if issues:
        for lineno, msg in issues:
            print(f"Line {lineno}: {msg}")
        sys.exit(1)
    else:
        print("No lint errors found.")
        sys.exit(0)
```

Extend this with rules specific to your style guide. Each rule should be deterministic. If you find yourself adding judgment calls to the script, those belong in the qualitative review instead.

### Step 2: Qualitative review

Read the full document and evaluate each dimension below. Flag genuine problems only. Do not flag hypothetical ones.

**Concision**
Flag sentences that use more words than necessary. Setup phrases, hedging language, and redundant qualifiers are the most common culprits. Test: can the sentence be shortened without losing meaning?

**Information density**
Flag sentences or paragraphs where little or no new information is delivered: restatements of what a heading already says, throat-clearing introductions, and transition sentences that describe what the next paragraph will say.

**Scanability**
Flag:
* Paragraphs longer than 5 sentences that could be lists
* Sections with no visual break between dense prose blocks
* Missing or weak lead sentences that do not orient the reader

**Redundancy**
Flag content that appears more than once. Note both locations.

**Voice**
Flag passive constructions. Note when passive may be justified (actor is unknown or irrelevant).

**Heading quality**
Flag headings that:
* Use title case instead of sentence case
* Are vague ("Overview," "More information," "Details")
* Do not match the content type. Task sections use action verbs. Concept sections use noun phrases.

**Action clarity**
For procedural sections, flag instructions that are ambiguous, incomplete, or missing an explicit outcome. A good instruction tells the reader what to do and what to expect when they have done it.

**Progressive disclosure**
Flag when information appears before the reader needs it. Background and context should follow actionable content, not precede it.

**Style guide compliance**
Flag violations of your project's style guide. At minimum, check:
* No em dashes
* No semicolons
* No bare demonstrative pronouns ("This prevents..." becomes "This value prevents...")
* Sentence case for all headings
* Consistent list marker style

**AI-sounding phrasing**
Flag phrases that signal generated text: "delve into", "it's worth noting", "comprehensive", "robust", "leverage", "seamlessly", "empower", "streamline", "unlock", "harness", "moreover", "furthermore", "take advantage of", "this allows you to", "this enables you to."

### Step 3: Clarity sub-agent check

Spawn a sub-agent with no context from this conversation. Give it only the document content and these three questions:

1. What does this doc help you do?
2. Who is it written for?
3. What is the first thing you should do after reading it?

If the sub-agent's answers do not match the doc's stated purpose, that is a finding. Report what it got wrong and which section caused the confusion.

### Step 4: Write the report

Write findings to `[workspace]/[TICKET-ID]/review.md` if inside the writing workflow, or output directly to the conversation if used standalone.

Use this format for each finding:

```
### [Line number or section name]: [Issue type]

Severity: Critical | Major | Minor
Confidence: High | Medium | Low
Problem: [What is wrong and why it hurts the reader]
Suggested rewrite: [Improved version, or "N/A: structural issue"]
```

Order findings by severity (Critical first), then by position in the document.

End the report with a one-paragraph summary: overall quality assessment, the single most impactful change, and a count of findings by severity.

## Example finding

```
### Introduction: AI-generated phrasing + style violation

Severity: Critical
Confidence: High
Problem: "It's worth noting" is AI-generated filler and adds no information.
"Utilize" should be "use" per the style guide. The opening sentence is 38 words
and restates the page title without adding meaning.
Suggested rewrite: Use rate limiting to control how many requests the API accepts
within a given time window.
```

## Output

`[workspace]/[TICKET-ID]/review.md` (or inline in conversation if standalone)

## Severity definitions

* **Critical:** Must fix before publish. Style guide violation or broken instruction.
* **Major:** Fix before publish. Significantly hurts clarity or consistency.
* **Minor:** Improvement opportunity. Writer's discretion.

## Confidence definitions

* **High:** Objectively wrong per the style guide.
* **Medium:** Clear pattern match, but context could justify the choice.
* **Low:** Judgment call. The writer may have good reason for it.

## Rules

* Do not verify factual accuracy. That is the writer's responsibility.
* Do not question structure or doc type decisions. Those were made in `plan-doc`.
* Do not rewrite large sections unprompted. Provide findings. Let the writer decide.
* If the writer asks for a rewrite of a specific section after seeing the findings, do it.
