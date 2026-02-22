# Org-Level Best Practices for Copilot Configuration

> **Note:** This is a reference guide. The main workshop uses exercises 01 through 05. This content supplements the workshop with information about managing Copilot configuration across an organization.

---

## Overview

GitHub Copilot configuration files can exist at both the organization and repository levels. Organizations that manage many repositories benefit from shared defaults. This guide explains how to structure, layer, and maintain Copilot configuration across an organization.

---

## The Org-Level `.github` Repository

GitHub supports a special repository named `.github` within an organization. Files in this repository serve as organization-wide defaults. When a repository does not define its own version of a file, Copilot uses the org-level file instead.

To set up the org-level repository:

1. Navigate to your organization on GitHub.
2. Create a repository named exactly `.github`.
3. Add configuration files using the same paths as repository-level files.

Any repository in the organization inherits these files automatically.

---

## Configuration Hierarchy

The table below shows each configuration file type and its path at both levels.

| File type | Repository-level path | Org-level path (in the `.github` repo) |
|-----------|----------------------|----------------------------------------|
| Custom instructions | `.github/copilot-instructions.md` | `.github/copilot-instructions.md` |
| Path-specific instructions | `.github/instructions/*.instructions.md` | `.github/instructions/*.instructions.md` |
| Agent instructions | `AGENTS.md` (root or any subdirectory) | `AGENTS.md` (root) |
| Custom agents | `.github/agents/*.agent.md` | `.github/agents/*.agent.md` (or in `.github-private`) |
| Prompt files | `.github/prompts/*.prompt.md` | `.github/prompts/*.prompt.md` |

---

## Precedence Rules

Repository-level files always override org-level files. Copilot does not merge the two levels. If a repository defines its own `copilot-instructions.md`, the org-level version is ignored for that repository.

Key points about precedence:

- `copilot-instructions.md`: repository replaces org entirely.
- Path-specific instructions: both levels can be active for the same file pattern. Avoid conflicting rules between levels.
- `AGENTS.md`: the nearest file in the directory tree wins. A repository-level file overrides the org-level file.
- Custom agents: if both levels define an agent with the same name, the repository-level agent wins in that repository.
- Prompt files: repository-level files with the same name override org-level files.

---

## Best Practices

### Scope org-level instructions to universal rules

The org-level `copilot-instructions.md` should contain only rules that apply to every repository. Good candidates include security policies, documentation standards, and code review expectations.

```markdown
# Org-Level Custom Instructions

## Security

- Never include secrets, API keys, or credentials in code.
- Flag hardcoded connection strings as a security concern.

## Documentation

- All public APIs must include documentation comments.
```

### Do not repeat org-level content in repository files

The repository-level file replaces the org-level file. It does not extend it. Copy only the rules you want to keep, then add project-specific details.

```markdown
# Repository Custom Instructions

## Language and Runtime

- This project uses TypeScript 5+ with strict mode enabled.
- Target Node.js 22 for the backend.

## Testing

- Use Vitest for all tests.
- Place test files alongside source files with a `.test.ts` suffix.
```

### Use consistent naming for path-specific files

Adopt a standard naming pattern across all repositories:

| Purpose | File name |
|---------|-----------|
| Python rules | `python.instructions.md` |
| TypeScript rules | `typescript.instructions.md` |
| Test rules | `tests.instructions.md` |
| Security rules | `security.instructions.md` |
| Documentation rules | `docs.instructions.md` |

### Prefix org-level agent filenames with the org name

This prevents naming collisions with repository-level agents.

- Org-level: `acme-security-reviewer.agent.md`
- Repository-level: `security-reviewer.agent.md`

### Audit loaded instructions regularly

Open the **Used _n_ references** panel in Copilot Chat to see which instruction files are active. Check this panel after adding or changing configuration files at any level.

---

## Example: Org-Level vs. Repository-Level Split

Consider the Task Manager project from the workshop exercises. Here is how you might split configuration between the two levels.

### Org-level files (in the `.github` repository)

```
.github/
  copilot-instructions.md        # Security, documentation, review standards
  instructions/
    python.instructions.md       # Org-wide Python style rules
    security.instructions.md     # Security rules for all file types
  agents/
    acme-code-reviewer.agent.md  # Org-wide code review agent
```

**Org-level `copilot-instructions.md`:**

```markdown
# Org Custom Instructions

- Never commit secrets or credentials.
- All public functions must have docstrings.
- Suggest error handling for I/O and network calls.
```

### Repository-level files (in the Task Manager repository)

```
.github/
  copilot-instructions.md          # Project-specific language, architecture, testing
  instructions/
    data-models.instructions.md    # Rules for model files in this project
  agents/
    task-planner.agent.md          # Project-specific planning agent
```

**Repository-level `copilot-instructions.md`:**

```markdown
# Task Manager Custom Instructions

- This project uses Python 3.12 with FastAPI.
- Data models live in `src/models/` and use SQLAlchemy.
- Tests use pytest. Place test files in `tests/` with a `test_` prefix.
```

The org-level file covers universal rules. The repository-level file covers project-specific details. There is no overlap between the two.

---

## Verification: Checking Loaded Instructions

You can verify which instructions Copilot applies to your current context.

1. Open Copilot Chat in VS Code.
2. Send a prompt while you have a file open in the editor.
3. Look for the **Used _n_ references** indicator below the response.
4. Click the indicator to expand the list of loaded instruction files.
5. Confirm that both org-level and repository-level files appear as expected.

If an expected file is missing:

- Check the file path matches the required structure.
- Confirm the `applyTo` pattern matches the open file (for path-specific instructions).
- Verify the repository-level file does not override the org-level file unintentionally.

---

## Further Reading

- [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)
- [Managing Copilot policies for your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization)
- [Using agent mode in VS Code](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)
