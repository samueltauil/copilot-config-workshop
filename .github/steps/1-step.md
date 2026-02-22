## Step 1: Prompt Engineering for GitHub Copilot

Your team is adopting GitHub Copilot, and the results have been inconsistent. Some requests produce exactly what you need; others produce generic code that misses the mark. The difference comes down to how you phrase your prompts. In this step, you practice six [prompt engineering](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat) strategies that consistently improve Copilot's responses.

### 📖 Theory: What makes a good prompt?

A prompt is a request you make to GitHub Copilot. The quality of Copilot's response depends heavily on how you write your prompt. Six strategies consistently improve results.

| Strategy | Description |
|----------|-------------|
| Start general, then get specific | State the goal first, then add constraints |
| Give examples | Show example inputs and outputs |
| Break tasks into steps | Compose complex features from smaller prompts |
| Avoid ambiguity | Name functions and files explicitly |
| Indicate relevant code | Open only relevant files; use `#file` to attach context |
| Experiment and iterate | Follow up in the same conversation to refine results |

## ⌨️ Activity: Set up your environment

1. Open this repository in a **GitHub Codespace** by clicking **Code > Codespaces > Create codespace on main** on the repository page. Alternatively, clone it locally and open it in VS Code.

1. Verify Copilot is active: look for the Copilot icon in the VS Code status bar at the bottom of the screen. A checkmark or the Copilot logo indicates it is active.

1. Open Copilot Chat by clicking the chat icon in the sidebar, or press `Ctrl+Alt+I` (Windows/Linux) or `Cmd+Shift+I` (macOS).

1. Open the starter file: `exercises/01-prompt-engineering/starter.js`

## ⌨️ Activity: Practice the six prompt strategies

You will copy each generated function into `starter.js` as you go. At the end, you will commit and push the file.

### Strategy 1: Start general, then get specific

1. In Copilot Chat, type a vague prompt:

    ```
    Write a function to validate input
    ```

1. Read the response. Notice the assumptions Copilot made. Now try a specific prompt:

    ```
    Write a JavaScript function called `validateEmail` that accepts a single
    string argument called `email`. Return `true` if the string matches
    standard email format (e.g., user@domain.com). Return `false` otherwise.
    Do not use any external libraries.
    ```

1. Compare the two responses. The specific prompt produces a precise, usable function. Copy the `validateEmail` function into `starter.js`.

### Strategy 2: Give examples

1. Provide example inputs and outputs so Copilot has a clear target:

    ```
    Write a JavaScript function called `formatPhoneNumber` that formats
    a phone number.

    Examples:
    - Input: "5551234567" → Output: "(555) 123-4567"
    - Input: "15551234567" → Output: "(555) 123-4567"
    - Input: "555-123-4567" → Output: "(555) 123-4567"

    The function should handle these three input formats and always return
    the same formatted output.
    ```

1. Copy the generated function into `starter.js`. Add test calls at the bottom of the file and run it:

    ```bash
    node exercises/01-prompt-engineering/starter.js
    ```

1. Confirm all three inputs produce `(555) 123-4567`.

### Strategy 3: Break tasks into steps

1. Build a data processing pipeline in three small prompts instead of one large one. First:

    ```
    Write a JavaScript function called `readCSVLine` that accepts a
    comma-separated string and returns an array of trimmed string values.
    Example: "Alice, 30 , engineer" → ["Alice", "30", "engineer"]
    ```

1. Copy the result into `starter.js`. Then ask:

    ```
    Write a JavaScript function called `parseEmployee` that accepts an
    array of three strings [name, age, role] and returns an object with
    properties `name` (string), `age` (number), and `role` (string).
    ```

1. Copy the result into `starter.js`. Then combine them:

    ```
    Write a JavaScript function called `processCSV` that accepts an array
    of comma-separated strings. Use the `readCSVLine` and `parseEmployee`
    functions to return an array of employee objects.
    ```

1. Copy the result into `starter.js` and verify:

    ```javascript
    const lines = ["Alice, 30, engineer", "Bob, 25, designer"];
    console.log(processCSV(lines));
    ```

### Strategy 4: Avoid ambiguity

1. Try a vague prompt:

    ```
    What does this do?
    ```

    Copilot does not know what "this" refers to. Now select the `processCSV` function in `starter.js` and try:

    ```
    Explain what the `processCSV` function in my current file does,
    step by step.
    ```

    The explicit reference produces a clear, accurate explanation.

### Strategy 5: Indicate relevant code

1. Close all other files so only `starter.js` is open. Use the `#file` variable to attach it as context:

    ```
    #file:starter.js Write a complete test file for all functions in this
    file. Use the built-in Node.js assert module. Print a summary of passed
    and failed tests.
    ```

1. Save the generated tests to `exercises/01-prompt-engineering/starter.test.js`.

1. Run the tests:

    ```bash
    node exercises/01-prompt-engineering/starter.test.js
    ```

1. If any tests fail, select the error output and ask Copilot to fix it. Run again until all tests pass.

### Strategy 6: Experiment and iterate

1. Ask Copilot to sort employees:

    ```
    Write a JavaScript function called `sortEmployees` that sorts an array
    of employee objects by age ascending. If two employees have the same age,
    sort them alphabetically by name.
    ```

1. If the result does not handle the tie-breaking case, follow up in the same conversation:

    ```
    Update the function to handle the tie-breaking case where two employees
    have the same age.
    ```

1. Copy the final function into `starter.js`.

## ⌨️ Activity: Commit and push your work

1. Save all changes to `starter.js` and `starter.test.js`.

1. Commit and push:

    ```bash
    git add exercises/01-prompt-engineering/
    git commit -m "Complete prompt engineering exercises"
    git push
    ```

1. After you push, the workflow checks your work and posts the next step.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure the GitHub Copilot extension is installed and you are signed in to GitHub in VS Code.
- The Copilot icon appears in the VS Code status bar at the bottom of the screen. A checkmark or logo indicates it is active.
- If Copilot does not respond, try closing and reopening the Chat panel.
- For a deeper walkthrough of each strategy, see [exercises/01-prompt-engineering/README.md](exercises/01-prompt-engineering/README.md).

</details>
