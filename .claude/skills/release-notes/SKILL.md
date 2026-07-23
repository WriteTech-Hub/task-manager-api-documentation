---
name: release-notes
description: Collect release items from the issue tracker, write a release notes blog post, and open a pull request in a single skill run.
---

# release-notes

Collect release items from your issue tracker, write a release notes post, and open a pull request in a single skill run.

## When to use this skill

Run this each time you publish a release notes update. This skill handles the mechanical work: querying tickets, writing the post, and opening the PR.

**Adapted for this repo:** this is a single-product project (the Task Manager API), so there is no multi-folder routing map. Every release note goes to one place: `blog/`, following the Docusaurus blog post convention.

## Inputs

* Release date: `YYYY-MM-DD` format

## Steps

### Step 1: Collect release items

Query your issue tracker for tickets that are:
* Status: Ready for release (or your equivalent "done and approved" status)
* Release notes field: not empty

For each ticket, collect:
* Ticket key
* Public-facing release notes text (the dedicated release notes field, not the description or title)

Also query for tickets that are ready for release but have an empty release notes field. For each of these, draft suggested release notes text from the ticket description and present them to the writer for review before proceeding. Do not write anything to disk until the writer approves the suggested text.

### Step 2: Write the release notes post

Write `blog/[YYYY-MM-DD]-release-notes.md`.

Before creating the file, check if a post for this date already exists. If it does, append entries to the appropriate section rather than overwrite.

**File format (Docusaurus blog front matter):**

```markdown
---
slug: [YYYY-MM-DD]-release-notes
title: Release notes: [YYYY-MM-DD]
authors: [writetechhub]
tags: [release-notes]
---

#### New features

* [Release note text]

#### Updates and fixes

* [Release note text]
```

**Section headings (use only what applies):**

* `#### New features`: significant new capabilities
* `#### Updates and fixes`: updates, maintenance changes, and bug fixes
* `#### Fixes`: when all entries are bug fixes only
* `#### Deprecated`: features or items being deprecated

**Writing rules:**

* Use the release notes field text as the source. Do not rewrite the substance.
* Edit lightly for grammar and style: active voice, sentence case, no em dashes, no semicolons.
* Link feature or endpoint names to their documentation pages in `docs/api/` when you can confirm the page exists. Do not add links you cannot verify.

### Step 3: Review before committing

List all entries that will be added, with the ticket key and the release notes text each one produced. Ask the writer to confirm before proceeding.

**Stop here and wait for the writer's confirmation.**

### Step 4: Create the branch

If not already on a feature branch, create one:

```bash
git checkout -b release-notes-[YYYY-MM-DD]
```

### Step 5: Commit the changes

Stage and commit only the release notes file:

```bash
git add blog/[YYYY-MM-DD]-release-notes.md
git commit -m "Add release notes for [YYYY-MM-DD]"
```

Use the release date in the commit message, not today's date.

### Step 6: Push and open a pull request

```bash
git push -u origin [branch-name]
```

Open a pull request with:
* **Title:** `Add release notes for [YYYY-MM-DD]`
* **Body:** List of each ticket key included with a one-line summary of its release notes text

**Stop and ask the writer for explicit confirmation before pushing or opening the PR.** Pushing a branch and opening a PR are visible to the rest of the team; do not do this automatically as part of a dry run or test.

### Step 7: Report the PR URL

Show the PR URL to the writer.

## Output

* A release notes post at `blog/[YYYY-MM-DD]-release-notes.md`
* A pull request with the changes

## Example output

Given a ticket with release notes text "Added comments support to the Tasks API, including add, list, and delete endpoints", the skill produces:

```markdown
---
slug: 2026-07-23-release-notes
title: Release notes: 2026-07-23
authors: [writetechhub]
tags: [release-notes]
---

#### New features

* Added [comments support](/docs/api/tasks#comments) to the Tasks API, including add, list, and delete endpoints.
```

The link is only added if the page exists. If it cannot be confirmed, the name appears as plain text.

## Edge cases

* If a ticket's release notes text contains internal jargon or is clearly not public-facing: ask the writer before including it.
* If the release date in the ticket title differs from today's date: use the date from the ticket, not today's date.

## Rules

* Use the release notes field text, not the ticket description or title.
* Do not invent release notes content for tickets that are missing it. Present drafts for writer approval.
* Do not link to documentation pages you have not confirmed exist.
* Always wait for writer confirmation in Step 3 before committing anything, and again in Step 6 before pushing or opening a PR.
