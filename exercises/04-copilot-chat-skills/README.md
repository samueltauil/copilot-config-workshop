# Exercise 4: Copilot Chat Participants, Commands, and Variables

**Learning objectives:**
- Use chat participants (`@`) to scope questions to a specific domain
- Use slash commands (`/`) to trigger common actions efficiently
- Use chat variables (`#`) to add specific context to your prompts
- Use the `@github` participant to access GitHub-specific skills

**Duration:** ~30 minutes

**Prerequisites:** Visual Studio Code with the GitHub Copilot extension installed and authenticated.

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

1. Open this repository in VS Code.
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

## Summary

You used the three types of Copilot Chat special keywords:

| Keyword | Example | What it does |
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

---

## Next Steps

Proceed to [Exercise 5: Agent Instruction Files](../05-agent-files/README.md).
