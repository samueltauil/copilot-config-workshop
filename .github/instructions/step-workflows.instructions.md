---
applyTo: "**/.github/workflows/*.yml"
---

# Exercise Workflow Instructions

These instructions define the patterns and conventions for GitHub Actions workflow files in GitHub Skills exercises. When something is unclear, always refer to the [exercise-template](https://github.com/skills/exercise-template) repository.

## Core Workflow Pattern

Exercises use a **step-based workflow pattern** where each step has its own workflow file. Only one step workflow is active at a time:

- `0-start-exercise.yml` — Initializes the exercise, creates the issue, enables step 1.
- `1-step.yml`, `2-step.yml`, etc. — Monitor learner progress, grade (optionally), and transition.
- Final step — Posts review content and calls `finish-exercise.yml`.

## Naming Conventions

**Workflow names** — simple and consistent:
- `name: Step 0` for the start exercise workflow
- `name: Step 1`, `name: Step 2`, etc. for step workflows

**File names** — numbered: `N-brief-summary.yml`

## Required Jobs Per Step Workflow

Each step workflow has 2 or 3 jobs:

1. `find_exercise` — Reusable workflow that finds the exercise issue.
2. `check_step_work` (optional) — Grading job that verifies learner output.
3. `post_next_step_content` — Posts feedback and transitions to the next step.

## Workflow Templates

### Step 0: Start Exercise

```yaml
name: Step 0

on:
  push:
    branches:
      - main

permissions:
  contents: write
  actions: write
  issues: write

env:
  STEP_1_FILE: ".github/steps/1-step-name.md"

jobs:
  start_exercise:
    if: |
      !github.event.repository.is_template
    name: Start Exercise
    uses: skills/exercise-toolkit/.github/workflows/start-exercise.yml@v0.8.1
    with:
      exercise-title: "Exercise Title"
      intro-message: "Brief introduction message."

  post_next_step_content:
    name: Post next step content
    runs-on: ubuntu-latest
    needs: [start_exercise]
    env:
      ISSUE_NUMBER: ${{ needs.start_exercise.outputs.issue-number }}
      ISSUE_REPOSITORY: ${{ github.repository }}

    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          ref: main

      - name: Get response templates
        uses: actions/checkout@v6
        with:
          repository: skills/exercise-toolkit
          path: exercise-toolkit
          ref: v0.8.1

      - name: Create comment - add step content
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: ${{ env.STEP_1_FILE }}
          vars: |
            login: ${{ github.actor }}
            full_repo_name: ${{ github.repository }}

      - name: Create comment - watching for progress
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: exercise-toolkit/markdown-templates/step-feedback/watching-for-progress.md

      - name: Enable next step workflow
        run: gh workflow enable "Step 1"
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Step N: Without Grading

```yaml
name: Step N

on:
  workflow_dispatch:
  # Add the appropriate event trigger for this step

permissions:
  contents: read
  actions: write
  issues: write

env:
  STEP_NEXT_FILE: ".github/steps/NEXT-step-name.md"

jobs:
  find_exercise:
    name: Find Exercise Issue
    uses: skills/exercise-toolkit/.github/workflows/find-exercise-issue.yml@v0.8.1

  post_next_step_content:
    name: Post next step content
    needs: [find_exercise]
    runs-on: ubuntu-latest
    env:
      ISSUE_REPOSITORY: ${{ github.repository }}
      ISSUE_NUMBER: ${{ needs.find_exercise.outputs.issue-number }}

    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Get response templates
        uses: actions/checkout@v6
        with:
          repository: skills/exercise-toolkit
          path: exercise-toolkit
          ref: v0.8.1

      - name: Create comment - step finished
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: exercise-toolkit/markdown-templates/step-feedback/step-finished-prepare-next-step.md
          vars: |
            next_step_number: NEXT

      - name: Create comment - add step content
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: ${{ env.STEP_NEXT_FILE }}

      - name: Create comment - watching for progress
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: exercise-toolkit/markdown-templates/step-feedback/watching-for-progress.md

      - name: Disable current workflow and enable next one
        run: |
          gh workflow disable "${{ github.workflow }}"
          gh workflow enable "Step NEXT"
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Step N: With Grading

When `check_step_work` is present, `post_next_step_content` **must** include it in `needs`.

```yaml
name: Step N

on:
  workflow_dispatch:
  # Add the appropriate event trigger

permissions:
  contents: read
  actions: write
  issues: write

env:
  STEP_NEXT_FILE: ".github/steps/NEXT-step-name.md"

jobs:
  find_exercise:
    name: Find Exercise Issue
    uses: skills/exercise-toolkit/.github/workflows/find-exercise-issue.yml@v0.8.1

  check_step_work:
    name: Check step work
    runs-on: ubuntu-latest
    needs: [find_exercise]
    env:
      ISSUE_REPOSITORY: ${{ github.repository }}
      ISSUE_NUMBER: ${{ needs.find_exercise.outputs.issue-number }}

    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Get response templates
        uses: actions/checkout@v6
        with:
          repository: skills/exercise-toolkit
          path: exercise-toolkit
          ref: v0.8.1

      - name: Find last comment
        id: find-last-comment
        uses: peter-evans/find-comment@v4
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          direction: last

      - name: Update comment - checking work
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          comment-id: ${{ steps.find-last-comment.outputs.comment-id }}
          file: exercise-toolkit/markdown-templates/step-feedback/checking-work.md
          edit-mode: replace

      # START: Check practical exercise

      - name: Check if file exists
        id: check-file-exists
        continue-on-error: true
        uses: skills/exercise-toolkit/actions/file-exists@v0.8.1
        with:
          file: TARGET_FILE

      - name: Check for keyphrase
        id: check-keyphrase
        continue-on-error: true
        uses: skills/action-keyphrase-checker@v1
        with:
          text-file: TARGET_FILE
          keyphrase: EXPECTED_PHRASE

      - name: Update comment - step results
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          comment-id: ${{ steps.find-last-comment.outputs.comment-id }}
          edit-mode: replace
          file: exercise-toolkit/markdown-templates/step-feedback/step-results-table.md
          vars: |
            step_number: N
            results_table:
              - description: "Checked if file exists"
                passed: ${{ steps.check-file-exists.outcome == 'success' }}
              - description: "Checked for keyphrase"
                passed: ${{ steps.check-keyphrase.outcome == 'success' }}

      # END: Check practical exercise

      - name: Fail job if not all checks passed
        if: contains(steps.*.outcome, 'failure')
        run: exit 1

  post_next_step_content:
    name: Post next step content
    needs: [find_exercise, check_step_work]
    runs-on: ubuntu-latest
    env:
      ISSUE_REPOSITORY: ${{ github.repository }}
      ISSUE_NUMBER: ${{ needs.find_exercise.outputs.issue-number }}

    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Get response templates
        uses: actions/checkout@v6
        with:
          repository: skills/exercise-toolkit
          path: exercise-toolkit
          ref: v0.8.1

      - name: Create comment - step finished
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: exercise-toolkit/markdown-templates/step-feedback/step-finished-prepare-next-step.md
          vars: |
            next_step_number: NEXT

      - name: Create comment - add step content
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: ${{ env.STEP_NEXT_FILE }}

      - name: Create comment - watching for progress
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: exercise-toolkit/markdown-templates/step-feedback/watching-for-progress.md

      - name: Disable current workflow and enable next one
        run: |
          gh workflow disable "${{ github.workflow }}"
          gh workflow enable "Step NEXT"
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Last Step

```yaml
name: Step N

on:
  workflow_dispatch:
  # Add the appropriate event trigger

permissions:
  contents: write
  actions: write
  issues: write

env:
  REVIEW_FILE: ".github/steps/x-review.md"

jobs:
  find_exercise:
    name: Find Exercise Issue
    uses: skills/exercise-toolkit/.github/workflows/find-exercise-issue.yml@v0.8.1

  post_review_content:
    name: Post review content
    needs: [find_exercise]
    runs-on: ubuntu-latest
    env:
      ISSUE_REPOSITORY: ${{ github.repository }}
      ISSUE_NUMBER: ${{ needs.find_exercise.outputs.issue-number }}

    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Get response templates
        uses: actions/checkout@v6
        with:
          repository: skills/exercise-toolkit
          path: exercise-toolkit
          ref: v0.8.1

      - name: Create comment - final review
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: exercise-toolkit/markdown-templates/step-feedback/lesson-review.md

      - name: Create comment - add review content
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: ${{ env.REVIEW_FILE }}

      - name: Disable current workflow
        run: gh workflow disable "${{ github.workflow }}"
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  finish_exercise:
    name: Finish Exercise
    needs: [find_exercise, post_review_content]
    uses: skills/exercise-toolkit/.github/workflows/finish-exercise.yml@v0.8.1
    with:
      issue-url: ${{ needs.find_exercise.outputs.issue-url }}
      exercise-title: "Exercise Title"
```

## Safety Rules

> **CAUTION**: These rules prevent workflows from firing when the exercise is copied.

- Do **NOT** trigger on `main` without a `paths` filter (except `0-start-exercise.yml`).
- Do **NOT** use `paths` filters for **existing** files — only new files.
- If a `main` trigger without filtering is unavoidable, add `github.run_number != 1` to `if`.
- Always include `workflow_dispatch` on every step workflow for manual testing.

## Trigger Patterns

- **Start Exercise**: `push` to `main` branch.
- **Steps**: Match the event to the learner's activity (`push`, `pull_request`, `issues`, etc.).
- Refer to the [GitHub Actions events docs](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows).

## Grading Guidelines

- Only add grading if **useful feedback** can guide the learner to correct a mistake.
- It is OK to skip grading — better to let learners progress than leave them stuck.
- All grading checks **must** use `continue-on-error: true`.
- Keep checks **independent** — do not combine them.
- Mark grading sections with `# START: Check practical exercise` / `# END: Check practical exercise`.
- The grading job **does not create new comments** — it updates the last comment in place.
- Available grading actions:
  - `skills/exercise-toolkit/actions/file-exists` — file existence check
  - `skills/action-keyphrase-checker` — keyphrase check in files
  - Custom `run` steps for anything else

**Psychology — Feedback Loops**: Grading feedback should be specific and actionable. Name exactly what was checked. On failure, tell the learner exactly what to fix and where.

## Comment Management

```yaml
# Create new comment from file
- uses: GrantBirki/comment@v2.1.1
  with:
    repository: ${{ env.ISSUE_REPOSITORY }}
    issue-number: ${{ env.ISSUE_NUMBER }}
    file: path/to/file.md
    vars: |
      variable_name: value

# Find and update the last comment
- id: find-last-comment
  uses: peter-evans/find-comment@v4
  with:
    repository: ${{ env.ISSUE_REPOSITORY }}
    issue-number: ${{ env.ISSUE_NUMBER }}
    direction: last

- uses: GrantBirki/comment@v2.1.1
  with:
    comment-id: ${{ steps.find-last-comment.outputs.comment-id }}
    edit-mode: replace
    file: path/to/update.md
```

## Workflow State Management

```yaml
- name: Disable current workflow
  run: gh workflow disable "${{ github.workflow }}"

- name: Enable next step
  run: gh workflow enable "Step N"
```

## File Organization

| Purpose | Path |
|---------|------|
| Step content | `.github/steps/N-step-name.md` |
| Step workflows | `.github/workflows/N-step-name.yml` |
| Review content | `.github/steps/x-review.md` |
| Images | `.github/images/` |
