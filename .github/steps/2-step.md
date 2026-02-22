## Step 2: Repository-Wide Custom Instructions

Copilot is giving your team inconsistent suggestions. One developer gets ES module syntax; another gets CommonJS. You need a way to set project-wide defaults once so every team member gets consistent help. [Repository-wide custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) let you do exactly that.

### 📖 Theory: What are custom instructions?

The file `.github/copilot-instructions.md` lets you write instructions once and have Copilot apply them automatically to every chat request. Instead of repeating context like "use TypeScript" or "follow our error handling patterns" in every prompt, you write it once.

Key facts:

- The file must be at `.github/copilot-instructions.md` (case-sensitive).
- It uses plain Markdown.
- It applies to Copilot Chat and Copilot code review.
- It does **not** apply to inline completion suggestions (ghost text).
- Collaborators benefit from it automatically.

## ⌨️ Activity: Create your custom instructions file

1. In your repository, create the file `.github/copilot-instructions.md`.

    You can use the VS Code Explorer panel or run:

    ```bash
    touch .github/copilot-instructions.md
    ```

1. Add the following content to the file:

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

1. Save the file.

## ⌨️ Activity: Verify Copilot uses your instructions

1. Open Copilot Chat and ask:

    ```
    Write a function that fetches a list of users from a REST API endpoint
    and returns the response body as parsed JSON.
    ```

1. Review the response. Based on your custom instructions, it should:
    - Use `import`/`export` syntax (not `require`)
    - Use `const` for variable declarations
    - Include a `try/catch` block
    - Include a JSDoc comment

1. Click the **Used n references** link at the top of the Copilot response. You should see `.github/copilot-instructions.md` listed. This confirms Copilot loaded your instructions.

## ⌨️ Activity: Commit and push your work

1. Commit and push:

    ```bash
    git add .github/copilot-instructions.md
    git commit -m "Add repository-wide custom instructions for Copilot"
    git push
    ```

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Confirm the file is saved at exactly `.github/copilot-instructions.md` (path is case-sensitive on Linux/macOS).
- Check that the file is not empty.
- Try closing and reopening the Copilot Chat panel.
- Open a new chat thread if an existing thread does not show the reference.
- For a deeper walkthrough, see [exercises/02-custom-instructions/README.md](exercises/02-custom-instructions/README.md).

</details>
