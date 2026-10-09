#!/usr/bin/env bash
# Push this demo repo to a GitHub organization and create the tickets as Issues.
# Usage: ./publish.sh <your-org> [repo-name]
# Requires: git and GitHub CLI (gh), logged in with `gh auth login`.
set -euo pipefail
ORG="${1:?Usage: ./publish.sh <your-org> [repo-name]}"
REPO="${2:-shopcart-demo}"

gh auth status >/dev/null
if [ ! -d .git ]; then
  git init -q -b main
  git add .
  git commit -qm "Initial commit: shopcart demo"
fi
gh repo create "$ORG/$REPO" --private --source . --push

gh label create bug --repo "$ORG/$REPO" --color d73a4a --force >/dev/null
gh label create enhancement --repo "$ORG/$REPO" --color a2eeef --force >/dev/null

for f in tickets/*.md; do
  title=$(head -1 "$f" | sed 's/^# //')
  label=$(grep -m1 '^\*\*Labels:\*\*' "$f" | sed 's/.*\*\* //')
  body=$(tail -n +2 "$f" | grep -v '^\*\*Labels:\*\*')
  gh issue create --repo "$ORG/$REPO" --title "$title" --body "$body" --label "$label" >/dev/null
  echo "Created issue: $title"
done
echo "Done: https://github.com/$ORG/$REPO"
