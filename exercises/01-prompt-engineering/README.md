# Exercise 1: Prompt Engineering for GitHub Copilot

**Learning objectives:**
- Understand what makes a good prompt
- Apply the core prompt engineering strategies from the official GitHub documentation
- Compare the quality of vague versus specific prompts
- Use inline suggestions and Copilot Chat effectively

**Duration:** ~30 minutes

**Prerequisites:** GitHub Codespaces or Visual Studio Code with the GitHub Copilot extension installed.

---

## Background

A prompt is a request you make to GitHub Copilot. The quality of Copilot's response depends heavily on how you write your prompt. The [prompt engineering guide](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat) identifies several strategies that consistently improve results. This exercise walks you through each strategy with concrete examples.

---

## Setup

**Option A: GitHub Codespaces (recommended)**

1. Open this repository on GitHub.
2. Click **Code > Codespaces > Create codespace on main**.
3. Wait for the Codespace to build. Node.js, Python, and the Copilot extensions are pre-installed.
4. Open the starter file: `exercises/01-prompt-engineering/starter.js`

**Option B: Local VS Code**

1. Clone the repository and open it in VS Code:
   ```bash
   git clone https://github.com/<your-username>/copilot-config-workshop.git
   cd copilot-config-workshop
   code .
   ```
2. Open the starter file: `exercises/01-prompt-engineering/starter.js`

**Verify Copilot is active:**

Look for the Copilot icon in the VS Code status bar at the bottom of the screen. A checkmark or the Copilot logo indicates it is active. If it shows a warning, click it and sign in to GitHub.

---

## Strategy 1: Start General, Then Get Specific

Effective prompts begin with a broad goal and then add specific requirements.

**Step 1.1 - Vague prompt (observe the result):**

1. Open Copilot Chat by clicking the chat icon in the VS Code sidebar (or press `Ctrl+Alt+I` on Windows/Linux, `Cmd+Shift+I` on macOS).
2. Type the following prompt and press `Enter`:
   ```
   Write a function to validate input
   ```
3. Read Copilot's response. Notice that the response makes assumptions about what type of input to validate. The function may or may not match what you need.

**Step 1.2 - Specific prompt (compare the result):**

1. In the same chat window, type the following prompt and press `Enter`:
   ```
   Write a JavaScript function that validates an email address.
   
   The function should:
   - Accept a single string argument called `email`
   - Return `true` if the string matches standard email format (e.g., user@domain.com)
   - Return `false` otherwise
   - Not use any external libraries
   ```
2. Compare this response to the previous one. The response should now be precise, without ambiguity.

**Validation:** The second function should have a name like `validateEmail`, accept one argument, and return a boolean.

---

## Strategy 2: Give Examples

Providing example inputs and outputs gives Copilot a clear target.

**Step 2.1:**

1. In Copilot Chat, type the following prompt:
   ```
   Write a JavaScript function that formats a phone number.
   
   Examples:
   - Input: "5551234567" → Output: "(555) 123-4567"
   - Input: "15551234567" → Output: "(555) 123-4567"
   - Input: "555-123-4567" → Output: "(555) 123-4567"
   
   The function should handle these three input formats and always return the same formatted output.
   ```
2. Press `Enter` and review the response.

**Validation:** The generated function should handle all three input formats shown in the examples.

**Step 2.2 - Verify the function:**

1. Copy the generated function into the `starter.js` file.
2. Add the following test calls at the bottom of the file:
   ```javascript
   console.log(formatPhoneNumber("5551234567"));    // Expected: (555) 123-4567
   console.log(formatPhoneNumber("15551234567"));   // Expected: (555) 123-4567
   console.log(formatPhoneNumber("555-123-4567"));  // Expected: (555) 123-4567
   ```
3. Run the file:
   ```bash
   node exercises/01-prompt-engineering/starter.js
   ```
4. Confirm all three lines print `(555) 123-4567`.

---

## Strategy 3: Break Complex Tasks into Simpler Tasks

Large, complex prompts often produce incomplete results. Breaking a task into steps gives Copilot manageable scope at each step.

**Step 3.1 - Avoid a single complex prompt:**

Do not ask Copilot to build an entire feature in one prompt. Instead, break it into parts.

**Step 3.2 - Build a simple data processing pipeline step by step:**

1. In Copilot Chat, type:
   ```
   Write a JavaScript function called `readCSVLine` that accepts a comma-separated string and returns an array of trimmed string values.
   
   Example: "Alice, 30 , engineer" → ["Alice", "30", "engineer"]
   ```
2. Copy the result into `starter.js`.

3. Next, type:
   ```
   Write a JavaScript function called `parseEmployee` that accepts an array of three strings [name, age, role] and returns an object with the properties `name` (string), `age` (number), and `role` (string).
   
   Example: ["Alice", "30", "engineer"] → { name: "Alice", age: 30, role: "engineer" }
   ```
4. Copy the result into `starter.js`.

