# Exercise 5: Creating Custom Agents for GitHub Copilot

**Learning objectives:**

- Understand what custom agents are and how they differ from other Copilot customization files
- Create custom agent profiles (`.agent.md`) with YAML frontmatter and prompt instructions
- Configure agent properties: name, description, tools, and model
- Use custom agents in VS Code and on GitHub.com
- Explore real-world custom agent examples from the community

**Duration:** ~30 minutes

**Prerequisites:** Complete [Exercise 4](../04-copilot-chat-skills/README.md) before this exercise.

---

## Background

Custom agents allow you to create specialized AI assistants tailored to specific tasks in your development workflow. Each custom agent has its own identity, tools, and behavioral instructions. You can create agents for testing, code review, planning, debugging, documentation, and more.

A custom agent is a Markdown file with the `.agent.md` suffix. It contains YAML frontmatter that defines the agent's properties and a Markdown body that serves as the agent's system prompt. Custom agents are available in VS Code, JetBrains IDEs, Eclipse, Xcode, and on GitHub.com with the Copilot coding agent.

For the full reference, see [Creating custom agents for Copilot coding agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents).

---

## Custom Agents vs Other Copilot Files

| File | Purpose | Used by |
|------|---------|---------|
| `.agent.md` | Define specialized agents with specific tools and behaviors | Copilot Chat (IDE) + Copilot coding agent (GitHub.com) |
| `copilot-instructions.md` | Repository-wide context for all Copilot interactions | Copilot Chat (interactive sessions) |
| `.instructions.md` | Path-specific rules for certain file types | Copilot Chat (when matching files are open) |
| `.prompt.md` | Reusable prompt templates for common tasks | Copilot Chat (invoked manually) |
| `AGENTS.md` | Repository onboarding context for autonomous agents | AI coding agents (autonomous tasks) |

Custom agents go further than instructions or prompts: they create an entirely new Copilot personality with a defined name, description, and restricted (or expanded) tool access.

---

## Anatomy of a Custom Agent File

A custom agent file has two parts: YAML frontmatter and a Markdown prompt body.

```markdown
---
name: test-specialist
description: Focuses on test coverage and testing best practices
tools: ["read", "edit", "search", "runTests"]
---

You are a testing specialist. Your responsibilities:

- Analyze existing tests and identify coverage gaps
- Write unit tests, integration tests, and end-to-end tests
- Review test quality and suggest improvements
- Focus only on test files. Do not modify production code.
```

### YAML frontmatter properties

| Property | Required | Description |
|----------|----------|-------------|
| `name` | No | Display name for the agent. Defaults to the filename without the `.agent.md` suffix. |
| `description` | Yes | A brief explanation of what the agent does. Appears in the agent dropdown. |
| `tools` | No | List of tools the agent can use. Omit to grant access to all available tools. |
| `model` | No | The AI model the agent should use (VS Code and JetBrains only). |

### Where to store agent files

| Location | Scope |
|----------|-------|
| `.github/agents/` in a repository | Available in that repository (workspace) |
| VS Code user profile folder | Available across all your workspaces (personal) |
| `.github-private` repository (org) | Available across all repositories in the organization |

---

## Step 1: Create a Test Specialist Agent

This agent focuses exclusively on writing and improving tests. It has access to all tools by omitting the `tools` property.

1. Create the directory and file:

   ```bash
   mkdir -p .github/agents
   ```

2. Create a new file at `.github/agents/test-specialist.agent.md`:

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

3. Save the file.

---

## Step 2: Create an Implementation Planner Agent

This agent creates technical plans without writing code. It restricts tools to reading, searching, and editing only.

1. Create a new file at `.github/agents/implementation-planner.agent.md`:

   ```markdown
   ---
   name: implementation-planner
   description: Creates detailed implementation plans and technical specifications in Markdown format
   tools: ["read", "search", "edit"]
   ---

   You are a technical planning specialist focused on creating comprehensive
   implementation plans. Your responsibilities:

   - Analyze requirements and break them down into actionable tasks
   - Create detailed technical specifications and architecture documentation
   - Generate implementation plans with clear steps, dependencies, and
     milestones
   - Document API designs, data models, and system interactions
   - Create Markdown files with structured plans that development teams
     can follow

   Always structure your plans with clear headings, task breakdowns, and
   acceptance criteria. Include considerations for testing, deployment,
   and potential risks. Focus on creating thorough documentation rather
   than implementing code.
   ```

2. Save the file.

---

## Step 3: Create a Debug Agent

This agent follows a structured debugging process. It has access to terminal, testing, and editing tools.

1. Create a new file at `.github/agents/debug.agent.md`:

   ```markdown
   ---
   name: debug
   description: Systematically identifies, analyzes, and resolves bugs using a structured debugging process
   tools: ["read", "edit", "search", "runInTerminal", "runTests", "problems"]
   ---

   You are in debug mode. Follow this structured process:

   ## Phase 1: Assess
   - Read error messages, stack traces, or failure reports
   - Reproduce the bug by running the application or tests
   - Document the expected vs actual behavior

   ## Phase 2: Investigate
   - Trace the code execution path leading to the bug
   - Check for common issues: null references, off-by-one errors,
     race conditions, incorrect assumptions
   - Form specific hypotheses about the root cause

   ## Phase 3: Fix
   - Make targeted, minimal changes to address the root cause
   - Follow existing code patterns and conventions
   - Consider edge cases and potential side effects

   ## Phase 4: Verify
   - Run tests to verify the fix resolves the issue
   - Run broader test suites to ensure no regressions
   - Summarize what you fixed and why

   Be systematic. Do not jump to solutions. Always reproduce and
   understand the bug before attempting to fix it.
   ```

