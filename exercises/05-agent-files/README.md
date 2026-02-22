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

Before building the Orchestrator, review two advanced features: the `tools` property and `#file:` references.

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
---

You are the Orchestrator. You coordinate the full software development
lifecycle by guiding the user through five phases in order.

## Workflow

Follow these phases in sequence for every feature request:

### Phase 1: Plan
- Analyze the feature request and break it into user stories.
- Update `docs/project-plan.md` with the new feature scope.
- Follow the planning conventions in #file:.github/agents/planner.agent.md.

### Phase 2: Design
- Update `docs/schema.md` with any new or modified data properties.
- Follow the design conventions in #file:.github/agents/architect.agent.md.
- Reference #file:.github/copilot-instructions.md for coding standards.

### Phase 3: Develop
- Implement the feature in `src/`.
- Follow the implementation patterns in #file:.github/agents/developer.agent.md.
- Use only built-in Node.js modules. Do not add external dependencies.

### Phase 4: Test
- Add or update tests in `tests/`.
- Follow the testing conventions in #file:.github/agents/tester.agent.md.
- Run tests after every code change:

```bash
node --test tests/
```

### Phase 5: Document
- Update `docs/project-plan.md` to mark the feature as complete.
- Summarize what changed in each file.

## Rules

- Complete each phase before starting the next one.
- Show the plan at the start of each phase so the user can review it.
- Follow all project instructions in #file:.github/copilot-instructions.md.
- Use only built-in Node.js modules (assert, crypto, fs, path, etc.).
- Run tests after every code change and fix failures before continuing.
```

### 2. Review the front matter

| Property | Value | Purpose |
|----------|-------|---------|
| `name` | `orchestrator` | Appears in the Copilot Chat dropdown |
| `description` | Coordinates the full SDLC workflow... | Tells users what the agent does |
| `tools` | `edit`, `search`, `runInTerminal`, `runTests` | Grants file editing, search, terminal, and test capabilities |

The Orchestrator needs more tools than most agents because it must edit files, search the codebase, run commands, and execute tests.

### 3. Review the `#file:` references

The prompt body references five files:

| Reference | Purpose |
|-----------|---------|
| `#file:.github/agents/planner.agent.md` | Planning conventions |
| `#file:.github/agents/architect.agent.md` | Design conventions |
| `#file:.github/agents/developer.agent.md` | Implementation patterns |
| `#file:.github/agents/tester.agent.md` | Testing conventions |
| `#file:.github/copilot-instructions.md` | Repository-wide coding standards |

These references ensure the Orchestrator follows the same conventions that each specialized agent uses. The user does not need to attach these files manually.

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

### 3. Follow the Orchestrator's phases

The Orchestrator works through each phase in order. At each phase, review the proposed changes before the agent continues.

**Phase 1: Plan**

The agent updates `docs/project-plan.md` with the new feature scope. Verify it adds user stories for the category feature.

**Phase 2: Design**

The agent updates `docs/schema.md` to include the `category` property. Verify the schema shows:

| Property | Type | Details |
|----------|------|---------|
| `category` | `string` | Optional, defaults to `"general"` |

**Phase 3: Develop**

The agent modifies files in `src/` to add the category property, filter function, and list function. Verify the code uses only built-in Node.js modules.

**Phase 4: Test**

The agent adds tests in `tests/` covering:

- Creating a task with a category
- Default category value
- Filtering tasks by category
- Listing unique categories

**Phase 5: Document**

The agent updates `docs/project-plan.md` to mark the feature as complete.

### 4. Run the tests

After the Orchestrator finishes, run the full test suite to confirm everything passes:

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

You have now seen three types of Copilot customization files. Each serves a different purpose.

| File type | Extension | Purpose | Activation |
|-----------|-----------|---------|------------|
| Custom instructions | `.instructions.md` | Define rules for how Copilot writes code | Automatic when matching files are open |
| Prompt files | `.prompt.md` | Save reusable multi-step prompts | Manual via `/` command in Chat |
| Agent files | `.agent.md` | Create specialized Copilot personalities | Manual via agent dropdown in Chat |

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

### Combining all three

The most effective setup uses all three together:

1. **Instructions** set the baseline rules for code style and conventions.
2. **Prompt files** encode common workflows that any developer can trigger.
3. **Agents** create specialized roles that each follow instructions and can invoke prompts.

The Orchestrator agent demonstrates this combination. It references instruction files via `#file:`, follows the conventions those instructions define, and coordinates multiple specialized agents.

---

## Verification Checklist

Before moving on, confirm each item:

- [ ] All five agent files exist in `.github/agents/`:
  - `planner.agent.md`
  - `architect.agent.md`
  - `developer.agent.md`
  - `tester.agent.md`
  - `orchestrator.agent.md`
- [ ] The `orchestrator.agent.md` file has valid YAML front matter with `name`, `description`, and `tools`
- [ ] The Orchestrator prompt references other agent files with `#file:` syntax
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
| Multi-phase workflow | Delivered a feature through Plan, Design, Develop, Test, Document |
| Agents vs instructions vs prompts | Chose the right customization file for each use case |

---

## Next Steps

Proceed to [Exercise 6: Org-Level Best Practices](../06-org-level-best-practices/README.md).
