# Exercise 6: Org-Level Best Practices for Copilot Configuration

**Learning objectives:**

- Understand how Copilot configuration files are organized at the organization level
- Identify when to use org-level vs. repository-level configuration
- Apply naming conventions and file organization strategies for managing multiple repositories
- Avoid conflicts and duplication between org-level and repository-level instruction files
- Understand the hierarchy and precedence of configuration files at both levels

**Duration:** ~25 minutes

**Prerequisites:** Complete exercises 2, 3, and 5 before this exercise, as they introduce all the configuration files covered here.

---

## Background

GitHub Copilot configuration files can exist at the organization level in addition to individual repositories. When you manage many repositories, maintaining a consistent Copilot configuration across all of them is important for productivity and code quality. This exercise explains how to structure that configuration using GitHub's organization-level `.github` repository. See [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) for the full reference.

---

## The Org-Level `.github` Repository

GitHub supports a special repository named `.github` within an organization. Files placed in this repository serve as organization-wide defaults. When a repository in the organization does not define its own version of a configuration file, GitHub uses the org-level file as the default.

To create or access the org-level `.github` repository:

1. Navigate to your organization on GitHub.
2. Create a repository named exactly `.github`.
3. Place configuration files in the repository following the same directory structure as repository-level files.

---

## Configuration File Hierarchy

The following table shows where each Copilot configuration file can live and how the levels interact.

| File | Repository level path | Org level path |
|------|----------------|----------------|
| `copilot-instructions.md` | `.github/copilot-instructions.md` | `.github/copilot-instructions.md` in the org's `.github` repository |
| Path-specific instructions | `.github/instructions/*.instructions.md` | `.github/instructions/*.instructions.md` in the org's `.github` repository |
| `AGENTS.md` | Repository root or any subdirectory | Root of the org's `.github` repository |
| Custom agents (`.agent.md`) | `.github/agents/*.agent.md` | `.github/agents/*.agent.md` in the org's `.github` repository or the `.github-private` repository |

**Key precedence rule:** Repository-level configuration takes precedence over org-level configuration. When a repository defines its own `copilot-instructions.md`, the org-level file is not merged with it. The repository-level file is used exclusively for that repository.

---

## When to Use Org-Level Configuration

### Use org-level configuration when:

- The same conventions apply across most or all repositories (language standards, security policies, documentation requirements).
- You want to establish a baseline that individual teams can override.
- You manage many repositories and cannot maintain per-repository configuration files.
- A new repository should start with sensible defaults without manual setup.

### Use repository-level configuration when:

- The repository has specialized conventions that differ from the org default.
- The repository uses a different language, framework, or toolchain.
- The repository serves a different audience (for example, a public open-source project vs. an internal tool).
- A team needs more granular control over Copilot's behavior for their specific project.

---

## Best Practices for `copilot-instructions.md`

### Org-level file

Focus the org-level `copilot-instructions.md` on standards that apply universally:

```markdown
# Org-Level Custom Instructions

## Security

- Never include secrets, API keys, or credentials in code suggestions.
- Flag any hardcoded connection strings or passwords as a security concern.

## Documentation

- All public APIs must include documentation comments.
- Reference the official documentation when suggesting usage of third-party libraries.

## Code Review

- Suggest error handling for all I/O operations and network calls.
- Flag missing null or undefined checks in critical code paths.
```

### Repository-level file

Focus the repository-level file on project-specific context that does not belong in a shared org policy:

```markdown
# Project Custom Instructions

## Language and Runtime

- This project uses TypeScript 5+ with strict mode enabled.
- Target: Node.js 22 for the backend, modern browsers for the frontend.

## Architecture

- This project uses the repository pattern for data access.
- Business logic lives in the `src/services/` directory.
- Data models are defined in `src/models/`.

## Testing

- Use Vitest for unit and integration tests.
- Test files live alongside source files with the `.test.ts` suffix.
```

### What to avoid

- Do not repeat org-level content in repository-level files. The repository-level `copilot-instructions.md` replaces the org-level one; it does not add to it.
- Do not include team-specific instructions in the org-level file. Team-specific rules belong in the repository.
- Do not add instructions that conflict with each other within the same file.

