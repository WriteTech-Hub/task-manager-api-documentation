---
name: plan-doc
description: Produce a structured documentation outline from the research brief, for writer approval before any drafting begins.
---

# plan-doc

Produce a structured documentation outline from the research brief, for writer approval before any drafting begins.

## When to use this skill

Run this after `discover-feature` has produced an approved research brief. Always plan before drafting. Changing structure after a draft exists is expensive.

## Inputs

* `[workspace]/[TICKET-ID]/discover-feature.md`

If this file does not exist, ask the writer to run `discover-feature` first.

## Steps

### Step 1: Read the research brief

Read the discover-feature brief. Identify the feature, the target audience, and what the reader will need to do after reading the documentation.

### Step 2: Determine the doc type

Use the Diataxis framework to select the appropriate doc type:

| Type | Reader need | Shape |
|---|---|---|
| **How-to guide** | Complete a specific task | Numbered steps, minimal explanation |
| **Tutorial** | Learn by doing for the first time | Guided end-to-end sequence, hand-holding tone |
| **Concept** | Understand how something works | Prose explanation, no procedures |
| **Reference** | Look up a value, parameter, or behavior | Tables, lists, terse descriptions |

Choose the type that matches what the reader will actually do with the doc. If the ticket requires more than one type, plan separate files.

### Step 3: Apply outline principles

Before writing headings, reason through these four dimensions:

**Front-load value.** The most useful information comes first. A reader scanning the top of the page should immediately understand what the doc covers and whether it applies to them. Background follows actionable content. It does not precede it.

**Optimize for scanning.** Readers rarely read linearly. Each heading should clearly signal the content beneath it. Avoid vague headings like "Overview" or "More information."

**Separate concept from procedure.** Do not mix explanation and steps in the same section. If readers need to understand something before they can do something, that understanding belongs in its own section, not embedded inside a procedure.

**Identify prerequisites.** What must the reader already know or have set up before this doc is useful? This belongs near the top.

### Step 4: Determine the file path

Based on the doc type and subject matter, identify where the file belongs in the content directory. Use existing files in the same area as a guide for naming conventions. If this is an update to an existing file, note that instead.

### Step 5: Write the plan

Write `[workspace]/[TICKET-ID]/plan.md` using this structure:

```markdown
# Plan: [TICKET-ID]

## Doc type
[Type]: [One sentence explaining why this type fits the reader need]

## File
* Path: content/[path/to/file.md]
* Status: New file | Update to existing file

## Front matter
title: [Proposed title]
description: [One sentence describing what the reader will learn or accomplish]

## Prerequisite knowledge
[What the reader must already know. If none, say so.]

## Outline

### [Section heading]
Purpose: [What this section does for the reader, in one sentence]
Content: [Key points, decisions, or data this section must cover]

### [Section heading]
Purpose: ...
Content: ...
```

## Output

`[workspace]/[TICKET-ID]/plan.md`

## Transition

After writing the plan, show the outline to the writer as a summary (headings and purpose only). Ask:

> "Does this structure look right, or do you want to adjust anything before drafting?"

**Stop here and wait for the writer's response before taking any further action.**

Once approved, offer to continue with `draft-doc`.

## Rules

* Do not start drafting until the plan is approved.
* If the research brief is missing information needed to plan a section, note it in that section's Content notes rather than inventing content.
* Choose the doc type based on reader need, not on what is easiest to write.
