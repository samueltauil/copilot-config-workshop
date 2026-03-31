## Step 1: Prompt Engineering - Build a Planner Agent

_Welcome, {{ login }}! You are working in [{{ full_repo_name }}](https://github.com/{{ full_repo_name }})._

_SDLC Phase: **Planning & Requirements**_

> **Why this matters:** Every project starts with a plan. In the SDLC, the Planning phase defines what you will build, for whom, and why. Copilot can accelerate this phase by helping you brainstorm requirements, structure user stories, and draft project plans, all through natural language conversation.

Over the next seven exercises you build a suite of specialized Copilot agents that cover the entire software development lifecycle (SDLC). Together, these agents will **plan, design, implement, test, review, secure, and orchestrate** a Task Manager application.

In this first step, you learn [prompt engineering](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat) strategies, explore Copilot's interaction modes, and create a **Planner Agent** that generates project plans.

> **What is prompt engineering?** Prompt engineering is the practice of writing clear, structured requests so that an AI assistant produces the best possible response. Think of it as giving precise instructions to a colleague.

### 📖 Theory: Copilot interaction modes

Copilot offers five ways to work. Each mode fits a different situation. You do not need to memorize them all right now. The table below is a quick reference you can revisit any time.

| Mode | How to access | Best for |
|------|---------------|----------|
| **Inline suggestions** | Start typing in the editor | Completing lines and functions as you code |
| **Ask mode** | Chat panel (default mode) | Asking questions, understanding code, exploring options |
| **Agent mode** | Mode selector &rarr; **Agent** | Multi-step tasks that create, edit, and run files autonomously |
| **Plan mode** | Mode selector &rarr; **Plan** | Reviewing and approving a step-by-step plan before Copilot acts |
| **Inline chat** | `Ctrl+I` / `Cmd+I` | Quick edits at the cursor without leaving the editor |

> **Where is the mode selector?** Look at the top of the Copilot Chat panel. A dropdown lets you switch between Ask, Agent, and Plan modes.
>
> <img width="350" alt="Screenshot: Copilot Chat mode selector" src="https://raw.githubusercontent.com/skills/getting-started-with-github-copilot/main/.github/images/ask-mode-selection.png" />

> **Plan mode vs. a Planner Agent:** Plan mode lets Copilot outline steps and wait for your approval before executing them. That is useful for one-off tasks, but it does not retain project-specific rules between conversations. A custom Planner Agent, on the other hand, carries persistent instructions (role, output format, constraints) so every conversation starts with the same context. In this workshop you build agents because they are reusable, shareable with your team, and composable across the entire SDLC.

### 📖 Theory: Six prompt engineering strategies

Good prompts lead to good results. These six strategies help you communicate with Copilot more effectively, regardless of your technical background.

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

1. Verify Copilot is active: look for the Copilot icon (a small sparkle icon) in the VS Code status bar at the bottom of the window.

1. Open Copilot Chat by clicking the chat icon in the sidebar (or press `Ctrl+Alt+I` / `Cmd+Alt+I`).

## ⌨️ Activity: Explore Copilot interaction modes

Try each mode briefly so you know what is available.

1. **Inline suggestions:** Open `exercises/01-prompt-engineering/starter.js`, place your cursor at the bottom, and type `function hello(name) {`. Pause and observe the grey ghost text. Press `Tab` to accept or `Esc` to dismiss.

    <img width="700" alt="Screenshot: Copilot inline suggestion ghost text" src="https://raw.githubusercontent.com/skills/getting-started-with-github-copilot/main/.github/images/shadow-text.gif" />

1. **Ask mode:** In Copilot Chat (default mode), type:

    ```
    What features would a Task Manager CLI application need?
    ```

    Read the response. Ask mode is great for brainstorming without changing files.

1. **Agent mode:** Switch the mode selector to **Agent** (see the mode selector screenshot in the theory section above). You will use this mode to run the Planner Agent in the next activity.

## ⌨️ Activity: Create the Planner Agent

> **What is an agent file?** An agent file is a Markdown document that gives Copilot a specialized role. It tells Copilot who it should act as, what output format to use, and what rules to follow. Think of it as a job description for your AI assistant.

A custom agent is a `.agent.md` file with a YAML front matter block (a small configuration header) and a Markdown prompt body. You store agents in `.github/agents/`.

1. In the VS Code Explorer sidebar, right-click the `.github` folder and select **New Folder**. Name it `agents`.

1. Right-click the new `.github/agents` folder and select **New File**. Name it `planner.agent.md`.

1. Paste the following content into the file:

    ```markdown
    ---
    name: planner
    description: Generates structured project plans with user stories and acceptance criteria
    tools: ["edit", "search"]
    handoffs: 
    - agent: architect
      label: "Design the architecture"
      prompt: "Read #file:docs/project-plan.md and update docs/schema.md with any new or modified data structures."
      send: false
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

    > 💡 **Tip:** In Codespaces, files save automatically. If you are working locally, save with `Ctrl+S` / `Cmd+S`.

    > ⚠️ **Expected warning:** VS Code may show a validation warning that the `architect` agent referenced in `handoffs` does not exist yet. This is expected — you will create the Architect Agent in Step 2. The handoff will work once all agents are in place. You will use these handoffs in the final exercise (Step 7) to chain all agents together.

    > 💡 **Tip:** Learn more about custom agents:
    >
    > - [VS Code Docs: Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
    > - [GitHub Docs: Custom Agents Configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)

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

1. In the VS Code left sidebar, click the **Source Control** tab (the icon that looks like a branch).

1. You should see your changed files listed. Hover over each file and click the **+** (Stage Changes) button to add them to the commit.

    <img width="300" alt="Screenshot: Stage changes icon in VS Code Source Control" src="https://raw.githubusercontent.com/skills/getting-started-with-github-copilot/main/.github/images/staging-changes-icon.png" />

    > 💡 **Tip:** You can also click the **+** icon next to **Changes** to stage all files at once.

1. In the **Message** text box above the file list, type a short description, for example:

    ```
    Add Planner Agent and generate project plan
    ```

1. Click the **Commit** button, then click **Sync Changes** to push your work to GitHub.

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure the GitHub Copilot extension is installed and you are signed in to GitHub in VS Code.
- If the planner agent does not appear in the dropdown, reload the VS Code window (`Ctrl+Shift+P` &rarr; **Reload Window**).
- Confirm `.github/agents/planner.agent.md` has valid YAML front matter (the `description` property is required).
- If the agent does not create the file, right-click in the Explorer sidebar and select **New Folder**, name it `docs`, then re-run the prompt.
- For a deeper walkthrough, see [exercises/01-prompt-engineering/README.md](exercises/01-prompt-engineering/README.md).

</details>
