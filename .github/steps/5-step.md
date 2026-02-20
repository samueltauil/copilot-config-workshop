## Step 5: Agent Instruction Files

Your team has started assigning issues to the GitHub Copilot coding agent. The agent is capable but keeps making the same exploratory mistakes: it tries to run build scripts that do not exist, uses `npm install` in a repository with no `package.json`, and ignores project conventions. An `AGENTS.md` file gives the agent the context it needs before it starts work.

### 📖 Theory: What are agent instruction files?

Unlike Copilot Chat custom instructions (which guide Copilot in interactive sessions), agent instruction files are designed for agents that complete multi-step tasks independently. When an AI agent opens a repository, it reads the nearest `AGENTS.md` file in the directory tree.

| File | Location | Used by |
|------|----------|---------|
| `AGENTS.md` | Anywhere in the repository | GitHub Copilot coding agent and other AI agents |
| `copilot-instructions.md` | `.github/` | Copilot Chat (interactive) |

An `AGENTS.md` file should help an agent answer these questions without needing to explore the repository:

1. What is this project and what does it do?
1. How do I build the project?
1. How do I run the tests?
1. What conventions should I follow when making changes?
1. What should I avoid doing?

### ⌨️ Activity: Create agent instruction files

1. Create a file named `AGENTS.md` at the root of your repository.

1. Add the following content (updated to match your repository):

    ```markdown
    # Agent Instructions

    This file provides guidance to AI coding agents working in this repository.
    Read this file before exploring the codebase or making any changes.

    ## Repository Purpose

    This repository is a workshop for learning how to configure GitHub Copilot.
    It contains exercises covering prompt engineering, custom instructions,
    path-specific instructions, Copilot Chat skills, and agent instruction files.
    There is no application code to build or deploy.

    ## Repository Structure

    - `exercises/` - One subdirectory per exercise, each containing a `README.md`
      with step-by-step instructions and any starter code files.
    - `.github/copilot-instructions.md` - Repository-wide Copilot custom instructions.
    - `.github/instructions/` - Path-specific Copilot instruction files.
    - `slides/index.html` - Self-contained slide deck (no build step required).
    - `AGENTS.md` - This file.
    - `README.md` - Workshop landing page.

    ## Build and Test

    This repository contains no application code, build system, or test runner.
    There is nothing to compile, bundle, or run.

    ## Conventions

    - All prose is written in US English.
    - Markdown headings use ATX style (`#`, `##`).
    - Code blocks include a language identifier.
    - Relative links are used for cross-references within the repository.
    - Exercise numbers are zero-padded (e.g., `01`, `02`).

    ## Constraints

    - Do not add build tools, package managers, or runtime dependencies.
    - Do not rename or delete exercise directories.
    - Keep this file under 150 lines.
    ```

1. Save and commit:

    ```bash
    git add AGENTS.md
    git commit -m "Add agent instruction file"
    git push
    ```

1. Optionally, create a subdirectory-level `AGENTS.md` in `exercises/` to give agents more specific guidance for that part of the project.

1. Follow the full step-by-step instructions in [exercises/05-agent-files/README.md](../../exercises/05-agent-files/README.md) to complete this exercise.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Confirm that `AGENTS.md` is at the repository root.
- Check that the file is committed and pushed (the Copilot coding agent reads the committed version, not uncommitted local changes).
- Both `AGENTS.md` and `copilot-instructions.md` can coexist; they are used by different tools.

</details>
