# Plan: DOC-101

## Doc type
Reference: the reader needs to look up an endpoint's method, path, auth/role requirement, and request/response shape before calling it — not learn a workflow or a concept. This matches the existing `docs/api/tasks.md` reference style (endpoint table + numbered sections), which the acceptance criteria explicitly require reusing.

## File
* Path: `docs/api/tasks.md`
* Status: Update to existing file. The comments endpoints are sub-resources of a task (`/api/tasks/:taskId/comments`), so they belong in the same file as the rest of the Tasks API rather than a new page. No new file is created; no front matter changes (the file currently has no front matter block to preserve or alter, and none is being added since that's outside this ticket's scope).

## Prerequisite knowledge
Same as the rest of `docs/api/tasks.md`: the reader already knows the JWT bearer-token auth model (`docs/api/authentication.md`) and the Admin/Member role model used throughout this file. No new prerequisite is introduced by comments.

## Outline

### Endpoints Overview table (update)
Purpose: Let a reader scanning the top-of-file table see the three new endpoints alongside existing task endpoints, consistent with how checklist endpoints are already listed there.
Content: Add three rows after the existing checklist rows:
* `POST /:taskId/comments` — Add a comment to a task — Yes — Admin / Member <!-- VERIFY: can any Member comment on any task, or only tasks they created/are assigned to, mirroring task-level access? -->
* `GET /:taskId/comments` — List all comments on a task — Yes — Admin / Member <!-- VERIFY: same read-access question as above -->
* `DELETE /:taskId/comments/:commentId` — Delete a comment — Yes — Author / Admin

### Comment Structure (new subsection, mirrors "Task Structure")
Purpose: Give the reader a single reference for the comment object shape before it appears in three separate endpoint examples, matching how "Task Structure" precedes the numbered task sections.
Content: Fields per the ticket: `text`, `authorId`, `createdAt`, plus an identifier field.
<!-- GAP: ticket specifies the identifier field as `id`, but every other resource in this API (tasks, users, checklist items) uses `_id`. Draft should use `id` as given (source of truth per ticket) but flag this inconsistency rather than silently normalizing to `_id`. -->

### 9. Add a Comment
Purpose: Tell the reader how to post a new comment and what they get back.
Content:
* `POST` `/:taskId/comments`
* Auth: required. Role: Admin / Member <!-- VERIFY: task-level access restriction, per Endpoints Overview note above -->
* Request body: `{ "text": string }`
* Response: 201 with created comment (`id`/`_id`? — see GAP above, `text`, `authorId`, `createdAt`)
* No documented 400 case in the ticket for missing/empty `text`. Existing task endpoints document 400 for invalid/missing fields (see "Common Error Responses"). <!-- GAP: no confirmed 400 behavior or text length limit for this endpoint; do not invent one. -->

### 10. List Comments
Purpose: Tell the reader how to retrieve all comments on a task and what order to expect.
Content:
* `GET` `/:taskId/comments`
* Auth: required. Role: Admin / Member <!-- VERIFY: same read-access question as above -->
* Response: 200 with an array of comment objects, oldest first
* No request body

### 11. Delete a Comment
Purpose: Tell the reader who is allowed to delete a comment and what happens when they're not.
Content:
* `DELETE` `/:taskId/comments/:commentId`
* Auth: required. Role: comment author or Admin only
* Response: 200 on success <!-- GAP: exact success response body not specified (e.g. a `message` string like the existing "Delete Task" section, or empty body). Draft should follow the existing `{ "message": ... }` pattern used by other deletes in this file and flag it as an assumption, since the ticket doesn't state the body. -->
* 403 if requester is neither the author nor an Admin

### Common Error Responses (existing table, no changes planned)
Purpose: Keep the file's single shared error table authoritative rather than duplicating error rows per section.
Content: The existing 400/401/403/404 rows already cover the cases stated in the ticket (403 for the delete-permission case). No new status code is confirmed by the ticket, so no row is added. <!-- GAP: whether a "Comment not found" 404 case exists (distinct from "Task not found") is not stated in the ticket; not added to the table without confirmation. -->
