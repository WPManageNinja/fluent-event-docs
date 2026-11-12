# CLAUDE.md — FluentEvent User Documentation

End-user documentation for **FluentEvent** (by WPManageNinja): community events, RSVPs, guest management
and reminder emails for **FluentCommunity**. Built with **VitePress 1.6+** / **Vue 3.5**, cloned from the
Ninja Tables docs scaffold (same theme, same screenshot pipeline).

## Commands

| Command | Action |
| --- | --- |
| `npm install` | Install dependencies (once) |
| `npm run docs:dev` | Dev server, `http://localhost:5173` |
| `npm run docs:build` | Production build → `.vitepress/dist/` (gitignored) |
| `npm run docs:preview` | Preview the build (`http://127.0.0.1:4173`) |
| `npm run shots -- scripts/screenshots/plans/<plan>.json` | Take screenshots from the local site |
| `npm run featured:generate` | Social-share card for every page that lacks one |

Run `npm run docs:build` after any structural change. A green build does **not** verify images: run the
five image checks in *Images → Verifying images* below.

## The plugin (source of truth)

- Plugin code (READ-ONLY): `~/Local Sites/test/app/public/wp-content/plugins/fluent-event` (v1.0.0).
  Never edit it. `readme.txt` there is the feature/changelog source. Admin SPA = `resources/admin/` (Vue 3 +
  Element Plus), REST = `app/Http/Routes` + `app/Http/Controllers`, emails = `app/Views/emails`,
  FluentCommunity integration = `Modules/FluentCommunity` + `resources/fcom-portal`.
- Requires **FluentCommunity** (free is enough). Events are FluentCommunity posts in discussion spaces; each
  space has one **calendar**. Only site administrators (and staff granted permission) manage events.
- Local site: `http://localhost:10023` (Local "test" site, login `admin` / `admin`). It already has demo
  data (calendars, events, guests). Admin app: `/wp-admin/admin.php?page=fluent-event#/<route>`.
- Admin routes: `/` dashboard · `/events` · `/events/new` · `/events/:id` (detail + guests) · `/events/:id/edit`
  · `/calendars` · `/calendars/new` · `/calendars/:id` · `/calendars/:id/edit` · `/settings/general` ·
  `/settings/email-notifications`.
- Feature map and doc coverage: `.claude/plugin-memory/CATALOG.md`.

## Repository layout

```
/
├── index.md                 ← home (layout: home)
├── CLAUDE.md                ← this file
├── public/                  ← logo.svg, favicon.png, images/<category>/<short-slug>/<n>.-<Label>.webp, images/featured/
├── .vitepress/config.mts    ← site config + nav + sidebar (single source of truth)
├── .vitepress/theme/        ← style.css (brand), Layout.vue, Feedback, ZoomableImage, tabs/faq blocks, motion, aurora
├── docs/<category>/<slug>.md  ← every page, one folder deep, no sub-folders
├── scripts/screenshots/     ← runner (shoot.cjs), lib/, plans/*.json, placeholders.mjs
└── .claude/skills, .claude/agents, .claude/plugin-memory
```

Categories (folders): `getting-started` · `events` · `guests` · `calendars` · `dashboard` · `community` ·
`emails` · `settings` · `help`. (`public/images/` is assets, not a category.)

## URL convention

`docs/<category>/<slug>.md` is served at `/<slug>` through `rewrites` in `config.mts`
(`'docs/:category/:slug.md': ':slug.md'`, `cleanUrls: true`). Internal links are always
`[Text](/<slug>)`: no `.md`, no relative links, no `/guide/` prefix, no category in the URL. Slugs are unique across
categories. Renaming or moving a page changes its URL: rewrite inbound links and regenerate its card.

## Sidebar — mandatory when adding/renaming a page

Nav + sidebar are inline arrays in `.vitepress/config.mts` (no auto-discovery). Groups follow the reader's
journey (Get Started → Events → Guests → Calendars → Community → Emails → Settings → Help), not folder
names. Labels are short and do not repeat the H1. Leaf shape: `{ text: 'Label', link: '/<slug>' }`.

## Tabs, FAQ, keycaps

