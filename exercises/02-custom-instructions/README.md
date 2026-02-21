# Exercise 2: Repository-Wide Custom Instructions

**Learning objectives:**
- Understand what repository-wide custom instructions are and when to use them
- Create a `.github/copilot-instructions.md` file from scratch
- Verify that Copilot uses your custom instructions in responses

**Duration:** ~25 minutes

**Prerequisites:** Completion of [Exercise 1](../01-prompt-engineering/README.md) is recommended but not required. GitHub Codespaces or Visual Studio Code with the GitHub Copilot extension installed.

---

## Background

Repository-wide custom instructions allow you to give GitHub Copilot persistent guidance that applies to every request made in the context of a repository. Instead of repeating the same context in every prompt (such as "use TypeScript", "follow our error handling patterns", or "this project uses PostgreSQL"), you write it once in a file and Copilot picks it up automatically.

The file is named `copilot-instructions.md` and must be placed in the `.github` directory at the root of your repository. See [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) for the full reference.

---

## What Custom Instructions Support

Repository-wide custom instructions are used by the following Copilot features (as of the current documentation):

- Copilot Chat in VS Code, Visual Studio, JetBrains IDEs, and on GitHub.com
- Copilot code review

They are **not** used for inline code completion suggestions (the ghost text that appears as you type). For inline completions, the content of open files provides context.

---

## Setup

1. Open this repository in a Codespace or in VS Code locally.
2. Confirm that the `.github` directory exists at the root of the repository. If it does not, create it:
   ```bash
   mkdir .github
   ```

---

## Step 1: Create the Custom Instructions File

1. In VS Code, create a new file at:
   ```
   .github/copilot-instructions.md
   ```
   You can do this in the VS Code Explorer panel (left sidebar) by right-clicking the `.github` folder and selecting **New File**, or by running:
   ```bash
   touch .github/copilot-instructions.md
   ```

2. Open the file. It should be empty.

   > **Screenshot reference:** The Explorer panel in VS Code shows the `.github` folder containing `copilot-instructions.md`. The file tab is open and the editor area shows an empty file.

---

## Step 2: Write Your Custom Instructions

Custom instructions are written in plain Markdown. They should contain information about your project that you would otherwise repeat in every prompt.

**Guidelines from the official documentation:**
- Do not include instructions that refer to specific code (use path-specific instructions for that, covered in Exercise 3).
- Keep instructions concise - they are included in every request.
- Focus on coding conventions, tools, and project context.
- Avoid instructions that conflict with each other.

Copy the following example into `.github/copilot-instructions.md`:

```markdown
# Project Custom Instructions

## Language and Runtime

- This project uses JavaScript (Node.js 20+).
- Use ES module syntax (`import`/`export`) rather than CommonJS (`require`).
- Target environments: Node.js for backend files, modern browsers for frontend files.

## Code Style

- Use 2-space indentation.
- Use single quotes for strings.
- Use `const` for variables that are not reassigned; use `let` otherwise. Never use `var`.
- Add JSDoc comments to all exported functions.

## Error Handling

- Always use `try/catch` blocks around async operations.
- Throw `Error` objects with descriptive messages. Do not throw plain strings.
- Log errors using `console.error`, not `console.log`.

## Testing

- Write tests using the built-in Node.js `assert` module.
- Test file names should end in `.test.js`.
- Each test function should test exactly one behavior.
```

3. Save the file (`Ctrl+S` on Windows/Linux, `Cmd+S` on macOS).

---

## Step 3: Verify That Copilot Uses Your Instructions

1. Open Copilot Chat in VS Code (click the chat icon in the sidebar, or press `Ctrl+Alt+I` on Windows/Linux, `Cmd+Shift+I` on macOS).

2. Ask the following question:
   ```
   Write a function that fetches a list of users from a REST API endpoint and returns the response body as parsed JSON.
   ```

3. Review the response. Based on the custom instructions you wrote, the response should:
   - Use `import`/`export` syntax (not `require`)
   - Use `const` for variable declarations
   - Include a `try/catch` block
   - Include a JSDoc comment

4. To confirm that Copilot loaded your instructions, look at the **Used n references** link at the top of the Copilot response. Click it to expand the list.

   > **Screenshot reference:** After Copilot responds, there is a dropdown link labeled "Used 2 references" (or similar number) at the top of the response. Clicking it expands a list of files, including `.github/copilot-instructions.md`. This confirms Copilot read your instructions.

   If you see `.github/copilot-instructions.md` listed in the references, the instructions are working correctly.

---

## Step 4: Test the Instructions with a Contrast Prompt

To see the difference your instructions make, temporarily observe what happens without them.

1. Start a new chat thread in Copilot Chat (click the `+` icon to open a new conversation, or close and reopen the Chat panel).

2. Ask:
   ```
   Write a function that reads a JSON file from disk and returns its contents.
   ```

3. The response should still follow your custom instructions (using ES modules, `const`, `try/catch`, etc.).

4. Now try asking Copilot explicitly for something that contradicts your instructions:
   ```
   Write the same function using require() and var declarations.
   ```

5. Notice that Copilot responds with the code you asked for. Custom instructions provide default behavior; they do not prevent you from overriding them in a specific prompt.

---

## Step 5: Review the Example File

This repository includes a fully-commented example of a real-world `copilot-instructions.md` file:

```
exercises/02-custom-instructions/example-copilot-instructions.md
```

Open that file and read through it. It shows:
- How to structure instructions for a larger project
- What types of information are most useful to include
- What to avoid

---

## Step 6: Commit Your Custom Instructions

1. Stage and commit the file:
   ```bash
   git add .github/copilot-instructions.md
   git commit -m "Add repository-wide custom instructions for Copilot"
   git push
   ```

2. The file is now part of your repository. Every collaborator who uses Copilot in this repository will benefit from these instructions automatically.

---

## Troubleshooting

**Copilot does not seem to use my instructions:**
- Confirm the file is saved at exactly `.github/copilot-instructions.md` (the path is case-sensitive on Linux/macOS).
- Check that the file is not empty.
- Try closing and reopening the Copilot Chat panel.
- Confirm that your organization has not disabled repository custom instructions (requires administrator access to verify).

**The "Used n references" link does not show my instructions file:**
- Open a new chat thread (old threads may not reload the instructions automatically).
- Confirm the file path is correct: the file must be named `copilot-instructions.md` inside the `.github` folder at the repository root.

---

## Summary

You created a `copilot-instructions.md` file that gives Copilot persistent, project-specific context. Key points:

- The file lives at `.github/copilot-instructions.md`.
- It uses plain Markdown.
- It applies to all Copilot Chat requests in the repository.
- It does not apply to inline completion suggestions.
- It can be overridden in specific prompts if needed.

---

## Next Steps

Proceed to [Exercise 3: Path-Specific Instructions](../03-path-specific-instructions/README.md).
