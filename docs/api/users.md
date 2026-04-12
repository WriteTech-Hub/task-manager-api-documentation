> **For AI agents:** A complete documentation index is available at [`/llms.txt`](https://task-manager-api-documentation.vercel.app/llms.txt). Markdown versions of all pages are available by appending `.md` to any URL.

# Users API

The Users API provides endpoints for managing user profiles, roles, and listings within the project management system. This includes retrieving user details, listing team members, updating profile information, and (for admins) managing user roles.

By default, all standard users have the role `member`, while elevated permissions require an `admin` role.

All endpoints in this section require authentication unless stated otherwise.

---

## Base URL

```
/api/users
```

---

## Endpoints Overview

| Method | Endpoint | Description | Auth Required | Role |
|--------|----------|-------------|---------------|------|
| GET | `/` | List all users in the workspace | Yes | Admin-only |
| GET | `/me` | Get the currently authenticated user's profile | Yes | Member / Admin |
| GET | `/:userId` | Get details for a specific user | Yes | Admin (full) / Member (limited) |
| PATCH | `/me` | Update your own profile (name, photo) | Yes | Member / Admin |
| PATCH | `/:userId/role` | Update a user's role | Yes | Admin-only |

---

## User Structure

A user record looks like this:

```json
{
  "_id": "65f93b8c9e9a2d52c3a421de",
  "name": "John Doe",
  "email": "john@example.com",
  "role": "member",
  "profileImageUrl": null
}
```

---

## 1. Get All Users (Admin Only)

**GET** `/`

Returns a list of all registered users in the workspace.

### Headers

```
Authorization: Bearer <admin_token>
```

### Response (200 OK)

```json
[
  {
    "_id": "65f93b8c9e9a2d52c3a421de",
    "name": "John Doe",
    "email": "john@example.com",
    "role": "member"
  },
  {
    "_id": "65f93cfb19a3e92f9bd4c23b",
    "name": "Admin One",
    "email": "admin@example.com",
    "role": "admin"
  }
]
```

---

## 2. Get Your Own Profile

**GET** `/me`

Returns your own user information. Useful for frontend user states after session validation.

### Response (200 OK)

```json
{
  "_id": "65f93b8c9e9a2d52c3a421de",
  "name": "John Doe",
  "email": "john@example.com",
  "role": "member",
  "profileImageUrl": null
}
```

---

## 3. Get User by ID

**GET** `/:userId`

Returns detailed profile information for a specific user.

### Access Rules

- **Admin** → Sees all details
- **Member** → Can only see basic info of others (no email / admin metadata exposed)

### Response (200 OK) - Admin View

```json
{
  "_id": "65f93cfb19a3e92f9bd4c23b",
  "name": "Admin One",
  "email": "admin@example.com",
  "role": "admin",
  "profileImageUrl": null
}
```

---

## 4. Update Your Profile

**PATCH** `/me`

Updates profile details such as name, profile photo, and display settings.

### Request Body

```json
{
  "name": "John Updated",
  "profileImageUrl": "https://cdn.app.com/images/profile_01.jpg"
}
```

### Response (200 OK)

```json
{
  "message": "Profile updated successfully",
  "user": {
    "_id": "65f93b8c9e9a2d52c3a421de",
    "name": "John Updated",
    "profileImageUrl": "https://cdn.app.com/images/profile_01.jpg"
  }
}
```

---

## 5. Update User Role (Admin Only)

**PATCH** `/:userId/role`

Converts a member to admin or demotes an admin to member.

### Request Body

```json
{
  "role": "admin"
}
```

### Response (200 OK)

```json
{
  "message": "User role updated successfully",
  "user": {
    "_id": "65f93cfb19a3e92f9bd4c23b",
    "name": "Admin One",
    "role": "admin"
  }
}
```

---

## Common Error Responses

| Status | Reason |
|--------|--------|
| 400 | Missing or invalid fields |
| 401 | Missing or invalid JWT token |
| 403 | Action restricted by role |
| 404 | User not found |