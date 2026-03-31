# Exercise 06: Dependency Security - Enable Dependabot and Dependency Review

**SDLC Phase: Security**

> **Why this matters:** Every external dependency is a potential attack vector. The Security phase ensures your project's supply chain is monitored and that vulnerable dependencies are flagged before they reach production. GitHub provides automated tools — Dependabot alerts, security updates, and the dependency review action — that make this continuous and low-effort.

In Exercise 05, you added the `chalk` npm package to the Task Manager. This introduced a `package.json` with external dependencies. In this exercise, you configure GitHub's security features to monitor those dependencies automatically.

**Duration:** ~20 minutes

---

## Workshop Roadmap

| Exercise | Copilot Concept | Agent | SDLC Phase |
|----------|----------------|-------|------------|
| 01 | Prompt engineering and interaction modes | Planner | Planning |
| 02 | Repository-wide custom instructions | Architect | Design |
| 03 | Path-specific instructions | Developer | Implementation |
| 04 | Prompt files | Tester | Testing |
| 05 | Copilot code review | — | Code Review |
| **06 (this one)** | **Dependency security** | **—** | **Security** |
| 07 | Agent files and orchestration | Orchestrator | Full lifecycle |

---

## Learning Objectives

- Understand how GitHub dependency security features work
- Enable Dependabot alerts and security updates on a repository
- Configure Dependabot version updates with `dependabot.yml`
- Add the dependency review GitHub Action to gate pull requests
- View the dependency graph and verify dependencies are tracked
- Connect the Security phase of the SDLC to GitHub features

---

## Prerequisites

- Completion of [Exercise 05](../05-code-review/README.md) (you need `package.json` with the chalk dependency)
- Repository access to enable Dependabot (Settings → Code security)
- GitHub Codespaces or VS Code with the GitHub Copilot extension installed

---

## Understanding Dependency Security

### The three layers

GitHub provides three layers of dependency security that work together:

| Layer | What it does | When it runs |
|-------|-------------|--------------|
| **Dependabot alerts** | Notifies you when a dependency has a known vulnerability (CVE) | Continuously, whenever a new advisory is published |
| **Dependabot security updates** | Automatically opens PRs to update vulnerable dependencies to a safe version | When an alert is created |
| **Dependabot version updates** | Opens PRs to keep dependencies current, even when no vulnerability exists | On a schedule you configure |

### The dependency graph

GitHub builds a **dependency graph** from manifest files (`package.json`, `package-lock.json`, etc.). This graph maps:

- **Direct dependencies** — packages you explicitly installed (e.g., `chalk`)
- **Transitive dependencies** — packages your dependencies depend on
- **Known vulnerabilities** — CVEs that affect specific versions

The dependency graph powers all three Dependabot features. Without it, GitHub cannot identify which versions you use or whether they are affected.

### The dependency review action

The dependency review action runs on pull requests. It compares the dependency graph before and after the PR's changes. If a PR introduces (or updates to) a version with a known vulnerability, the check fails. This prevents vulnerable dependencies from being merged.

This is especially useful in teams: even if the person opening the PR is unaware of a vulnerability, the automated check catches it.

---

## Step 1: Enable Dependabot

1. Navigate to your repository on GitHub.com.

2. Go to **Settings → Code security** (in the left sidebar under "Security").

3. Enable the following features:

   - **Dependency graph** — should already be enabled for public repositories
   - **Dependabot alerts** — click **Enable** to receive notifications about vulnerable dependencies
   - **Dependabot security updates** — click **Enable** so Dependabot automatically opens PRs to fix known vulnerabilities

   > 🪧 **Note:** These settings may already be enabled by default depending on your repository visibility and organization policies. If a feature is already on, no action is needed.

---

## Step 2: Configure Dependabot Version Updates

Dependabot version updates are configured with a YAML file in your repository. Unlike alerts and security updates (which are enabled in Settings), version updates require a configuration file.

