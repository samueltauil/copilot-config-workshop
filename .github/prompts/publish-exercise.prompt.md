---
agent: "agent"
description: "Publish a GitHub Skills exercise repository to a GitHub account."
---

# Publish Exercise

Publish a GitHub Skills exercise repository to the user's GitHub account.

## Process

1. **Check for existing remote.** If the repository already has a remote, confirm with the user before proceeding.

2. **Determine the target account.**
   - Check `gh` CLI authenticated user.
   - Check environment variables.
   - Ask the user if unclear.

3. **Confirm with the user.** Ask if they want to publish to `{owner}/{exercise-name}`.

4. **Create the repository:**
   ```bash
   gh repo create {owner}/{exercise-name} --private
   ```

5. **Disable Actions** to prevent workflows from triggering during publishing:
   ```bash
   gh api -X PUT repos/{owner}/{exercise-name}/actions/permissions -F enabled=false | cat
   ```

6. **Configure repository settings:**

   Set as template:
   ```bash
   gh api -X PATCH /repos/{owner}/{exercise-name} -F is_template=true | cat
   ```

   Set description (from README intro):
   ```bash
   gh api -X PATCH /repos/{owner}/{exercise-name} -f description="{description}" | cat
   ```

7. **Push the exercise:**
   ```bash
   git push -u origin main
   ```
   If this fails, there is likely a permissions issue — ask the user to push manually.

8. **Disable all workflows, then re-enable Actions:**

   List workflows:
   ```bash
   gh api -X GET /repos/{owner}/{exercise-name}/actions/workflows | cat
   ```

   Disable each workflow:
   ```bash
   gh api -X PUT /repos/{owner}/{exercise-name}/actions/workflows/{workflow_id}/disable | cat
   ```

   Re-enable Actions (workflows stay disabled and untriggered):
   ```bash
   gh api -X PUT repos/{owner}/{exercise-name}/actions/permissions -F enabled=true | cat
   ```

9. **Confirm success.** Share the repository URL with the user.
