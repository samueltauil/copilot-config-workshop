## Step 2: Custom Instructions - Build an Architect Agent

_SDLC Phase: **Design & Architecture**_

> **Why this matters:** After planning, the Design phase translates requirements into technical decisions: what data structures to use, how to organize code, and what patterns to follow. Copilot can help by applying your team's standards automatically, so every suggestion already follows your project conventions.

Your Planner Agent produced a project plan. Now you need to turn that plan into a concrete data schema and file structure. In this step, you create [repository-wide custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) that standardize how Copilot writes code in this project, then build an **Architect Agent** that designs the data model.

### 📖 Theory: What are custom instructions?

The file `.github/copilot-instructions.md` gives Copilot persistent, project-wide context. Instead of repeating your preferences in every prompt, you write them once and Copilot applies them automatically. Think of this file as a style guide that Copilot reads before every response.

Key facts:

- The file must be at `.github/copilot-instructions.md` (case-sensitive).
- It uses plain Markdown.
- It applies to Copilot Chat and Copilot code review.
- It does **not** apply to inline completion suggestions (ghost text).

## ⌨️ Activity: Define project conventions

1. Open your project plan at `docs/project-plan.md` and review the technology choices and conventions.

1. Create a new file at `.github/copilot-instructions.md`. In the VS Code Explorer sidebar, right-click the `.github` folder and select **New File**. Name it `copilot-instructions.md`. Paste the following content and adjust based on your project plan:

    ```markdown
    # Task Manager - Project Conventions

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

    > 💡 **Tip:** In Codespaces, files save automatically. If you are working locally, save with `Ctrl+S` / `Cmd+S`.

## ⌨️ Activity: Verify Copilot uses your instructions

1. Open Copilot Chat (Ask mode) and type:

    ```
    Based on the project conventions, describe the technology stack,
    coding standards, and data model for this project.
    ```

1. Click the **Reviewed n files** link at the top of the response. Confirm `.github/copilot-instructions.md` appears in the list. The response should reflect the conventions you defined (ES modules, single quotes, the Task entity properties, and so on).

    > 🪧 **Note:** The **Reviewed n files** link appears at the top of each Copilot Chat response. Click it to expand the list of loaded instruction files.
    >
    > <img width="504" alt="Screenshot: Copilot Chat showing Reviewed n files panel" src="../../.github/images/file-references.png" />

## ⌨️ Activity: Create the Architect Agent

1. Create a new file at `.github/agents/architect.agent.md` with this content:

    ```markdown
    ---
    name: architect
    description: Reads a project plan and produces a detailed data schema and file structure
    tools: ["edit", "search", "read"]
    handoffs: 
    - agent: developer
      label: "Implement the feature"
      prompt: "Read #file:docs/schema.md and implement the feature in src/. Use only built-in Node.js modules."
      send: false
    ---

    You are a software architect. Given a project plan, you produce a detailed
    technical design document.

    ## Output structure

    1. **Data models** - for each entity, list every property with its type,
       whether it is required, and any validation rules.
    2. **File structure** - show the complete directory tree with a one-line
       description of each file's purpose.
    3. **Module responsibilities** - describe what each module exports and
       how modules depend on each other.
    4. **Error handling strategy** - list the error types and where they
       are thrown.

    ## Rules

    - Follow the conventions in `.github/copilot-instructions.md`.
    - Keep the design minimal. Only include what the project plan requires.
    - Save the design document to `docs/schema.md`.
    ```

    > 💡 **Tip:** In Codespaces, files save automatically. If you are working locally, save with `Ctrl+S` / `Cmd+S`.

    > ⚠️ **Expected warning:** VS Code may show a validation warning that the `developer` agent referenced in `handoffs` does not exist yet. This is expected — you will create the Developer Agent in Step 3. The handoff will work once all agents are in place. You will use these handoffs in the final exercise (Step 7) to chain all agents together.

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

1. In the VS Code left sidebar, click the **Source Control** tab.

1. Hover over each changed file and click the **+** (Stage Changes) button, or click the **+** next to **Changes** to stage everything.

    <img width="300" alt="Screenshot: Stage changes icon in VS Code Source Control" src="https://raw.githubusercontent.com/skills/getting-started-with-github-copilot/main/.github/images/staging-changes-icon.png" />

1. In the **Message** text box, type:

    ```
    Add project conventions and Architect Agent with schema
    ```

1. Click **Commit**, then click **Sync Changes** to push to GitHub.

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Confirm `.github/copilot-instructions.md` is saved at the exact path (case-sensitive).
- Open a new chat thread if an existing thread does not show the reference.
- If the architect agent does not create `docs/schema.md`, create the file manually and re-run.
- For a deeper walkthrough, see [exercises/02-custom-instructions/README.md](exercises/02-custom-instructions/README.md).

</details>
