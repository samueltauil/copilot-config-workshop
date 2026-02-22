## Step 6: Org-Level Best Practices for Copilot Configuration

Your organization now manages dozens of repositories. Each team has configured Copilot independently, and the configurations are drifting apart. You need a strategy to share configuration across all repositories while still letting individual teams customize for their projects.

### 📖 Theory: Org-level vs. repository-level configuration

GitHub supports a special `.github` repository at the organization level. Files placed there serve as defaults for all repositories in the organization that do not define their own. This creates a two-level hierarchy.

| File | Repository level | Org level (`.github` repository) |
|------|-----------|---------------------------|
| `copilot-instructions.md` | `.github/copilot-instructions.md` | `.github/copilot-instructions.md` in the org's `.github` repo |
| Path-specific instructions | `.github/instructions/*.instructions.md` | `.github/instructions/*.instructions.md` in the org's `.github` repo |
| `AGENTS.md` | Repository root or any subdirectory | Root of the org's `.github` repository |
| Custom agents (`.agent.md`) | `.github/agents/*.agent.md` | `.github/agents/*.agent.md` in org `.github` or `.github-private` repo |

**Precedence rule:** Repository-level configuration takes precedence over org-level configuration. If a repository defines its own `copilot-instructions.md`, the org-level file is not merged; the repository-level file is used exclusively.

### 📖 Theory: Key best practices

| Practice | Details |
|----------|---------|
| Scope org-level instructions to universal rules | Avoid repository-specific details in the org-level file |
| Do not repeat org-level content in repo files | Repository-level files replace, not extend, the org-level file |
| Use consistent naming for path-specific files | Follow the `topic.instructions.md` naming pattern |
| Prefix org-level agent filenames with the org name | Prevents name conflicts with repository-level agents |
| Audit loaded instructions regularly | Use the **Used n references** panel in Copilot Chat |

## ⌨️ Activity: Review your configuration hierarchy

1. Review the configuration files you created in previous steps:
    - `.github/copilot-instructions.md` (Step 2)
    - `.github/instructions/python.instructions.md` (Step 3)
    - `.github/agents/*.agent.md` (Step 5)

1. For each file, identify which instructions are truly universal (suitable for an org-level file) and which are project-specific (suitable for repository-level only).

1. Add a scope comment at the top of each file as a Markdown blockquote:

    ```markdown
    > **Scope:** This file applies to all files in this repository.
    > An org-level version would contain: security policies, documentation standards.
    ```

## ⌨️ Activity: Design an org-level configuration

For this activity, you do not need to create an actual org-level repository. Instead, plan what the org-level files would contain.

1. Open a new file at `exercises/06-org-level-best-practices/org-level-plan.md`.

1. Write a brief plan that answers these questions:
    - What rules from your `copilot-instructions.md` would move to the org level?
    - What rules are project-specific and must stay at the repository level?
    - What path-specific instruction files would you create at the org level?
    - What custom agents would you share across the organization?

1. Save the file.

## ⌨️ Activity: Finish the workshop

1. When you have completed your review, go to the **Actions** tab in your repository on GitHub.

1. Select the **Step 6** workflow from the left sidebar.

1. Click **Run workflow** to complete the workshop and see the final review.

<details>
<summary>Having trouble? 🤷</summary><br/>

- The org-level `.github` repository must be named exactly `.github` under your organization.
- Repository-level files always take precedence over org-level files; there is no merging of `copilot-instructions.md`.
- Use the **Used n references** panel in Copilot Chat to verify which instruction files are loaded.
- For a deeper walkthrough, see [exercises/06-org-level-best-practices/README.md](exercises/06-org-level-best-practices/README.md).

</details>
