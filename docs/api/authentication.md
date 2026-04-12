> **For AI agents:** A complete documentation index is available at [`/llms.txt`](https://task-manager-api-documentation.vercel.app/llms.txt). Markdown versions of all pages are available by appending `.md` to any URL.

# Authentication API

The Authentication API handles user registration, login, profile retrieval, and role-based access. All protected endpoints require a **JWT Bearer Token**, which must be included in the request headers as:

```
Authorization: Bearer <your_token_here>
```

If the token is missing or invalid, the API will return a `401 Unauthorized` response.

---

## Base URL

```
/api/auth
```

---

## Endpoints Overview

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register` | Register a new user | No |
| POST | `/api/auth/login` | Authenticate an existing user and get a token | No |
| GET | `/profile` | Get details of the logged-in user | Yes |
| POST | `/invite-admin` | Create a new admin user (admin-only route) | Yes (Admin) |

---

## 1. Register User

**POST** `/api/auth/register`

Registers a new user into the system.

### Request Body

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "yourpassword"
}
```

### Response (201 Created)

```json
{
  "message": "User registered successfully",
  "user": {
    "_id": "65f93b8c9e9a2d52c3a421de",
    "name": "John Doe",
    "email": "john@example.com",
    "role": "member"
  }
}
```

---

## 2. Login User

**POST** `/api/auth/login`

Authenticates a user and returns a JWT token required for accessing protected endpoints.

### Request Body

```json
{
  "email": "john@example.com",
  "password": "yourpassword"
}
```

### Response (200 OK)

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR...",
  "user": {
    "_id": "65f93b8c9e9a2d52c3a421de",
    "name": "John Doe",
    "email": "john@example.com",
    "role": "member"
  }
}
```

---

## 3. Get Current Authenticated User

**GET** `/profile`

Returns profile information of the currently logged-in user. This is useful for front-end applications to fetch user details after login.

### Headers

```
Authorization: Bearer <token>
```

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

## 4. Invite Admin (Admin Only)

**POST** `/invite-admin`

Allows an existing admin to create another admin user.

### Headers

```
Authorization: Bearer <admin_token>
```

### Request Body

```json
{
  "name": "Admin Two",
  "email": "admin2@example.com",
  "password": "strongpassword"
}
```

### Response (200 OK)

```json
{
  "message": "Admin user created successfully",
  "user": {
    "_id": "65f93ed19e9323e39f41b234",
    "name": "Admin Two",
    "email": "admin2@example.com",
    "role": "admin"
  }
}
```

---

## Common Error Responses

| Status | Reason | Example |
|--------|--------|---------|
| 400 | Missing fields | `{"message": "Email and password required"}` |
| 401 | Invalid or missing token | `{"message": "Not authorized"}` |
| 403 | User does not have permission | `{"message": "Access denied, admin only"}` |
| 409 | Email already registered | `{"message": "User already exists"}` |