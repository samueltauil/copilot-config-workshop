## Step 2: Repository-Wide Custom Instructions

Repository-wide custom instructions give GitHub Copilot persistent, project-specific context that applies to every Copilot Chat request in your repository.

### 📖 Theory: What are custom instructions?

The file `.github/copilot-instructions.md` lets you write instructions once and have Copilot apply them automatically to every chat request. Instead of repeating context like "use TypeScript" or "follow our error handling patterns" in every prompt, you write it once.

Key facts:

- The file must be at `.github/copilot-instructions.md` (case-sensitive).
- It uses plain Markdown.
- It applies to Copilot Chat and Copilot code review.
- It does **not** apply to inline completion suggestions (ghost text).
- Collaborators benefit from it automatically.

### ⌨️ Activity: Create your custom instructions file

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

1. Save and commit the file:

    ```bash
    git add .github/copilot-instructions.md
    git commit -m "Add repository-wide custom instructions for Copilot"
    git push
    ```

1. Open Copilot Chat and ask:

    ```
    Write a function that fetches a list of users from a REST API endpoint and returns the response body as parsed JSON.
    ```

1. Look at the **Used n references** link at the top of the Copilot response. Click it to expand the list. You should see `.github/copilot-instructions.md` listed.

1. Follow the full step-by-step instructions in [exercises/02-custom-instructions/README.md](../../exercises/02-custom-instructions/README.md) to complete this exercise.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Confirm the file is saved at exactly `.github/copilot-instructions.md` (path is case-sensitive on Linux/macOS).
- Check that the file is not empty.
- Try closing and reopening the Copilot Chat panel.
- Open a new chat thread if an existing thread does not show the reference.

</details>
