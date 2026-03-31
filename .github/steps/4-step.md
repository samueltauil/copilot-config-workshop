## Step 4: Prompt Files - Build a Tester Agent

_SDLC Phase: **Testing & Quality Assurance**_

> **Why this matters:** The Testing phase verifies that what was built actually works as intended. It catches defects before they reach users. Copilot can automate test creation and run tests repeatedly, turning a time-consuming manual task into a guided, repeatable workflow.

The Developer Agent generated your implementation code. Before you can trust it, you need tests. In this step, you build a **Tester Agent** that generates and runs tests automatically, then create [prompt files](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#creating-prompt-files) that capture reusable testing workflows and route them through the Tester Agent.

### 📖 Theory: How prompt files work

Prompt files let you save multi-step instructions as reusable templates. Instead of typing a long prompt every time you want to generate tests, you save it once as a file and invoke it with a single command.

Prompt files use the `.prompt.md` suffix and live in `.github/prompts/`. Each file has a YAML front matter block (the configuration header) and a Markdown prompt body.

| Field | Purpose |
|-------|---------|
| `description` | Short label shown in the `/` command list |
| `agent` | Which Copilot mode or custom agent runs the prompt |
| `argument-hint` | Placeholder text shown in the argument input |

You invoke a prompt file by typing `/` in Copilot Chat and selecting it from the list. This turns a multi-step workflow into a single action.

> 🪧 **Note:** When you type `/` in the Copilot Chat input, a menu appears listing all available prompt files from `.github/prompts/`.
>
> The Codespace uses Node.js 20, which supports the built-in test runner (`node --test`). If you are working locally, confirm you have Node.js 18 or later installed.

## ⌨️ Activity: Create the Tester Agent

1. Create a new file at `.github/agents/tester.agent.md`:

    ```markdown
    ---
    name: tester
    description: Generates and runs tests for the Task Manager, iterating until all tests pass
    ---

    You are a quality assurance engineer. Your job is to test the
    Task Manager implementation thoroughly.

    ## Process

    1. Read all source files under `src/`.
    2. Generate a test file for each module under `tests/`.
    3. Use the built-in Node.js test runner (`node --test`) and
       `node:assert` for assertions.
    4. Run the full test suite after generation.
    5. If any tests fail, read the error output, fix the issue
       (in the test or in the source code), and re-run.
    6. Repeat until all tests pass.

    ## Rules

    - Never skip or delete a failing test. Fix the root cause.
    - Test both success paths and error paths.
    - Each test file must be runnable independently.
    - Use descriptive test names that explain the expected behavior.
    ```

    > 💡 **Tip:** In Codespaces, files save automatically. If you are working locally, save with `Ctrl+S` / `Cmd+S`.

## ⌨️ Activity: Create prompt files

1. In the VS Code Explorer sidebar, right-click the `.github` folder and select **New Folder**. Name it `prompts`.

1. Right-click the new `.github/prompts` folder and select **New File**. Name it `generate-tests.prompt.md`. Paste the following content:

    ```markdown
    ---
    description: Generate unit tests for a source module
    agent: tester
    argument-hint: Path to the source file to test (e.g. src/models/task.js)
    ---

    # Generate Unit Tests

    Your goal is to generate unit tests for the module the user specifies.

    ## Steps

    1. Read the target source file.
    2. Identify all exported functions and classes.
    3. Generate tests that cover:
       - Normal inputs with expected outputs
       - Edge cases (empty strings, zero, negative numbers, null, undefined)
       - Error conditions (invalid types, missing required fields)
    4. Use the built-in Node.js `node:assert` module and Node.js test runner.
    5. Save the test file to `tests/` using the convention `<module>.test.js`.
    6. Run the tests with `node --test` and fix any failures.
    ```

1. Right-click `.github/prompts` again, select **New File**, and name it `test-edge-cases.prompt.md`. Paste the following content:

    ```markdown
    ---
    description: Add edge case tests for an existing test file
    agent: tester
    argument-hint: Path to the existing test file
    ---

    # Add Edge Case Tests

    Review the existing test file the user provides. Add tests for any
    edge cases not already covered.

    Focus on:
    - Boundary values (empty arrays, max integers, very long strings)
    - Type mismatches (passing a number where a string is expected)
    - Concurrent modifications (adding while iterating)
    - Missing optional fields
    - Duplicate entries

    Run all tests after adding the new cases and fix any failures.
    ```

    > 💡 **Tip:** In Codespaces, files save automatically. If you are working locally, save with `Ctrl+S` / `Cmd+S`.

    > 🪧 **Note:** Both prompt files set `agent: tester`. This means invoking either prompt will automatically use the Tester Agent you just created, combining the reusable workflow from the prompt file with the persona and rules from the agent.

## ⌨️ Activity: Use the Tester Agent to generate tests

1. In Copilot Chat, select **tester** from the agent dropdown.

1. Type:

    ```
    Read all source files in src/ and generate comprehensive tests
    in the tests/ directory. Cover the Task model, the task service,
    and the validator utilities. Run the tests and fix any failures.
    ```

1. Watch the agent generate test files, run them, and iterate on failures.

1. When the agent finishes, verify independently:

    ```bash
    node --test tests/
    ```

## ⌨️ Activity: Use the test-edge-cases prompt to add coverage

1. Type `/` in Copilot Chat and select **test-edge-cases** from the list.

1. Provide the path to an existing test file, such as `tests/models/task.test.js`.

1. Because the prompt sets `agent: tester`, the Tester Agent runs the workflow automatically. It adds edge case tests, runs them, and fixes any failures.

1. When it finishes, verify independently:

    ```bash
    node --test tests/
    ```

## ⌨️ Activity: Commit and push your work

1. In the VS Code left sidebar, click the **Source Control** tab.

1. Hover over each changed file and click the **+** (Stage Changes) button, or click the **+** next to **Changes** to stage everything.

    <img width="300" alt="Screenshot: Stage changes icon in VS Code Source Control" src="https://raw.githubusercontent.com/skills/getting-started-with-github-copilot/main/.github/images/staging-changes-icon.png" />

1. In the **Message** text box, type:

    ```
    Add prompt files and Tester Agent with tests
    ```

1. Click **Commit**, then click **Sync Changes** to push to GitHub.

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Prompt files must end with `.prompt.md` and live in `.github/prompts/`.
- The YAML front matter must start on the very first line.
- If `node --test` is not available, you are on Node.js < 18. The Codespace uses Node.js 20, which supports `node --test`.
- If tests fail because source code has issues, let the tester agent fix both the tests and the source.
- For a deeper walkthrough, see [exercises/04-copilot-chat-skills/README.md](exercises/04-copilot-chat-skills/README.md).

</details>
