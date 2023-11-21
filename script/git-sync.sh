#!/usr/bin/env bash

set -e

PROJECT_ENV="$HOME/workspace/github/shaonianche/"

cd "$PROJECT_ENV"

MESSAGE="changes on $(date)"
git add .
git commit -m "${MESSAGE}"

git pull --rebase
git push origin main
