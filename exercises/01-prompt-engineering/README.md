# Exercise 1: Prompt Engineering

**SDLC Phase: Planning & Requirements**

In this exercise you learn how to communicate with GitHub Copilot and build a **Planner Agent** that generates structured project plans. The Planner Agent is the first of five agents you create across this workshop. Together these agents cover the full software development lifecycle: **plan, design, implement, test, and orchestrate**.

## Workshop Roadmap

| Exercise | Copilot Concept | Agent | SDLC Phase |
|----------|----------------|-------|------------|
| **01 (this one)** | Prompt engineering and interaction modes | Planner | Planning |
| 02 | Repository-wide custom instructions | Architect | Design |
| 03 | Path-specific instructions | Developer | Implementation |
| 04 | Prompt files | Tester | Testing |
| 05 | Agent files and orchestration | Orchestrator | Full lifecycle |

Each exercise builds on the output of the previous one. The Planner Agent produces a project plan. The Architect Agent reads that plan and generates a schema. The Developer Agent reads the schema and writes code. This chain continues through all five exercises.

## Learning Objectives

After completing this exercise you will be able to:

- Identify the five Copilot interaction modes and choose the right one for a task
- Apply six prompt engineering strategies to get better results from Copilot
- Create a custom agent file (`.agent.md`) with YAML front matter
- Use an agent to generate structured Markdown output

## Prerequisites

- A GitHub account with Copilot access
- **GitHub Codespaces** (recommended, no local setup required) or VS Code with the GitHub Copilot extension and Node.js 20+

> **Using Codespaces?** Click **Code > Codespaces > Create codespace on main** in your repository. Node.js 20, the Copilot extension, and Copilot Chat are pre-installed. No local configuration is needed.

## The Application: Task Manager CLI

All five exercises build toward the same application. Here is the scope:

- **Runtime:** Node.js, no external dependencies, built-in modules only
- **Storage:** In-memory (no database)
- **Operations:** Create, read, update, and delete tasks; filter by status or priority; sort by date or priority
- **Task model:**

| Property | Type | Details |
|----------|------|---------|
| `id` | `string` | Generated with `crypto.randomUUID()` |
| `title` | `string` | Required |
| `description` | `string` | Optional, defaults to empty string |
| `status` | `string` | One of `todo`, `in-progress`, `done` |
| `priority` | `string` | One of `low`, `medium`, `high` |
| `createdAt` | `string` | ISO 8601 timestamp |
| `updatedAt` | `string` | ISO 8601 timestamp |

---

## Copilot Interaction Modes

Copilot offers five ways to interact. Each mode fits different tasks.

### Inline Suggestions

Start typing in the editor and Copilot shows grey ghost text. Press `Tab` to accept or `Esc` to dismiss.

**Best for:** Completing lines, finishing functions, writing repetitive code.

**Try it:** Open `exercises/01-prompt-engineering/starter.js` and type the following on a new line:

```javascript
function greet(name) {
```

Pause and watch for the suggestion. Press `Tab` to accept it.

### Ask Mode

Open Copilot Chat (click the chat icon in the sidebar). The default mode is Ask. Type a question and Copilot answers without changing your files.

**Best for:** Asking questions, understanding code, brainstorming ideas.

**Try it:**

```text
What features would a Task Manager CLI application need?
```

### Edit Mode

Switch the mode selector in Copilot Chat to **Edit**. Copilot makes targeted changes to files you specify.

**Best for:** Changing specific files, refactoring code, updating documentation.

### Agent Mode

Switch the mode selector to **Agent**. Copilot performs multi-step tasks: creating files, editing code, and running commands autonomously.

**Best for:** Complex tasks that span multiple files or require running commands.

### Inline Chat

Press `Ctrl+I` (Windows/Linux) or `Cmd+I` (macOS) to open a small chat input at the cursor position.

**Best for:** Quick edits at a specific location without leaving the editor.

---

## Prompt Engineering Strategies

The quality of Copilot's response depends on how you write your prompt. The [GitHub prompt engineering guide](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat) identifies six strategies.

### Strategy 1: Start General, Then Get Specific

State the broad goal first. Then add constraints, types, and requirements.

**Vague prompt (produces unpredictable results):**

```text
Write a function to validate input
```

**Specific prompt (produces focused results):**

```text
Write a JavaScript function called `validateEmail` that accepts
a single string argument and returns `true` if the string matches
a standard email format (user@domain.com), `false` otherwise.
Do not use external libraries.
```

The specific prompt names the language, function name, argument type, return type, and constraints.

### Strategy 2: Give Examples

Show expected inputs and outputs. Examples remove ambiguity faster than descriptions.

```text
Write a JavaScript function that formats a phone number.

Examples:
- Input: "5551234567"    -> Output: "(555) 123-4567"
- Input: "15551234567"   -> Output: "(555) 123-4567"
- Input: "555-123-4567"  -> Output: "(555) 123-4567"
```

