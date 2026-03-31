## Step 6: Dependency Security - Enable Dependabot and Dependency Review

_SDLC Phase: **Security**_

> **Why this matters:** Every external dependency is a potential attack vector. The Security phase ensures your project's supply chain is monitored and that vulnerable dependencies are flagged before they reach production. GitHub provides automated tools — Dependabot alerts, security updates, and the dependency review action — that make this continuous and low-effort.

In the previous step, you added the `chalk` npm package to the Task Manager. This introduced a `package.json` with external dependencies. In this step, you configure GitHub's security features to monitor those dependencies automatically.

### 📖 Theory: GitHub dependency security

GitHub provides three layers of dependency security:

| Feature | What it does | When it runs |
|---------|-------------|--------------|
| **Dependabot alerts** | Notifies you when a dependency has a known vulnerability | Continuously, whenever a new advisory is published |
| **Dependabot security updates** | Automatically opens PRs to update vulnerable dependencies | When an alert is created |
| **Dependabot version updates** | Opens PRs to keep dependencies up-to-date, even without vulnerabilities | On a schedule you configure (daily, weekly, monthly) |
| **Dependency review action** | Blocks PRs that introduce dependencies with known vulnerabilities | On every pull request |

These features work together: Dependabot monitors your existing dependencies, and the dependency review action prevents new vulnerable dependencies from being merged.

### 📖 Theory: The dependency graph

GitHub builds a **dependency graph** from your manifest files (`package.json`, `requirements.txt`, etc.). This graph shows:

- All direct dependencies your project uses
- Transitive dependencies (dependencies of your dependencies)
- Known vulnerabilities for each version

You can view the dependency graph at **Settings → Code security and analysis** or under the **Insights → Dependency graph** tab.

## ⌨️ Activity: Enable Dependabot

1. Navigate to your repository on GitHub.com.

1. Go to **Settings → Advanced Security** (in the left sidebar under "Security").

1. Enable the following features:

    - **Dependency graph** — should already be enabled for public repos
    - **Dependabot alerts** — click **Enable** to receive notifications about vulnerable dependencies
    - **Dependabot security updates** — click **Enable** so Dependabot can automatically open PRs to fix vulnerable dependencies

    > 🪧 **Note:** These settings may already be enabled by default depending on your repository visibility and organization policies.

## ⌨️ Activity: Configure Dependabot version updates

1. Back in your Codespace or VS Code, create a new file at `.github/dependabot.yml`. Paste the following content:

    ```yaml
    version: 2
    updates:
      - package-ecosystem: "npm"
        directory: "/"
        schedule:
          interval: "weekly"
    ```

    This tells Dependabot to check for newer versions of npm dependencies every week and open PRs to update them.

    > 💡 **Tip:** In Codespaces, files save automatically. If you are working locally, save with `Ctrl+S` / `Cmd+S`.

## ⌨️ Activity: Add the dependency review action

The dependency review action runs on pull requests and checks whether any newly introduced dependencies have known vulnerabilities. If they do, the PR check fails, preventing the merge.

1. Create a new file at `.github/workflows/dependency-review.yml`. Paste the following content:

    ```yaml
    name: Dependency Review
    on: [pull_request]

    permissions:
      contents: read

    jobs:
      dependency-review:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout
            uses: actions/checkout@v4

          - name: Dependency Review
            uses: actions/dependency-review-action@v4
    ```

    This workflow runs on every pull request and scans the diff for new dependencies with known vulnerabilities.

    > 💡 **Tip:** In Codespaces, files save automatically. If you are working locally, save with `Ctrl+S` / `Cmd+S`.

## ⌨️ Activity: Verify the dependency graph

1. On GitHub.com, navigate to your repository.

1. Go to **Insights → Dependency graph**.

1. You should see `chalk` listed as a dependency, along with any transitive dependencies it brings in.

    > 🪧 **Note:** The dependency graph updates after each push. If you just pushed, it may take a minute to reflect the latest changes.

## ⌨️ Activity: Commit and push your work

1. In the VS Code left sidebar, click the **Source Control** tab.

1. Hover over each changed file and click the **+** (Stage Changes) button, or click the **+** next to **Changes** to stage everything.

    <img width="300" alt="Screenshot: Stage changes icon in VS Code Source Control" src="https://raw.githubusercontent.com/skills/getting-started-with-github-copilot/main/.github/images/staging-changes-icon.png" />

1. In the **Message** text box, type:

    ```
    Add Dependabot config and dependency review workflow
    ```

1. Click **Commit**, then click **Sync Changes** to push to GitHub.

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- The file must be at exactly `.github/dependabot.yml` (not `dependabot.yaml` or inside another folder).
- The `dependency-review.yml` workflow must be inside `.github/workflows/`.
- If the dependency graph does not show `chalk`, make sure `package.json` and `package-lock.json` exist and are pushed to the `main` branch.
- Dependabot alerts may take a few minutes to appear after enabling.
- For a deeper walkthrough, see [exercises/06-dependency-security/README.md](exercises/06-dependency-security/README.md).

</details>
