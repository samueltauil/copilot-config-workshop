---
agent: "agent"
description: "Review the format, quality, and learning design of a GitHub Skills exercise."
---

# Review Exercise

Perform a comprehensive review of an existing GitHub Skills exercise. Check technical correctness, content quality, and learning design.

## Review Process

### 1. General Checks

- [ ] All images can be retrieved (no broken relative paths).
- [ ] All links are working (docs, badges, exercise links).
- [ ] `.gitignore` and `LICENSE` files exist.
- [ ] Repository is configured as a template.

### 2. README Review

- [ ] Introduction does not teach new material — only provides a brief overview.
- [ ] "Copy Exercise" button URL has correct `template_owner`, `template_name`, `name`, `description`.
- [ ] Overview matches what's actually taught in the steps.
- [ ] Prerequisites are relevant and accurate.
- [ ] Time estimate is realistic (expert time × 4).
- [ ] **Psychology — ARCS**: Does the intro grab attention and explain relevance?

### 3. Step Content Review

For each step file (`.github/steps/N-*.md`):

- [ ] Theory section is concise and introduces one concept.
- [ ] Key terms link to GitHub Docs (not listed at the end).
- [ ] Activity steps are numbered correctly — nothing breaks the numbering (images, alerts).
- [ ] Troubleshooting `<details>` block is present.
- [ ] No typos or confusing wording.
- [ ] Images use relative paths from `.github/images/`.
- [ ] Nunjucks variables are properly escaped when showing Actions syntax examples.
- [ ] **Psychology — Scaffolding**: Is Step 1 the most guided? Do later steps reduce hand-holding?
- [ ] **Psychology — Cognitive Load**: Does each step introduce only one new concept?
- [ ] **Psychology — Self-Efficacy**: Can Step 1 be completed in under 3 minutes?
- [ ] **Psychology — Dual Coding**: Does each step include at least one visual element?

### 4. Workflow Review

For each workflow file (`.github/workflows/N-*.yml`):

- [ ] `workflow_dispatch` is included as a trigger.
- [ ] Event trigger matches the learner's expected activity.
- [ ] `STEP_N_FILE` env var points to the correct step file.
- [ ] Workflow name matches the enable/disable commands (`Step 1`, `Step 2`, etc.).
- [ ] All `vars` passed to `GrantBirki/comment` match what the markdown template expects.
- [ ] Grading checks use `continue-on-error: true`.
- [ ] When `check_step_work` exists, `post_next_step_content` lists it in `needs`.
- [ ] The last step calls `finish-exercise.yml`; intermediate steps do not.
- [ ] No workflow triggers on `main` without a `paths` filter (except Step 0).
- [ ] **Psychology — Feedback**: Does grading feedback name specific checks and provide corrective actions?

### 5. Review File Check

- [ ] `x-review.md` celebrates completion.
- [ ] Accomplishment recap matches what was actually taught.
- [ ] "What's next?" links are relevant and working.

### 6. Learner Walkthrough (Sanity Check)

Read through the entire exercise as if you were a learner:

- If something seems illogical → note it.
- If you don't understand something → note it.
- If something could be misinterpreted → note it.
- If you would get stuck → note it.
- If you would get bored → note it.
- If you would feel lost about what to do next → note it.

## Output Format

Organize findings into:

1. **Blockers** — Issues that would prevent the exercise from working.
2. **Improvements** — Issues that would confuse or frustrate learners.
3. **Suggestions** — Nice-to-have enhancements for better learning experience.
