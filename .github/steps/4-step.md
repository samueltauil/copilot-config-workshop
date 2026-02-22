## Step 4: Prompt Files &mdash; Build a Tester Agent

_SDLC Phase: **Testing & Quality Assurance**_

The Developer Agent generated your implementation code. Before you can trust it, you need tests. In this step you create [prompt files](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#creating-prompt-files) that capture reusable testing workflows, then build a **Tester Agent** that generates and runs tests automatically.

### 📖 Theory: How prompt files work

Prompt files use the `.prompt.md` suffix and live in `.github/prompts/`. Each file has a YAML front matter block and a Markdown prompt body.

| Field | Purpose |
|-------|---------|
| `description` | Short label shown in the `/` command list |
| `agent` | Which Copilot mode runs the prompt (often `agent`) |
| `argument-hint` | Placeholder text shown in the argument input |

You invoke a prompt file by typing `/` in Copilot Chat and selecting it from the list. This turns a multi-step workflow into a single action.

## ⌨️ Activity: Create prompt files

1. Create the prompts directory:

    ```bash
    mkdir -p .github/prompts
    ```

1. Create `.github/prompts/generate-tests.prompt.md`:

    ```markdown
    ---
    description: Generate unit tests for a source module
    agent: agent
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

1. Create `.github/prompts/test-edge-cases.prompt.md`:

    ```markdown
    ---
    description: Add edge case tests for an existing test file
    agent: agent
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

1. Save both files.

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

1. Save the file.

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

1. Try the `/generate-tests` prompt file: type `/` in Copilot Chat, select **generate-tests**, and provide the path `src/utils/validators.js`. Compare the output to the tests the agent already wrote.

## ⌨️ Activity: Commit and push your work

1. Commit and push:

    ```bash
    git add .github/prompts/ .github/agents/ tests/
    git commit -m "Add prompt files and Tester Agent with tests"
    git push
    ```

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Prompt files must end with `.prompt.md` and live in `.github/prompts/`.
- The YAML front matter must start on the very first line.
- If `node --test` is not available, you are on Node.js < 18. The Codespace uses Node.js 20, which supports `node --test`.
- If tests fail because source code has issues, let the tester agent fix both the tests and the source.
- For a deeper walkthrough, see [exercises/04-copilot-chat-skills/README.md](exercises/04-copilot-chat-skills/README.md).

</details>
