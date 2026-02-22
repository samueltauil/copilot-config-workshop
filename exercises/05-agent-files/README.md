# Exercise 5: Agent Orchestration

**SDLC Phase: Full Lifecycle**

In this exercise you build an **Orchestrator Agent** that coordinates the four agents you created in Exercises 1 through 4. The Orchestrator drives features through the full software development lifecycle: **Plan, Design, Develop, Test, and Document**. You also learn advanced agent properties and deliver a new feature end to end.

## Workshop Roadmap

| Exercise | Copilot Concept | Agent | SDLC Phase |
|----------|----------------|-------|------------|
| 01 | Prompt engineering and interaction modes | Planner | Planning |
| 02 | Repository-wide custom instructions | Architect | Design |
| 03 | Path-specific instructions | Developer | Implementation |
| 04 | Prompt files | Tester | Testing |
| **05 (this one)** | Agent files and orchestration | Orchestrator | Full lifecycle |

Each exercise builds on the output of the previous one. The Planner Agent produces a project plan. The Architect Agent reads that plan and generates a schema. The Developer Agent reads the schema and writes code. The Tester Agent reads the code and writes tests. Now the Orchestrator coordinates all four in sequence.

## Learning Objectives

After completing this exercise you will be able to:

- Verify and review a multi-agent suite
- Use the `tools` property to restrict agent capabilities
- Use `#file:` references to attach context from other files
- Create an Orchestrator agent that coordinates multiple agents across SDLC phases
- Deliver a new feature by running every agent in sequence

## Prerequisites

- Exercises 01 through 04 complete
- All four agents exist in `.github/agents/`:
  - `planner.agent.md`
  - `architect.agent.md`
  - `developer.agent.md`
  - `tester.agent.md`
- The Task Manager CLI application runs and passes tests
- Node.js 20 or later

---

## Review Your Agent Suite

Before creating the Orchestrator, confirm that all four agents exist and are functional.

### 1. Check that every agent file exists

Run the following command from the repository root:

```bash
ls .github/agents/
```

You should see these four files:

- `planner.agent.md`
- `architect.agent.md`
- `developer.agent.md`
- `tester.agent.md`

### 2. Verify each agent has valid front matter

Open each file and confirm it contains a `---` delimited YAML front matter block with at least `name` and `description`. For example:

```markdown
---
name: planner
description: Generates structured project plans with user stories and acceptance criteria
tools: ["edit", "search"]
---
```

### 3. Confirm existing deliverables

Verify the artifacts from previous exercises:

```bash
ls docs/project-plan.md docs/schema.md
ls src/
ls tests/
```

Each directory should contain files generated during the earlier exercises. If anything is missing, return to the relevant exercise and complete it first.

---

## Advanced Agent Properties

Before building the Orchestrator, review three advanced features: the `tools` property, `#file:` references, and `handoffs`.

### The `tools` property

The `tools` array restricts which Copilot capabilities an agent can use. Omitting `tools` grants access to everything. Listing specific tools limits the agent to those capabilities only.

| Approach | Syntax | Effect |
|----------|--------|--------|
| Unrestricted | Omit `tools` entirely | Agent can use all available tools |
| Restricted | `tools: ["edit", "search"]` | Agent can only edit files and search |
| Read-only | `tools: ["search"]` | Agent can search but not modify files |

Restricting tools enforces boundaries. A planner should not run code. A tester should not modify source files. Use `tools` to match each agent's role.

### `#file:` references

Inside an agent's prompt body, you can reference other files with `#file:` syntax. This attaches the referenced file as context every time the agent runs.

```markdown
Follow the conventions in #file:.github/copilot-instructions.md when generating code.
```

This ensures the agent reads your repository instructions without the user needing to mention them in every prompt.

Common uses for `#file:` references:

- Attach `copilot-instructions.md` for coding conventions
- Attach `docs/project-plan.md` for project scope
- Attach `docs/schema.md` for data model context

### Handoffs

Handoffs chain agents together. When an agent finishes its work, it presents one or more buttons that launch the next agent in the workflow. The user clicks a button to continue, keeping full control of the pipeline.

