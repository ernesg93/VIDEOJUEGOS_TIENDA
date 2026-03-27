---
name: agent-browser
description: >
  Use the agent-browser CLI (Vercel Labs) to automate a real browser for E2E-ish
  checks: open pages, take accessibility snapshots, click/fill using stable refs,
  and persist sessions safely.
  Trigger: when doing browser automation, E2E checks, or interactive UI flows.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

## When to Use

- Validate end-to-end flows (navigation, forms, basic UI behavior) without writing Playwright.
- Reproduce a UI bug quickly with deterministic steps.
- Smoke-check critical pages of this Django app (e.g., `/catalogo/`, later `/admin/`, login).

## Critical Patterns

- Prefer the snapshot + refs workflow:
  - `snapshot -i --json` -> parse refs -> `click @eN` / `fill @eN` / `get text @eN`.
- Always re-snapshot after actions that can change the DOM (click, navigation, form submit).
- Use `--json` when you need machine-readable output.
- Security defaults for agents:
  - Use `--allowed-domains "127.0.0.1,localhost"` when testing locally.
  - Avoid `eval` unless strictly necessary; if used, gate it with `--confirm-actions eval`.
  - Never commit auth state files; treat them as secrets.
- Persist sessions the safe way:
  - `--session-name <name>` for automatic cookies/localStorage persistence.
  - Prefer separate names per site/user (e.g., `admin-local`, `user-local`).

## Minimal Workflow (This Project)

Assumes Django is running locally (default): `http://127.0.0.1:8000`.

```bash
# 1) Open catalog page
agent-browser --allowed-domains "127.0.0.1,localhost" open http://127.0.0.1:8000/catalogo/

# 2) Wait and snapshot interactive elements
agent-browser wait --load networkidle
agent-browser snapshot -i --json

# 3) Use refs from snapshot
agent-browser click @e2
agent-browser snapshot -i --json

# 4) Visual debug
agent-browser screenshot --annotate
```

## Common Commands

```bash
# Navigation / state
agent-browser open <url>
agent-browser get url
agent-browser get title
agent-browser wait --load networkidle

# Snapshot (best for AI)
agent-browser snapshot
agent-browser snapshot -i
agent-browser snapshot -i --json

# Actions (prefer refs like @e1)
agent-browser click <sel|@eN>
agent-browser fill <sel|@eN> "text"
agent-browser type <sel|@eN> "text"
agent-browser press Enter

# Evidence
agent-browser screenshot
agent-browser screenshot --annotate

# Persistence
agent-browser --session-name <name> open <url>
agent-browser state save <path>
agent-browser state load <path>

# Cleanup
agent-browser close
agent-browser close --all
```

## Notes for Django

- Local URLs are typically `http://127.0.0.1:8000/...`.
- If you automate admin login later, use `--session-name` so you only log in once.
- If a page uses CSRF-protected POST forms, keep the interaction in-browser (don’t simulate HTTP).
