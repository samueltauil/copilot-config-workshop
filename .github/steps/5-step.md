## Step 5: Creating Custom Agents

Your team uses GitHub Copilot across multiple workflows: writing tests, debugging, planning implementations, and reviewing code. Instead of re-explaining the same context in every chat, you can create custom agents that specialize in each task. Each custom agent has its own identity, system prompt, and tool access.

### 📖 Theory: What are custom agents?

Custom agents are `.agent.md` files that create specialized Copilot assistants for specific tasks. Each agent has YAML frontmatter (name, description, tools) and a Markdown prompt body that defines its behavior.

| File | Location | Used by |
|------|----------|---------|
| `.agent.md` | `.github/agents/` in a repository | Copilot Chat (IDE) + Copilot coding agent (GitHub.com) |
| `copilot-instructions.md` | `.github/` | Copilot Chat (interactive sessions) |
| `AGENTS.md` | Anywhere in the repository | AI coding agents (autonomous tasks) |

Custom agents go further than instructions: they create an entirely new Copilot personality with a defined name, restricted tools, and behavioral focus.

### ⌨️ Activity: Create a custom agent

1. Create the agents directory:

    ```bash
    mkdir -p .github/agents
    ```

1. Create a file named `.github/agents/test-specialist.agent.md` with the following content:

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

1. Save and commit:

    ```bash
    git add .github/agents/
    git commit -m "Add test-specialist custom agent"
    git push
    ```

1. In VS Code, open Copilot Chat. Your custom agent appears in the agent dropdown at the bottom of the chat panel. Select it and try a prompt.

1. Create additional agents for debugging, planning, or code review. The exercise README has templates for all of these.

1. Follow the full step-by-step instructions in [exercises/05-agent-files/README.md](../../exercises/05-agent-files/README.md) to complete this exercise.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Confirm the file is in `.github/agents/` and has the `.agent.md` suffix.
- Check that the YAML frontmatter is valid (correct indentation, no missing colons).
- Verify the `description` property is present. It is required.
- In VS Code, try reopening the chat panel or reloading the window if the agent does not appear.
- Review the [official documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents) for the full agent reference.

</details>
