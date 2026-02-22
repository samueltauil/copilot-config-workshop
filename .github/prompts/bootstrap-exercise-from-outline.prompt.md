---
agent: "agent"
description: "Bootstrap a complete exercise repository from an existing outline."
---

# Bootstrap Exercise from Outline

Generate a complete GitHub Skills exercise from an existing outline. The output should be a fully functional exercise repository ready for testing.

## Prerequisites

- An exercise outline file must exist (created via `/create-exercise-outline` or manually).
- Read the outline completely before generating any files.

## Process

### 1. Repository Structure

Create all required files following the [exercise-template](https://github.com/skills/exercise-template) structure:

```
├── .github/
│   ├── images/           # Placeholder directory
│   ├── steps/
│   │   ├── 1-*.md        # One per step from outline
│   │   ├── 2-*.md
│   │   ├── ...
│   │   └── x-review.md   # Review/finish content
│   └── workflows/
│       ├── 0-start-exercise.yml
│       ├── 1-*.yml        # One per step from outline
│       ├── 2-*.yml
│       └── N-last-step.yml
├── .gitignore
├── LICENSE                # MIT
└── README.md
```

### 2. README

- Replace template placeholders with exercise-specific info from the outline.
- Update the "Copy Exercise" button URL with correct `template_owner`, `template_name`, `name`, and `description`.
- Follow [readme-exercise.instructions.md](../instructions/readme-exercise.instructions.md).

### 3. Step Content Files

For each step in the outline:

- Create `.github/steps/N-step-name.md`.
- Add the story/intro from the outline.
- Convert theory into digestible sections with inline links to references.
- Transform activities into numbered, actionable instructions.
- Add troubleshooting `<details>` blocks.
- Add image placeholders where screenshots would help: `<img alt="(description)" src="../images/(filename).png" />`.
- Follow [step-content.instructions.md](../instructions/step-content.instructions.md).

Apply scaffolding: Step 1 should have the most explicit instructions. Later steps progressively reduce guidance.

### 4. Review File

Create `.github/steps/x-review.md`:
- Celebrate completion.
- Recap accomplishments (mapped from outline).
- Provide "What's next?" links.

### 5. Workflow Files

For each step:

- Create `.github/workflows/N-step-name.yml`.
- Configure the event trigger from the outline's "Actions Trigger".
- Add grading checks from the outline's "Grading-Check" (if not `None`).
- Use the correct template: without grading, with grading, or last step.
- Follow [step-workflows.instructions.md](../instructions/step-workflows.instructions.md).

For `0-start-exercise.yml`:
- Set `exercise-title` and `intro-message` from the outline.
- Include any "On Start" automation.

For the last step workflow:
- Call `finish-exercise.yml` instead of enabling a next step.

### 6. Supporting Files

- Create `.gitignore` (OS-generated files at minimum).
- Create `LICENSE` (MIT).
- Create `.github/images/` directory (with a `.gitkeep` if needed).

### 7. Validation

Before finishing, verify:

- [ ] All workflow `STEP_N_FILE` env vars point to correct step files.
- [ ] Workflow names (`Step 1`, `Step 2`, etc.) match the enable/disable commands.
- [ ] Event triggers align with the learner's expected actions.
- [ ] All `vars` passed to `GrantBirki/comment` match what the markdown templates use.
- [ ] The last step workflow calls `finish-exercise.yml`; intermediate steps do not.
- [ ] Steps build progressively (scaffolding check).
- [ ] Step 1 is the easiest (self-efficacy check).
- [ ] Each step introduces one concept (cognitive load check).