Each handoff entry specifies:

| Field | Purpose |
|-------|---------|
| `agent` | The name of the next agent to invoke (matches the `name` field in the target agent's front matter) |
| `label` | The text shown on the button in Copilot Chat |
| `prompt` | The pre-filled message sent to the next agent |
| `send` | `true` to auto-submit the prompt, `false` to let the user review it first |

Example front matter with handoffs:

```yaml
---
name: planner
description: Generates structured project plans
handoffs:
  - agent: architect
    label: "Design the architecture"
    prompt: "Read #file:docs/project-plan.md and update docs/schema.md."
    send: false
---
```

Setting `send: false` keeps the user in the loop. They can edit the pre-filled prompt before it runs.

> **Note:** Handoffs are supported in VS Code and GitHub Codespaces. They are not supported when running agents on GitHub.com.

### Agent naming conventions

Follow these conventions when naming agents:

- Use lowercase with hyphens: `planner.agent.md`, not `Planner.agent.md`
- The filename (minus the `.agent.md` suffix) becomes the default display name
- Keep names short and descriptive: one to two words maximum
- Choose names that reflect the agent's SDLC role

---

## Step by Step: Create the Orchestrator Agent

### 1. Create the agent file

Create a new file at `.github/agents/orchestrator.agent.md` with the following content:

```markdown
---
name: orchestrator
description: Coordinates the full SDLC workflow by delegating to Planner, Architect, Developer, and Tester agents
tools: ["edit", "search", "runInTerminal", "runTests"]
handoffs:
  - agent: planner
    label: "1. Plan the feature"
    prompt: "Analyze the feature request above and update docs/project-plan.md with the new feature scope. Follow the planning conventions in #file:.github/agents/planner.agent.md."
    send: false
  - agent: architect
    label: "2. Design the architecture"
    prompt: "Read #file:docs/project-plan.md and update docs/schema.md to include any new or modified data properties. Reference #file:.github/copilot-instructions.md for coding standards."
    send: false
  - agent: developer
    label: "3. Implement the feature"
    prompt: "Read #file:docs/schema.md and implement the feature in src/. Use only built-in Node.js modules. Run the app after changes to verify there are no errors."
    send: false
  - agent: tester
    label: "4. Test the feature"
    prompt: "Read the updated source files in src/ and add or update tests in tests/. Run node --test tests/ and fix any failures before finishing."
    send: false
---

You are the Orchestrator. You coordinate the full software development
lifecycle by guiding the user through four phases in order.

When the user describes a feature, summarize the work to be done across
all four phases, then use the handoff buttons below to hand off to each
specialized agent.

## Phases

1. **Plan** - The Planner Agent updates `docs/project-plan.md`.
2. **Design** - The Architect Agent updates `docs/schema.md`.
3. **Develop** - The Developer Agent implements the feature in `src/`.
4. **Test** - The Tester Agent writes and runs tests in `tests/`.

## Rules

- Summarize the full plan before handing off to the first agent.
- Follow all project instructions in #file:.github/copilot-instructions.md.
- Use only built-in Node.js modules (assert, crypto, fs, path, etc.).
```

### 2. Review the front matter

| Property | Value | Purpose |
|----------|-------|---------|
| `name` | `orchestrator` | Appears in the Copilot Chat dropdown |
| `description` | Coordinates the full SDLC workflow... | Tells users what the agent does |
| `tools` | `edit`, `search`, `runInTerminal`, `runTests` | Grants file editing, search, terminal, and test capabilities |
| `handoffs` | List of four entries | Creates buttons that launch each specialized agent in sequence |

The `handoffs` list creates four buttons in Copilot Chat. Each button pre-fills a prompt and switches to the named agent. The user clicks each button in order to move the feature through the full lifecycle.

### 3. Review the handoffs

| Button label | Target agent | What it does |
|---|---|---|
| 1. Plan the feature | `planner` | Opens the Planner Agent with a prompt to update `docs/project-plan.md` |
| 2. Design the architecture | `architect` | Opens the Architect Agent with a prompt to update `docs/schema.md` |
| 3. Implement the feature | `developer` | Opens the Developer Agent with a prompt to implement the feature |
| 4. Test the feature | `tester` | Opens the Tester Agent with a prompt to write and run tests |

All handoffs use `send: false`, which means the pre-filled prompt appears in the chat input but does not run until the user presses Enter. This keeps the user in control at every step.

### 4. Verify the agent appears

1. Open Copilot Chat in VS Code.
2. Open the agent dropdown.
3. Confirm **orchestrator** appears in the list.

If it does not appear, reload the VS Code window: press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) and type **Reload Window**.

