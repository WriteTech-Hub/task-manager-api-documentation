---
name: branch
description: Create a correctly named git branch from a ticket ID before starting any documentation work.
---

# branch

Create a correctly named git branch from a ticket before starting any documentation work.

## When to use this skill

Run this as the first step when starting work on any ticket. It ensures branch names are consistent, traceable to the ticket, and do not require the writer to manually construct the slug.

## Inputs

* Ticket ID: the full ticket identifier, for example `DOC-1234` or `ISSUE-567`

## Steps

### Step 1: Check the current branch

Run `git branch --show-current`.

If the current branch is not the main branch, stop and tell the writer:

> Cannot create branch: you are currently on `[branch-name]`, not `main`. Switch to `main` first.

Do not proceed until the writer is on the main branch.

### Step 2: Fetch the ticket title

Use your issue tracker integration to fetch the ticket and read its title or summary field. The field name varies by tool: `summary` in Jira, `title` in GitHub Issues and Linear.

### Step 3: Derive the branch name slug

Transform the ticket title into a URL-safe slug:

* Replace spaces with hyphens
* Remove parentheses, commas, and periods
* Replace any remaining special characters (except letters, digits, and hyphens) with hyphens
* Collapse consecutive hyphens into one
* Preserve original casing

Examples:

| Ticket | Title | Branch name |
|---|---|---|
| DOC-1234 | Release notes (June 3, 2024) | `DOC-1234-Release-notes-June-3-2024` |
| DOC-1189 | Add rate limiting to API reference | `DOC-1189-Add-rate-limiting-to-API-reference` |

### Step 4: Create the branch

```bash
git checkout -b [TICKET-ID]-[TITLE-SLUG]
```

Confirm the branch was created and report the full branch name to the writer.

## Output

A new local git branch named `[TICKET-ID]-[TITLE-SLUG]`.

## Rules

* Never create a branch from anything other than the main branch.
* Never modify the ticket title when deriving the slug. Only apply the transformations in Step 3.
