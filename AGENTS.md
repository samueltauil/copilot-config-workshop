# Agent Instructions

This file provides guidance to AI coding agents working in this repository.
Read this file before exploring the codebase or making any changes.

## Repository Purpose

This repository is a workshop for learning how to configure GitHub Copilot.
It contains six exercises covering prompt engineering, custom instructions,
path-specific instructions, Copilot Chat skills, agent instruction files,
and org-level best practices. There is no application code to build or deploy.

## Repository Structure

- `exercises/` - One subdirectory per exercise, each with a `README.md` and optional starter code.
- `.github/copilot-instructions.md` - Repository-wide Copilot Chat custom instructions.
- `.github/instructions/` - Path-specific Copilot instruction files (`.instructions.md` suffix).
- `.github/steps/` - Step content files for the GitHub Skills framework.
- `.github/workflows/` - GitHub Actions workflows that gate step progression.
- `slides/index.html` - Self-contained HTML slide deck (no build step required).
- `AGENTS.md` - This file.
- `README.md` - Workshop landing page.
- `LICENSE` - MIT license.

## Build and Test

This repository contains no build system, package manager, or test runner.
There is nothing to compile, bundle, or execute.

To verify Markdown files, any standard Markdown linter may be used.
No linter is pre-configured.

## Conventions

- All prose uses US English.
- Markdown headings use ATX style (`#`, `##`).
- Code blocks include a language identifier (e.g., ```bash, ```js).
- Cross-references within the repository use relative links.
- Exercise directories use zero-padded numbers (e.g., `01`, `02`).

## Constraints

- Do not add build tools, package managers, or runtime dependencies.
- Do not rename or delete exercise directories.
- Do not modify the Reveal.js CDN links in `slides/index.html`.
- Keep this file under 60 lines.