---

## Step by Step: Deliver a New Feature End to End

Use the Orchestrator to add a **task categories** feature to the Task Manager. This feature adds a `category` property to every task. Users can assign a category when creating a task and filter tasks by category.

### 1. Select the Orchestrator

In Copilot Chat, switch to **Agent** mode and select **orchestrator** from the agent dropdown.

### 2. Enter the feature request

Type the following prompt:

```text
Add a "category" feature to the Task Manager.

Requirements:
- Add a "category" property to the task model (string, optional, defaults to "general")
- Allow setting category when creating a task
- Add a function to filter tasks by category
- Add a function to list all unique categories
- Update the schema, source code, and tests
- Run all tests and confirm they pass
```

### 3. Use the handoff buttons

After the Orchestrator summarizes the plan, you see four buttons at the bottom of the response:

**1. Plan the feature** → **2. Design the architecture** → **3. Implement the feature** → **4. Test the feature**

Click each button in order. Each handoff pre-fills a prompt and switches to the named agent. Review the prompt and press Enter to run it.

**Phase 1: Plan (Planner Agent)**

The Planner Agent updates `docs/project-plan.md` with the new feature scope. Verify it adds user stories for the category feature.

**Phase 2: Design (Architect Agent)**

The Architect Agent updates `docs/schema.md` to include the `category` property. Verify the schema shows:

| Property | Type | Details |
|----------|------|---------|
| `category` | `string` | Optional, defaults to `"general"` |

**Phase 3: Develop (Developer Agent)**

The Developer Agent modifies files in `src/` to add the category property, filter function, and list function. Verify the code uses only built-in Node.js modules.

**Phase 4: Test (Tester Agent)**

The Tester Agent adds tests in `tests/` covering:

- Creating a task with a category
- Default category value
- Filtering tasks by category
- Listing unique categories

### 4. Run the tests

After the final handoff finishes, run the full test suite to confirm everything passes:

```bash
node --test tests/
```

All tests should pass, including the new category tests.

### 5. Review the changes

Check that these files were created or updated:

```bash
git diff --name-only
```

You should see changes in:

- `docs/project-plan.md`
- `docs/schema.md`
- Files in `src/`
- Files in `tests/`

---

## When to Use What

You have now seen four types of Copilot customization files. Each serves a different purpose.

| File type | Extension | Purpose | Activation |
|-----------|-----------|---------|------------|
| Custom instructions | `.instructions.md` | Define rules for how Copilot writes code | Automatic when matching files are open |
| Prompt files | `.prompt.md` | Save reusable multi-step prompts | Manual via `/` command in Chat |
| Agent files | `.agent.md` | Create specialized Copilot personalities | Manual via agent dropdown in Chat |
| Agent handoffs | `handoffs:` in front matter | Chain agents in sequence with one-click buttons | Triggered by the previous agent's handoff button |

### Choose instructions when...

- You want rules applied automatically without user action
- The rules apply to a specific file type or directory
- Examples: coding standards, naming conventions, framework patterns

### Choose prompt files when...

- You want a repeatable workflow the user triggers on demand
- The prompt is long or complex and should not be retyped each time
- Examples: "generate tests", "create a migration", "review for security"

### Choose agents when...

- You want a fundamentally different Copilot personality
- The task requires specific tool restrictions
- Multiple people on your team should use the same specialized behavior
- Examples: planner, architect, developer, tester, orchestrator

### Combining all four

The most effective setup uses all four together:

