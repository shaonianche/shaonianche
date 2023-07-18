#!/usr/bin/env bash

set -e

PROJECT_ENV="$HOME/workspace/shaonianche/"

cd "$PROJECT_ENV"

CHANGED_FILES=$(git diff-index --cached HEAD --name-only --relative)
if [ -n "$CHANGED_FILES" ]; then
  git add -- "${CHANGED_FILES}"
fi

MESSAGE="changes on $(date)"

git commit -m "${MESSAGE}"

git pull --rebase
git push origin main
