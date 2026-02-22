---
applyTo: "**/*.{js,ts,py,css,html,rb,go,java,sh}"
---

# Code Style for GitHub Skills Exercises

You are writing sample code for a learning exercise. The code will be read and modified by learners who may be encountering these concepts for the first time.

## Core Principles

- **Prioritize clarity over cleverness** — code must be immediately understandable.
- **Avoid advanced language features** unless they are the specific learning objective.
- **Avoid production complexities** (extensive error handling, edge cases) unless teaching them.
- **Use realistic but simplified scenarios** — the code should feel like a real project, not a toy.
- **Prefer explicit behavior** over implicit magic — no "it just works" abstractions.
- **Ensure code is complete and runnable** unless otherwise specified.

## Writing Guidelines

- Use descriptive variable and function names. Abbreviations confuse beginners.
- Add comments sparingly — explain *why*, not *what*. The code should be self-documenting.
- Keep files short. If a file exceeds 50 lines, consider whether it can be simplified.
- Use consistent formatting. Match the conventions of the language ecosystem.
- Provide complete examples, not fragments. Learners should be able to copy-paste and run.

## Psychology — Cognitive Load

- One concept per code example. Don't demonstrate 3 features in a single snippet.
- Use familiar patterns. Don't introduce unusual coding styles alongside new GitHub features.
- Provide expected output as comments when the result isn't obvious.
