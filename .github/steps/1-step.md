## Step 1: Prompt Engineering &mdash; Build a Planner Agent

_SDLC Phase: **Planning & Requirements**_

Over the next five exercises you build a suite of specialized Copilot agents that cover the entire software development lifecycle. Together these agents will **plan, design, implement, test, and orchestrate** a Task Manager application.

In this first step you learn [prompt engineering](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat) strategies, explore Copilot's interaction modes, and create a **Planner Agent** that generates project plans.

### 📖 Theory: Copilot interaction modes

| Mode | How to access | Best for |
|------|---------------|----------|
| **Inline suggestions** | Start typing in the editor | Completing lines and functions as you code |
| **Ask mode** | Chat panel (default mode) | Asking questions, understanding code, exploring options |
| **Edit mode** | Mode selector &rarr; **Edit** | Making targeted changes to specific files |
| **Agent mode** | Mode selector &rarr; **Agent** | Multi-step tasks that create, edit, and run files autonomously |
| **Inline chat** | `Ctrl+I` / `Cmd+I` | Quick edits at the cursor without leaving the editor |

### 📖 Theory: Six prompt engineering strategies

| # | Strategy | Key idea |
|---|----------|----------|
| 1 | Start general, then get specific | State the goal, then add constraints |
| 2 | Give examples | Show expected inputs and outputs |
| 3 | Break tasks into steps | Compose complex features from smaller prompts |
| 4 | Avoid ambiguity | Name functions, files, and types explicitly |
| 5 | Indicate relevant code | Use `#file` to attach context |
| 6 | Experiment and iterate | Follow up in the same conversation to refine |

## ⌨️ Activity: Set up your environment

1. Open this repository in a **GitHub Codespace** (click **Code > Codespaces > Create codespace on main**). Alternatively, clone it locally and open it in VS Code.

1. Verify Copilot is active: look for the Copilot icon in the VS Code status bar.

1. Open Copilot Chat by clicking the chat icon in the sidebar.

## ⌨️ Activity: Explore Copilot interaction modes

Try each mode briefly so you know what is available.

1. **Inline suggestions:** Open `exercises/01-prompt-engineering/starter.js`, place your cursor at the bottom, and type `function hello(name) {`. Pause and observe the grey ghost text. Press `Tab` to accept or `Esc` to dismiss.

1. **Ask mode:** In Copilot Chat (default mode), type:

    ```
    What features would a Task Manager CLI application need?
    ```

    Read the response. Ask mode is great for brainstorming without changing files.

1. **Agent mode:** Switch the mode selector to **Agent**. You will use this mode to run the Planner Agent in the next activity.

## ⌨️ Activity: Create the Planner Agent

A custom agent is a `.agent.md` file with a YAML front matter block and a Markdown prompt body. You store agents in `.github/agents/`.

1. Create the agents directory:

    ```bash
    mkdir -p .github/agents
    ```

1. Create a new file at `.github/agents/planner.agent.md` with this content:

    ```markdown
    ---
    name: planner
    description: Generates structured project plans with user stories and acceptance criteria
    tools: ["edit", "search"]
    ---

    You are a software project planner. When the user describes an application
    idea, generate a comprehensive project plan in Markdown format.

    ## Output structure

    1. **Project overview** - one paragraph summarizing the application.
    2. **User stories** - numbered list, each with acceptance criteria.
    3. **Data model** - list the entities, their properties, and types.
    4. **File structure** - propose a directory layout under `src/`.
    5. **Implementation phases** - break the work into ordered milestones.

    ## Rules

    - Target Node.js 20+ with no external dependencies.
    - Use only built-in Node.js modules (fs, path, assert, etc.).
    - Keep the scope small enough for a workshop exercise.
    - Save the plan to `docs/project-plan.md`.
    ```

1. Save the file.

## ⌨️ Activity: Use the Planner Agent to generate a project plan

1. In Copilot Chat, select **planner** from the agent/mode dropdown.

1. Type the following prompt. Notice how it applies the **"start general, then get specific"** and **"give examples"** strategies:

    ```
    Create a project plan for a Task Manager CLI application.

    The app should support:
    - Creating, listing, updating, and deleting tasks
    - Each task has: title, description, status (todo/in-progress/done),
      priority (low/medium/high), createdAt, updatedAt
    - Filtering tasks by status or priority
    - Sorting tasks by priority or creation date
    - Storing data in memory (no database)

    Save the plan to docs/project-plan.md
    ```

1. Review the generated plan. If something is missing, follow up in the same conversation (**"experiment and iterate"** strategy):

    ```
    Add a section on error handling conventions and input validation rules.
    ```

1. Confirm `docs/project-plan.md` exists and contains a structured plan.

## ⌨️ Activity: Commit and push your work

1. Commit and push:

    ```bash
    git add docs/ .github/agents/
    git commit -m "Add Planner Agent and generate project plan"
    git push
    ```

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure the GitHub Copilot extension is installed and you are signed in to GitHub in VS Code.
- If the planner agent does not appear in the dropdown, reload the VS Code window (`Ctrl+Shift+P` &rarr; **Reload Window**).
- Confirm `.github/agents/planner.agent.md` has valid YAML front matter (the `description` property is required).
- If the agent does not create the file, create `docs/` manually (`mkdir -p docs`) and re-run the prompt.
- For a deeper walkthrough, see [exercises/01-prompt-engineering/README.md](exercises/01-prompt-engineering/README.md).

</details>
