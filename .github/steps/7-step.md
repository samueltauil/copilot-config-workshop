## Step 7: Agent Orchestration - Build an Orchestrator Agent

_SDLC Phase: **Full Lifecycle**_

> **Why this matters:** Real software development is not a series of isolated steps. Features flow from planning through design, implementation, and testing. An orchestrator coordinates these phases so nothing falls through the cracks. This mirrors how teams use project management tools to track work across the SDLC.

You now have four agents that each own one phase of the software development lifecycle: **Planner** (plan), **Architect** (design), **Developer** (implement), and **Tester** (test). In this final exercise, you create an **Orchestrator Agent** that uses **handoffs** to chain all four agents into a guided pipeline, and then prove it works by delivering a new feature end-to-end.

### 📖 Theory: Bringing agents together

Each agent file you created teaches Copilot a specialized role. An orchestrator agent ties them together using the `handoffs:` front matter property.

> **Think of it like a relay race.** Each agent runs one leg and then passes the baton to the next. The orchestrator is the coach who organizes the handoffs.

| Agent | SDLC Phase | Key Artifacts |
|-------|-----------|---------------|
| Planner | Planning | `docs/project-plan.md` |
| Architect | Design | `docs/schema.md` |
| Developer | Implementation | `src/**/*.js` |
| Tester | Testing | `tests/**/*.test.js` |
| **Orchestrator** | **Full lifecycle** | **Coordinates all of the above** |

### 📖 Theory: How handoffs work

In the previous steps, each agent included a `handoffs` entry in its YAML front matter that references the next agent in the pipeline (for example, the Planner hands off to the Architect). You may have noticed VS Code showed a validation warning because the target agent did not exist yet at the time. Now that all four agents are created, those handoffs resolve correctly.

Handoffs create one-click buttons in Copilot Chat. When an agent finishes its work, the buttons appear at the bottom of the response. Each button pre-fills a prompt and switches to the named agent. You click each button in order to move the feature through the full lifecycle.

Each handoff entry in the YAML front matter specifies four fields:

