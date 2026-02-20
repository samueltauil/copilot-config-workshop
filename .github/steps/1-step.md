## Step 1: Prompt Engineering for GitHub Copilot

Effective prompts are the foundation of productive Copilot interactions. In this step, you practice six prompt engineering strategies from the official GitHub documentation.

### 📖 Theory: What makes a good prompt?

A prompt is a request you make to GitHub Copilot. The quality of Copilot's response depends heavily on how you write your prompt. Six strategies consistently improve results:

| Strategy | Description |
|----------|-------------|
| Start general, then get specific | State the goal first, then add constraints |
| Give examples | Show example inputs and outputs |
| Break tasks into steps | Compose complex features from smaller prompts |
| Avoid ambiguity | Name functions and files explicitly |
| Indicate relevant code | Open only relevant files; use `#file` to attach context |
| Experiment and iterate | Follow up in the same conversation to refine results |

### ⌨️ Activity: Practice prompt strategies

1. Open Visual Studio Code and open this repository.

1. Open the starter file: `exercises/01-prompt-engineering/starter.js`

1. Open Copilot Chat (click the chat icon in the sidebar, or press `Ctrl+Alt+I` on Windows/Linux, `Cmd+Shift+I` on macOS).

1. Try a vague prompt first:

    ```
    Write a function to validate input
    ```

1. Then try a specific prompt and compare:

    ```
    Write a JavaScript function that validates an email address.

    The function should:
    - Accept a single string argument called `email`
    - Return `true` if the string matches standard email format (e.g., user@domain.com)
    - Return `false` otherwise
    - Not use any external libraries
    ```

1. Practice the "give examples" strategy. Ask Copilot:

    ```
    Write a JavaScript function that formats a phone number.

    Examples:
    - Input: "5551234567" → Output: "(555) 123-4567"
    - Input: "15551234567" → Output: "(555) 123-4567"
    - Input: "555-123-4567" → Output: "(555) 123-4567"

    The function should handle these three input formats and always return the same formatted output.
    ```

1. Copy the generated function into `starter.js` and run it to verify:

    ```bash
    node exercises/01-prompt-engineering/starter.js
    ```

1. Follow the full step-by-step instructions in [exercises/01-prompt-engineering/README.md](../../exercises/01-prompt-engineering/README.md) to complete all six strategies.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Make sure the GitHub Copilot extension is installed and you are signed in to GitHub in VS Code.
- The Copilot icon appears in the VS Code status bar at the bottom of the screen. A checkmark or logo indicates it is active.
- If Copilot does not respond, try closing and reopening the Chat panel.

</details>
