# Workshop Complete

You have finished all seven exercises and built a full suite of SDLC agents:

| Agent | SDLC Phase | What it does | Created in |
|-------|-----------|--------------|------------|
| Planner | Planning | Generates project plans and user stories | Exercise 01 |
| Architect | Design | Produces data schemas and file structures | Exercise 02 |
| Developer | Implementation | Writes code following project conventions | Exercise 03 |
| Tester | Testing | Creates and runs tests until they pass | Exercise 04 |
| Orchestrator | Full Lifecycle | Coordinates all agents end-to-end | Exercise 07 |

You also configured Copilot code review (Exercise 05) and Dependabot dependency security (Exercise 06) to protect your project's code quality and supply chain.

---

## Where Else Can Custom Agents Help?

The SDLC pipeline you built is just one pattern. The same building blocks (agent files, custom instructions, prompt files, and handoffs) apply to many other scenarios. Below are ideas to inspire your next set of agents.

### DevOps and Infrastructure

| Agent idea | What it does |
|------------|-------------|
| **Deployer** | Generates CI/CD pipeline configurations, Dockerfiles, and deployment manifests |
| **Incident Responder** | Analyzes error logs and suggests fixes based on runbooks and past incidents |
| **Security Auditor** | Scans code for OWASP Top 10 vulnerabilities and suggests remediations |

### Documentation and Knowledge

| Agent idea | What it does |
|------------|-------------|
| **API Documenter** | Reads source code and generates OpenAPI specs or API reference docs |
| **Onboarding Guide** | Answers new team member questions using the repository structure and README files |
| **Decision Recorder** | Captures architectural decisions in ADR (Architecture Decision Record) format |

### Data and Analytics

| Agent idea | What it does |
|------------|-------------|
| **Data Modeler** | Designs database schemas, migrations, and seed data from requirements |
| **Query Optimizer** | Reviews SQL queries and suggests performance improvements |
| **Report Builder** | Generates data transformation scripts and summary reports from raw datasets |

### Team Workflows

| Agent idea | What it does |
|------------|-------------|
| **PR Reviewer** | Reviews pull requests against team coding standards and leaves structured feedback |
| **Release Manager** | Generates changelogs, bumps versions, and drafts release notes |
| **Refactorer** | Identifies duplicated code and suggests clean abstractions |

Each agent follows the same pattern you learned: a `.agent.md` file with YAML front matter, a clear role description, structured output rules, and constraints. Combine agents with custom instructions and prompt files to build workflows tailored to your team.

---

## Building Your Own Agent: Quick Recipe

1. **Define the role.** What persona should Copilot adopt? (e.g., "You are a security auditor.")
2. **Define the output.** What sections or artifacts should the agent produce?
3. **Set constraints.** What tools, languages, or rules must the agent follow?
4. **Add custom instructions.** Use `.github/copilot-instructions.md` for project-wide conventions and `.github/instructions/*.instructions.md` for directory-level rules.
5. **Create prompt files.** Save reusable workflows as `.prompt.md` files in `.github/prompts/`.
6. **Orchestrate with handoffs.** Use the `handoffs:` front matter property to chain agents into a pipeline.

---

## Org-Level Configuration

Organizations that manage many repositories benefit from shared defaults. GitHub supports a special repository named `.github` within an organization. Files placed there serve as organization-wide defaults.

| File type | Repository-level path | Org-level path (in `.github` repository) |
|-----------|----------------------|----------------------------------------|
| Custom instructions | `.github/copilot-instructions.md` | `.github/copilot-instructions.md` |
| Path-specific instructions | `.github/instructions/*.instructions.md` | `.github/instructions/*.instructions.md` |
| Custom agents | `.github/agents/*.agent.md` | `.github/agents/*.agent.md` in org `.github-private` repo |
| Prompt files | `.github/prompts/*.prompt.md` | `.github/prompts/*.prompt.md` |

Repository-level files always override org-level files. Use the org level for universal rules (security policies, documentation standards) and the repository level for project-specific conventions.

---

## Further Reading

- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [Adding repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)
- [VS Code Docs: Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [GitHub Docs: Custom Agents Configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)
- [Managing Copilot policies for your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization)
- [Awesome Copilot](https://github.com/github/awesome-copilot) - Community collection of custom agents, prompts, and instructions
