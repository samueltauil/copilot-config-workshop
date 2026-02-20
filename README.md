# GitHub Copilot Configuration Workshop

_Learn to configure and use GitHub Copilot effectively through hands-on exercises._

## Welcome

- **Who is this for**: Developers with a GitHub Copilot subscription who want to get the most out of Copilot through proper configuration and prompting techniques.

- **What you'll learn**:
  - How to write effective prompts for GitHub Copilot
  - How to create repository-wide custom instructions using `copilot-instructions.md`
  - How to create path-specific instruction files
  - How to use Copilot Chat participants, slash commands, and chat variables
  - How to create agent instruction files (`AGENTS.md`)
  - How to manage Copilot configuration files at the organization level

- **What you'll build**: A complete set of Copilot configuration files for a sample repository, including custom instructions, path-specific instructions, and an agent instruction file.

- **Prerequisites**:
  - An active [GitHub Copilot subscription](https://github.com/features/copilot) (Individual, Business, or Enterprise)
  - [Visual Studio Code](https://code.visualstudio.com/) with the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) installed
  - Basic familiarity with Git and GitHub

- **How long**: Each exercise takes approximately 20-30 minutes. The full workshop takes about 2.5-3 hours.

In this exercise, you will:

1. Apply prompt engineering strategies to write more effective Copilot prompts
1. Create a `copilot-instructions.md` file to give Copilot persistent project context
1. Create path-specific instruction files for targeted guidance
1. Use Copilot Chat participants, slash commands, and chat variables
1. Create `AGENTS.md` files to guide AI coding agents
1. Learn best practices for managing Copilot configuration at the organization level

### How to start this exercise

Copy the exercise to your account, then give GitHub about 20 seconds to prepare the first step, then refresh the page.

[![Copy Exercise](https://img.shields.io/badge/Copy%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/new?template_owner=samueltauil&template_name=copilot-config-workshop&owner=%40me&name=copilot-config-workshop&description=Exercise:+GitHub+Copilot+Configuration+Workshop&visibility=public)

<details>
<summary>Having trouble? 🤷</summary><br/>

When copying the exercise, use these settings:

- For owner, choose your personal account or an organization to host the repository.
- Create a public repository, since private repositories use Actions minutes.

If the exercise is not ready in 20 seconds, check the [Actions](../../actions) tab.

- Check to see if a job is running. Sometimes it takes a bit longer.
- If the page shows a failed job, submit an issue.

</details>

---

## Workshop Overview

This workshop is structured as six progressive exercises. Each exercise builds on the previous one and includes clear step-by-step instructions you can follow exactly as written.

| Exercise | Topic | Duration |
|----------|-------|----------|
| [Exercise 1](./exercises/01-prompt-engineering/README.md) | Prompt Engineering for GitHub Copilot | ~30 min |
| [Exercise 2](./exercises/02-custom-instructions/README.md) | Repository-Wide Custom Instructions | ~25 min |
| [Exercise 3](./exercises/03-path-specific-instructions/README.md) | Path-Specific Instructions | ~20 min |
| [Exercise 4](./exercises/04-copilot-chat-skills/README.md) | Copilot Chat: Participants, Commands, and Variables | ~30 min |
| [Exercise 5](./exercises/05-agent-files/README.md) | Agent Instruction Files | ~20 min |
| [Exercise 6](./exercises/06-org-level-best-practices/README.md) | Org-Level Best Practices | ~25 min |

---

## How to Use This Workshop

### Option A: Use the GitHub Skills framework (recommended)

1. Click the **Copy Exercise** button above to create your own copy of this repository.
1. Wait about 20 seconds for the first step to be posted as a GitHub Issue in your copy.
1. Refresh the page and follow the issue for step-by-step instructions.

The GitHub Skills framework delivers each step as an issue comment and automatically checks your work before advancing to the next step.

### Option B: Work directly in a local clone

1. Fork this repository to your own GitHub account.
1. Clone your fork locally:
   ```bash
   git clone https://github.com/<your-username>/copilot-config-workshop.git
   cd copilot-config-workshop
   ```
1. Open the repository in Visual Studio Code:
   ```bash
   code .
   ```
1. Follow each exercise in order, starting with [Exercise 1](./exercises/01-prompt-engineering/README.md).

### Option C: Use the slide deck

A self-contained slide deck is available at [`slides/index.html`](./slides/index.html). Open this file in any web browser to view the workshop content in presentation format. No internet connection or additional tools are required.

---

## Repository Structure

This repository itself demonstrates several Copilot configuration techniques:

- **`.github/copilot-instructions.md`** - Repository-wide custom instructions (Exercise 2)
- **`.github/instructions/markdown.instructions.md`** - Path-specific instructions for Markdown files (Exercise 3)
- **`.github/steps/`** - Step content files for the GitHub Skills framework
- **`.github/workflows/`** - GitHub Actions workflows that gate step progression
- **`AGENTS.md`** - Agent instruction file for AI coding agents (Exercise 5)

---

## Official Documentation References

All exercises are based exclusively on official GitHub documentation:

- [About GitHub Copilot](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)
- [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)
- [Adding repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)
- [Asking Copilot questions in your IDE](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)
- [GitHub Copilot Chat cheat sheet](https://docs.github.com/en/copilot/using-github-copilot/github-copilot-chat-cheat-sheet)
- [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)

---

## License

This workshop is licensed under the [MIT License](./LICENSE).