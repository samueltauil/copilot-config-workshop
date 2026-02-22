## Step 3: Path-Specific Instructions

Your repository contains both JavaScript and Python code. Copilot should follow Python conventions (4-space indentation, type annotations, Google-style docstrings) when helping with Python files, but those rules should not bleed into JavaScript files. [Path-specific instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) let you apply targeted guidance only to files matching a particular pattern.

### 📖 Theory: How path-specific instructions work

A path-specific instruction file lives inside `.github/instructions/` and uses the `.instructions.md` suffix. It contains a YAML front matter block that specifies which file paths trigger it.

When Copilot is working on a file that matches the pattern, it combines:

1. The repository-wide instructions from `.github/copilot-instructions.md`
1. The matching path-specific instructions

Both sets of instructions are active at the same time.

Example front matter:

```yaml
---
applyTo: "**/*.py"
---
```

This pattern activates the instructions for any Python file in any subdirectory.

## ⌨️ Activity: Create a path-specific instruction file

1. Create the instructions directory if it does not exist:

    ```bash
    mkdir -p .github/instructions
    ```

1. Create a new file at `.github/instructions/python.instructions.md` with this content:

    ```markdown
    ---
    applyTo: "**/*.py"
    ---

    # Python File Instructions

    ## Style

    - Follow PEP 8 style conventions.
    - Use 4-space indentation.
    - Use double quotes for strings.
    - Add type annotations to all function parameters and return values.

    ## Error Handling

    - Use specific exception types rather than bare `except:` clauses.
    - Log exceptions using the `logging` module.

    ## Documentation

    - Add a docstring to every function and class using the Google style format.

    ## Testing

    - Use `pytest` as the test runner.
    - Prefix test function names with `test_`.
    ```

1. Save the file.

## ⌨️ Activity: Verify the instructions are loaded

1. Create a temporary Python file at the root of your repository. You can name it `sample.py`.

1. Open `sample.py` in VS Code and open Copilot Chat. Ask:

    ```
    Write a function that reads a CSV file and returns a list of
    dictionaries, where each dictionary represents one row.
    ```

1. Review the response. Because you are working in a Python file, your path-specific instructions should be active. The response should:
    - Use 4-space indentation
    - Include type annotations
    - Include a Google-style docstring
    - Use specific exception types (not bare `except:`)

1. Click the **Used n references** link at the top of the Copilot response. You should see both:
    - `.github/copilot-instructions.md` (from Step 2)
    - `.github/instructions/python.instructions.md` (the file you just created)

1. Verify path-specific instructions do not apply to non-matching files. Open `exercises/01-prompt-engineering/starter.js` and ask the same question. The references should show only `.github/copilot-instructions.md`, not the Python instructions.

## ⌨️ Activity: Commit and push your work

1. Commit and push:

    ```bash
    git add .github/instructions/python.instructions.md
    git commit -m "Add path-specific custom instructions for Python files"
    git push
    ```

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Confirm the file is inside `.github/instructions/` (not `.github/` directly).
- Confirm the file name ends with `.instructions.md`.
- Confirm the YAML front matter starts on the very first line (no blank lines before the opening `---`).
- Confirm the `applyTo` value is a quoted string.
- For a deeper walkthrough, see [exercises/03-path-specific-instructions/README.md](exercises/03-path-specific-instructions/README.md).

</details>
