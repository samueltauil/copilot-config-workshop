## Step 3: Path-Specific Instructions

Your repository contains both JavaScript and Python code. Copilot should follow Python conventions (4-space indentation, type annotations, Google-style docstrings) when helping with Python files, but those rules should not bleed into JavaScript files. Path-specific instructions let you apply targeted guidance only to files matching a particular pattern.

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

### ⌨️ Activity: Create path-specific instruction files

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

1. Save and commit your work:

    ```bash
    git add .github/instructions/python.instructions.md
    git commit -m "Add path-specific custom instructions for Python files"
    git push
    ```

1. Create a temporary file `sample.py` at the root of your repository and open it in VS Code.

1. Open Copilot Chat and ask a Python question:

    ```
    Write a function that reads a CSV file and returns a list of dictionaries, where each dictionary represents one row.
    ```

1. Click **Used n references** in the Copilot response. You should see both `.github/copilot-instructions.md` and `.github/instructions/python.instructions.md` listed.

1. Follow the full step-by-step instructions in [exercises/03-path-specific-instructions/README.md](../../exercises/03-path-specific-instructions/README.md) to complete this exercise.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Confirm the file is inside `.github/instructions/` (not `.github/` directly).
- Confirm the file name ends with `.instructions.md`.
- Confirm the YAML front matter starts on the very first line (no blank lines before the opening `---`).
- Confirm the `applyTo` value is a quoted string.

</details>
