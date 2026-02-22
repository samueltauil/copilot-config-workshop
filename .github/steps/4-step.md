## Step 4: Copilot Chat Participants, Commands, Variables, and Prompt Files

You are spending too much time writing long prompts to explain what file you mean, what code you want explained, or what tests you need. Copilot Chat provides special keywords called [participants, commands, and variables](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) that let you express context quickly and precisely. You can also create reusable [prompt files](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#creating-prompt-files) to turn multi-step workflows into one-click actions.

### 📖 Theory: Chat participants, slash commands, chat variables, and prompt files

| Keyword | Name | Purpose |
|---------|------|---------|
| `@` | Chat participant | Scopes the prompt to a domain expert |
| `/` | Slash command | Triggers a specific action |
| `#` | Chat variable | Attaches specific context to the prompt |

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

**Prompt files** use the `.prompt.md` suffix and live in `.github/prompts/`. Each file contains a YAML front matter block and a Markdown prompt body. You invoke them with the `/` command in Copilot Chat.

## ⌨️ Activity: Use chat participants

1. Open this repository in a Codespace or in VS Code locally.

1. Open the starter file: `exercises/04-copilot-chat-skills/starter.py`

1. Open Copilot Chat and use `@workspace` to ask about your project:

    ```
    @workspace What files are in this repository and what is the purpose
    of each one?
    ```

1. The response should reference real file paths from this repository (such as `exercises/`, `slides/`, `.github/`).

1. Use `@github` to access GitHub-specific skills:

    ```
    @github What are the supported file types for path-specific Copilot
    instructions?
    ```

## ⌨️ Activity: Use slash commands

1. Open `exercises/04-copilot-chat-skills/starter.py` and select all the code (`Ctrl+A` or `Cmd+A`).

1. In Copilot Chat, type `/explain` and press Enter. Copilot explains the selected code in detail.

1. Use `/tests` to generate tests. With `starter.py` still selected, type:

    ```
    /tests
    ```

1. Save the generated tests to `exercises/04-copilot-chat-skills/test_starter.py`.

1. Run the tests:

    ```bash
    python3 -m pytest exercises/04-copilot-chat-skills/test_starter.py -v
    ```

    If `pytest` is not installed, use the built-in test runner:

    ```bash
    python3 -m unittest exercises/04-copilot-chat-skills/test_starter.py -v
    ```

1. If any tests fail, paste the error output into Copilot Chat and ask it to fix the test file. Run again until all tests pass.

## ⌨️ Activity: Use chat variables and inline chat

1. Use `#file` to reference a specific file without having it open:

    ```
    #file:starter.py What functions are defined in this file and what
    do they return?
    ```

1. Select one function in `starter.py` and use `#selection`:

    ```
    #selection Rewrite this function to handle an empty input by returning
    an empty list instead of raising an exception.
    ```

1. Try inline chat: click on a line in `starter.py`, press `Ctrl+I` (Windows/Linux) or `Cmd+I` (macOS), and type a prompt directly in the editor. Use the **Accept** or **Discard** buttons to keep or reject the change.

## ⌨️ Activity: Create a reusable prompt file

1. Create the prompts directory:

    ```bash
    mkdir -p .github/prompts
    ```

1. Create a new file at `.github/prompts/add-tests.prompt.md` with this content:

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

1. Save the file.

1. Test it: open Copilot Chat, type `/` in the prompt box, and select `add-tests` from the list. Copilot executes the prompt and provides a structured response.

## ⌨️ Activity: Commit and push your work

1. Commit and push:

    ```bash
    git add .github/prompts/
    git commit -m "Add reusable prompt file for Copilot Chat"
    git push
    ```

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- The `@github` participant requires you to be signed in to GitHub in VS Code.
- If a participant is not available, check that your Copilot extension is up to date.
- Slash commands appear as you type `/` in the Copilot Chat input box.
- Chat variables appear as you type `#` in the Copilot Chat input box.
- Prompt files must end with `.prompt.md` and live in `.github/prompts/`.
- For a deeper walkthrough, see [exercises/04-copilot-chat-skills/README.md](exercises/04-copilot-chat-skills/README.md).

</details>
