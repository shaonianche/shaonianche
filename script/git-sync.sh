#!/usr/bin/env bash
cd "$(
  cd "$(dirname -- "$0")"
  pwd
)" && cd ..

autocorrect --fix */*.md

git add --all
git commit -m "changes on $(date)"
git pull --all
git push
