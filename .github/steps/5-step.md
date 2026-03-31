## Step 5: Code Review - Review a Pull Request with Copilot

_SDLC Phase: **Code Review**_

> **Why this matters:** Code review catches issues that testing alone cannot find: naming inconsistencies, missing documentation, design concerns, and potential security problems. Copilot can automate parts of this process by reviewing pull requests and leaving structured feedback, so reviewers can focus on the high-value decisions.

Your Tester Agent verified that the code works. Before merging new features, your team needs to review the code. In this step, you add a new feature to the Task Manager, ask Copilot to create a pull request, and then use Copilot code review to review the changes.

### 📖 Theory: Copilot code review

GitHub Copilot can review pull requests on GitHub.com. When a PR is opened, Copilot analyzes the changes and leaves review comments with suggestions, just like a human reviewer.

Key facts:

- Copilot code review works on pull requests in GitHub.com.
- It analyzes the diff and leaves inline comments.
- It can suggest code changes that you can accept with one click.
- It respects your custom instructions from `.github/copilot-instructions.md`.
- You can request a review from Copilot just like you request a review from a teammate.

### 📖 Theory: Why add a dependency now?

Until this point, the Task Manager used only built-in Node.js modules. Real-world projects eventually need external dependencies. Adding one now lets you practice the review workflow and sets up the next step, where you configure Dependabot to monitor your dependencies for security vulnerabilities.

## ⌨️ Activity: Add colored output with chalk

The Task Manager CLI prints plain text. Adding colored status labels makes the output more readable. This feature uses the [chalk](https://www.npmjs.com/package/chalk) npm package.

1. In Copilot Chat, select **Agent** mode and enter the following prompt:

    ```
    Add colored terminal output to the Task Manager using the chalk
    npm package. Follow these requirements:

    - Status "done" should display in green
    - Status "in-progress" should display in yellow
    - Status "todo" should display in red
    - Priority "high" should display in bold red
    - Priority "medium" should display in bold yellow
    - Priority "low" should display in dim text

    Steps:
    1. Initialize the project with npm init if package.json does not
       exist. Set "type": "module" in package.json for ES module support.
    2. Install chalk as a dependency.
    3. Create src/utils/colors.js with helper functions that wrap
       status and priority values in chalk colors.
    4. Update src/index.js to use the color helpers when displaying tasks.
    5. Run src/index.js to verify the colored output works.

    After everything works:
    6. Create a new branch called feature/colored-output.
    7. Commit all changes to that branch.
    8. Push the branch and create a pull request to main with the title
       "Add colored CLI output with chalk" and a description of changes.
    ```

1. Review the changes Copilot makes. Approve file creations and edits as prompted.

1. When Copilot finishes, verify the PR was created. You should see a link to the PR in the chat output, or you can check the repository on GitHub.

    > 🪧 **Note:** If Copilot cannot create the PR directly, you can create it manually: open the VS Code Source Control sidebar, click the **...** menu, and select **Create Pull Request**. Or navigate to the repository on GitHub and create the PR from the `feature/colored-output` branch.

## ⌨️ Activity: Review the PR with Copilot

1. Open the pull request on GitHub.com.

1. In the **Reviewers** section on the right sidebar, click the gear icon and select **Copilot** to request a code review.

    > 🪧 **Note:** If Copilot code review is not available on your repository, you can review the PR manually. Read through the diff and check that the implementation follows your project conventions (ES modules, single quotes, JSDoc comments, etc.).

1. Wait for Copilot to complete the review. It will leave a summary comment with a table of reviewed files and inline comments on the PR diff.

1. At the bottom of the review summary, click **Fix all with Copilot** to let Copilot automatically address every comment it raised. Copilot will push fix commits directly to the PR branch.

    <img width="600" alt="Screenshot: Copilot review summary with the Fix all with Copilot button" src="../../.github/images/fix-all.png" />

    > 🪧 **Note:** You can also address comments individually — click **Commit suggestion** on a single comment to apply that fix, or make the change manually and push.

1. Once all review feedback is addressed, **merge the pull request** on GitHub.

## ⌨️ Activity: Pull the merged changes

1. Back in your Codespace or VS Code, click the **branch name** in the bottom-left corner of the status bar.

    <img width="400" alt="Screenshot: Branch name in VS Code status bar" src="../../.github/images/update-main.png" />

1. In the branch picker that appears, select **main** to switch branches.

    <img width="500" alt="Screenshot: Branch picker showing main branch" src="../../.github/images/switch-main.png" />

1. Open the VS Code Source Control sidebar and click **Sync Changes** to pull the merged PR changes.

## ⌨️ Activity: Update project conventions

The project now has an external dependency. Update your custom instructions to reflect this.

1. Open `.github/copilot-instructions.md` and update the Dependencies section:

    ```markdown
    ## Dependencies

    - Use only built-in Node.js modules for core functionality.
    - The `chalk` package is approved for terminal output formatting.
    - Do not add other external dependencies without approval.
    ```

## ⌨️ Activity: Commit and push your work

1. In the VS Code left sidebar, click the **Source Control** tab.

1. Hover over each changed file and click the **+** (Stage Changes) button, or click the **+** next to **Changes** to stage everything.

    <img width="300" alt="Screenshot: Stage changes icon in VS Code Source Control" src="https://raw.githubusercontent.com/skills/getting-started-with-github-copilot/main/.github/images/staging-changes-icon.png" />

1. In the **Message** text box, type:

    ```
    Add colored output feature and update project conventions
    ```

1. Click **Commit**, then click **Sync Changes** to push to GitHub.

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If Copilot cannot run `npm init` or `npm install`, run them manually in the terminal: `npm init -y && npm pkg set type=module && npm install chalk`.
- If the branch and PR were not created automatically, create them manually via the VS Code Source Control sidebar or with `git checkout -b feature/colored-output && git add -A && git commit -m "Add colored output" && git push -u origin feature/colored-output`, then open the PR on GitHub.
- If Copilot code review is not available, review the PR yourself — the learning goal is the review workflow.
- After merging the PR, remember to switch back to `main` and pull the changes before committing the convention updates.
- For a deeper walkthrough, see [exercises/05-code-review/README.md](exercises/05-code-review/README.md).

</details>
