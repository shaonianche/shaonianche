#!/usr/bin/env bash

set -e

git_root=$(git rev-parse --show-toplevel 2> /dev/null)

if [[ $? -eq 0 ]]; then
    cd "$git_root"
    git add .
    git commit -m "changes on $(date)"
    git pull
    git push
else
    echo "error: not found .git"
fi
