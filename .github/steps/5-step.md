## Step 5: Agent Orchestration &mdash; Build an Orchestrator Agent

_SDLC Phase: **Full Lifecycle**_

You now have four agents that each own one phase of the software development lifecycle: **Planner** (plan), **Architect** (design), **Developer** (implement), and **Tester** (test). In this final exercise you create an **Orchestrator Agent** that uses **handoffs** to chain all four agents into a guided pipeline, and then prove it works by delivering a new feature end-to-end.

### 📖 Theory: Bringing agents together

Each agent file you created teaches Copilot a specialized role. An orchestrator agent ties them together using the `handoffs:` front matter property. Handoffs create one-click buttons in Copilot Chat. Each button pre-fills a prompt and switches to the named agent. The user clicks each button in order to move the feature through the full lifecycle.

| Agent | SDLC Phase | Key Artifacts |
|-------|-----------|---------------|
| Planner | Planning | `docs/project-plan.md` |
| Architect | Design | `docs/schema.md` |
| Developer | Implementation | `src/**/*.js` |
| Tester | Testing | `tests/**/*.test.js` |
| **Orchestrator** | **Full lifecycle** | **Coordinates all of the above** |

Agent files support these advanced properties:

| Property | Purpose |
|----------|---------|
| `tools` | Restrict the agent to specific tools (e.g., `["read", "edit", "runInTerminal"]`) |
| `#file:` references | Attach other files as context inside the agent prompt body |
| `handoffs` | Define buttons that chain to the next agent with a pre-filled prompt |

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
    tools: ["edit", "search", "runInTerminal", "runTests"]
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
    handoff buttons below to guide the user through each phase.

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

1. Save the file.

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

    - **1. Plan the feature** — The Planner Agent updates `docs/project-plan.md`.
    - **2. Design the architecture** — The Architect Agent updates `docs/schema.md`.
    - **3. Implement the feature** — The Developer Agent implements the feature in `src/`.
    - **4. Test the feature** — The Tester Agent writes and runs tests in `tests/`.

    Each button pre-fills a prompt. Review it and press Enter to run it.

1. **Verify the full suite:**

    ```bash
    node --test tests/
    ```

## ⌨️ Activity: Commit and push your work

1. Commit and push:

    ```bash
    git add .github/agents/ docs/ src/ tests/
    git commit -m "Add Orchestrator Agent with handoffs and deliver category feature end-to-end"
    git push
    ```

1. After you push, the workflow checks your work and posts the final review.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If an agent does not appear in the dropdown, reload the VS Code window (`Ctrl+Shift+P` or `Cmd+Shift+P` → **Developer: Reload Window**).
- If the handoff buttons do not appear, confirm the `handoffs:` block is inside the YAML front matter (between the `---` markers). Each entry needs `agent`, `label`, `prompt`, and `send`.
- Handoffs are supported in VS Code and GitHub Codespaces. If you are using a different environment, switch to the next agent manually.
- If tests fail after adding the category feature, let the tester agent fix both tests and source code.
- For a deeper walkthrough, see [exercises/05-agent-files/README.md](exercises/05-agent-files/README.md).

</details>