### Strategy 3: Break Tasks into Steps

Do not ask Copilot to build an entire feature in one prompt. Break the work into small, focused requests.

Instead of this:

```text
Build a complete CSV parser with validation and error handling
```

Do this:

1. Ask for a function that splits a CSV line into an array.
2. Ask for a function that validates each field.
3. Ask for a function that combines both into a pipeline.

Each prompt produces a small, testable piece.

### Strategy 4: Avoid Ambiguity

Do not use pronouns like "it", "this", or "that" without context. Name the function, file, or concept explicitly.

**Ambiguous:**

```text
What does this do?
```

**Explicit:**

```text
Explain what the processCSV function in starter.js does, step by step.
```

### Strategy 5: Indicate Relevant Code

Use `#file` in Copilot Chat to attach a specific file as context.

```text
#file:starter.js Add JSDoc comments to all functions in this file.
```

You can also select code in the editor and use `#selection` to reference it:

```text
#selection Explain this function and suggest improvements.
```

### Strategy 6: Experiment and Iterate

If the first response is not right, follow up in the same conversation. You do not need to start over.

```text
Write a function to sort tasks
```

Then refine:

```text
Update the function to sort by priority (high first), then by
creation date (newest first) for tasks with the same priority.
```

Continue the conversation until the output matches your needs.

---

## Step by Step: Create the Planner Agent

Agent files live in `.github/agents/` and use the `.agent.md` extension. Each file has a YAML front matter block followed by a Markdown prompt body.

### 1. Create the agents directory

```bash
mkdir -p .github/agents
```

### 2. Create the agent file

Create a new file at `.github/agents/planner.agent.md` with the following content:

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

### 3. Understand the YAML front matter

The front matter block between `---` markers configures the agent:

| Property | Required | Purpose |
|----------|----------|---------|
| `name` | Yes | Display name in the Copilot Chat dropdown |
| `description` | Yes | Tells Copilot (and users) what the agent does |
| `tools` | No | Grants the agent access to specific Copilot tools |

### 4. Understand the prompt body

The Markdown below the front matter is the agent's system prompt. It tells Copilot:

- **Role:** "You are a software project planner."
- **Output format:** The five sections the plan must contain.
- **Constraints:** Node.js only, no external dependencies.

Writing a clear system prompt applies the same strategies you learned above: be specific, provide structure, and set constraints.

---

## Step by Step: Generate a Project Plan

### 1. Switch to Agent mode

In Copilot Chat, open the mode selector and choose **Agent**. Then select **planner** from the agent dropdown. If the planner does not appear, reload the window (`Ctrl+Shift+P` then type **Reload Window**).

### 2. Enter the prompt

Type the following prompt. Notice how it applies "start general, then get specific" and "give examples":

```text
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

### 3. Review and iterate

Read the generated plan. If something is missing, follow up in the same conversation. For example:

```text
Add a section on error handling conventions and input validation rules.
```

This demonstrates the "experiment and iterate" strategy.

### 4. Verify the output

Confirm that the file `docs/project-plan.md` exists and contains a structured project plan with these sections:

- Project overview
- User stories with acceptance criteria
- Data model
- File structure
- Implementation phases

---

## Verification Checklist

Before moving on, confirm each item:

- [ ] `.github/agents/planner.agent.md` exists
- [ ] The agent file has valid YAML front matter with `name` and `description`
- [ ] `docs/project-plan.md` exists
- [ ] The project plan covers the Task Manager CLI scope
- [ ] The plan references Node.js with no external dependencies

## Commit and Push

```bash
git add docs/ .github/agents/
git commit -m "Add Planner Agent and generate project plan"
git push
```

After you push, the workflow checks your work and posts the next step as an issue comment.

---

## Troubleshooting

**Copilot icon missing from the status bar**

Install the GitHub Copilot extension from the VS Code marketplace. Sign in to GitHub when prompted.

**Planner agent does not appear in the dropdown**

Reload the VS Code window: press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) and type **Reload Window**. Confirm the file is at `.github/agents/planner.agent.md` with the `.agent.md` extension.

**YAML front matter errors**

The `---` markers must start on the very first line with no blank lines above them. The `description` property is required.

**Agent does not create the docs directory**

Create it manually and re-run the prompt:

```bash
mkdir -p docs
```

**Agent produces incomplete output**

Follow up in the same conversation with a specific request for the missing section. Breaking the task into smaller prompts often helps.

---

## Key Takeaways

| Strategy | What you practiced |
|----------|--------------------|
| Start general, then get specific | Wrote a detailed prompt for the Planner Agent |
| Give examples | Specified task properties and expected behaviors |
| Break tasks into steps | Separated agent creation from plan generation |
| Avoid ambiguity | Named files and formats explicitly |
| Indicate relevant code | Used `#file` references in prompts |
| Experiment and iterate | Refined the plan in a follow-up message |

---
