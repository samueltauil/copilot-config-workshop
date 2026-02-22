# Exercise 02: Custom Instructions — Build an Architect Agent

**SDLC Phase: Design & Architecture**

In this exercise you create repository-wide custom instructions and build an **Architect Agent** that turns a project plan into a data schema. You learn how `.github/copilot-instructions.md` works, what to include in it, and how to verify that Copilot loads it.

**Duration:** ~30 minutes

---

## Learning Objectives

- Understand what repository-wide custom instructions do and when Copilot loads them
- Create a `.github/copilot-instructions.md` file with project conventions
- Know what to include and what to avoid in custom instructions
- Build an Architect Agent that reads a project plan and produces a data schema
- Verify Copilot references your instructions using the **Used n references** panel

---

## Prerequisites

- Completion of [Exercise 01](../01-prompt-engineering/README.md) (you need `docs/project-plan.md`)
- GitHub Codespaces or VS Code with the GitHub Copilot extension installed
- The `.github/agents/` directory exists from Exercise 01

---

## Understanding Custom Instructions

### What are custom instructions?

The file `.github/copilot-instructions.md` gives Copilot persistent, project-wide context. Instead of repeating "use ES modules" or "follow our error handling patterns" in every prompt, you write it once. Copilot applies it automatically to every relevant interaction.

### Where does the file live?

The file must be at `.github/copilot-instructions.md` in the repository root. The path is case-sensitive on Linux and macOS.

### When does Copilot load it?

Copilot loads custom instructions for:

- Copilot Chat in VS Code, Visual Studio, JetBrains IDEs, and GitHub.com
- Copilot code review

Custom instructions do **not** apply to inline completion suggestions (ghost text). For inline completions, open files provide context.

### What to include

- Language and runtime requirements
- Code style conventions (indentation, quotes, variable declarations)
- Error handling patterns
- Testing conventions and tools
- Project-specific data models or terminology

### What to avoid

- References to specific files or code paths (use path-specific instructions for that)
- Instructions that conflict with each other
- Overly long content (the file is included in every request)
- Instructions about Copilot behavior (e.g., "always explain your code")

See the [official documentation](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) for the full reference.

---

## Step 1: Create the Custom Instructions File

1. Open your repository in a Codespace or in VS Code locally.

2. Create the file at `.github/copilot-instructions.md`. You can right-click the `.github` folder in the Explorer panel and select **New File**, or run:

   ```bash
   touch .github/copilot-instructions.md
   ```

3. Open `docs/project-plan.md` from Exercise 01. Review the technology choices and conventions your Planner Agent defined.

4. Open `.github/copilot-instructions.md` and add the following content. Adjust it if your project plan specifies different conventions:

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

   ## Dependencies

   - Do not add external dependencies.
   - Use only built-in Node.js modules (fs, path, assert, crypto, etc.).
   ```

5. Save the file.

---

## Step 2: Verify Copilot Uses Your Instructions

1. Open Copilot Chat in VS Code (click the chat icon in the sidebar or press `Ctrl+Alt+I`).

2. Select **Ask** mode and type:

   ```
   Write a function that creates a new task object with default values.
   ```

3. Review the response. It should follow your conventions:

   - ES module syntax (`export`)
   - Single quotes for strings
   - `const` for variable declarations
   - JSDoc comment on the function
   - A `try/catch` block if the function performs error-prone operations

4. Click the **Used n references** link at the top of the response. Expand the list and confirm `.github/copilot-instructions.md` appears.

   If you see your instructions file listed, Copilot loaded them.

5. Open a new chat thread and try a prompt that contradicts your instructions:

   ```
   Write a function that reads a JSON file using require() and var.
   ```

   Copilot follows your explicit request. Custom instructions set defaults but do not override direct prompts.

---

## Step 3: Create the Architect Agent

The Architect Agent reads a project plan and produces a data schema with file structure. It bridges the gap between planning (Exercise 01) and implementation (Exercise 03).

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

2. Save the file.

### How the agent file works

- The YAML front matter (`name`, `description`, `tools`) registers the agent in Copilot Chat.
- The `tools` array grants the agent permission to edit files, search the workspace, and read files.
- The Markdown body is the system prompt. It tells the agent what role to play and what rules to follow.
- The agent automatically inherits your custom instructions from `.github/copilot-instructions.md`.

---

## Step 4: Generate the Data Schema

1. In Copilot Chat, select **architect** from the agent dropdown.

2. Type the following prompt:

   ```
   Read #file:docs/project-plan.md and design the data schema and file
   structure for the Task Manager. Save the result to docs/schema.md.
   ```

3. Review the generated `docs/schema.md`. Verify it includes:

   - A Task data model with properties, types, and validation rules
   - A directory tree showing where each file lives under `src/`
   - Module responsibilities describing what each file exports
   - An error handling strategy

4. If something is missing, iterate in the same conversation:

   ```
   Add validation rules for each property in the Task model.
   ```

5. Open `docs/schema.md` and confirm the content looks complete and follows your project conventions.

### What a good schema includes

The Task model should define at minimum:

| Property | Type | Required | Validation |
|----------|------|----------|------------|
| id | string | yes | Generated by `crypto.randomUUID()` |
| title | string | yes | Non-empty, max 100 characters |
| description | string | no | Max 500 characters |
| status | string | yes | One of: todo, in-progress, done |
| priority | string | yes | One of: low, medium, high |
| createdAt | string (ISO 8601) | yes | Set on creation |
| updatedAt | string (ISO 8601) | yes | Updated on every change |

Your schema may differ. The exact content depends on your project plan and the agent's output.

---

## Step 5: Commit and Push

1. Stage and commit all new files:

   ```bash
   git add .github/copilot-instructions.md .github/agents/ docs/
   git commit -m "Add project conventions and Architect Agent with schema"
   git push
   ```

2. After you push, the workflow validates that `copilot-instructions.md` and `docs/schema.md` exist, then posts the next step.

---

## Verification

Confirm the following before moving on:

- [ ] `.github/copilot-instructions.md` exists and contains project conventions
- [ ] Copilot Chat shows `.github/copilot-instructions.md` in the **Used n references** panel
- [ ] `.github/agents/architect.agent.md` exists with valid YAML front matter
- [ ] `docs/schema.md` exists and contains a data model, file structure, and module responsibilities
- [ ] All files are committed and pushed

---

## Troubleshooting

**Copilot does not use my instructions:**

- Confirm the file is saved at exactly `.github/copilot-instructions.md` (case-sensitive path).
- Check that the file is not empty.
- Open a new chat thread. Existing threads may not reload instructions.
- Confirm your organization has not disabled repository custom instructions.

**The "Used n references" panel does not list my instructions:**

- Open a new chat thread with the `+` icon.
- Verify the file name is `copilot-instructions.md` inside `.github/` at the repository root.

**The Architect Agent does not appear in the dropdown:**

- Reload the VS Code window (`Ctrl+Shift+P` then **Reload Window**).
- Confirm `.github/agents/architect.agent.md` has valid YAML front matter with a `description` property.

**The agent does not create `docs/schema.md`:**

- Create the `docs/` directory manually (`mkdir -p docs`) and re-run the prompt.
- Make sure you selected **architect** from the agent dropdown, not Ask or Edit mode.

---

## Reference: Example Custom Instructions

This repository includes a fully commented example at [example-copilot-instructions.md](example-copilot-instructions.md). Open it to see:

- How to structure instructions for a larger project
- What types of information are most useful to include
- Common patterns to avoid

---