5. Finally, type:
   ```
   Write a JavaScript function called `processCSV` that accepts an array of comma-separated strings. Use the `readCSVLine` and `parseEmployee` functions to return an array of employee objects.
   ```
6. Copy the result into `starter.js`.

**Validation:** Add the following to `starter.js` and run it:
```javascript
const lines = [
  "Alice, 30, engineer",
  "Bob, 25, designer",
  "Carol, 35, manager"
];
console.log(processCSV(lines));
```
Expected output:
```
[
  { name: 'Alice', age: 30, role: 'engineer' },
  { name: 'Bob', age: 25, role: 'designer' },
  { name: 'Carol', age: 35, role: 'manager' }
]
```

---

## Strategy 4: Avoid Ambiguity

Ambiguous words and pronouns ("it", "this", "that") lead to unpredictable responses. Always be explicit.

**Step 4.1 - Ambiguous prompt (observe the problem):**

1. In Copilot Chat, type:
   ```
   What does this do?
   ```
2. Notice that Copilot may not know what "this" refers to. It may ask for clarification or make an assumption.

**Step 4.2 - Explicit prompt:**

1. In `starter.js`, select the `processCSV` function you created earlier (click and drag to highlight it).
2. Right-click the selected code and choose **Copilot > Explain This**.
3. Alternatively, open Copilot Chat and type:
   ```
   Explain what the `processCSV` function in my current file does, step by step.
   ```

**Validation:** Copilot should provide a clear explanation of the function, referencing its name specifically.

---

## Strategy 5: Indicate Relevant Code

Copilot uses the files you have open as context. Manage which files are open to improve response quality.

**Step 5.1:**

1. Close all other files in VS Code so that only `starter.js` is open.
2. In Copilot Chat, type:
   ```
   Add JSDoc comments to all functions in the current file.
   ```
3. Copilot should add comments to the functions in `starter.js`. Because only one relevant file is open, Copilot focuses its attention there.

**Step 5.2 - Using the `#file` chat variable:**

You can also explicitly attach a file to your prompt:

1. In Copilot Chat, type `#` to see available chat variables.
2. Select `#file` and choose `starter.js`.
3. Complete your prompt:
   ```
   #file:starter.js Write unit tests for the `validateEmail` function using plain JavaScript assertions (no testing framework).
   ```

**Validation:** Copilot should generate test code that specifically tests the `validateEmail` function.

**Step 5.3 - Generate tests and run them:**

A key Copilot workflow is generating tests and then executing them to verify they pass. Practice this end-to-end flow:

1. In Copilot Chat, type:
   ```
   #file:starter.js Write a complete test file for all functions in this file. Use the built-in Node.js assert module. Include tests for normal inputs, edge cases, and error conditions. Print a summary of passed and failed tests at the end.
   ```
2. Review the generated test code. Confirm it covers the functions you added during this exercise (such as `validateEmail`, `formatPhoneNumber`, `readCSVLine`, `parseEmployee`, `processCSV`).
3. Save the generated tests to a new file:
   ```
   exercises/01-prompt-engineering/starter.test.js
   ```
4. Run the tests:
   ```bash
   node exercises/01-prompt-engineering/starter.test.js
   ```
5. If any tests fail, select the error output in the terminal, then use Copilot Chat to troubleshoot:
   ```
   #selection This test failed. Explain why and suggest a fix.
   ```
6. Fix the issue (either in the test or in the function) and run the tests again until all pass.

**Validation:** All tests pass and the summary shows no failures.

---

## Strategy 6: Experiment and Iterate

If you do not get the result you want, iterate on your prompt. You do not need to start over.

**Step 6.1:**

1. In Copilot Chat, type:
   ```
   Write a function to sort employees
   ```
2. The result may sort by name alphabetically. If you want a different sort order, follow up:
   ```
   Update the function to sort employees by age in ascending order, and if two employees have the same age, sort them alphabetically by name.
   ```
3. Continue iterating until the function matches your requirements.

**Validation:** The sort function should handle the tie-breaking case. Test it by adding employees with the same age:
```javascript
const employees = [
  { name: "Carol", age: 30, role: "manager" },
  { name: "Alice", age: 25, role: "engineer" },
  { name: "Bob", age: 30, role: "designer" }
];
console.log(sortEmployees(employees));
// Expected: Alice (25), Bob (30), Carol (30)
```

---

## Summary

In this exercise you applied six prompt engineering strategies:

| Strategy | Key takeaway |
|----------|-------------|
| Start general, then get specific | State the goal first, then add constraints |
| Give examples | Show example inputs and outputs |
| Break tasks into steps | Compose complex features from smaller prompts |
| Avoid ambiguity | Name functions and files explicitly |
| Indicate relevant code | Open only relevant files; use `#file` to attach context |
| Experiment and iterate | Follow up in the same conversation to refine results |

---

## Next Steps

Proceed to [Exercise 2: Repository-Wide Custom Instructions](../02-custom-instructions/README.md).
