---
name: audit-fluent-event-docs
description: Read-only quality gate for the FluentEvent docs: build, links, sidebar coverage, image checks, style rules (em dashes, "(Pro)", relative links), frontmatter, and claim spot-checks against the plugin. Reports findings, changes nothing.
---

# Audit FluentEvent docs (read-only)

Run from the repo root and report, don't fix:

```bash
npm run docs:build 2>&1 | tail -20
# pages not in sidebar
for f in $(find docs -name '*.md'); do s=$(basename $f .md); c=$(dirname $f | xargs basename); grep -q "link: '/$s'" .vitepress/config.mts || echo "NOT IN SIDEBAR: $f"; done
# internal links that don't resolve
grep -rhoE '\]\(/[a-z0-9-]+[)#]' docs index.md | sed 's/](\///; s/[)#]$//' | sort -u | while read s; do [ -n "$(find docs -name "$s.md")" ] || echo "BROKEN: /$s"; done
grep -rn '—' docs | head; grep -rn '(Pro)' docs | head; grep -rnE '\]\((\./|\.\./|[a-z])' docs | grep -v http | head
grep -rLE '^description: .{20,}' docs
```

Then the five image checks from `CLAUDE.md`, and spot-check 5 random claims (labels, defaults, who-can-do-what) against
the plugin source. Report: counts, each problem as `file:line — issue`, and what was not verified.