1. **Instructions** set the baseline rules for code style and conventions.
2. **Prompt files** encode common workflows that any developer can trigger.
3. **Agents** create specialized roles that each follow instructions and can invoke prompts.
4. **Handoffs** chain agents in a guided pipeline, so the user clicks through each phase instead of switching agents manually.

The Orchestrator agent demonstrates this combination. It uses `handoffs:` to present a one-click pipeline, references instruction files via `#file:`, and coordinates multiple specialized agents.

---

## Verification Checklist

Before moving on, confirm each item:

- [ ] All five agent files exist in `.github/agents/`:
  - `planner.agent.md`
  - `architect.agent.md`
  - `developer.agent.md`
  - `tester.agent.md`
  - `orchestrator.agent.md`
- [ ] The `orchestrator.agent.md` file has valid YAML front matter with `name`, `description`, `tools`, and `handoffs`
- [ ] The `handoffs` list contains four entries targeting `planner`, `architect`, `developer`, and `tester`
- [ ] The four handoff buttons appear in Copilot Chat after running the Orchestrator
- [ ] The category feature is implemented in `src/`
- [ ] Tests for the category feature exist in `tests/`
- [ ] All tests pass when you run `node --test tests/`
- [ ] `docs/project-plan.md` and `docs/schema.md` reflect the new feature

## Commit and Push

```bash
git add .github/agents/ docs/ src/ tests/
git commit -m "Add Orchestrator Agent and deliver category feature"
git push
```

After you push, the workflow checks your work and posts the next step as an issue comment.

---

## Troubleshooting

**Handoff buttons do not appear**

Confirm the `handoffs:` block is inside the YAML front matter (between the `---` markers, not in the Markdown body). Each entry must have `agent`, `label`, `prompt`, and `send`. Reload the VS Code window after saving the file.

**Orchestrator agent does not appear in the dropdown**

Reload the VS Code window: press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) and type **Reload Window**. Confirm the file is at `.github/agents/orchestrator.agent.md` with the `.agent.md` extension.

**YAML front matter errors**

The `---` markers must start on the very first line with no blank lines above them. Check for correct indentation and no missing colons. The `description` property is required.

**`#file:` references not loading**

Confirm the referenced files exist at the paths specified. Relative paths in `#file:` start from the repository root. For example, `#file:.github/copilot-instructions.md` expects a file at `.github/copilot-instructions.md`.

**Agent skips phases or produces incomplete output**

Follow up in the same conversation with a specific request:

```text
You skipped the Test phase. Add tests for the category feature
in tests/ and run them.
```

Breaking the work into smaller prompts often helps.

**Tests fail after the Orchestrator finishes**

Run the failing tests individually to see detailed output:

```bash
node --test tests/
```

Copy the failure output into Copilot Chat and ask the Orchestrator to fix the issue. The agent's rules require it to run tests and fix failures before continuing.

**External dependencies added by mistake**

Check `package.json` for unexpected dependencies. This workshop uses only built-in Node.js modules. If the agent added an external package, ask it to rewrite the code using only built-in modules.

---

## Workshop Complete

You have now built all five SDLC agents:

| Agent | SDLC Phase | Copilot Concept |
|-------|------------|----------------|
| Planner | Planning | Prompt engineering |
| Architect | Design | Custom instructions |
| Developer | Implementation | Path-specific instructions |
| Tester | Testing | Prompt files |
| Orchestrator | Full lifecycle | Agent files and orchestration |

Together these agents form a complete workflow. The Orchestrator coordinates the others to deliver features from plan through tested implementation.

## Key Takeaways

| Concept | What you practiced |
|---------|--------------------|
| Agent suite review | Verified all four agents exist and have valid front matter |
| `tools` property | Restricted the Orchestrator to edit, search, terminal, and test tools |
| `#file:` references | Attached agent files and instructions as persistent context |
| `handoffs` property | Created one-click buttons that chain agents across the SDLC |
| Multi-phase workflow | Delivered a feature through Plan, Design, Develop, Test |
| Agents vs instructions vs prompts | Chose the right customization file for each use case |

---
