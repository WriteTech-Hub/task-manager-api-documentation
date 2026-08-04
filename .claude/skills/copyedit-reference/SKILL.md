---
name: copyedit-reference
description: Grammar, style, and consistency copyedit for reference documentation, parameter tables, and API reference material.
---

# copyedit-reference

Grammar, style, and consistency copyedit for reference documentation: parameter tables, field descriptions, configuration options, and API reference material.

## When to use this skill

Use this on reference docs that describe parameters, fields, configuration options, or API inputs and outputs. It applies a focused set of rules specific to the challenges of reference material: inconsistent formatting, missing required/optional labels, unclear descriptions, and raw URLs.

## Inputs

* File path of the reference document to review

## Steps

### Step 1: Grammar and spelling check

Check for basic grammar errors, spelling mistakes, and punctuation inconsistencies. Flag each issue with its location.

### Step 2: Code formatting

* Variable names, parameter names, and values that appear inline use code formatting (backticks).
* Uppercase words (like UUID, ID) do not use backticks unless they are specifically a parameter name in this document.
* Example values are always code-formatted.

### Step 3: Links

* Every raw URL gets descriptive link text.
* Link text is the destination page title or a clear description. Do not use "click here," "here," or the raw URL.
* Internal links use relative paths, not absolute URLs.

### Step 4: Sentences and punctuation

* Every sentence ends with a period, including sentences that end with a link.
* If a sentence ends with a link, the period comes after the closing link markup.
* Capitalize the first word after a colon when it introduces a complete sentence.

### Step 5: Word choice

* Write out abbreviations: "for example" not "e.g.," "such as" not "i.e.," "and so on" not "etc."
* Use "ID" not "id" or "Id."

### Step 6: Capitalization

* Use sentence case for parameter titles, field labels, and action titles.
* Do not capitalize common nouns unless a vendor requires it (for example, a brand name).
* Product and feature names follow the project's terminology guide.

### Step 7: Required/optional labels

* Label each parameter as **(Required)**, **(Optional)**, or **(Recommended)**.
* Labels appear in parentheses at the beginning of the description.
* Do not use all caps (REQUIRED) or other formatting variations.

### Step 8: Parameter description structure

Where possible, descriptions follow this order:

1. What the parameter does
1. Format, accepted values, and example inputs
1. Additional behavior notes or conditions
1. Link to supporting documentation (if applicable)

### Step 9: Report findings and produce revision

List each issue found with:
* Location (field name, section, or line number)
* Problem description
* Recommended fix

Then provide the full revised text.

## Output

Findings list followed by the complete revised document.

## Example: before and after

**Before:**
```
API Key (REQUIRED): The API Key for your account e.g. abc123. You can find this
in Settings > API Keys. Utilize this to authenticate requests.
```

**After:**
```
`api_key` (Required): Your account API key, used to authenticate requests.
Format: alphanumeric string. Example: `abc123`.
To find your key, go to **Settings > API Keys**.
```

What changed:
* `api_key` is code-formatted because it is a parameter name
* "(REQUIRED)" → "(Required)": sentence case, not all caps
* "e.g." → inline example with code formatting
* "Utilize" → removed. Description rewritten as direct action.
* Description follows the structure: what it does → format → where to find it

## Rules

* Preserve technical accuracy while simplifying wording.
* Do not rewrite descriptions that are technically correct. Only fix language and formatting issues.
* Do not invent accepted values, defaults, or behaviors.
* If a description is unclear about what a parameter does, mark it as a gap rather than guessing.
