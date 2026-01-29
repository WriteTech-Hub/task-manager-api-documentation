# Authentication API

The Authentication API handles user registration, login, profile retrieval, and role-based access. All protected endpoints require a JWT Bearer Token, which must be included in the request headers as:

```javascript
Authorization: Bearer <your_token_here>
```

If the token is missing or invalid, the API will return a `401 Unauthorized` response.

***

## Base URL

```javascript
/api/auth
```

***

## Endpoints Overview

<table isTableHeaderOn="true" columnWidths="[object Object]">
  <tr>
    <td>
      <p>Method</p>
    </td>
    <td>
      <p>Endpoint</p>
    </td>
    <td>
      <p>Description</p>
    </td>
    <td>
      <p>Auth Required</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>POST</p>
    </td>
    <td>
      <p><code>/api/auth/register</code></p>
    </td>
    <td>
      <p>Register a new user</p>
    </td>
    <td>
      <p>No</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>POST</p>
    </td>
    <td>
      <p><code>/api/auth/login</code></p>
    </td>
    <td>
      <p>Authenticate an existing user and get a token</p>
    </td>
    <td>
      <p>No</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>GET</p>
    </td>
    <td>
      <p><code>/profile</code></p>
    </td>
    <td>
      <p>Get details of the logged-in user</p>
    </td>
    <td>
      <p>Yes</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>POST</p>
    </td>
    <td>
      <p><code>/invite-admin</code></p>
    </td>
    <td>
      <p>Create a new admin user (admin-only route)</p>
    </td>
    <td>
      <p>Yes (Admin)</p>
    </td>
  </tr>
</table>

***

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

***

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

***

## 3. Get Current Authenticated User

**GET** `/profile`

Returns profile information of the currently logged-in user. This is useful for front-end applications to fetch user details after login.

### Headers

```javascript
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

***

## 4. Invite Admin (Admin Only)

**POST** `/invite-admin`

Allows an existing admin to create another admin user.

### Headers

```javascript
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

***

## Common Error Responses

<table isTableHeaderOn="true" columnWidths="[object Object]">
  <tr>
    <td>
      <p>Status</p>
    </td>
    <td>
      <p>Reason</p>
    </td>
    <td>
      <p>Example</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>400</p>
    </td>
    <td>
      <p>Missing fields</p>
    </td>
    <td>
      <p><code>{"message": "Email and password required"}</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p>401</p>
    </td>
    <td>
      <p>Invalid or missing token</p>
    </td>
    <td>
      <p><code>{"message": "Not authorized"}</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p>403</p>
    </td>
    <td>
      <p>User does not have permission</p>
    </td>
    <td>
      <p><code>{"message": "Access denied, admin only"}</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p>409</p>
    </td>
    <td>
      <p>Email already registered</p>
    </td>
    <td>
      <p><code>{"message": "User already exists"}</code></p>
    </td>
  </tr>
</table>

