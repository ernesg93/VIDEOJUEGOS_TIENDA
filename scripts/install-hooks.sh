#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

if [ ! -d .git/hooks ]; then
  echo "Error: .git/hooks not found (is this a git repo?)" >&2
  exit 1
fi

mkdir -p .git/hooks

timestamp="$(date +%Y%m%d%H%M%S)"
for hook in pre-commit post-commit; do
  src=".githooks/$hook"
  dst=".git/hooks/$hook"

  if [ ! -f "$src" ]; then
    echo "Error: missing $src" >&2
    exit 1
  fi

  if [ -f "$dst" ]; then
    cp "$dst" "$dst.bak-$timestamp"
  fi

  cp "$src" "$dst"
  chmod +x "$dst" || true
done

echo "Installed git hooks (backup suffix: $timestamp)"