1. In your Codespace or VS Code, create a new file at `.github/dependabot.yml`. Paste the following content:

   ```yaml
   version: 2
   updates:
     - package-ecosystem: "npm"
       directory: "/"
       schedule:
         interval: "weekly"
   ```

   This tells Dependabot to check for newer versions of npm packages every week and open PRs to update them.

2. Save the file.

### What each field means

| Field | Value | Purpose |
|-------|-------|---------|
| `version` | `2` | The Dependabot configuration format version |
| `package-ecosystem` | `"npm"` | Tells Dependabot to look for `package.json` and `package-lock.json` |
| `directory` | `"/"` | Where the manifest file is, relative to the repo root |
| `schedule.interval` | `"weekly"` | How often to check for updates (daily, weekly, monthly) |

---

## Step 3: Add the Dependency Review Action

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

2. Save the file.

### How this workflow works

- **Trigger:** Runs on every pull request.
- **Step 1:** Checks out the code.
- **Step 2:** The `dependency-review-action` compares dependencies in the PR against the GitHub Advisory Database. If a newly added or updated dependency has a known vulnerability, the check fails.

This acts as a gate: PRs that introduce vulnerable dependencies cannot be merged until the issue is resolved.

---

## Step 4: Verify the Dependency Graph

1. On GitHub.com, navigate to your repository.

2. Go to **Insights → Dependency graph**.

3. You should see `chalk` listed as a dependency under the **npm** ecosystem, along with any transitive dependencies.

   > 🪧 **Note:** The dependency graph updates after each push. If you just pushed, it may take a minute to reflect the latest changes.

4. Optionally, check the **Security → Dependabot** tab to see if any alerts have been created. For a healthy dependency like `chalk`, you may see no alerts — which is a good sign.

---

## Step 5: Commit and Push

1. In the VS Code left sidebar, click the **Source Control** tab.

2. Hover over each changed file and click the **+** (Stage Changes) button, or click the **+** next to **Changes** to stage everything.

    <img width="300" alt="Screenshot: Stage changes icon in VS Code Source Control" src="https://raw.githubusercontent.com/skills/getting-started-with-github-copilot/main/.github/images/staging-changes-icon.png" />

3. In the **Message** text box, type:

    ```
    Add Dependabot config and dependency review workflow
    ```

4. Click **Commit**, then click **Sync Changes** to push to GitHub.

5. After you push, the workflow validates that `dependabot.yml` and the dependency review workflow exist, then posts the next step.

---

## Verification Checklist

Before moving on, confirm each item:

- [ ] Dependabot alerts are enabled in repository settings
- [ ] Dependabot security updates are enabled in repository settings
- [ ] `.github/dependabot.yml` exists with npm ecosystem configuration
- [ ] `.github/workflows/dependency-review.yml` exists with the dependency review action
- [ ] The dependency graph shows `chalk` as a dependency
- [ ] All files are committed and pushed

---

## Troubleshooting

**Cannot access Settings → Code security:**

- You need admin access to the repository. If you used the template, you should be the owner.
- For organization-owned repos, ask an admin to enable Dependabot.

**Dependabot alerts do not appear:**

- Alerts may take a few minutes to process after enabling.
- If `chalk` has no known vulnerabilities, you will see no alerts — that is expected.
- The alerts section will populate whenever a vulnerability is published for any dependency in your graph.

**The dependency graph is empty:**

- Ensure `package.json` is committed and pushed to the `main` branch.
- The graph only updates after a push. Check that your last push succeeded.

**The dependency review workflow does not run:**

- The workflow triggers on `pull_request` events, so it will not run until you open a new PR.
- You can verify the file exists at `.github/workflows/dependency-review.yml`.

---

## How Security Fits the SDLC

Security is not a phase that happens once — it is continuous. The tools you configured in this exercise run automatically:

| Timing | What happens |
|--------|-------------|
| Every push to main | Dependency graph updates; Dependabot checks for new advisories |
| Every pull request | Dependency review action scans for vulnerable new dependencies |
| Whenever a new CVE is published | Dependabot creates an alert if your dependency is affected |
| Whenever a fix is available | Dependabot opens a PR to update the vulnerable version |

This means your project is protected without any manual effort after the initial setup.

---
