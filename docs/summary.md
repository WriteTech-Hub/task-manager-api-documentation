# Task Manager API Documentation

Welcome to the Task Manager API - Build powerful task management features into your application.

---

## Getting Started

- [Introduction](intro.md)
- [Quick Start](quick-start.md)
- [Authentication Overview](authentication-overview.md)

---

## API Reference

### Authentication API

- [POST /register](api/auth/register.md)
- [POST /login](api/auth/login.md)
- [GET /me](api/auth/me.md)
- [POST /invite-admin](api/auth/invite-admin.md)

### Tasks API

- [GET /tasks](api/tasks/get-tasks.md)
- [POST /tasks](api/tasks/create-task.md)
- [GET /tasks/:id](api/tasks/get-task-by-id.md)
- [PUT /tasks/:id](api/tasks/update-task.md)
- [DELETE /tasks/:id](api/tasks/delete-task.md)

### Users API

- [GET /users](api/users/get-users.md)
- [GET /users/:id](api/users/get-user-by-id.md)
- [PUT /users/:id](api/users/update-user.md)
- [DELETE /users/:id](api/users/delete-user.md)

---

## Guides

- [Working with Task Priorities](guides/task-priorities.md)
- [Implementing Role-Based Access](guides/role-based-access.md)
- [Pagination and Filtering](guides/pagination-filtering.md)

---

## Error Handling

- [Error Response Format](errors/error-format.md)
- [HTTP Status Codes](errors/status-codes.md)
- [Common Errors](errors/common-errors.md)

---

## Reference

- [Changelog](changelog.md)
- [OpenAPI Specification](task-manager-openapi.json)

---

## Support

Need help? Reach out to us:
- Email: support@writetechhub.org
- GitHub Issues: https://github.com/WriteTech-Hub/task-tracker-app/issues