description: Rewrite a passage or file to publication-ready style, in place.
---

Rewrite the following text to publication-ready technical documentation standard. If $ARGUMENTS is a file path, read that file's content as the text to edit; otherwise treat $ARGUMENTS as the text itself.

Rules:
* Active voice. Subject performs the action.
* Sentence case for headings.
* No em dashes, semicolons, or smart quotes.
* No bare demonstrative pronouns. Follow "This/These/That/Those" with a noun.
* No filler: remove "it's worth noting", "please note", "keep in mind", "in order to", "due to the fact that".
* No AI-sounding language: remove "leverage", "utilize", "streamline", "comprehensive", "robust", "seamlessly".
* Lead each sentence with its information, not a preamble announcing the information.
* One idea per sentence. Split compounds.
* Conditions before instructions: "To X, do Y."

Preserve technical accuracy. Do not invent behavior, parameters, or UI labels not present in the original text.

Text to edit: $ARGUMENTS