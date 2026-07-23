description: Audit a document for inconsistent naming of the same concept.
---

Audit the document at $ARGUMENTS for terminology consistency. Identify every instance where the same concept, feature, component, or action is referred to by different names.

## What to check

* Feature names: Is the same feature called different things in different sections?
* UI element names: Are buttons, fields, pages, and tabs named consistently?
* Actions: Is the same user action described with different verbs? "Configure" vs "set up" vs "enable"
* Technical terms: Are API objects, parameters, and values referred to the same way throughout? "API key" vs "api_key" vs "access token"
* Roles and actors: "User" vs "admin" vs "account owner" vs "you". Is the audience addressed consistently?

## Output format

### Terminology map

For each concept with inconsistent naming:

| Concept | Terms used | Locations | Recommended term |
|---|---|---|---|
| [concept] | [all variants found] | [sections/lines] | [one term to standardize on] |

### Undefined terms
List any technical terms, acronyms, or jargon used without definition on first occurrence.

### Recommendations
* Which term to standardize on for each inconsistency
* Whether any terms need a glossary entry
* Whether any inconsistencies reflect actual product inconsistencies that need to be escalated