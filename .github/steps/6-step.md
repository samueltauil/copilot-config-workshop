## Workshop Complete 🎉

You have finished all five exercises and built a full suite of SDLC agents:

| Agent | SDLC Phase | What it does | Created in |
|-------|-----------|--------------|------------|
| Planner | Planning | Generates project plans and user stories | Step 1 |
| Architect | Design | Produces data schemas and file structures | Step 2 |
| Developer | Implementation | Writes code following project conventions | Step 3 |
| Tester | Testing | Creates and runs tests until they pass | Step 4 |
| Orchestrator | Full Lifecycle | Coordinates all agents end-to-end | Step 5 |

You also used these agents together to deliver a new feature from plan through tested code, covering every phase of the software development lifecycle.

### 💡 Where else can custom agents help?

The SDLC pipeline you built is just one pattern. Here are ideas for agents you can design for other scenarios:

**DevOps and Infrastructure**

| Agent idea | What it does |
|------------|-------------|
| **Deployer** | Generates CI/CD pipeline configurations, Dockerfiles, and deployment manifests |
| **Incident Responder** | Analyzes error logs and suggests fixes based on runbooks and past incidents |
| **Security Auditor** | Scans code for OWASP Top 10 vulnerabilities and suggests remediations |

**Documentation and Knowledge**

| Agent idea | What it does |
|------------|-------------|
| **API Documenter** | Reads source code and generates OpenAPI specs or API reference docs |
| **Onboarding Guide** | Answers new team member questions using the repository structure and README files |
| **Decision Recorder** | Captures architectural decisions in ADR (Architecture Decision Record) format |

**Data and Analytics**

| Agent idea | What it does |
|------------|-------------|
| **Data Modeler** | Designs database schemas, migrations, and seed data from requirements |
| **Query Optimizer** | Reviews SQL queries and suggests performance improvements |
| **Report Builder** | Generates data transformation scripts and summary reports from raw datasets |

**Team Workflows**

| Agent idea | What it does |
|------------|-------------|
| **PR Reviewer** | Reviews pull requests against team coding standards and leaves structured feedback |
| **Release Manager** | Generates changelogs, bumps versions, and drafts release notes |
| **Refactorer** | Identifies duplicated code and suggests clean abstractions |

Each agent follows the same pattern you learned: a `.agent.md` file with YAML front matter, a clear role description, structured output rules, and constraints. Combine agents with custom instructions and prompt files to build workflows tailored to your team.

## ⌨️ Activity: Finish the workshop

1. Go to the **Actions** tab in your repository on GitHub.

1. Select the **Step 6** workflow from the left sidebar.

1. Click **Run workflow** to see the final review of everything you accomplished.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If you do not see the **Step 6** workflow in the sidebar, check that the previous step completed successfully in the **Actions** tab.
- If the workflow fails, click the failed run to view the error details and submit an issue.
- You can also trigger the workflow by clicking **Run workflow** on the **main** branch.

</details>
