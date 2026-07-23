description: Audit a document for low-information, fillable sentences.
---

Audit the document at $ARGUMENTS for information density. Identify every sentence or paragraph that does not deliver new, actionable information to the reader.

## What counts as low-density content

* Restatements: sentences that repeat what a heading, previous sentence, or adjacent paragraph already says
* Throat-clearing: opening sentences that announce what is coming instead of delivering it. "This section describes how to..." "In this guide, you will learn..."
* Transition filler: sentences whose only purpose is connecting two paragraphs. If removing the sentence does not break the reader's understanding, it is filler.
* Redundant qualifiers: "very important", "absolutely necessary", "completely optional". The qualifier adds no information the noun does not already carry.
* UI narration: describing what the reader can already see on screen. "The Save button saves your changes."
* Defensive hedging: "It should be noted that...", "Keep in mind that...", "Please be aware that...". Strip the hedge and keep the content.

## Output format

For each finding, report on its own line:
Line [N]: [quoted sentence or phrase]
Problem: [which low-density pattern it matches]
Action: [delete / merge with adjacent sentence / replace with: "..."]

End with a summary:
* Total sentences in document
* Sentences flagged as low-density
* Percentage that could be cut or compressed
* Estimated word count reduction