| Field | Purpose |
|-------|---------|
| `agent` | The name of the next agent to invoke (matches the `name` field in the target agent's front matter) |
| `label` | The text shown on the button in Copilot Chat |
| `prompt` | The pre-filled message sent to the next agent |
| `send` | `true` to auto-submit the prompt, `false` to let the user review it first |

Setting `send: false` keeps the user in the loop. They can edit the pre-filled prompt before it runs.

```yaml
handoffs:
  - agent: architect
    label: "Design the architecture"
    prompt: "Read #file:docs/project-plan.md and update docs/schema.md."
    send: false
```

> 🪧 **Note:** Handoffs are supported in VS Code and GitHub Codespaces. They are not supported when running agents on GitHub.com.

The Orchestrator Agent below uses handoffs to expose all four agents as a sequential pipeline.

> 🪧 **Note:** After the Orchestrator responds, you see four handoff buttons at the bottom of the message labeled **1. Plan the feature**, **2. Design the architecture**, **3. Implement the feature**, and **4. Test the feature**.

Agent files support these advanced properties:

| Property | Purpose |
|----------|---------|
| `tools` | Controls what the agent can do (e.g., read files, edit files, run commands) |
| `#file:` references | Attaches other files as context inside the agent prompt body |
| `handoffs` | Creates buttons that switch to the next agent with a pre-filled prompt |

## ⌨️ Activity: Review your agents

Before building the orchestrator, verify the agent suite is complete.

1. Confirm these files exist:

    ```
    .github/agents/planner.agent.md
    .github/agents/architect.agent.md
    .github/agents/developer.agent.md
    .github/agents/tester.agent.md
    ```

1. Open each file and confirm it has valid YAML front matter with `name` and `description`.

1. If any file is missing, go back to the corresponding exercise step and create it.

## ⌨️ Activity: Create the Orchestrator Agent

1. Create `.github/agents/orchestrator.agent.md`:

    ```markdown
    ---
    name: orchestrator
    description: Coordinates the full SDLC workflow for new features using the planner, architect, developer, and tester agents
    tools: [read/readFile, search]
    handoffs:
      - agent: planner
        label: "1. Plan the feature"
        prompt: "Analyze the feature request above and update docs/project-plan.md with the new feature scope."
        send: false
      - agent: architect
        label: "2. Design the architecture"
        prompt: "Read #file:docs/project-plan.md and update docs/schema.md with any new or modified data structures."
        send: false
      - agent: developer
        label: "3. Implement the feature"
        prompt: "Read #file:docs/schema.md and implement the feature in src/. Use only built-in Node.js modules."
        send: false
      - agent: tester
        label: "4. Test the feature"
        prompt: "Read the updated source files in src/ and update tests/ to cover the new feature. Run node --test tests/ and fix any failures."
        send: false
    ---

    You are the orchestrator. When the user requests a new feature you
    summarize the work to be done across all four phases, then use the
    handoff buttons below to guide the user through each phase. Do not start the first phase until the user clicks the handoff button. After each phase, summarize the results and next steps before moving to the next phase.

    ## Phases

    1. **Plan** - The Planner Agent updates `docs/project-plan.md`.
    2. **Design** - The Architect Agent updates `docs/schema.md`.
    3. **Develop** - The Developer Agent implements the feature in `src/`.
    4. **Test** - The Tester Agent writes and runs tests in `tests/`.

    ## Rules

    - Summarize the full plan before handing off to the first agent.
    - Follow all repository and path-specific instructions.
    - Use only built-in Node.js modules.
    - Run tests after every code change.
    ```

    > 💡 **Tip:** In Codespaces, files save automatically. If you are working locally, save with `Ctrl+S` / `Cmd+S`.

## ⌨️ Activity: Add a new feature using the full lifecycle

Use the Orchestrator to add **task categories** to the Task Manager.

1. In Copilot Chat, select the **orchestrator** agent and enter this prompt:

    ```
    Add a "category" feature to the Task Manager. Users should be able
    to assign a category (e.g., "work", "personal", "urgent") when
    creating a task and filter tasks by category. The category property
    is optional and defaults to "general".
    ```

1. After the Orchestrator summarizes the plan, click the handoff buttons in order:

    - **1. Plan the feature** - The Planner Agent updates `docs/project-plan.md`.
    - **2. Design the architecture** - The Architect Agent updates `docs/schema.md`.
    - **3. Implement the feature** - The Developer Agent implements the feature in `src/`.
    - **4. Test the feature** - The Tester Agent writes and runs tests in `tests/`.

    Each button pre-fills a prompt. Review it and press Enter to run it. You stay in control at every step.

1. **Verify the full suite:**

    Open the terminal in VS Code by pressing `` Ctrl+` `` (or `` Cmd+` `` on macOS), or go to **Terminal → New Terminal** in the menu bar. Then run:

    ```bash
    node --test tests/
    ```

## ⌨️ Activity: Try the category feature

Before committing, verify the feature works interactively. In the terminal (press `` Ctrl+` `` or `` Cmd+` `` if it is not already open), run the app:

```bash
node src/index.js
```

Then ask Copilot to help you test it manually. In Copilot Chat, enter:

```
Show me how to run the Task Manager and test the category feature
interactively. I want to:
- Create a task with category "work"
- Create a task without a category (should default to "general")
- List all tasks and confirm categories are shown
- Filter tasks by the "work" category
```

Copilot will provide the exact commands or code snippets based on your implementation.

## ⌨️ Activity: Commit and push your work

1. In the VS Code left sidebar, click the **Source Control** tab.

1. Hover over each changed file and click the **+** (Stage Changes) button, or click the **+** next to **Changes** to stage everything.

    <img width="300" alt="Screenshot: Stage changes icon in VS Code Source Control" src="https://raw.githubusercontent.com/skills/getting-started-with-github-copilot/main/.github/images/staging-changes-icon.png" />

1. In the **Message** text box, type:

    ```
    Add Orchestrator Agent with handoffs and deliver category feature end-to-end
    ```

1. Click **Commit**, then click **Sync Changes** to push to GitHub.

1. After you push, the workflow checks your work and posts the final review.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If an agent does not appear in the dropdown, reload the VS Code window (`Ctrl+Shift+P` or `Cmd+Shift+P` → **Developer: Reload Window**).
- If the handoff buttons do not appear, confirm the `handoffs:` block is inside the YAML front matter (between the `---` markers). Each entry needs `agent`, `label`, `prompt`, and `send`.
- Handoffs are supported in VS Code and GitHub Codespaces. If you are using a different environment, switch to the next agent manually.
- If tests fail after adding the category feature, let the tester agent fix both tests and source code.
- For a deeper walkthrough, see [exercises/07-agent-files/README.md](exercises/07-agent-files/README.md).

</details>
