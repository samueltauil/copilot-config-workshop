## Step 5: Creating Custom Agents

Your team uses GitHub Copilot across multiple workflows: writing tests, debugging, planning implementations, and reviewing code. Instead of re-explaining the same context in every chat, you can create [custom agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents) that specialize in each task. Each custom agent has its own identity, system prompt, and tool access.

### 📖 Theory: What are custom agents?

Custom agents are `.agent.md` files that create specialized Copilot assistants for specific tasks. Each agent has YAML frontmatter (name, description, tools) and a Markdown prompt body that defines its behavior.

| File | Location | Used by |
|------|----------|---------|
| `.agent.md` | `.github/agents/` in a repository | Copilot Chat (IDE) + Copilot coding agent (GitHub.com) |
| `copilot-instructions.md` | `.github/` | Copilot Chat (interactive sessions) |
| `AGENTS.md` | Anywhere in the repository | AI coding agents (autonomous tasks) |

Custom agents go further than instructions: they create an entirely new Copilot personality with a defined name, restricted tools, and behavioral focus.

### YAML frontmatter properties

| Property | Required | Description |
|----------|----------|-------------|
| `name` | No | Display name for the agent. Defaults to the filename. |
| `description` | Yes | A brief explanation of what the agent does. |
| `tools` | No | List of tools the agent can use. Omit to grant all tools. |

## ⌨️ Activity: Create a test-specialist agent

1. Create the agents directory:

    ```bash
    mkdir -p .github/agents
    ```

1. Create a new file at `.github/agents/test-specialist.agent.md` with the following content:

    ```markdown
    ---
    name: test-specialist
    description: Focuses on test coverage, quality, and testing best practices without modifying production code
    ---

    You are a testing specialist focused on improving code quality through
    comprehensive testing. Your responsibilities:

    - Analyze existing tests and identify coverage gaps
    - Write unit tests, integration tests, and end-to-end tests following
      best practices
    - Review test quality and suggest improvements for maintainability
    - Ensure tests are isolated, deterministic, and well-documented
    - Focus only on test files and avoid modifying production code unless
      specifically requested

    Always include clear test descriptions and use appropriate testing
    patterns for the language and framework.
    ```

1. Save the file.

## ⌨️ Activity: Use the test-specialist agent

1. Open Copilot Chat in VS Code. Your custom agent appears in the agent dropdown at the bottom of the chat panel.

1. Select **test-specialist** from the dropdown and ask it to generate tests:

    ```
    Generate a comprehensive test file for
    exercises/04-copilot-chat-skills/starter.py.
    Include tests for normal inputs, edge cases (empty lists, single items),
    and error conditions (invalid input types). Use pytest conventions.
    Save the tests to exercises/04-copilot-chat-skills/test_starter.py.
    ```

1. Review the generated test file. Confirm it includes tests for `calculate_average`, `find_duplicates`, and `flatten`.

1. Run the tests:

    ```bash
    python3 -m pytest exercises/04-copilot-chat-skills/test_starter.py -v
    ```

1. If any tests fail, stay in the test-specialist agent and paste the error output. The agent focuses exclusively on test quality and avoids modifying `starter.py`.

1. Run the tests again until all pass.

## ⌨️ Activity: Create additional agents (optional)

You can create more agents for other tasks. Here are two examples you can try:

**Debug agent** at `.github/agents/debug.agent.md`:

```markdown
---
name: debug
description: Systematically identifies, analyzes, and resolves bugs using a structured debugging process
tools: ["read", "edit", "search", "runInTerminal", "runTests", "problems"]
---

You are in debug mode. Follow this process:
1. Read error messages and stack traces
2. Reproduce the bug by running the application or tests
3. Trace the code execution path and form a hypothesis
4. Make minimal, targeted fixes
5. Run tests to verify the fix and check for regressions
```

**Implementation planner** at `.github/agents/implementation-planner.agent.md`:

```markdown
---
name: implementation-planner
description: Creates detailed implementation plans and technical specifications in Markdown format
tools: ["read", "search", "edit"]
---

You are a technical planning specialist. Create implementation plans
with clear headings, task breakdowns, and acceptance criteria. Focus
on documentation rather than implementing code.
```

## ⌨️ Activity: Commit and push your work

1. Commit and push:

    ```bash
    git add .github/agents/
    git commit -m "Add custom agents for testing and other workflows"
    git push
    ```

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Confirm the file is in `.github/agents/` and has the `.agent.md` suffix.
- Check that the YAML frontmatter is valid (correct indentation, no missing colons).
- Verify the `description` property is present. It is required.
- In VS Code, try reopening the chat panel or reloading the window if the agent does not appear.
- For a deeper walkthrough, see [exercises/05-agent-files/README.md](exercises/05-agent-files/README.md).
- Browse the [awesome-copilot](https://github.com/github/awesome-copilot) community collection for more agent examples.

</details>
