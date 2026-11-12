---
name: fluent-event-take-screenshots
description: Take clean, annotated FluentEvent doc screenshots with the headless runner (scripts/screenshots/shoot.cjs) against the local site http://localhost:10023. Covers plan JSON, step types, framing, arrows/badges/highlights, FluentCommunity front-end shots, the quality checklist and the per-page workflow. USE FOR: any screenshot for a doc page, refreshing shots after a release.
---

# FluentEvent: take screenshots

## Hard rules

- Only the headless runner (`npm run shots -- <plan>`): local Google Chrome via `playwright-core`. NEVER use
  `mcp__claude-in-chrome__*`, `mcp__Claude_Browser__*`, `mcp__computer-use__*`, `mcp__remote-devices__*`,
  RemoteTrigger, SendMessage, `screencapture`. Another PC is connected to this account. Tell every subagent this.
- Plugin is read-only. Site `http://localhost:10023` (`admin`/`admin`) holds demo data (calendars, events, guests):
  shoot it, never delete it. A shot that needs a state change (e.g. add a guest, toggle a setting) must be undone in the
  same plan, or use a clearly named sample (`Docs Sample Event`) and delete exactly that afterwards.
- Never hand-edit an image. Never invent UI: if the screen doesn't match the page text, fix the text, not the image.
- No commits.

## Runner

Full step reference is the header of `scripts/screenshots/shoot.cjs` (`admin`, `front`, `viewport`, `click`, `hover`,
`fill`, `scrollTo`, `hideCss`, `css`, `eval`, `wait`, `shot` with `clip`, `arrows`, `highlights`, `badges`, `crop`).

```jsonc
{
  "doc": "docs/events/create-an-event-from-the-admin.md",
  "outDir": "public/images/events/create-event-admin",
  "viewport": {"width": 1440, "height": 900},
  "steps": [
    {"admin": "/events"},                               // → /wp-admin/admin.php?page=fluent-event#/events
    {"shot": {"name": "1.-Events-List", "clip": "app", "arrows": [{"target": {"text": "Add Event"}, "from": "left", "len": 140}]}},
    {"click": {"text": "Add Event"}}, {"wait": 1200},
    {"shot": {"name": "2.-Event-Form", "clip": "app", "crop": "auto"}}
  ]
}
```

Preview first: `npm run shots -- scripts/screenshots/plans/<slug>.json --out=<scratchpad>/<slug>`; final run without `--out`
writes `.webp` (q82, 2x) into `outDir`. Plans stay in `scripts/screenshots/plans/` as regression fixtures.

Admin app root is `#fluent-event-app`; the page canvas is `#fluent-event-router`; top nav (Dashboard / Calendars /
Events / Settings) is `.fe-navbar`. Element Plus is used for dialogs (`.el-dialog`), drawers (`.el-drawer`), selects
(`.el-select`), switches (`.el-switch`) and date pickers. WP admin chrome is hidden by the harness.

Front end (FluentCommunity portal) shots: `{"front": "/<community-slug>/..."}`: find the real portal URL first with a
probe (the portal base is set in FluentCommunity settings; try `/community/` and follow links). Logged-in as admin.
Use the member view where the page is about members. The composer, feed card and space events page are FluentCommunity
UI + FluentEvent additions; shoot at 1440 x 900 (mobile 390 x 844 only if the page is about mobile).

## Quality bar (every image)

1. Natural: light theme, real demo data, nothing loading or half-animated, no WP chrome/notices/dialog nags, no scrollbar or caret.
2. Right state: the tab/dialog/dropdown/values match what the surrounding text says.
3. Step is obvious: one arrow for a single click; numbered badges (matching the step numbers in the text) when one image covers several
   steps; a highlight box for a field/group the text then explains. Max 1 arrow, or up to 4 badges + 1 highlight. Pink `#FF4E6B` only.
4. Framing: first appearance of a screen = `"clip": "app"`; a dialog/drawer = `{"element": ".el-dialog", "pad": 32}`; keep headings in frame;
   no empty band > ~10% of the height.
5. One idea per image. Numbering `<n>.-<Short-Label>` follows the order on the page and is contiguous.
6. Sensitive data: demo emails/names only. Hide anything that looks like a real customer.

## Per-page workflow

1. Read the page (or its outline) to list the screens/steps that need an image.
2. Probe selectors: read the Vue file, or run a 10-line probe with `lib/harness.cjs` (`launch`, `gotoAdmin`, `page.evaluate`).
   A comma selector returns first DOM match, so use one precise selector. Hash routes sometimes need `{"wait": 1500}`.
3. Write the plan, preview, **Read every image**, fix, final run.
4. Insert `![alt](/images/…)` lines into the page at the right step; run image checks 1-4 from `CLAUDE.md`.
5. Report: plan path, each image with PASS/FAIL, anything you could not shoot and why.

## Setup that may be needed

Some screens need data the site may not have (a cancelled guest, a checked-in guest, a past event, an Open-mode event).
Look first (events list filters, guest tabs). If missing, create a clearly named sample through the real UI in the plan
or a probe, shoot, then delete exactly that sample. Report what you created and removed.
