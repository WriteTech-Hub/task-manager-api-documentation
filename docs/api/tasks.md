# Tasks API

The Tasks API allows authenticated users to create, assign, update, track, and manage tasks. Tasks can include descriptions, due dates, assigned users, attachments, and progress tracking.

Both **Admin** and **Member** roles can interact with tasks, but access levels differ:

| Role | Permissions |
|------|-------------|
| **Admin** | Can view, create, update, and delete *any* task |
| **Member** | Can create tasks and only view or update tasks they created or are assigned to |

---

## Base URL

```
/api/tasks
```

---

## Endpoints Overview

| Method | Endpoint | Description | Auth Required | Role |
|--------|----------|-------------|---------------|------|
| POST | `/` | Create a new task | Yes | Admin / Member |
| GET | `/` | Get tasks visible to the user | Yes | Admin / Member |
| GET | `/:taskId` | Get details of a specific task | Yes | Admin / Member (if assigned) |
| PUT | `/:taskId` | Update a task | Yes | Admin / Member (if creator/assigned) |
| DELETE | `/:taskId` | Delete a task | Yes | Admin only |
| PATCH | `/:taskId/progress` | Update task progress (0–100%) | Yes | Admin / Member (if assigned) |
| POST | `/:taskId/checklist` | Add a checklist item | Yes | Admin / Member (if assigned) |
| PATCH | `/:taskId/checklist/:itemId` | Update a checklist item's completion state | Yes | Admin / Member (if assigned) |

---

## Task Structure

A task contains the following fields:

```json
{
  "title": "Prepare Project Report",
  "description": "Compile milestone achievements",
  "priority": "High",
  "status": "Pending",
  "dueDate": "2025-01-20",
  "assignedTo": ["<user_id>"],
  "attachments": ["https://filelink.com/file.pdf"],
  "todoChecklist": [
    { "text": "Gather docs", "completed": false }
  ],
  "progress": 40
}
```

---

## 1. Create a Task

**POST** `/`

Creates a new task in the system.

### Request Body

```json
{
  "title": "Design Homepage UI",
  "description": "Initial UI/UX layout",
  "priority": "High",
  "dueDate": "2025-01-29",
  "assignedTo": ["65f93b8c9e9a2d52c3a421de"]
}
```

### Response (201 Created)

```json
{
  "message": "Task created successfully",
  "task": {
    "_id": "65f94a9c19d23e",
    "title": "Design Homepage UI",
    "priority": "High",
    "status": "Pending"
  }
}
```

![Postman Sample](../assets/image-one.jpg)
---

## 2. Get Tasks (Filtered by Role)

**GET** `/`

Retrieves tasks based on the user's role:

- **Admin** → Gets all tasks.
- **Member** → Gets only tasks they created or were assigned to.

### Response (200 OK)

```json
[
  {
    "_id": "65f94a9c19d23e",
    "title": "Design Homepage UI",
    "status": "Pending",
    "assignedTo": ["65f93b8c9e9a2d52c3a421de"],
    "progress": 40
  }
]
```

---

## 3. Get Task by ID

**GET** `/:taskId`

Returns detailed information for a single task.

### Response (200 OK)

```json
{
  "_id": "65f94a9c19d23e",
  "title": "Design Homepage UI",
  "description": "Initial UI/UX layout",
  "assignedTo": ["65f93b8c9e9a2d52c3a421de"],
  "todoChecklist": [
    { "text": "Sketch wireframe", "completed": false }
  ]
}
```

---

## 4. Update Task

**PUT** `/:taskId`

Updates task content including title, status, description, and other fields.

### Request Body

```json
{
  "status": "InProgress",
  "description": "Working on visual layout"
}
```

### Response (200 OK)

```json
{
  "message": "Task updated successfully",
  "task": {
    "_id": "65f94a9c19d23e",
    "title": "Design Homepage UI",
    "status": "InProgress",
    "description": "Working on visual layout"
  }
}
```

---

## 5. Delete Task (Admin Only)

**DELETE** `/:taskId`

Permanently removes a task from the system. Only admins can delete tasks.

### Response (200 OK)

```json
{
  "message": "Task deleted successfully"
}
```

---

## 6. Update Task Progress

**PATCH** `/:taskId/progress`

Updates the progress percentage of a task (0–100%).

### Request Body

```json
{
  "progress": 75
}
```

### Response (200 OK)

```json
{
  "message": "Progress updated",
  "progress": 75
}
```

---

## 7. Add Checklist Item

**POST** `/:taskId/checklist`

Adds a new item to the task's checklist.

### Request Body

```json
{
  "text": "Run accessibility audit"
}
```

### Response (201 Created)

```json
{
  "message": "Checklist item added successfully",
  "checklist": [
    { "_id": "65f95b2d3a1f34", "text": "Run accessibility audit", "completed": false }
  ]
}
```

---

## 8. Update Checklist Completion

**PATCH** `/:taskId/checklist/:itemId`

Updates the completion status of a specific checklist item.

### Request Body

```json
{
  "completed": true
}
```

### Response (200 OK)

```json
{
  "message": "Checklist item updated",
  "item": {
    "_id": "65f95b2d3a1f34",
    "text": "Run accessibility audit",
    "completed": true
  }
}
```

---

## Common Error Responses

| Status | Meaning |
|--------|---------|
| 400 | Invalid input or missing required fields |
| 401 | Missing or invalid token |
| 403 | User does not have permission |
| 404 | Task not found |

---
