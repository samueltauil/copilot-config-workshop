## Step 6: Org-Level Best Practices for Copilot Configuration

Your organization now manages dozens of repositories. Each team has configured Copilot independently, and the configurations are drifting apart. Security teams have no way to enforce a common baseline. You need a strategy to share configuration across all repositories while still letting individual teams customize for their projects.

### 📖 Theory: Org-level vs. repository-level configuration

GitHub supports a special `.github` repository at the organization level. Files placed there serve as defaults for all repositories in the organization that do not define their own. This creates a two-level hierarchy.

#### Configuration file hierarchy

| File | Repository level | Org level (`.github` repository) |
|------|-----------|---------------------------|
| `copilot-instructions.md` | `.github/copilot-instructions.md` | `.github/copilot-instructions.md` in the org's `.github` repository |
| Path-specific instructions | `.github/instructions/*.instructions.md` | `.github/instructions/*.instructions.md` in the org's `.github` repository |
| `AGENTS.md` | Repository root or any subdirectory | Root of the org's `.github` repository |
| `copilot-agents.yml` | `.github/copilot-agents.yml` | `.github/copilot-agents.yml` in the org's `.github` repository |

**Precedence rule:** Repository-level configuration takes precedence over org-level configuration. If a repository defines its own `copilot-instructions.md`, the org-level file is not merged; the repository-level file is used exclusively for that repository.

#### When to use org-level configuration

Use the org-level `.github` repository when:

- The same conventions apply across most or all repositories (language, style guides, security policies).
- You want to establish a baseline that individual teams can override.
- You manage a large number of repositories and cannot maintain per-repository configuration files.

Use repository-level configuration when:

- The repository has specialized conventions that differ from the org default.
- The repository uses a different language, framework, or toolchain.
- The repository serves a different audience (for example, a public open-source project vs. an internal tool).

### 📖 Theory: Naming conventions and file organization

#### `copilot-instructions.md`

- Org-level: Keep the file focused on standards that apply universally (security practices, documentation standards, code review expectations).
- Repository-level: Add project-specific context (framework version, architecture, team conventions).
- The repository-level `copilot-instructions.md` replaces the org-level one; it does not add to it. Do not repeat org-level content.

#### Path-specific instruction files

- Use consistent naming across the organization: `language.instructions.md` or `topic.instructions.md`.
- Org-level path-specific files set baseline rules for a file type across all repositories.
- When both an org-level and a repository-level path-specific file match the same file, Copilot receives the combined content from both. This behavior is additive and can produce conflicting instructions if not managed carefully.
- Avoid overlapping `applyTo` patterns between org and repository files where possible to prevent conflicts.

#### `AGENTS.md`

- The org-level `AGENTS.md` can describe org-wide conventions and prohibited actions.
- Repository-level `AGENTS.md` files should describe repository-specific context (build commands, test commands, repository structure).
- The nearest `AGENTS.md` in the directory tree takes precedence for a given file path.

#### `copilot-agents.yml`

- Org-level custom agents are available to all repositories in the organization.
- Repository-level custom agents are available only in the defining repository.
- Name org-level agents with a prefix that identifies the organization (for example, `acme-security-reviewer`) to avoid name conflicts with repository-level agents.

### 📖 Theory: Avoiding conflicts and duplication

Follow these practices to keep org-level and repository-level files from conflicting:

1. **Scope org-level instructions to universal rules.** Avoid specifics that only some repositories need.
1. **Document the org-level file location.** Add a comment or link in repository-level files so contributors know where org defaults are defined.
1. **Use `applyTo` patterns that do not overlap** between org and repository path-specific files unless you intend additive behavior.
1. **Review combined instructions periodically.** Copilot Chat shows all loaded instruction files in the **Used n references** panel; use this to audit what Copilot receives.
1. **Test instructions with representative prompts** after making changes at either level.

### ⌨️ Activity: Review and document your configuration hierarchy

1. Open the full exercise guide: [exercises/06-org-level-best-practices/README.md](../../exercises/06-org-level-best-practices/README.md)

1. Review the configuration files you have created in previous steps:
    - `.github/copilot-instructions.md`
    - `.github/instructions/python.instructions.md`
    - `AGENTS.md`

1. For each file, write a one-sentence comment at the top (as a Markdown blockquote) that describes its scope:

    ```markdown
    > **Scope:** This file applies to all files in this repository.
    ```

1. Consider what would belong in an org-level version of each file versus what should remain repository-specific. Write a brief note in each file to distinguish the two.

1. Read the [best practices section](../../exercises/06-org-level-best-practices/README.md#best-practices-summary) of the exercise guide and confirm your understanding.

<details>
<summary>Having trouble? 🤷</summary><br/>

- The org-level `.github` repository must be named exactly `.github` under your organization.
- Repository-level files always take precedence over org-level files; there is no merging of `copilot-instructions.md`.
- Use the **Used n references** panel in Copilot Chat to verify which instruction files are loaded.

</details>
