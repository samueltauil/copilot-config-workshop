# Exercise 3: Path-Specific Instructions

**Learning objectives:**
- Understand the difference between repository-wide and path-specific instructions
- Create a path-specific instruction file that applies only to certain file types
- Verify that path-specific instructions are combined with repository-wide instructions

**Duration:** ~20 minutes

**Prerequisites:** Complete [Exercise 2](../02-custom-instructions/README.md) before this exercise, as it introduces the `.github` directory structure.

---

## Background

Path-specific custom instructions apply only when Copilot is working with files that match a specified path pattern. This lets you give Copilot targeted guidance for specific parts of your project without cluttering your repository-wide instructions.

For example, you might want Copilot to follow specific rules for:
- Python files in a data science subdirectory
- SQL migration files
- React component files
- Test files

Path-specific instruction files use the `.instructions.md` suffix and live inside or below `.github/instructions/` in your repository. For the full reference, see [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot).

---

## How Path-Specific Instructions Work

A path-specific instruction file contains a YAML front matter block at the top that specifies which file paths it applies to. When Copilot is working on a file that matches the pattern, it combines:

1. The repository-wide instructions from `.github/copilot-instructions.md` (if it exists)
2. The matching path-specific instructions

Both sets of instructions are active at the same time.

---

## Step 1: Create the Instructions Directory

1. In VS Code, create a new directory at:
   ```
   .github/instructions/
   ```
   You can do this in the Explorer panel (right-click `.github`, select **New Folder** and type `instructions`), or run:
   ```bash
   mkdir .github/instructions
   ```

---

## Step 2: Create a Path-Specific Instruction File

In this step, you will create an instruction file that applies to Python files.

1. Create a new file at:
   ```
   .github/instructions/python.instructions.md
   ```

2. Every path-specific instruction file must start with a YAML front matter block. The `applyTo` field specifies the glob pattern that determines which files trigger these instructions.

   Copy the following content into the file:

   ```markdown
   ---
   applyTo: "**/*.py"
   ---

   # Python File Instructions

   ## Style

   - Follow PEP 8 style conventions.
   - Use 4-space indentation (not 2 spaces, which is used in other parts of this project).
   - Use double quotes for strings, not single quotes.
   - Add type annotations to all function parameters and return values.

   ## Imports

   - Group imports in the following order: standard library, third-party, local modules.
   - Separate each group with a blank line.
   - Use absolute imports, not relative imports.

   ## Error Handling

   - Use specific exception types rather than bare `except:` clauses.
   - Log exceptions using the `logging` module.

   ## Documentation

   - Add a docstring to every function and class using the Google style format.

   ## Testing

   - Use `pytest` as the test runner.
   - Prefix test function names with `test_`.
   ```

3. Save the file.

   > **Screenshot reference:** The `.github/instructions/` folder appears in the VS Code Explorer panel containing the file `python.instructions.md`. The file is open and shows the YAML front matter (`---` block) at the top followed by Markdown content.

---

## Step 3: Verify the Path-Specific Instructions

**Step 3.1 - Create a Python file to work with:**

1. Create a new file in the repository root:
   ```bash
   touch sample.py
   ```
2. Open `sample.py` in VS Code.

**Step 3.2 - Open Copilot Chat and ask a question:**

1. Open Copilot Chat in VS Code.
2. Make sure `sample.py` is the active file in the editor (click on it in the Explorer panel).
3. Ask:
   ```
   Write a function that reads a CSV file and returns a list of dictionaries, where each dictionary represents one row.
   ```

4. Review the response. Because you are working in a Python file, your path-specific instructions should be active. The response should:
   - Use 4-space indentation
   - Include type annotations
   - Include a Google-style docstring
   - Use specific exception types (not bare `except:`)

**Step 3.3 - Confirm both instruction sets are loaded:**

1. Look at the **Used n references** link at the top of the Copilot response.
2. Click it to expand the reference list.
3. You should see both:
   - `.github/copilot-instructions.md` (the repository-wide instructions from Exercise 2)
   - `.github/instructions/python.instructions.md` (the path-specific instructions)

   > **Screenshot reference:** The expanded references list shows two files: `.github/copilot-instructions.md` and `.github/instructions/python.instructions.md`. This confirms that both instruction sets are applied simultaneously.

---

## Step 4: Test with a Non-Matching File

Confirm that path-specific instructions are not applied when working with a file that does not match the pattern.

1. Open `exercises/01-prompt-engineering/starter.js` in VS Code (this is a JavaScript file, so `**/*.py` does not match).
2. Open Copilot Chat and ask:
   ```
   Write a function that reads a CSV file and returns an array of objects, one per row.
   ```
3. Look at the **Used n references** link. You should see only `.github/copilot-instructions.md` (the repository-wide instructions), not `python.instructions.md`.

---

## Step 5: Create a Second Path-Specific Instruction File

Practice creating another instruction file with a different pattern.

1. Create a new file at:
   ```
   .github/instructions/tests.instructions.md
   ```

2. Copy the following content into it:
   ```markdown
   ---
   applyTo: "**/*.test.js"
   ---

   # Test File Instructions

   ## Testing Approach

   - Each test file must import only the module it tests and the assertion library.
   - Use `describe` blocks to group related tests.
   - Each `it` or `test` block must test exactly one behavior.
   - Use descriptive test names that start with a verb (e.g., "returns an error when input is null").

   ## Assertions

   - Use the built-in Node.js `assert` module (not a third-party library).
   - Prefer `assert.strictEqual` over `assert.equal`.
   - For objects and arrays, use `assert.deepStrictEqual`.
   ```

3. Save the file.

4. Verify it works by creating `starter.test.js` temporarily, opening it, and checking that the reference list in a Copilot Chat response includes `tests.instructions.md`.

---

## Step 6: Review the Example File

This repository includes a working example of a path-specific instruction file:

```
exercises/03-path-specific-instructions/example.instructions.md
```

Open and review it to see another example with inline comments explaining each section.

---

## Step 7: Commit Your Work

```bash
git add .github/instructions/
git commit -m "Add path-specific custom instructions for Python and test files"
git push
```

---

## Troubleshooting

**Path-specific instructions are not being loaded:**
- Confirm the file is inside `.github/instructions/` (not inside `.github/` directly).
- Confirm the file name ends with `.instructions.md`.
- Confirm the YAML front matter block starts on the very first line of the file (no blank lines before the opening `---`).
- Confirm the `applyTo` pattern matches the file you have open. Use standard glob syntax (`**/*.py` matches any `.py` file in any subdirectory).

**The YAML front matter syntax is incorrect:**
- The block must begin with three hyphens on their own line: `---`
- It must end with three hyphens on their own line: `---`
- The `applyTo` value must be a quoted string.

---

## Summary

You created path-specific instruction files that apply only to files matching a glob pattern. Key points:

- Files live inside `.github/instructions/` and end with `.instructions.md`.
- Each file starts with a YAML front matter block containing an `applyTo` field.
- When a matching file is open, both repository-wide and path-specific instructions are active.
- When no file matches, only repository-wide instructions are active.

---

## Next Steps

Proceed to [Exercise 4: Copilot Chat Participants, Commands, and Variables](../04-copilot-chat-skills/README.md).
