## Step 5: Agent Orchestration &mdash; Build an Orchestrator Agent

_SDLC Phase: **Full Lifecycle**_

You now have four agents that each own one phase of the software development lifecycle: **Planner** (plan), **Architect** (design), **Developer** (implement), and **Tester** (test). In this final exercise you create an **Orchestrator Agent** that coordinates all four agents and then prove it works by delivering a new feature end-to-end.

### 📖 Theory: Bringing agents together

Each agent file you created teaches Copilot a specialized role. An orchestrator agent ties them together by defining the workflow sequence and telling the user which agent to invoke at each phase.

| Agent | SDLC Phase | Key Artifacts |
|-------|-----------|---------------|
| Planner | Planning | `docs/project-plan.md` |
| Architect | Design | `docs/schema.md` |
| Developer | Implementation | `src/**/*.js` |
| Tester | Testing | `tests/**/*.test.js` |
| **Orchestrator** | **Full lifecycle** | **Coordinates all of the above** |

Agent files also support advanced properties:

| Property | Purpose |
|----------|---------|
| `tools` | Restrict the agent to specific tools (e.g., `["read", "edit", "runInTerminal"]`) |
| Prompt references | Use `#file:` inside the agent body to attach other files as context |

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
    ---

    You are the orchestrator. When the user requests a new feature you
    guide them through the full software development lifecycle.

    ## Workflow

    1. **Plan** - Describe what the feature requires. Update
       `docs/project-plan.md` with a new section for the feature.
    2. **Design** - Update `docs/schema.md` with any new or changed
       data structures, validation rules, and file changes.
    3. **Develop** - Implement the feature in `src/` following the
       conventions in `.github/copilot-instructions.md` and the
       path-specific instructions in `.github/instructions/`.
    4. **Test** - Generate or update tests in `tests/` for the new
       code. Run all tests and fix any failures.
    5. **Document** - Add a brief summary of the change to
       `docs/changelog.md`. Create the file if it does not exist.

    ## Rules

    - Complete each phase before starting the next.
    - Show the user what you plan to do at each phase and wait for
      approval before proceeding.
    - Follow all repository and path-specific instructions.
    - Use only built-in Node.js modules.
    - Run tests after every code change.
    ```

1. Save the file.

## ⌨️ Activity: Add a new feature using the full lifecycle

Use your agents to add **task categories** to the Task Manager.

1. **Plan the feature.** In Copilot Chat, select the **planner** agent:

    ```
    Add a "category" feature to the Task Manager. Users should be able
    to assign a category (e.g., "work", "personal", "urgent") when
    creating a task and filter tasks by category. Update
    docs/project-plan.md with a new section for this feature.
    ```

1. **Design the change.** Switch to the **architect** agent:

    ```
    Read #file:docs/project-plan.md and update #file:docs/schema.md
    to include the new category property on the Task model. Define
    the allowed values, default value, and any new service functions
    needed.
    ```

1. **Implement.** Switch to the **developer** agent:

    ```
    Read #file:docs/schema.md and implement the category feature.
    Update the Task model, task service, validators, and the entry
    point. Run the app to verify it works.
    ```

1. **Test.** Switch to the **tester** agent:

    ```
    Read the updated source files in src/ and update the tests in
    tests/ to cover the category feature. Run all tests and fix
    any failures.
    ```

1. **Verify the full suite:**

    ```bash
    node --test tests/
    ```

## ⌨️ Activity: Commit and push your work

1. Commit and push:

    ```bash
    git add .github/agents/ docs/ src/ tests/
    git commit -m "Add Orchestrator Agent and deliver category feature end-to-end"
    git push
    ```

1. After you push, the workflow checks your work and posts the final review.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If an agent does not appear in the dropdown, reload the VS Code window (`Ctrl+Shift+P` or `Cmd+Shift+P` → **Developer: Reload Window**).
- The orchestrator coordinates the *workflow*. You still switch agents manually for each phase.
- If tests fail after adding the category feature, let the tester agent fix both tests and source code.
- For a deeper walkthrough, see [exercises/05-agent-files/README.md](exercises/05-agent-files/README.md).

</details>
