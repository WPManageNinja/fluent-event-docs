---
name: write-fluent-event-doc
description: Procedure for creating or editing a FluentEvent doc page: pick category + slug, verify facts in plugin code, write the page, add the sidebar entry, take screenshots, generate the featured card, build and check. USE FOR: add a new page, change an existing page, rename/move a page.
---

# Write or edit a FluentEvent doc page

Load `fluent-event-doc-writer` first (voice + format).

## New page

1. **Check coverage**: `grep -ril "<feature>" docs` and `.claude/plugin-memory/CATALOG.md`. Don't duplicate; link instead.
2. **Category + slug**: category = one of `getting-started events guests calendars dashboard community emails settings help`.
   Slug = lowercase-hyphen, descriptive, unique across all categories (`ls docs/*/<slug>.md`).
3. **Facts**: follow `fluent-event-code-to-docs` (read the Vue/PHP, then look at the live screen).
4. **Write** `docs/<category>/<slug>.md` (frontmatter, H1, intro, body). Leave no placeholders: take the screenshots
   (`fluent-event-take-screenshots`) and insert the image lines in the right steps.
5. **Sidebar**: add `{ text: 'Short label', link: '/<slug>' }` in the right group in `.vitepress/config.mts`.
6. **Cross-links**: link to it from 1-2 related pages; make sure it links onward to 2-3 pages.
7. **Card**: `npm run featured:generate`.
8. **Gate**: `npm run docs:build` clean + the five image checks in `CLAUDE.md`.

## Edit a page

Re-verify the changed claim in code/live UI, edit in place, keep image numbering contiguous, rebuild. If a UI label
changed, grep the whole `docs/` folder for the old label.

## Rename / move

URL changes. Update: sidebar, every inbound link (`grep -rn "/<old>" docs index.md .vitepress/config.mts`),
rename the image folder and its references, delete the old featured card then regenerate. Rebuild.

## Changelog

`docs/help/change-log.md`: reverse-chronological `## FluentEvent vX.Y.Z`, `*Released on Month D, YYYY*`, then a
`::: code-group` with fenced tabs (` ```md [🆕 New Features]`, `[🔧 Improvements]`, `[🐛 Bug fixes]`) and `• ` bullets.
Only non-empty tabs. Source: plugin `readme.txt` changelog.
