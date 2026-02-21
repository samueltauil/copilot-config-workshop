# Example: Repository-Wide Custom Instructions

This file is a reference example of a `copilot-instructions.md` file for a real-world project.
In your own repository, this file should be placed at `.github/copilot-instructions.md`.

---

# Project Custom Instructions

## Project Overview

This is a web application built with Node.js (backend) and React (frontend). The backend exposes
a REST API. The frontend consumes the API and renders a single-page application.

Providing this overview helps Copilot understand the general architecture without needing to
explore the full codebase on each request.

---

## Language and Runtime

- Backend: Node.js 20, TypeScript 5
- Frontend: React 18, TypeScript 5
- Package manager: npm (not yarn or pnpm)

---

## Code Style

- Use 2-space indentation for all files.
- Use single quotes for strings in TypeScript and JavaScript files.
- Do not use semicolons at the end of statements (the project uses a no-semicolon ESLint rule).
- Use arrow functions for callbacks and anonymous functions.
- Use `const` for all variables that are not reassigned. Use `let` only when reassignment is
  necessary. Never use `var`.
- Use ES module syntax (`import`/`export`). Do not use CommonJS `require()`.

---

## TypeScript

- Prefer explicit return types on exported functions.
- Do not use `any`. If the type is unknown, use `unknown` and narrow it.
- Use interface declarations for object shapes. Use type aliases for unions and intersections.
- Strict mode is active; write code compatible with `"strict": true`.

---

## File Naming Conventions

- React component files: PascalCase (e.g., `UserProfile.tsx`)
- Utility and service files: camelCase (e.g., `userService.ts`)
- Test files: same name as the file under test with `.test.ts` suffix (e.g., `userService.test.ts`)
- Constants: `UPPER_SNAKE_CASE` for values; camelCase for the file name

---

## Error Handling

- All async functions must use `try/catch` or return a `Result<T, E>` type.
- Never swallow errors silently. If an error is caught and not re-thrown, log it.
- Use the project's custom `AppError` class (defined in `src/errors/AppError.ts`) for all
  application-level errors. Do not throw plain `Error` objects or plain strings.
- Log errors using the project's logger (`import { logger } from '@/lib/logger'`), not
  `console.error`.

---

## API Design (Backend)

- All API endpoints follow REST conventions.
- Route files live in `src/routes/`. Each route file corresponds to one resource.
- Controllers live in `src/controllers/`. A controller function handles exactly one endpoint.
- Services live in `src/services/`. Business logic must not go in controllers.
- Validate all incoming request bodies using the `zod` library before processing.
- Return errors as JSON objects with the shape: `{ error: string, code: string }`.

---

## Testing

- Test files live in `src/__tests__/` and mirror the source directory structure.
- Use `vitest` as the test runner (not Jest or Mocha).
- Each `describe` block should test one module or function.
- Each `it` block should test exactly one behavior.
- Use `vi.mock()` to mock external modules in unit tests.
- Integration tests that call a real database must use the `testDb` fixture from
  `src/__tests__/fixtures/db.ts`.

---

## What to Avoid

- Do not suggest adding new npm dependencies without noting that the team must approve them.
- Do not generate code that uses `process.exit()` except in the application entry point.
- Do not generate inline SQL strings. Use the project's query builder (`src/lib/db.ts`).
