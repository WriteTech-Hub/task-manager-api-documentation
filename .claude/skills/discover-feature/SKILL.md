---
name: discover-feature
description: Research a ticket and produce a structured research brief before any writing begins.
---

# discover-feature

Research a ticket and produce a structured research brief before any writing begins.

## When to use this skill

Run this before planning or drafting any documentation. It is the foundation everything else builds on. The research brief produced here becomes the input to `plan-doc` and `draft-doc`.

Use it any time you need to document a feature or change that you did not build yourself and are not yet fully familiar with.

## Inputs

* Ticket ID: the full ticket identifier

## Steps

### Step 1: Parse the ticket ID

Extract the ticket ID from whatever the writer provided: a URL, a plain ID, or a mention. Use the full ID as-is.

### Step 2: Create the workspace directory

Create a workspace directory for this ticket (for example, `.claude/workspace/[TICKET-ID]/` or your tool's equivalent). This directory holds all working files for this ticket and is scoped to the feature branch. It never merges to main.

### Step 3: Fetch the ticket

Use your issue tracker integration to fetch the ticket. This could be a Jira MCP, the GitHub Issues API, a Linear integration, or any tool that gives the agent access to your tickets. Collect:

* Title and description
* Acceptance criteria
* Any linked tickets
* Any linked documentation pages (fetch each one)
* Any file attachments: read text-based files directly and note binary files you cannot read

For each attachment you cannot read, note the filename and type in the brief under "Unread attachments."

### Step 4: Search the knowledge base

Search your internal knowledge base for context related to this feature. Use the ticket title and key terms as your search query. This could be Confluence, Notion, a search tool like Glean, or any internal wiki your team uses. Look for:

* Engineering documentation or design specs
* Product specs
* Related feature context that fills gaps in the ticket

### Step 5: Find related existing documentation

Search the content directory for existing documentation related to this feature. Note the file paths of any docs that may need to be updated or cross-linked.

### Step 6: Write the research brief

Write `[workspace]/[TICKET-ID]/discover-feature.md` using this structure:

```markdown
# [TICKET-ID]: [Ticket title]

## What this feature does
Plain-language explanation. What it is, what problem it solves, what a user
can do with it that they could not do before.

## What's changing
Specifically what is new, changed, or removed. Be concrete.
* New: [what was added]
* Changed: [what was modified and how it differs from before]
* Removed: [what no longer exists]

## Target audience
Who uses this feature. Their technical level, role, and goal.

## Existing docs
List of related files with paths. Note whether each needs to be updated or cross-linked.

## Open questions
Things that are unclear, missing, or contradictory in the source material.
Format each as a specific, answerable question.

## Sources
Ticket URL, pages read, attachments read, knowledge base results used.

## Unread attachments
[Omit this section if all attachments were read successfully.]
```

## Output

`[workspace]/[TICKET-ID]/discover-feature.md`

## Transition

After writing the brief, summarize the key findings in 3–5 sentences and ask:

> "Ready to plan the doc structure, or do you want to review the brief first?"

**Stop here and wait for the writer's response before taking any further action.**

## Rules

* Only include information stated or directly supported by the source material.
* Do not invent product behavior. If something is unclear, put it in Open questions.
* If information is implied but not stated, note it in Open questions, not in the main sections.
* Terminology inconsistency is a factual error. Note exact phrasing from sources and use it consistently.
