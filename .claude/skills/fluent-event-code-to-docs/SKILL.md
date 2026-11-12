---
name: fluent-event-code-to-docs
description: How to turn the FluentEvent plugin source and the live local site into accurate documentation: where each feature lives in code, how to read it, how to verify on the running admin, and how to sync docs after a new plugin release. USE FOR: before documenting any feature, verifying a claim, checking labels/defaults/permissions, release sync.
---

# FluentEvent: code → docs

Plugin (READ-ONLY): `~/Local Sites/test/app/public/wp-content/plugins/fluent-event`. Live site: `http://localhost:10023`
(`admin`/`admin`). Never edit either's data permanently.

## Where things live

| Topic | Look at |
|---|---|
| Feature list, FAQ, changelog | `readme.txt` |
| Admin screens (labels, fields, buttons, empty states) | `resources/admin/modules/{dashboard,events,calendars,settings}/**/*.vue`, shared `resources/admin/components/` |
| Admin routes | `resources/admin/router/routes.js` |
| Event create/edit form | `modules/events/CreateOrUpdateEvent.vue`; detail + guests `events/detail.vue`, `parts/EventGuests.vue`, `Guest*Modal.vue` |
| Event list views (card/timeline/calendar) | `modules/events/index.vue`, `parts/Events*.vue` |
| Calendars | `modules/calendars/**` |
| Settings (general, email) | `modules/settings/general.vue`, `email-notifications.vue` |
| REST API + validation + who may call it | `app/Http/Routes/*.php`, `Controllers/`, `Requests/`, `Policies/`, `Middleware/` |
| Models/statuses/defaults | `app/Models/`, `app/Services/`, `app/Utils/` |
| Emails (templates, triggers, reminder timing) | `app/Views/emails/`, `app/Hooks/Handlers/`, `app/Services/*Email*`, `*Reminder*` |
| FluentCommunity integration (composer, space events page, portal timeline/calendar, RSVP UI) | `Modules/FluentCommunity/`, `resources/fcom-portal/`, `resources/portal/`, `app/Views/portal/`, `app/Http/Controllers/Portal*.php`, `CommunityEventController.php` |
| Add to calendar (Google/.ics) | grep `ics`, `google` in `app/` and `resources/` |
| Team permissions | `app/Http/Policies/`, `app/Utils/Auth/`, settings screens |
| Strings | wrap with `__('…', 'fluent-event')` — grep the exact label to confirm spelling |

## Method

1. Read the screen's Vue file for labels, defaults, validation and which fields are conditional.
2. Read the controller/request for rules (required fields, limits, statuses).
3. Open the live screen with the runner or a probe script (`scripts/screenshots/lib/harness.cjs`) and read the DOM text
   to confirm what a user sees. Docs describe what the user sees; code explains why.
4. Note anything ambiguous or not shipped in `.claude/plugin-memory/CATALOG.md` under *Gaps*; don't guess in the page.

## Release sync

Replace the plugin folder (or pull) → diff `readme.txt` changelog → for each change grep `docs/` for the affected
label/feature → update pages + CATALOG + `docs/help/change-log.md` → re-run the affected screenshot plans → build + checks.
