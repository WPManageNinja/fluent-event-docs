---
name: fluent-event-doc-writer
description: Master voice-and-format guide for FluentEvent end-user docs (docs/**/*.md). Load before writing, drafting, expanding or proofreading any page. Covers page rules, tone, UI-path and bold conventions, linking, callouts, images, and the never-do list. USE FOR: write a doc, draft a page, rewrite a section, proofread, match house style, document a FluentEvent feature.
---

# FluentEvent Doc Writer (master skill)

You write for **FluentEvent**, the WPManageNinja plugin that adds events, RSVPs, guest management and reminder
emails to **FluentCommunity**. Readers are community owners and their staff (site admins), plus a few pages for
members who RSVP. Site: VitePress, pages at `/<slug>`. Procedure for creating/editing files:
`write-fluent-event-doc`. Where facts come from: `fluent-event-code-to-docs`.

## 1. Page rules

- Frontmatter `title` + a one-sentence `description` (what the reader can do), then a bare `# H1` = title.
- Intro of 1-3 sentences: what it is, what it does for the reader, when to use it. Bold the **feature name** on
  first use. Never "In this guide we will", "Welcome to", "This article explains".
- `##` main sections, `###` sub-topics. Nothing deeper.
- Links: absolute `[Text](/<slug>)`; the target must exist. Anchor = the key noun in the sentence,
  never "here"/"learn more". Link each destination once per page, only when the reader would otherwise be stuck.
- Images: `![Descriptive alt](/images/<category>/<short-slug>/<n>.-<Short-Label>.webp)` from the screenshot pipeline.
- End on the action or outcome ("Click **Save** to keep your changes."). No sign-offs, no "contact support".

## 2. Voice

Second person ("you"), present tense, imperative steps ("Click", "Choose", "Turn on"). Short direct sentences,
one idea each; explain *why* in one clause when a choice matters. Use "guests" for people who RSVP, "members" for
FluentCommunity users, "admins" for site administrators. Lead into every list or code block with a bridge sentence.

## 3. Formatting

- **No em dashes.** Use a colon, comma, parentheses or a full stop.
- Bold: UI labels (buttons, tabs, fields, options), the feature name on first use, and UI paths joined with
  ` › ` (U+203A, spaces each side, each segment bold): `**FluentEvent** › **Events** › **Add Event**`.
  No inner whitespace inside bold markers.
- Options: `- **Label** (default): what it does.`
- Numbered lists only for ordered procedures; first step names the path: `1. Go to **FluentEvent** › **Events**.`
- Callouts: only `::: tip` and `::: warning`, at most one per page. Never `::: info` or `> [!TIP]`.
- Tabs (`::: tabs`, `== Label`) only when one task has different routes (e.g. admin vs composer). FAQ block at the bottom for short why/what-if.
- Keys: `<kbd>Esc</kbd>`. Inline code for slugs, shortcodes, hooks. No code blocks of plugin source.

## 4. Accuracy rules (FluentEvent specific)

- Use the **exact UI labels** from the plugin (`resources/admin/**/*.vue`, `app/Views/**`, `readme.txt`). If a label
  isn't verified in code or on the live admin, don't quote it.
- v1.0.0 has no Pro tier. Do not write "(Pro)". Paid tickets, recurring events, member-created events and standalone
  (non-FluentCommunity) use are **not** available; say so plainly where a reader might expect them.
- Who can do what: only site administrators create events; staff (editor/author/contributor) get access through
  Team permissions; members view and RSVP. Meeting links on RSVP events show only to guests who are Going.
- Never invent settings, defaults or numbers. Reminder default = 24 hours before; check everything else in code.

## 5. Page types

- **Concept/overview**: intro, what you can do (bullets), how the pieces connect, where to go next (2-3 links).
- **How-to**: intro, prerequisites line if any, numbered steps each with its screenshot, result line, tip/warning if needed.
- **Settings/reference screen**: intro, one `##` per section or tab, option bullets with defaults, then **Save**.
- **Member-facing** (RSVP, add to calendar): address the member ("you"), show the FluentCommunity portal UI.

## 6. Never

Relative or external image paths · `.md` in links · pages outside a category folder · em dashes · "(Pro)" ·
support boilerplate · screenshots of anything the plugin doesn't show · claims you didn't verify in code or on the site.
