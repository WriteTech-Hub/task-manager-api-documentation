# Task Manager API Documentation

## What this project is
Developer-facing API documentation for the Task Manager API: authentication, task
CRUD, user roles/permissions, and reporting endpoints. Audience is engineers
integrating with the API. Content is built with Docusaurus and deployed to
task-manager-api-documentation.vercel.app.

## Primary goals
When editing documentation, prioritize:
1. Accuracy
2. Clarity
3. Consistency with existing docs
4. Minimal diffs

Do not introduce stylistic rewrites unless explicitly asked.
Prefer small targeted edits over large rewrites.

## Repository structure
* `docs/api/`: API reference pages (authentication.md, tasks.md, users.md)
* `docs/intro.md`: landing page for the docs site
* `docs/assets/`: images referenced from doc pages
* `docs/config.md`: project/config reference
* `blog/`: release-notes / announcement style posts
* `src/`: Docusaurus site source (theme, components) — not documentation content
* `tests/` and `.doc-detective/tests/`: Doc Detective test specs that validate
  documented behavior against the live API/UI
* `.github/workflows/`: existing CI — `agent-docs.yml` (agent-friendliness check)
  and `doc-detective.yml` (doc behavior tests). Do not duplicate these; new CI
  added by this pipeline (Vale linting, PR quality summaries) is additive.

## Writing style rules
* Sentence case for all headings
* Keep the existing table-heavy reference style for endpoint docs (Method /
  Endpoint / Description / Auth Required / Role) — don't convert to prose
* Ordered lists: use 1. for every item, not sequential numbers
* No bare demonstrative pronouns: "The endpoint returns..." not "This returns..."
* No marketing language: avoid powerful, seamless, robust, unlock, leverage
* Do not use "utilize" — use "use"
* Do not use "allows you to" / "enables you to" — use direct action language
  ("Creates a new task", not "This endpoint allows you to create a new task")

> These are starting defaults inferred from the existing docs. Replace with your
> team's actual style guide once you have one — see 03-editor-prompts.md for
> where these rules also get enforced inline.

## Front matter
Docusaurus front matter: `id`, `title`, `sidebar_position` (see `docs/intro.md`
for the pattern). Every page needs `id` and `title`. Do not remove or reorder
front matter fields. The agent may update `title` or `sidebar_position` only if
explicitly asked.

## Special syntax
* Every doc page opens with this fixed callout — preserve it verbatim, do not
  edit or remove it when drafting or reviewing:
  ```
  > **For AI agents:** A complete documentation index is available at
  [`/llms.txt`](https://task-manager-api-documentation.vercel.app/llms.txt).
  Markdown versions of all pages are available by appending `.md` to any URL.
  ```
* Images are referenced with relative paths into `docs/assets/`
  (e.g. `![Postman Sample](../assets/image-one.jpg)`) — keep this pattern for
  new screenshots rather than absolute URLs.

## What the agent may do without being asked
* Fix typos and grammar errors
* Apply the style rules listed above
* Normalize heading case to sentence case
* Keep the "For AI agents" callout and `llms.txt` reference intact when editing
  a page

## What the agent must not do without being asked
* Change endpoint paths, HTTP methods, parameter names, or response shapes
* Modify code/JSON examples
* Rewrite large sections or restructure a page's flow
* Remove or reorder front matter fields
* Add or remove Doc Detective test specs in `tests/` or `.doc-detective/tests/`

## When uncertain
If product behavior is unclear from the source material, insert:
`<!-- VERIFY: [describe what needs confirmation] -->`

If information is missing and the doc cannot be completed without it:
`<!-- GAP: [describe what is missing] -->`
