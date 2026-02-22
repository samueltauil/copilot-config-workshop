---
applyTo: "**/.github/steps/*.md"
---

# Step Content File Instructions

These instructions define the format, conventions, and structure for step content files (`.github/steps/*.md`) used in GitHub Skills exercises. Step files are posted as issue comments to guide learners.

## File Location and Naming

- Step files live in `.github/steps/` within the exercise repository.
- Each step is a separate markdown file: `1-step-name.md`, `2-step-name.md`, etc.
- The final review file is named `x-review.md`.

## Step File Template

```markdown
## Step N: Step Title

_Brief story acknowledging the learner completed the previous step._ :wave:

### 📖 Theory: Concept Title

Brief explanation of the concept. Turn key terms into links to GitHub Docs
rather than listing references at the end.

### ⌨️ Activity: Activity Title

1. First instruction

   Additional context for this instruction (properly indented).

1. Second instruction

1. Additional instructions as needed

<details>
<summary>Having trouble? 🤷</summary><br/>

- Troubleshooting tip or hint
- Additional tips as needed

</details>
```

## Two Components Per Step

### 1. Theory Section

Each step introduces a **small amount** of theory. The goal is awareness, not mastery.

Writing guidelines:
- Keep theory brief and relevant to the activity that follows.
- Instead of listing references at the end, change key words into **inline links**. Most people ignore a "references" section.
- Avoid jargon or assumptions beyond the stated prerequisites.
- Follow the [GitHub Docs style guide](https://docs.github.com/en/contributing/style-guide-and-content-model/style-guide).
- Use Alerts sparingly so they don't get ignored.
- Avoid content likely to change (quotas, limits, pricing).
- Don't copy from GitHub Docs — introduce the concept and link to the docs.
- Include a **very short story element** to justify the upcoming activity (motivation hook).

**Psychology — Cognitive Load**: Present only one new concept. Front-load the key sentence. Hide supplementary details in `<details>` blocks.

**Psychology — Dual Coding**: Pair text with at least one visual element (screenshot, diagram, code example) per step.

### 2. Activity Section

Activities are hands-on practical work applying the newly learned theory.

Writing guidelines:
- Start with a `### ⌨️ Activity: <title>` header.
- Use ordered lists. Keep **1 blank line** between steps for consistent spacing.
- Use present tense and direct language: "Create a new branch", "Open the file".
- Each activity should practice **only one concept** from the theory.
- Keep instruction lists to **2 nesting levels maximum**. More nesting = split the activity.
- Mention context changes explicitly (web UI → codespace, exercise issue → working tab).
- Describe the **location** of a UI element before telling the learner to click it:
  - ✅ `In the right settings area, near the bottom, click the **Duplicate issue** button.`
  - ❌ `Click the **Duplicate issue** button at the bottom of the right settings area.`
- Use **bold** for names of things to interact with: `Click the **New issue** button.`
- Put values in backticks: `my-first-branch`.
- Use code blocks for commands or copy/paste values.
- End each activity with a troubleshooting `<details>` block.
- Each file should be self-contained.
- If a Codespace is introduced in Step 1, include an inline button to open it.

**Psychology — Scaffolding**: Step 1 has the most explicit instructions. Each subsequent step is slightly more open-ended. By the final step, the learner should work with minimal guidance.

**Psychology — Self-Efficacy**: Step 1 should be completable in under 3 minutes. Normalize mistakes in troubleshooting: "This is common" not "If you made an error".

**Psychology — ZPD**: Activities should require at least one decision from the learner, not just clicking a prescribed button.

## Nunjucks Templating

Step files support [Nunjucks](https://mozilla.github.io/nunjucks/) templating. Variables are injected by the workflow via the `vars` input on `GrantBirki/comment`.

```markdown
Hello {{ login }}!

You are working in [{{ full_repo_name }}](https://github.com/{{ full_repo_name }}).
```

**Escaping GitHub Actions syntax**: If your content includes Actions syntax examples, wrap them in raw tags:

```markdown
env:
  GITHUB_TOKEN: {% raw %}${{ secrets.GITHUB_TOKEN }}{% endraw %}
```

Prefer Nunjucks variables over text placeholders the user must replace.

## Images

- Store all images in `.github/images/`.
- Reference with relative paths: `../images/filename.png`.
- Relative links are replaced with `raw.githubusercontent` URLs when the exercise starts.
- Use HTML for size control:
  ```html
  <img width="300" alt="descriptive alt text" src="../images/my-image.png" />
  ```
- Include descriptive alt text and at least one size attribute.
- Reduce image file sizes for faster loading.
- **Psychology — Dual Coding**: Annotate screenshots to highlight the relevant UI element.

## Diagrams

- Do **NOT** create diagrams in external tools and insert as images — source documents get lost.
- Use editable `.drawio.svg` files or Mermaid syntax.

## Inline Alerts (inside ordered lists)

Standard GitHub Alert syntax breaks inside indented lists. Use these alternatives:

> 🪧 **Note:** Something extra you might want to know.

> 💡 **Tip:** This will help you with xyz.

> ❕ **Important:** This should be heavily considered.

> ⚠️ **Warning:** Be careful about this.

> ❗ **Caution:** Be really careful about this.

> ⏳ **Wait:** The following will take a moment.

> ✨ **Bonus:** Try doing this. It might be fun!

> 🧪 **Try this:** Something to experiment with.

## Long-Form Tips

For tips needing more than one line or including an image:

```html
<details>
<summary> <b> 💡 Tip:</b> Short description</summary><br/>

Additional information to explain the tip.

<img width="200" src="https://octodex.github.com/images/puddle_jumper_octodex.jpg"/>

</details>
```

## Review File (`x-review.md`)

```markdown
## Review

_Congratulations, you've completed this exercise and learned about TOPIC!_ 🎉

<img src="https://octodex.github.com/images/jetpacktocat.png" alt="celebrate" width=200 align=right>

Here's a recap of your accomplishments:

- Accomplishment 1
- Accomplishment N

### What's next?

- Follow-up Skills exercise link
- Documentation link
- Other resources
```

**Psychology — Satisfaction**: End with celebration and a tangible outcome. Recap accomplishments to reinforce what was learned. Provide clear next steps to maintain momentum.
