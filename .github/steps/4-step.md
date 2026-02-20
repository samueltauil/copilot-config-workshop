## Step 4: Copilot Chat Participants, Commands, and Variables

You are spending too much time writing long prompts to explain what file you mean, what code you want explained, or what tests you need. Copilot Chat provides three types of special keywords, called [participants, commands, and variables](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide), that let you express that context quickly and precisely.

### 📖 Theory: Chat participants, slash commands, and chat variables

| Keyword | Name | Purpose |
|---------|------|---------|
| `@` | Chat participant | Scopes the prompt to a domain expert |
| `/` | Slash command | Triggers a specific action |
| `#` | Chat variable | Attaches specific context to the prompt |

These keywords reduce the amount of context you need to explain in natural language and give Copilot a clearer, more structured input.

**Common participants:**

- `@workspace` - Has knowledge of all files in your current VS Code workspace
- `@github` - Has access to GitHub-specific features and web search

**Common slash commands:**

- `/explain` - Explains selected code
- `/fix` - Suggests a fix for selected code or error
- `/tests` - Generates unit tests for selected code
- `/doc` - Adds documentation comments to selected code

**Common chat variables:**

- `#file` - Attaches a specific file as context
- `#selection` - Attaches selected code as context
- `#codebase` - Searches across all workspace files

### ⌨️ Activity: Use participants, commands, and variables

1. Open this repository in VS Code.

1. Open the starter file: `exercises/04-copilot-chat-skills/starter.py`

1. Open Copilot Chat and use `@workspace` to ask about your project:

    ```
    @workspace What files are in this repository and what is the purpose of each one?
    ```

1. Use a slash command to explain the Python starter file. Select all the code in `starter.py`, then type:

    ```
    /explain
    ```

1. Use a slash command to generate tests. With `starter.py` still selected, type:

    ```
    /tests
    ```

1. Use `#file` to attach a specific file as context:

    ```
    #file:starter.py What functions are defined in this file and what do they return?
    ```

1. Try inline chat: click on a line in `starter.py`, press `Ctrl+I` (Windows/Linux) or `Cmd+I` (macOS), and type a prompt directly in the editor.

1. Follow the full step-by-step instructions in [exercises/04-copilot-chat-skills/README.md](../../exercises/04-copilot-chat-skills/README.md) to complete all parts of this exercise.

<details>
<summary>Having trouble? 🤷</summary><br/>

- The `@github` participant requires you to be signed in to GitHub in VS Code.
- If a participant is not available, check that your Copilot extension is up to date.
- Slash commands appear as you type `/` in the Copilot Chat input box.
- Chat variables appear as you type `#` in the Copilot Chat input box.

</details>
