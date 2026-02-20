---
applyTo: "**/*.md"
---

# Markdown File Instructions

This is an example path-specific instruction file. It applies to all Markdown files
(`**/*.md`) in this repository. When Copilot is working on a Markdown file, it will
combine these instructions with the repository-wide instructions in
`.github/copilot-instructions.md`.

---

## Writing Style

- Use present tense for all instructions and descriptions.
- Keep sentences short. Aim for a maximum of 25 words per sentence.
- Use active voice. For example, write "Run the command" not "The command should be run".
- Do not use em dashes (--). Use a comma or rewrite the sentence.
- Avoid filler words such as "simply", "just", "easily", and "obviously".

## Formatting

- Use ATX-style headings (`#`, `##`, `###`), not underline-style headings.
- Use fenced code blocks (```) with a language identifier for all code samples.
- Use ordered lists (1., 2., 3.) for sequential steps.
- Use unordered lists (-) for non-sequential items.
- Use a blank line before and after headings, lists, and code blocks.

## Links

- Use relative links for files within the repository.
- Include link text that describes the destination (avoid "click here").

## Code Examples

- Every code example must be complete and runnable.
- Include the expected output in a comment or a separate code block labeled `# Output`.
