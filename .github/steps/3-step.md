## Step 3: Path-Specific Instructions &mdash; Build a Developer Agent

_SDLC Phase: **Implementation**_

Your Architect Agent produced a schema and file structure. Now you turn that design into working code. In this step you create [path-specific instruction files](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) that give Copilot different coding conventions for different parts of the codebase, then build a **Developer Agent** that generates the implementation.

### 📖 Theory: How path-specific instructions work

Path-specific instruction files live in `.github/instructions/` and use the `.instructions.md` suffix. A YAML front matter block specifies which files trigger them via `applyTo`.

When Copilot works on a matching file, it combines:

1. The repository-wide instructions from `.github/copilot-instructions.md`
1. All matching path-specific instructions

Both sets are active at the same time.

```yaml
---
applyTo: "src/models/**"
---
```

## ⌨️ Activity: Create path-specific instruction files

1. Create the instructions directory:

    ```bash
    mkdir -p .github/instructions
    ```

1. Create `.github/instructions/models.instructions.md`:

    ```markdown
    ---
    applyTo: "src/models/**"
    ---

    # Model File Instructions

    - Export a single class per file.
    - Validate all constructor arguments. Throw a `TypeError` with a
      descriptive message for invalid inputs.
    - Include a `toJSON()` method that returns a plain object.
    - Generate unique IDs using `crypto.randomUUID()`.
    - Add JSDoc comments to the class and every public method.
    ```

1. Create `.github/instructions/services.instructions.md`:

    ```markdown
    ---
    applyTo: "src/services/**"
    ---

    # Service File Instructions

    - Export functions, not classes.
    - Every function that modifies data must return the modified object.
    - Return copies of data, never direct references to internal state.
    - Throw descriptive errors for "not found" and "invalid input" cases.
    - Keep functions small. Each function handles one operation.
    ```

1. Create `.github/instructions/utils.instructions.md`:

    ```markdown
    ---
    applyTo: "src/utils/**"
    ---

    # Utility File Instructions

    - Export pure functions only. No side effects.
    - Every function must validate its inputs and throw a `TypeError`
      for invalid arguments.
    - Include at least two usage examples in each JSDoc comment.
    ```

1. Save all three files.

## ⌨️ Activity: Create the Developer Agent

1. Create a new file at `.github/agents/developer.agent.md`:

    ```markdown
    ---
    name: developer
    description: Reads a schema document and generates implementation code following path-specific conventions
    ---

    You are a software developer. Given a data schema and file structure
    document, you generate working implementation code.

    ## Process

    1. Read the schema document the user provides.
    2. Create each file described in the schema's file structure.
    3. Follow the conventions in `.github/copilot-instructions.md`
       and any matching path-specific instruction files in
       `.github/instructions/`.
    4. After generating all files, run the entry point with Node.js
       to verify there are no syntax or runtime errors.
    5. Fix any errors and re-run until the code executes without issues.

    ## Rules

    - Use only built-in Node.js modules.
    - Place source files under `src/` following the structure in the schema.
    - Every file must use ES module syntax (`import`/`export`).
    - Add `console.log` calls in the entry point to demonstrate each feature.
    ```

1. Save the file.

## ⌨️ Activity: Use the Developer Agent to implement the Task Manager

1. In Copilot Chat, select **developer** from the agent dropdown.

1. Type:

    ```
    Read #file:docs/schema.md and implement the Task Manager application.

    Create these files:
    1. src/models/task.js — Task class with validation
    2. src/services/taskService.js — CRUD operations for tasks
    3. src/utils/validators.js — input validation helpers
    4. src/index.js — entry point that demonstrates all features

    After creating all files, run src/index.js with Node.js and fix
    any errors.
    ```

1. Approve each file creation when prompted. Watch the agent run the code and iterate on errors.

1. When the agent finishes, verify the output:

    ```bash
    node src/index.js
    ```

## ⌨️ Activity: Commit and push your work

1. Commit and push:

    ```bash
    git add .github/instructions/ .github/agents/ src/
    git commit -m "Add path-specific instructions and Developer Agent with implementation"
    git push
    ```

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Confirm instruction files are inside `.github/instructions/` and end with `.instructions.md`.
- The YAML front matter must start on the very first line (no blank lines before `---`).
- The `applyTo` value must be a quoted string.
- If the developer agent fails to run the code, check for ES module issues. You may need to add `"type": "module"` to a `package.json` or use `.mjs` extensions.
- For a deeper walkthrough, see [exercises/03-path-specific-instructions/README.md](exercises/03-path-specific-instructions/README.md).

</details>
