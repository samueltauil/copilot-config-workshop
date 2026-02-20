# Exercise 5: Agent Instruction Files

**Learning objectives:**
- Understand what agent instruction files are and when to use them
- Create an `AGENTS.md` file with structured information for AI coding agents
- Understand the difference between `AGENTS.md` and `copilot-instructions.md`
- Verify that the agent file is applied correctly

**Duration:** ~20 minutes

**Prerequisites:** Complete [Exercise 2](../02-custom-instructions/README.md) before this exercise.

---

## Background

Agent instruction files provide guidance to AI coding agents (such as the GitHub Copilot coding agent) that work autonomously in your repository. Unlike Copilot Chat custom instructions (which guide Copilot in interactive sessions), agent instruction files are designed for agents that complete multi-step tasks independently.

When an AI agent opens a repository, it reads the nearest `AGENTS.md` file in the directory tree. The agent uses this file to understand how to work efficiently in the repository without extensive exploration.

**Official documentation:** [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)

---

## Types of Agent Instruction Files

The official documentation describes the following agent instruction file formats:

| File | Location | Scope |
|------|----------|-------|
| `AGENTS.md` | Anywhere in the repository | Nearest file in the directory tree takes precedence |
| `CLAUDE.md` | Repository root | Applies to Claude-based agents |
| `GEMINI.md` | Repository root | Applies to Gemini-based agents |

For the GitHub Copilot coding agent, `AGENTS.md` is the recommended format. This exercise focuses on `AGENTS.md`.

---

## Difference Between `AGENTS.md` and `copilot-instructions.md`

| Aspect | `copilot-instructions.md` | `AGENTS.md` |
|--------|--------------------------|------------|
| Used by | Copilot Chat (interactive) | AI coding agents (autonomous) |
| Format | Plain Markdown | Plain Markdown |
| Location | `.github/copilot-instructions.md` | Anywhere in the repository tree |
| Purpose | Guide responses in conversations | Onboard agents to work efficiently |

Both files can coexist in the same repository and serve complementary purposes.

---

## What to Include in `AGENTS.md`

An `AGENTS.md` file should help an agent answer these questions without needing to explore the repository:

1. What is this project and what does it do?
2. How do I build the project?
3. How do I run the tests?
4. How do I run the linter?
5. What conventions should I follow when making changes?
6. What should I avoid doing?
7. Are there any known limitations or tricky areas?

Keep the file focused and concise. Two pages (approximately 100-150 lines) is a good target. An agent reads this file before starting work, so longer is not always better.

---

## Step 1: Create the `AGENTS.md` File

1. In VS Code, create a new file at the root of the repository:
   ```bash
   touch AGENTS.md
   ```
2. Open the file.

---

## Step 2: Write the Agent Instructions

Copy the following template into `AGENTS.md` and update each section to match your repository.

For this workshop repository, you can use the content as written since it is accurate for this project:

```markdown
# Agent Instructions

This file provides guidance to AI coding agents working in this repository.
Read this file before exploring the codebase or making any changes.

## Repository Purpose

This repository is a workshop for learning how to configure GitHub Copilot.
It contains five exercises covering prompt engineering, custom instructions,
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

To verify that Markdown files are well-formed, you may use any Markdown linter.
No linter is pre-configured in this repository.

## Conventions

- All prose is written in US English.
- Markdown headings use ATX style (`#`, `##`).
- Code blocks include a language identifier (e.g., ```bash, ```js).
- Relative links are used for cross-references within the repository.
- Exercise numbers are zero-padded (e.g., `01`, `02`).

## Constraints

- Do not add build tools, package managers, or runtime dependencies.
- Do not rename or delete exercise directories.
- Do not modify the slide deck structure (only content inside slides may change).
- Keep this file under 150 lines.
```

3. Save the file.

   > **Screenshot reference:** The `AGENTS.md` file appears in the root directory in the VS Code Explorer panel, alongside `README.md`. The file is open and shows the Markdown content with sections for repository purpose, structure, build and test, conventions, and constraints.

---

## Step 3: Understand How the Agent Uses This File

When the GitHub Copilot coding agent is assigned to an issue or pull request in this repository, it will:

1. Read `AGENTS.md` from the repository root.
2. Use the information to understand the project structure without exploring every file.
3. Follow the conventions and constraints listed.
4. Use the build and test instructions to validate its changes before submitting them.

You do not need to configure anything to enable this behavior. The Copilot coding agent reads `AGENTS.md` automatically when it is present.

---

## Step 4: Create a Subdirectory-Level `AGENTS.md`

You can also place `AGENTS.md` files in subdirectories to give agents more specific guidance for that part of the project. The nearest `AGENTS.md` file in the directory tree takes precedence over files higher up.

1. Create a subdirectory-level agent file:
   ```bash
   touch exercises/AGENTS.md
   ```

2. Add the following content:
   ```markdown
   # Agent Instructions (exercises/)

   This subdirectory contains the workshop exercises. Each exercise is in its own
   numbered directory (e.g., `01-prompt-engineering/`).

   ## When Modifying Exercises

   - Each exercise directory contains a `README.md` with step-by-step instructions.
   - Starter code files (e.g., `starter.js`, `starter.py`) are intentionally minimal.
   - Do not add dependencies or build steps to individual exercise directories.
   - Preserve the structure: one `README.md` per exercise directory.

   ## Validation

   Review the `README.md` for each modified exercise to confirm that:
   - All step numbers are sequential.
   - All file paths referenced in the steps exist.
   - All commands shown in code blocks are correct.
   ```

3. Save the file.

---

## Step 5: Review the Example File

This repository includes a fully-written example `AGENTS.md` for reference:

```
exercises/05-agent-files/example-AGENTS.md
```

Open and read through it. It shows how a real application project would structure its agent instructions, including commands for building and running tests.

---

## Step 6: Commit Your Work

```bash
git add AGENTS.md exercises/AGENTS.md
git commit -m "Add agent instruction files"
git push
```

---

## Troubleshooting

**The Copilot coding agent does not seem to follow my instructions:**
- Confirm that `AGENTS.md` is at the repository root or in the relevant subdirectory.
- Check that the file is committed and pushed (the agent reads the committed version, not uncommitted local changes).
- Review the agent's pull request description to see which files it referenced.

**I have both `AGENTS.md` and `copilot-instructions.md`. Which one is used?**
- `AGENTS.md` is used by the Copilot coding agent (autonomous tasks).
- `copilot-instructions.md` is used by Copilot Chat (interactive sessions).
- Both can coexist and are used independently for their respective purposes.

---

## Summary

You created `AGENTS.md` files to guide AI coding agents working in this repository. Key points:

- `AGENTS.md` is used by AI coding agents for autonomous tasks.
- The nearest `AGENTS.md` in the directory tree takes precedence.
- Include: project purpose, structure, build/test commands, conventions, and constraints.
- Keep it under two pages. Agents read it before starting work.
- It coexists with `copilot-instructions.md` and serves a different purpose.

---

## Workshop Complete

You have completed all five exercises in this workshop. Here is a summary of what you built:

| File | Purpose |
|------|---------|
| `.github/copilot-instructions.md` | Repository-wide custom instructions for Copilot Chat |
| `.github/instructions/python.instructions.md` | Path-specific instructions for Python files |
| `.github/instructions/tests.instructions.md` | Path-specific instructions for test files |
| `AGENTS.md` | Agent instruction file for the repository root |
| `exercises/AGENTS.md` | Agent instruction file for the exercises subdirectory |

---

**Official documentation:** [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)
