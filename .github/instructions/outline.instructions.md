---
applyTo: "**/*outline*"
---

# Exercise Outline Instructions

These instructions define the format and conventions for creating an outline document for a GitHub Skills exercise.

The outline is the **most important artifact** — every minute invested here saves hours on development. It should provide a concise, clear, high-level overview without excessive detail. Focus only on the requested topic. Do not teach additional content outside the primary skill.

> Example: If the exercise is about GitHub Packages, do not teach GitHub Actions automation — that's a separate exercise.

## Outline Structure

```markdown
# Logistics

- **Exercise Title:** Human-friendly title
- **Repo URL:** Tentative repository URL
- **Experience Level**: Beginner | Intermediate | Advanced
- **Recommended Grouping**: See groups on https://learn.github.com/skills or suggest a new one

### Relationships to other exercises

- **Previous Exercise:** Existing/future exercise this continues from
- **Next Exercise:** Existing/future exercise this leads to

---

# Outline

## (optional) Story Plot

A narrative that helps learners engage with the practical application of the skill.

## README

**Title:** Exercise title

Brief introduction (max 2 sentences).

### Overview

1. Learning objective / step summary
1. ...

### What you will build

Description of the tangible outcome (max 3 sentences).

### Prerequisites

- Required prior knowledge
- Required prior exercises

### (optional) On Start

Automation for the start-exercise workflow (nothing manual).

## Step 1 - Step Title

### (optional) Story

Scenario or context for this step.

### Theory

Key topic to be taught (keep concise).

- Background knowledge for context
- Key concepts

### References

- Official documentation links (1–3)

### Activity: Activity Title

1. High-level step-by-step instructions
1. ...

### Transition

- **Actions Trigger:** GitHub Actions event trigger
- **Grading-Check:** What to verify (or `None`)

## Step 2 - Step Title

...

## Review

Short recap (max 2 sentences).

- Skills learned

### What's next?

- Links to docs, exercises, resources
```

## Step Design Guidelines

### Theory
- Provide just **enough** background to understand the activity. Aim for awareness, not mastery.
- Provide real content from the docs, not generic descriptions.
- Use lists, tables, and diagrams to make it visually appealing.
- **Cognitive Load**: introduce only one new concept per step.

### References
- Include 1–3 official documentation links per step.
- Only use official GitHub sources:
  - GitHub Documentation (https://docs.github.com)
  - GitHub Learn (https://learn.github.com)
  - GitHub Blog (https://github.blog)
  - GitHub Changelog (https://github.blog/changelog)
  - VS Code Documentation (https://code.visualstudio.com/docs/)

### Activity
- Use action-oriented titles that describe the outcome.
- List high-level tasks, not granular click-by-click instructions (those go in the actual step file).
- Each activity should practice only **one concept** from the theory.

### Transition
- **Actions Trigger**: Select the event that naturally results from the learner's activity:

| Situation | Trigger |
|-----------|---------|
| Learner created or updated a file | `push` |
| Learner is submitting changes for review | `pull_request` |
| Learner published a package | `registry_package` |
| Learner built a GitHub Pages site | `page_build` |
| Learner created or updated an issue | `issues` |
| Codespace postCreateCommand sends an API call | `repository_dispatch` |
| A script sends an API call when finished | `repository_dispatch` |
| Learner provided a URL (codespace, resource) | `issue_comment` |
| Learner is answering a question | `issue_comment` |
| No other natural option | `issue_comment` |
| Learner created discussions | `discussion` |
| Learner made and ran a new workflow | `workflow_run` |
| Learner created a release | `release` |

- **Grading-Check**: Briefly describe what will be verified. Use `None` if no feedback is necessary.

## Worked Example

```markdown
## Step 1 - Setting Up Copilot Instructions

### Story

You need to establish consistent coding standards for your team and ensure Copilot follows your conventions.

### Theory

Repository custom instructions let you give Copilot persistent context about your project. By creating a `.github/copilot-instructions.md` file, every Copilot suggestion aligns with your standards automatically.

### References

- https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot

### Activity: Create Repository Custom Instructions

1. Create `.github/copilot-instructions.md`
1. Add coding standards and guidelines
1. Test by prompting Copilot about a file

### Transition

- **Actions Trigger:** [`push`](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#push)
- **Grading-Check:** Verify `.github/copilot-instructions.md` exists with `file-exists` action. Check for keyphrase with `action-keyphrase-checker`.
```

## Psychology Checklist for Outlines

- [ ] Does Step 1 provide a quick, confidence-building win?
- [ ] Does each step build on the previous one (scaffolding)?
- [ ] Is the story/context motivating and relevant (ARCS: Attention + Relevance)?
- [ ] Can the exercise be completed in 30–45 minutes?
- [ ] Does each step introduce exactly one new concept (cognitive load)?
