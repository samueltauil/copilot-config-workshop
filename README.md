# GitHub Copilot Configuration Workshop

_Learn to configure and use GitHub Copilot effectively through hands-on exercises._

---

**Who is this for:** Developers with a GitHub Copilot subscription who want to get the most out of Copilot through proper configuration and prompting techniques.

**What you will learn:**
- How to write effective prompts for GitHub Copilot
- How to create repository-wide custom instructions using `copilot-instructions.md`
- How to create path-specific instruction files
- How to use Copilot Chat participants, slash commands, and chat variables
- How to create agent instruction files (`AGENTS.md`)

**Prerequisites:**
- An active [GitHub Copilot subscription](https://github.com/features/copilot) (Individual, Business, or Enterprise)
- [Visual Studio Code](https://code.visualstudio.com/) with the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) installed
- Basic familiarity with Git and GitHub

**How long:** Each exercise takes approximately 20-30 minutes. The full workshop takes about 2-3 hours.

---

## Workshop Overview

This workshop is structured as five progressive exercises. Each exercise builds on the previous one and includes clear step-by-step instructions you can follow exactly as written.

| Exercise | Topic | Duration |
|----------|-------|----------|
| [Exercise 1](./exercises/01-prompt-engineering/README.md) | Prompt Engineering for GitHub Copilot | ~30 min |
| [Exercise 2](./exercises/02-custom-instructions/README.md) | Repository-Wide Custom Instructions | ~25 min |
| [Exercise 3](./exercises/03-path-specific-instructions/README.md) | Path-Specific Instructions | ~20 min |
| [Exercise 4](./exercises/04-copilot-chat-skills/README.md) | Copilot Chat: Participants, Commands, and Variables | ~30 min |
| [Exercise 5](./exercises/05-agent-files/README.md) | Agent Instruction Files | ~20 min |

---

## How to Use This Workshop

### Option A: Work directly in this repository

1. Fork this repository to your own GitHub account.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/<your-username>/copilot-config-workshop.git
   cd copilot-config-workshop
   ```
3. Open the repository in Visual Studio Code:
   ```bash
   code .
   ```
4. Follow each exercise in order, starting with [Exercise 1](./exercises/01-prompt-engineering/README.md).

### Option B: Use the slide deck

A self-contained slide deck is available at [`slides/index.html`](./slides/index.html). Open this file in any web browser to view the workshop content in presentation format. No internet connection or additional tools are required.

---

## Repository Structure

This repository itself demonstrates several Copilot configuration techniques:

- **`.github/copilot-instructions.md`** - Repository-wide custom instructions (Exercise 2)
- **`.github/instructions/markdown.instructions.md`** - Path-specific instructions for Markdown files (Exercise 3)
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