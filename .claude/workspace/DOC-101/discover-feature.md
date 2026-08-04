# DOC-101: Document the task comments endpoints

## What this feature does
The Tasks API now supports comments on a task. A user can add a comment to a
task, list all comments on a task, and delete a comment they authored. Admins
can also delete any comment, not just their own. This gives task collaborators
a way to discuss a task inline instead of relying on external channels.

## What's changing
* New: `POST /api/tasks/:taskId/comments` — add a comment to a task. Body:
  `{ "text": string }`. Returns 201 with the created comment (`id`, `text`,
  `authorId`, `createdAt`).
* New: `GET /api/tasks/:taskId/comments` — list all comments on a task,
  oldest first. Returns 200 with an array of comments.
* New: `DELETE /api/tasks/:taskId/comments/:commentId` — delete a comment.
  Only the comment's author or an Admin can delete it. Returns 200 on
  success, 403 if the requester is neither the author nor an Admin.
* Changed: none — this is additive to the existing Tasks API.
* Removed: nothing.

## Target audience
Same audience as the rest of `docs/api/`: engineers integrating with the Task
Manager API, already familiar with the existing task CRUD and auth model
(JWT bearer token, Admin/Member roles).

## Existing docs
* [docs/api/tasks.md](../../../docs/api/tasks.md) — needs to be updated. This is
  the primary target: the comments endpoints follow the same
  endpoint-table + numbered-section pattern already used here for task and
  checklist endpoints (sections 1–8, plus the "Endpoints Overview" table and
  "Common Error Responses" table at the bottom).
* [docs/api/authentication.md](../../../docs/api/authentication.md) — no update
  needed; referenced only for the auth-header pattern (`Authorization: Bearer
  <token>`) reused in the new sections.
* [docs/api/users.md](../../../docs/api/users.md) — no update needed; referenced
  only for Admin/Member role terminology consistency.
* No existing doc, test spec, or config file mentions "comment" — this is
  entirely new content in this repo.

## Open questions
* What HTTP status and error shape are returned when `text` is missing or
  empty on `POST`? The ticket gives no 400 case for this endpoint (unlike the
  existing task endpoints, which document 400 for invalid/missing fields).
* Is there a maximum length for `text`? Not stated in the ticket.
* Does the response body wrap the comment object (e.g. `{ "message": ...,
  "comment": {...} }`, matching the pattern used by `POST /` and `PUT
  /:taskId` in tasks.md) or return the comment bare (matching `GET /me` in
  users.md)? The ticket says "Returns 201 with the created comment" without
  specifying a wrapper.
* The ticket specifies the created-comment field as `id`, but every existing
  resource in this API (tasks, users, checklist items) uses `_id` as the
  identifier field. Is `id` intentional for comments, or should it be `_id`
  for consistency? This is a terminology/shape discrepancy worth flagging
  rather than silently normalizing.
* What does `DELETE` return in the body on success — a `message` string
  (matching the pattern in tasks.md section 5, "Delete Task"), or something
  else?
* What happens on `GET`/`DELETE` when the task itself doesn't exist, or when
  the comment ID doesn't exist under that task? Existing task endpoints
  document 404 for "Task not found" — is there an equivalent "Comment not
  found" case?
* Is `GET /api/tasks/:taskId/comments` restricted by the same
  visibility rule as `GET /:taskId` (Member can only see tasks they created
  or are assigned to), or can any authenticated user with access to the
  task ID read its comments? The ticket doesn't state a role restriction for
  the list/read endpoint beyond "list all comments on a task."
* Can a Member add a comment to any task, or only tasks they created/are
  assigned to (mirroring the task-level access model)?

## Sources
* Ticket DOC-101, provided directly in the writer's request (title,
  description, endpoint list, and acceptance criteria). No issue-tracker
  integration (Jira/Linear/GitHub Issues) is configured in this environment,
  so the ticket text quoted in the prompt is the sole source — nothing was
  fetched externally.
* No linked tickets or linked documentation pages were provided.
* No internal knowledge base (Confluence/Notion/Glean) is configured in this
  environment, so no search was performed there.
* Repo files read for existing pattern and terminology: `docs/api/tasks.md`,
  `docs/api/authentication.md`, `docs/api/users.md`.
* Repo-wide search for "comment" (case-insensitive) across tracked content
  turned up no existing documentation, config, or Doc Detective test spec
  referencing task comments.

## Unread attachments
None provided.
