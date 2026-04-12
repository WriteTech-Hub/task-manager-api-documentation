# Configuration for Code Snippets

This file configures code snippets to be displayed in the documentation.

---

## Authentication Example

Complete authentication flow example:

```snippet
{
  "file": "examples/auth-flow.js",
  "language": "javascript",
  "title": "Complete Authentication Flow"
}
```

---

## Task Creation Example

Example of creating a task with all fields:

```snippet
{
  "file": "examples/create-task.js",
  "language": "javascript",
  "title": "Create Task with All Fields"
}
```

---

## Error Handling Example

Comprehensive error handling:

```snippet
{
  "file": "examples/error-handling.js",
  "language": "javascript",
  "title": "API Error Handling"
}
```

---

## Python Client Example

Python client implementation:

```snippet
{
  "file": "examples/python-client.py",
  "language": "python",
  "title": "Python API Client"
}
```

---

## Environment Configuration

Sample environment variables:

```snippet
{
  "file": "examples/.env.example",
  "language": "bash",
  "title": "Environment Variables"
}
```

---

## Package Dependencies

NPM package.json example:

```snippet
{
  "file": "examples/package.json",
  "language": "json",
  "title": "Project Dependencies"
}
```

---

## Usage

Place this file in the same directory as your `summary.md` file. Archbee will automatically load the code snippets from the specified files.

**File structure:**
```
docs/
├── summary.md
├── config.md          ← This file
└── examples/
    ├── auth-flow.js
    ├── create-task.js
    ├── error-handling.js
    ├── python-client.py
    ├── .env.example
    └── package.json
```