# Agent Instructions (Example for a Web Application Project)

This is a reference example of an `AGENTS.md` file for a real-world Node.js web application.
Adapt the content to match your own project's structure, commands, and conventions.

---

## Repository Purpose

This is a REST API service built with Node.js and TypeScript. It provides user authentication
and data management endpoints. The service connects to a PostgreSQL database.

There is no frontend code in this repository. The API is consumed by a separate frontend
repository.

## Repository Structure

```
src/
  controllers/    - Request handlers (one file per resource)
  services/       - Business logic (one file per domain)
  routes/         - Express router definitions
  models/         - Database model definitions
  middleware/     - Express middleware (auth, logging, validation)
  lib/            - Shared utilities (logger, db connection, config)
  __tests__/      - Test files, mirroring the src/ structure
  errors/         - Custom error classes
  types/          - Shared TypeScript type definitions
.github/
  copilot-instructions.md
  instructions/
```

## Build

Install dependencies (only needed once after cloning or after updating package.json):
```bash
npm install
```

Compile TypeScript:
```bash
npm run build
```

The compiled output goes to `dist/`. Do not commit the `dist/` directory.

## Run the Development Server

```bash
npm run dev
```

This starts the server on port 3000 with hot reload. The server requires a running
PostgreSQL instance. See `docs/local-setup.md` for database setup instructions.

## Run Tests

All tests (unit + integration):
```bash
npm test
```

Unit tests only (no database required):
```bash
npm run test:unit
```

Integration tests (requires a running PostgreSQL instance on port 5432):
```bash
npm run test:integration
```

Always run `npm run test:unit` after making code changes to verify nothing is broken.
Run `npm run test:integration` before submitting a pull request.

## Lint and Format

Check for linting errors:
```bash
npm run lint
```

Auto-fix linting errors:
```bash
npm run lint:fix
```

Format code:
```bash
npm run format
```

Run lint and format before submitting changes.

## Database Migrations

To add a database migration:
1. Create a new file in `db/migrations/` following the naming pattern `YYYYMMDD_description.sql`.
2. Write the SQL for the migration.
3. Run the migration locally: `npm run db:migrate`.
4. Include both the migration file and any updated model files in the same commit.

Do not modify existing migration files. Only add new ones.

## Conventions

- Controllers only handle HTTP request/response logic. Business logic goes in services.
- Services do not import from controllers or routes.
- All database queries go through `src/lib/db.ts` (no inline SQL strings elsewhere).
- Use the `AppError` class for all application errors (`src/errors/AppError.ts`).
- Use the `logger` utility for all logging (`src/lib/logger.ts`).
- Test files mirror the source directory (e.g., `src/services/userService.ts` is tested
  in `src/__tests__/services/userService.test.ts`).

## Constraints

- Do not add npm dependencies without noting it in the pull request description.
  The team must approve new dependencies.
- Do not use `process.exit()` outside of `src/index.ts`.
- Do not write inline SQL strings. Use `src/lib/db.ts`.
- Do not commit the `dist/` directory or `node_modules/`.
- Keep this file under 150 lines.
