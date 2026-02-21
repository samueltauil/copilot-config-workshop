# Exercise 4: Copilot Chat Participants, Commands, and Variables

**Learning objectives:**
- Use chat participants (`@`) to scope questions to a specific domain
- Use slash commands (`/`) to trigger common actions efficiently
- Use chat variables (`#`) to add specific context to your prompts
- Use the `@github` participant to access GitHub-specific skills
- Create reusable prompt files (`.prompt.md`) for repeatable workflows
- Create custom agent modes (`.agent.md`) with specialized behavior

**Duration:** ~40 minutes

**Prerequisites:** GitHub Codespaces or Visual Studio Code with the GitHub Copilot extension installed.

---

## Background

Copilot Chat supports three types of special keywords that make prompts more precise and efficient:

| Keyword | Name | Purpose |
|---------|------|---------|
| `@` | Chat participant | Scopes the prompt to a domain expert |
| `/` | Slash command | Triggers a specific action |
| `#` | Chat variable | Attaches specific context to the prompt |

These keywords reduce the amount of context you need to explain in natural language and give Copilot a clearer, more structured input. See [Asking GitHub Copilot questions in your IDE](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) and the [GitHub Copilot Chat cheat sheet](https://docs.github.com/en/copilot/using-github-copilot/github-copilot-chat-cheat-sheet) for a full reference.

---

## Setup

1. Open this repository in a Codespace or in VS Code locally.
2. Open the starter file:
   ```
   exercises/04-copilot-chat-skills/starter.py
   ```
3. Open Copilot Chat by clicking the chat icon in the VS Code sidebar.

---

## Part 1: Chat Participants (`@`)

Chat participants are like domain experts you can invoke. Each participant has specialized knowledge about a particular area.

### Available participants in VS Code

Type `@` in the Copilot Chat prompt box to see the list of available participants. Common ones include:

- `@workspace` - Has knowledge of all files in your current VS Code workspace
- `@github` - Has access to GitHub-specific features and web search

### Step 1.1: Use `@workspace` to ask about your project

1. In Copilot Chat, type:
   ```
   @workspace What files are in this repository and what is the purpose of each one?
   ```
2. Press `Enter`.
3. Copilot will scan your workspace and provide a summary based on the actual files in your repository.

**Validation:** The response should reference real file paths from this repository (such as `exercises/`, `slides/`, `.github/`).

### Step 1.2: Use `@workspace` to ask about specific functionality

1. Type:
   ```
   @workspace Where are the custom instruction files in this repository?
   ```
2. Copilot should identify `.github/copilot-instructions.md` and `.github/instructions/`.

### Step 1.3: Use `@github` to access GitHub skills

The `@github` participant provides skills that go beyond your local workspace. It can search the web, reference GitHub documentation, and query repository information on GitHub.com.

1. Type:
   ```
   @github What are the supported file types for path-specific Copilot instructions?
   ```
2. Copilot will use a skill (such as web search or documentation retrieval) to answer.

3. Ask Copilot to list its available skills:
   ```
   @github What skills are available?
   ```

**Note:** The `@github` participant is available when you are signed in to GitHub in VS Code. The specific skills available may vary based on your subscription level.

---

## Part 2: Slash Commands (`/`)

Slash commands are shortcuts for common actions. They eliminate the need to write complex prompts for standard tasks.

### Step 2.1: Use `/explain` to understand code

1. Open `exercises/04-copilot-chat-skills/starter.py` in the editor.
2. Select the entire content of the file (press `Ctrl+A` on Windows/Linux, `Cmd+A` on macOS).
3. In Copilot Chat, type:
   ```
   /explain
   ```
4. Press `Enter`. Copilot will explain the selected code in detail.

**Validation:** The explanation should reference the actual content of `starter.py`.

### Step 2.2: Use `/fix` to correct a bug

1. In `starter.py`, introduce an intentional bug. For example, change the line:
   ```python
   return result
   ```
   to:
   ```python
   return reslt
   ```
2. Select the line with the bug.
3. In Copilot Chat, type:
   ```
   /fix
   ```
4. Copilot should identify the `NameError` and suggest the fix.
5. Undo the change after you have seen the result (`Ctrl+Z` / `Cmd+Z`).

### Step 2.3: Use `/tests` to generate unit tests

1. Open `starter.py` and select all the code.
2. In Copilot Chat, type:
   ```
   /tests
   ```
3. Copilot will generate unit tests for the functions in the file.

**Validation:** The generated tests should import the functions from `starter.py` and include at least one test per function.

### Step 2.4: Use `/doc` to add documentation

1. Select all the code in `starter.py`.
2. Type:
   ```
   /doc
   ```
3. Copilot will generate docstrings for each function.

### Step 2.5: Use `/new` to scaffold a new file

The `/new` command creates a new file based on your description.

1. In Copilot Chat, type:
   ```
   /new Create a Python script that defines a class called `DataProcessor` with methods `load`, `transform`, and `save`. Include docstrings for each method.
   ```
2. Copilot will generate the file content and offer to create it in your workspace.

---

## Part 3: Chat Variables (`#`)

Chat variables attach specific context to your prompt. Instead of describing a file or symbol in natural language, you reference it directly.

### Step 3.1: Use `#file` to reference a specific file

1. In Copilot Chat, type `#` to see available variables.
2. Select `#file` and choose `exercises/04-copilot-chat-skills/starter.py` from the picker.
3. Complete the prompt:
   ```
   #file:starter.py What functions are defined in this file and what do they return?
   ```
4. Press `Enter`.

**Validation:** The response should accurately describe the functions in `starter.py`, even if you currently have a different file open in the editor.

### Step 3.2: Use `#selection` to reference selected code

1. In the editor, open `starter.py` and select one of the functions.
2. In Copilot Chat, type:
   ```
   #selection Rewrite this function to handle an empty input by returning an empty list instead of raising an exception.
   ```
3. Press `Enter`. Copilot will apply your instruction to the selected code only.

### Step 3.3: Use `#codebase` to search across all files

The `#codebase` variable tells Copilot to search the entire workspace for relevant context.

1. In Copilot Chat, type:
   ```
   #codebase Where are custom instruction examples stored in this project?
   ```
2. Copilot will search across all files in the workspace and provide a precise answer.

---

## Part 4: Inline Chat

You can access Copilot Chat directly in the editor without switching to the sidebar.

### Step 4.1: Open inline chat

1. Open `starter.py` in the editor.
2. Click on a line where you want to add or modify code.
3. Press `Ctrl+I` on Windows/Linux, or `Cmd+I` on macOS.
4. A small input box appears in the editor at the current cursor position.

### Step 4.2: Use inline chat to modify code in place

1. Select one of the functions in `starter.py`.
2. Press `Ctrl+I` / `Cmd+I`.
3. Type:
   ```
   Add input validation at the start of this function. Raise a ValueError with a descriptive message if the input is None or an empty list.
   ```
4. Press `Enter`. Copilot will modify the selected code inline.
5. Use the **Accept** button to keep the change, or **Discard** to reject it.

   > **Screenshot reference:** After pressing `Ctrl+I`, a small chat box appears directly in the editor. After Copilot responds, the edited code is shown with a green highlight for added lines and a red highlight for removed lines. The **Accept** and **Discard** buttons appear above the modified block.

---

## Part 5: Smart Actions (Context Menu)

Copilot provides quick actions through the right-click context menu in VS Code.

### Step 5.1: Access smart actions

1. Select some code in `starter.py`.
2. Right-click the selected code.
3. Hover over **Copilot** in the context menu.
4. You will see options such as:
   - **Explain** - Same as `/explain`
   - **Fix** - Same as `/fix`
   - **Generate Docs** - Same as `/doc`
   - **Generate Tests** - Same as `/tests`

5. Select **Explain** and read the inline response.

---

## Part 6: Reusable Prompt Files (`.prompt.md`)

Prompt files let you save prompts as reusable files in your repository. You invoke them with the `/` command in Copilot Chat, turning complex multi-step prompts into one-click actions. See [Using prompt files](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#creating-prompt-files) for the full reference.

### How prompt files work

- Prompt files use the `.prompt.md` suffix and live in `.github/prompts/` by default.
- Each file contains a YAML front matter block followed by Markdown content.
- You select them via the `/` command in Copilot Chat.
- Prompt files can reference workspace files using Markdown links to provide additional context.

### Key front matter fields

| Field | Description |
|-------|-------------|
| `description` | Short text shown in the prompt picker |
| `agent` | The agent to use (e.g., `agent` for Agent Mode) |
| `argument-hint` | Hint text shown to the user when selecting the prompt |

### Step 6.1: Create a prompt file

1. Create the prompts directory:

   ```bash
   mkdir .github/prompts
   ```

2. Create a new file at `.github/prompts/add-tests.prompt.md`:

   ```markdown
   ---
   description: Generate unit tests for a module
   agent: agent
   argument-hint: Provide the file path to test
   ---

   # Generate Unit Tests

   Your goal is to generate comprehensive unit tests for the specified module.

   ## Steps

   1. Read the target file provided by the user.
   2. Identify all exported functions and classes.
   3. Generate unit tests that cover:
      - Normal inputs
      - Edge cases (empty input, null values)
      - Error conditions
   4. Use the project's test runner and conventions from the repository instructions.
   5. Save the test file alongside the source with a `.test` suffix.
   ```

3. Save the file.

### Step 6.2: Create a second prompt file

Create `.github/prompts/explain-architecture.prompt.md`:

```markdown
---
description: Explain the architecture of the current project
agent: agent
---

# Explain Project Architecture

Analyze the repository and provide a summary of:

1. The overall project structure and purpose.
2. Key directories and their roles.
3. How the main components interact.
4. Any configuration or instruction files that shape developer workflow.

Reference the [repository instructions](../../.github/copilot-instructions.md) for project context.
```

### Step 6.3: Test your prompt file

1. Open Copilot Chat.
2. Type `/` in the prompt box.
3. You should see your prompt files listed (e.g., `add-tests`, `explain-architecture`).
4. Select `explain-architecture` and press `Enter`.
5. Copilot executes the prompt and provides a structured response.

**Validation:** The response should reference actual files and directories in the repository.

### Prompt files vs. instructions files

| Aspect | Instruction files (`.instructions.md`) | Prompt files (`.prompt.md`) |
|--------|---------------------------------------|----------------------------|
| Focus | **How** tasks should be done (conventions, rules) | **What** task to perform (reusable workflows) |
| Activation | Automatic when a matching file is open | Manual via `/` command |
| Location | `.github/instructions/` | `.github/prompts/` |
| Use case | Coding standards and style rules | Repeatable multi-step tasks |

### Step 6.4: Commit your work

```bash
git add .github/prompts/
git commit -m "Add reusable prompt files for Copilot Chat"
git push
```

---

## Part 7: Custom Agent Modes (`.agent.md`)

Custom agent modes change how Copilot Chat behaves entirely. Instead of using the default Copilot personality, you create a specialized agent with specific tools, response styles, and even domain expertise. See [Creating custom agents](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#creating-custom-agents) for the full reference.

### How custom agents work

- Agent files use the `.agent.md` suffix and live in `.github/agents/` by default.
- Each file defines a specialized persona with a name, description, available tools, and behavior rules.
- You select them from the agent dropdown in Copilot Chat (instead of the default Copilot).

### Key front matter fields

| Field | Description |
|-------|-------------|
| `name` | Display name in the agent picker |
| `description` | Short description of what the agent does |
| `tools` | Array of tools the agent can use (e.g., `["search", "web"]`) |

### Step 7.1: Create a custom agent

1. Create the agents directory:

   ```bash
   mkdir .github/agents
   ```

2. Create a new file at `.github/agents/code-reviewer.agent.md`:

   ```markdown
   ---
   name: code-reviewer
   description: Reviews code for quality, security, and best practices
   tools: ["search"]
   ---

   # Code Review Agent

   You are a code review assistant. Follow this response format for every review:

   ## Response Format

   Every response follows this structure:

   **SUMMARY:** One-sentence overview of the code.
   **ISSUES:** Numbered list of problems found (severity: high/medium/low).
   **SUGGESTIONS:** Specific improvements with code examples.
   **VERDICT:** APPROVE, REQUEST CHANGES, or NEEDS DISCUSSION.

   ## Review Rules

   - Check for security vulnerabilities (injection, hardcoded secrets, missing validation).
   - Verify error handling covers all failure paths.
   - Flag any code that does not follow the project conventions.
   - Keep feedback constructive and specific.
   - Always suggest a fix, not only identify the problem.
   ```

3. Save the file.

### Step 7.2: Test your custom agent

1. Open Copilot Chat.
2. Look at the agent/mode dropdown at the top of the Chat panel (it may show "Copilot" or "Agent" by default).
3. Select your `code-reviewer` agent from the list.
4. Open `exercises/04-copilot-chat-skills/starter.py` and select all the code.
5. Ask:

   ```
   Review this code
   ```

6. The response should follow the structured format you defined (SUMMARY, ISSUES, SUGGESTIONS, VERDICT).

**Validation:** The agent should use the exact response format defined in the agent file, not a generic Copilot response.

### Step 7.3: Commit your work

```bash
git add .github/agents/
git commit -m "Add custom agent mode for code review"
git push
```

---

## Summary

You used the three types of Copilot Chat special keywords and two types of custom files:

| Feature | Example | What it does |
|---------|---------|-------------|
| `@workspace` | `@workspace Where is X?` | Searches all workspace files |
| `@github` | `@github What skills are available?` | Accesses GitHub-specific skills |
| `/explain` | `/explain` | Explains selected code |
| `/fix` | `/fix` | Suggests a fix for selected code |
| `/tests` | `/tests` | Generates unit tests |
| `/doc` | `/doc` | Adds documentation to selected code |
| `#file` | `#file:app.py ...` | Attaches a specific file as context |
| `#selection` | `#selection ...` | Attaches selected code as context |
| `#codebase` | `#codebase ...` | Searches the full workspace |
| Prompt files | `.github/prompts/add-tests.prompt.md` | Reusable multi-step prompts via `/` |
| Custom agents | `.github/agents/code-reviewer.agent.md` | Specialized Copilot personalities |

---

## Next Steps

Proceed to [Exercise 5: Agent Instruction Files](../05-agent-files/README.md).