---

## Best Practices for Path-Specific Instruction Files

### Naming conventions

Use consistent names across the organization:

| Pattern | File name |
|---------|-----------|
| All Python files | `python.instructions.md` |
| All TypeScript files | `typescript.instructions.md` |
| All SQL files | `sql.instructions.md` |
| Test files | `tests.instructions.md` |
| Documentation files | `docs.instructions.md` |
| Infrastructure-as-code files | `terraform.instructions.md` |

### Org-level vs. repository-level path-specific files

- Org-level files set baseline rules for a file type across all repositories.
- Repository-level files can supplement org-level files for the same pattern; both sets of instructions are active when a file matches.
- Avoid overlapping `applyTo` patterns between org and repository files where possible. When both match, Copilot receives the combined content, which can produce conflicting instructions.

### Example structure

Org-level (in the org's `.github` repository):

```
.github/
  instructions/
    python.instructions.md    # Org-wide Python standards
    security.instructions.md  # Org-wide security rules for all files
```

Repository-level (in an individual repository):

```
.github/
  instructions/
    python.instructions.md    # Repository-specific Python rules (combined with org-level for this repository)
    data-models.instructions.md  # Repository-specific instructions for data model files
```

---

## Best Practices for `AGENTS.md`

### Org-level `AGENTS.md`

The org-level `AGENTS.md` describes organization-wide conventions and constraints:

```markdown
# Agent Instructions (Org Level)

## Organization Conventions

- All code changes must pass the CI pipeline before merging.
- Do not modify files in the `vendor/` or `third-party/` directories.
- Follow the branching strategy: feature branches from `main`, named `feature/<ticket-id>-description`.

## Prohibited Actions

- Do not commit secrets or credentials.
- Do not modify GitHub Actions workflow files without explicit approval in the issue.
- Do not change dependency versions without verifying compatibility.
```

### Repository-level `AGENTS.md`

The repository-level `AGENTS.md` provides project-specific context the agent needs to work efficiently:

```markdown
# Agent Instructions

## Repository Purpose

This service handles payment processing for the e-commerce platform.

## Build and Test

- Install dependencies: `npm install`
- Run tests: `npm test`
- Run linter: `npm run lint`
- Build for production: `npm run build`

## Architecture

- `src/handlers/` - HTTP request handlers
- `src/services/` - Business logic
- `src/models/` - Database models (uses Prisma ORM)
```

### Hierarchy

The nearest `AGENTS.md` in the directory tree takes precedence over files higher up. This allows:

- Repository root `AGENTS.md` to provide general repository context
- Subdirectory `AGENTS.md` files to provide more specific guidance for that part of the project

---

## Best Practices for Custom Agents (`.agent.md`)

Custom agents are `.agent.md` files that create specialized Copilot assistants with their own name, description, tools, and behavioral prompt. The same org-level vs. repository-level distinction applies.

### Naming conventions

- Org-level agents: prefix the filename with the organization name to avoid conflicts.
  - Example: `acme-security-reviewer.agent.md`, `acme-docs-generator.agent.md`
- Repository-level agents: use descriptive filenames scoped to the project.
  - Example: `payment-validator.agent.md`, `schema-migrator.agent.md`

### Where to store agents

| Location | Scope |
|----------|-------|
| `.github/agents/` in a repository | Available in that repository (workspace) |
| VS Code user profile folder | Available across all your workspaces (personal) |
| `.github-private` repository (org) | Available across all repositories in the organization |

### Hierarchy

- Org-level agents (in `.github-private`) are available in all repositories in the organization.
- Repository-level agents are available only in the repository where they are defined.
- If both an org-level and a repository-level agent have the same name, the repository-level agent takes precedence in that repository.

---

## Best Practices Summary

| Practice | Details |
|----------|---------|
| Scope org-level instructions to universal rules | Avoid repository-specific details in the org-level file |
| Do not repeat org-level content in repository-level files | Repository-level files replace, not extend, the org-level file |
| Use consistent naming for path-specific files | Follow the `topic.instructions.md` naming pattern |
| Prefix org-level agent filenames with the org name | Prevents name conflicts with repository-level agents |
| Audit loaded instructions regularly | Use the **Used n references** panel in Copilot Chat |
| Document the org-level file location | Help contributors find where org defaults are defined |
| Test instructions with representative prompts | Verify behavior after changes at either level |

---

## Step 1: Audit Your Current Configuration

1. Review the files you created in previous exercises:
   - `.github/copilot-instructions.md`
   - `.github/instructions/python.instructions.md`
   - `.github/agents/*.agent.md`

2. For each file, identify which instructions are truly universal (suitable for org level) and which are project-specific (suitable for repository level only).

3. Add a comment at the top of each file to document its intended scope:

   ```markdown
   > **Scope:** This file applies to all files in this repository.
   > An org-level version of this file would contain: security policies, documentation standards.
   ```

---

## Step 2: Design an Org-Level Configuration

For this step, you do not need to create an actual org-level repository. Instead, plan what the org-level files would contain.

1. Open a new file at `exercises/06-org-level-best-practices/org-level-example/copilot-instructions.md`.

2. Write a sample org-level `copilot-instructions.md` file. Focus on rules that would apply to every repository in an organization.

3. Open a new file at `exercises/06-org-level-best-practices/org-level-example/instructions/security.instructions.md`.

4. Add content that applies security-focused instructions to all files (use `applyTo: "**/*"`).

---

## Step 3: Compare Org-Level and Repository-Level Files

1. Place your existing `.github/copilot-instructions.md` content and your new org-level example side by side.

2. Identify content that appears in both files and decide which level it belongs at.

3. Refactor the files so that:
   - The org-level file contains only universal rules.
   - The repository-level file contains only project-specific rules.
   - There is no duplicated content between the two.

---

## Troubleshooting

**The org-level instructions do not seem to apply to my repository:**

- Confirm the org-level repository is named exactly `.github` under your organization.
- Confirm the file path within the org's `.github` repository matches the expected path (for example, `.github/copilot-instructions.md` within the `.github` repository corresponds to `.github/copilot-instructions.md` at the org level).
- If the repository has its own `copilot-instructions.md`, the repository-level file takes precedence and the org-level file is not used for that repository.

**Both org-level and repository-level path-specific files are loaded, but they conflict:**

- Review the combined instructions using the **Used n references** panel in Copilot Chat.
- Refactor the org-level file to remove any rules that conflict with repository-level rules.
- If the conflict is intentional (the repository overrides an org rule), document the reason in both files.

**I cannot find the org-level `.github` repository:**

- Only organization owners can create the org-level `.github` repository.
- Navigate to `github.com/<your-org>` and look for the `.github` repository in the list of repositories.
- If it does not exist, create it by clicking **New repository** and naming it `.github`.

---

## Summary

Key points from this exercise:

- The org-level `.github` repository stores default Copilot configuration files that apply to all repositories in the organization.
- Repository-level configuration files always take precedence over org-level files; there is no merging.
- Scope org-level instructions to universal rules; keep project-specific rules in repository-level files.
- Use consistent naming for path-specific instruction files across the organization.
- Prefix org-level custom agent filenames to avoid conflicts with repository-level agents.
- Audit loaded instructions using the **Used n references** panel in Copilot Chat.

---

## Workshop Complete

You have completed all six exercises in this workshop. Here is a summary of what you built:

| File | Purpose |
|------|---------|
| `.github/copilot-instructions.md` | Repository-wide custom instructions for Copilot Chat |
| `.github/instructions/python.instructions.md` | Path-specific instructions for Python files |
| `.github/instructions/tests.instructions.md` | Path-specific instructions for test files |
| `.github/prompts/add-tests.prompt.md` | Reusable prompt file for generating unit tests |
| `.github/prompts/explain-architecture.prompt.md` | Reusable prompt file for architecture explanation |
| `.github/agents/code-reviewer.agent.md` | Custom agent for code review |
| `.github/agents/test-specialist.agent.md` | Custom agent for test coverage and quality |
| `.github/agents/implementation-planner.agent.md` | Custom agent for technical planning |
| `.github/agents/debug.agent.md` | Custom agent for structured debugging |
