---
agent: "agent"
description: "Create a structured exercise outline for a GitHub Skills exercise."
---

# Create Exercise Outline

Your task is to create a new exercise outline for a GitHub Skills exercise based on the information provided by the user. If critical information is missing, ask for it before proceeding.

## Process

1. **Understand the topic.** Clarify the primary skill to be taught, the target audience, and the experience level.

2. **Research the topic.** Search for relevant official GitHub documentation that can support the outline's theory and reference sections. Only use official sources (docs.github.com, learn.github.com, github.blog, code.visualstudio.com/docs).

3. **Create the outline file.** Follow the structure defined in the [outline instructions](../instructions/outline.instructions.md).
   - Name the file `{exercise-name}-outline.md`.
   - Save it in the current working directory or where the user specifies.

4. **Fill out each section:**
   - **Logistics**: Title, experience level, recommended grouping, relationships to other exercises.
   - **Story** (optional): A motivating narrative.
   - **README summary**: Title, introduction, overview, what you'll build, prerequisites.
   - **Steps (3–5)**: For each step, provide theory, references, activity, and transition (trigger + grading-check).
   - **Review**: Recap and next steps.

5. **Apply learning psychology:**
   - Sequence steps from easy to challenging (scaffolding).
   - Make Step 1 a quick confidence-builder (self-efficacy).
   - Ensure each step introduces exactly one new concept (cognitive load).
   - Connect activities to real-world value (intrinsic motivation).
   - Include a curiosity hook in the story/intro (attention).

6. **Validate the outline:**
   - Each step builds on previous knowledge.
   - Activities naturally produce the selected trigger events.
   - The exercise can be completed in 30–45 minutes.
   - Grading checks are feasible with available actions.
