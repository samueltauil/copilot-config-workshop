## Step 2: Custom Instructions &mdash; Build an Architect Agent

_SDLC Phase: **Design & Architecture**_

Your Planner Agent produced a project plan. Now you need to turn that plan into a concrete data schema and file structure. In this step you create [repository-wide custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) that standardize how Copilot writes code in this project, then build an **Architect Agent** that designs the data model.

### 📖 Theory: What are custom instructions?

The file `.github/copilot-instructions.md` gives Copilot persistent, project-wide context. Instead of repeating "use ES modules" or "follow our error handling patterns" in every prompt, you write it once and Copilot applies it automatically.

Key facts:

- The file must be at `.github/copilot-instructions.md` (case-sensitive).
- It uses plain Markdown.
- It applies to Copilot Chat and Copilot code review.
- It does **not** apply to inline completion suggestions (ghost text).

## ⌨️ Activity: Define project conventions

1. Open your project plan at `docs/project-plan.md` and review the technology choices and conventions.

1. Open `.github/copilot-instructions.md` and replace its contents with project-specific conventions. Use the following as a starting point and adjust based on your project plan:

    ```markdown
    # Task Manager — Project Conventions

    ## Language and Runtime

    - JavaScript, Node.js 20+.
    - Use ES module syntax (`import`/`export`), not CommonJS (`require`).

    ## Code Style

    - Use 2-space indentation.
    - Use single quotes for strings.
    - Use `const` by default; use `let` only when reassignment is needed. Never use `var`.
    - Add JSDoc comments to all exported functions and classes.

    ## Error Handling

    - Use `try/catch` blocks around operations that may fail.
    - Throw `Error` objects with descriptive messages. Do not throw plain strings.
    - Log errors with `console.error`, not `console.log`.

    ## Data Model

    - The Task entity has: id, title, description, status (todo/in-progress/done),
      priority (low/medium/high), createdAt, updatedAt.
    - Store all data in memory using plain JavaScript data structures.

    ## Testing

    - Use the built-in Node.js `assert` module.
    - Test files end with `.test.js`.
    - Each test function tests exactly one behavior.
    ```

1. Save the file.

## ⌨️ Activity: Verify Copilot uses your instructions

1. Open Copilot Chat (Ask mode) and type:

    ```
    Write a function that creates a new task object with default values.
    ```

1. Click the **Used n references** link at the top of the response. Confirm `.github/copilot-instructions.md` appears in the list. The response should follow your conventions (ES modules, single quotes, JSDoc).

## ⌨️ Activity: Create the Architect Agent

1. Create a new file at `.github/agents/architect.agent.md` with this content:

    ```markdown
    ---
    name: architect
    description: Reads a project plan and produces a detailed data schema and file structure
    tools: ["edit", "search", "read"]
    ---

    You are a software architect. Given a project plan, you produce a detailed
    technical design document.

    ## Output structure

    1. **Data models** — for each entity, list every property with its type,
       whether it is required, and any validation rules.
    2. **File structure** — show the complete directory tree with a one-line
       description of each file's purpose.
    3. **Module responsibilities** — describe what each module exports and
       how modules depend on each other.
    4. **Error handling strategy** — list the error types and where they
       are thrown.

    ## Rules

    - Follow the conventions in `.github/copilot-instructions.md`.
    - Keep the design minimal. Only include what the project plan requires.
    - Save the design document to `docs/schema.md`.
    ```

1. Save the file.

## ⌨️ Activity: Use the Architect Agent to design the schema

1. In Copilot Chat, select **architect** from the agent dropdown.

1. Type:

    ```
    Read #file:docs/project-plan.md and design the data schema and file
    structure for the Task Manager. Save the result to docs/schema.md.
    ```

1. Review the generated `docs/schema.md`. Verify it includes data model definitions, a file tree, and module responsibilities.

1. If something is missing, iterate:

    ```
    Add validation rules for each property in the Task model.
    ```

## ⌨️ Activity: Commit and push your work

1. Commit and push:

    ```bash
    git add .github/copilot-instructions.md .github/agents/ docs/
    git commit -m "Add project conventions and Architect Agent with schema"
    git push
    ```

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Confirm `.github/copilot-instructions.md` is saved at the exact path (case-sensitive).
- Open a new chat thread if an existing thread does not show the reference.
- If the architect agent does not create `docs/schema.md`, create the file manually and re-run.
- For a deeper walkthrough, see [exercises/02-custom-instructions/README.md](exercises/02-custom-instructions/README.md).

</details>