`::: tabs` / `::: faq` containers split by `== Label` lines (see `plugin-doc-blocks.ts`). Never nest another
`:::` block inside a section. Keyboard keys: `<kbd>Esc</kbd>`. UI labels: `**bold**`.

## Images

All screenshots are local `.webp` under `public/images/<category>/<short-slug>/<n>.-<Short-Label>.webp`
(`<n>` = order on the page). Markdown: `![Alt](/images/<category>/<short-slug>/<n>.-<Label>.webp)` — absolute,
never relative, never external (images render through `<ZoomableImage>`; a relative `src` 404s in production).
Never remove the `<ClientOnly>` wrapper in `plugin-zoomable.ts`. Screenshots come from the runner only, never by hand.

### Verifying images (run all after any image change; 1–4 must print nothing, 5 = report and ask)

```bash
comm -13 <(find public/images -type f | sed 's|^public||' | sort -u) <(grep -rhoE '\(/images/[^)]*\)' --include='*.md' docs index.md | tr -d '()' | sort -u)
grep -rn '!\[[^]]*\](http' --include='*.md' docs index.md
grep -rhoE '!\[[^]]*\]\([^)]+\)' --include='*.md' docs index.md | sed -E 's/.*\((.*)\)/\1/' | grep -vE '^/images/'
find public/images -type f ! -name '*.webp' ! -path 'public/images/featured/*'
comm -23 <(find public/images -type f ! -path 'public/images/featured/*' | sed 's|^public||' | sort -u) <(grep -rhoE '\(/images/[^)]*\)' --include='*.md' docs index.md | tr -d '()' | sort -u)
```

Then `pkill -f "vitepress preview"; npm run docs:build && npm run docs:preview` and curl every referenced image
(`http://127.0.0.1:4173/images/...`) for 200.

## Writing style (full guide: skill `fluent-event-doc-writer`)

1. Frontmatter `title` + one-sentence `description`, then bare `# H1` = title.
2. 1–3 sentence intro: what it is and when to use it; **bold** the feature name on first use.
3. `##` / `###` only. Bullets for options, numbered lists only for ordered steps.
4. Exact UI labels in bold; UI paths joined with ` › ` (`**FluentEvent** › **Events**`).
5. Second person, present tense, short sentences. No em dashes (`—`), no sign-offs, no support boilerplate.
6. FluentEvent has no Free/Pro split in v1.0.0: do not write "(Pro)". Features not in this version (paid
   tickets, recurring events, member-created events) are stated as not available, never promised.
7. At most one `::: tip` / `::: warning` per page.

## Hard constraints

- No `.md` directly under `docs/`; every page lives in a category folder.
- Never add `public/` anywhere but the repo root.
- Never add/rename a page without updating the sidebar, then run `npm run featured:generate` and `docs:build`.
- Never use the Chrome extension, `mcp__claude-in-chrome__*`, `mcp__Claude_Browser__*`, computer-use or
  `screencapture` (another PC is connected to this account). Browser work = local headless Chrome via the runner.
- Never edit the plugin, never change plugin settings or delete demo data on the site while shooting
  (read-only shots; if a shot needs a state change, undo it). Do not publish anything to the cloud.
- Never commit `node_modules/`, `.vitepress/dist/`, `.vitepress/cache/`. Only commit/push when asked.

## Brand

Teal `#12A9B5` (`--vp-c-brand-*` in `style.css`), same structure as the FluentCommunity docs. Logos from the designer pack in
`public/images/brand/` (light + dark lockups, icon); `public/logo.svg` + `public/favicon.png` are the pack icon. Annotation colour in screenshots: pink `#FF4E6B`.

## Skills (`.claude/skills/`)

- `fluent-event-doc-writer` — voice/format master (load before writing any page)
- `write-fluent-event-doc` — create/edit a page (file, sidebar, card, checks)
- `fluent-event-take-screenshots` — runner reference, plan format, quality bar
- `fluent-event-code-to-docs` — read plugin source → accurate page; release sync
- `audit-fluent-event-docs` — read-only quality gate (links, images, sidebar, claims)

Agent: `fluent-event-screenshotter` (Sonnet) for screenshot plans.

## Git

Only commit or push when explicitly asked. This folder is not a git repo yet.