2. Save the file.

---

## Step 4: Use Your Custom Agents in VS Code

1. Open GitHub Copilot Chat in VS Code.
2. At the bottom of the chat view, click the agent dropdown.
3. Your custom agents appear in the list with the names you defined.
4. Select **test-specialist** and ask it to analyze test coverage:

   ```
   Look at exercises/01-prompt-engineering/starter.js and suggest what tests
   should be written for the existing functions.
   ```

5. Switch to **implementation-planner** and ask it to plan a feature:

   ```
   Create an implementation plan for adding a new exercise about MCP servers
   to this workshop.
   ```

6. Switch to **debug** and try a debugging prompt:

   ```
   There is a bug in this code. The function returns undefined instead of
   the expected result. Help me debug it.
   ```

Each agent responds differently because it has a different system prompt, tool access, and behavioral focus.

---

## Step 5: Review the Example File

This repository includes an example custom agent for reference:

```
exercises/05-agent-files/example-agent.agent.md
```

Open and read through it. It shows a code reviewer agent with a structured review process, restricted tools, and specific output formatting instructions.

---

## Step 6: Explore the Community Collection

The [awesome-copilot](https://github.com/github/awesome-copilot) repository on GitHub contains a growing collection of community-contributed custom agents. Browse the `agents/` directory to find agents for:

- **Language experts:** C#, Python, Rust, Java, Go, Ruby, Swift, PHP, and more
- **Framework specialists:** Next.js, React, Laravel, Drupal, .NET MAUI, Electron
- **DevOps and infrastructure:** GitHub Actions, Kubernetes, Azure IaC, Terraform
- **Planning and architecture:** Blueprint mode, implementation plans, PRDs, ADRs
- **Testing:** Playwright, polyglot test suites, browser testing
- **Specialized tasks:** Accessibility audits, security reviews, code tours, documentation

To use a community agent in your project:

1. Find an agent file in the [agents directory](https://github.com/github/awesome-copilot/tree/main/agents).
2. Copy its content into a new `.agent.md` file in your `.github/agents/` directory.
3. Customize the prompt and tool list to match your project's needs.

---

## Step 7: Use Custom Agents on GitHub.com

Custom agents also work with the Copilot coding agent on GitHub.com. When you assign an issue to Copilot, you can select a specific custom agent to handle the task.

> **Note:** This step requires a GitHub Copilot subscription that includes the coding agent feature.

1. Navigate to [github.com/copilot/agents](https://github.com/copilot/agents) to see your available agents.
2. Create a new issue with a clear task for the coding agent:

   ```
   Title: Add unit tests for the formatDate function

   Body:
   Write unit tests for the `formatDate` function in
   `exercises/01-prompt-engineering/starter.js`.

   Requirements:
   - Test valid Date objects
   - Test edge cases (end of year, leap year)
   - Use clear test descriptions
   ```

3. When assigning the issue to **Copilot**, select your **test-specialist** agent from the agents dropdown.
4. The coding agent uses your custom agent's prompt and tool restrictions when implementing the task.
5. Review the resulting Pull Request and collaborate with `@copilot` via review comments.

---

## Step 8: Commit Your Agents

```bash
git add .github/agents/
git commit -m "Add custom agents for testing, planning, and debugging"
git push
```

---

## Tips for Designing Effective Agents

- **Be specific about the role.** A clear identity ("You are a testing specialist") produces better results than a vague one ("Help with code").
- **Restrict tools when appropriate.** A planning agent should not execute code. A documentation agent should not modify source files. Use the `tools` property to enforce boundaries.
- **Structure the prompt with headings.** Agents follow structured instructions more reliably than free-form text.
- **Keep prompts under 30,000 characters.** This is the maximum allowed by the platform.
- **Test with representative tasks.** Try several prompts to verify the agent behaves as expected before sharing it with your team.
- **Use descriptive filenames.** The filename becomes the default agent name. Use lowercase with hyphens: `test-specialist.agent.md`, not `TestSpecialist.agent.md`.

---

## Troubleshooting

**My custom agent does not appear in the agent dropdown:**

- Confirm the file is in `.github/agents/` and has the `.agent.md` suffix.
- Check that the YAML frontmatter is valid (correct indentation, no missing colons).
- Verify the `description` property is present. It is required.
- In VS Code, try reopening the chat panel or reloading the window.

**The agent does not follow its instructions:**

- Review the prompt for clarity. Shorter, more direct instructions work better.
- Check that the `tools` list includes the tools the agent needs.
- Verify the file is saved and committed (the coding agent on GitHub reads committed files).

**I want the agent available across all my workspaces:**

- In VS Code, select **User profile** as the location when creating the agent.
- The agent file is stored in your VS Code user profile folder, not in the repository.

---

## Summary

You created custom agent profiles to specialize Copilot for different tasks. Key points:

- Custom agents are `.agent.md` files with YAML frontmatter and a Markdown prompt body.
- Store agents in `.github/agents/` for workspace scope or in your user profile for global scope.
- Use the `description` property (required) to explain what the agent does.
- Use the `tools` property to restrict which capabilities the agent can use.
- Agents work in VS Code, JetBrains IDEs, and on GitHub.com with the coding agent.
- The [awesome-copilot](https://github.com/github/awesome-copilot) community collection has dozens of ready-to-use agents.
- Design agents with clear roles, structured prompts, and appropriate tool restrictions.

---

## Next Steps

Proceed to [Exercise 6: Org-Level Best Practices](../06-org-level-best-practices/README.md).
