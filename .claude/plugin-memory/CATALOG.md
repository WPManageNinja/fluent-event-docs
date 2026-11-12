# FluentEvent plugin catalog (v1.0.0)

Plugin (READ-ONLY): `~/Local Sites/test/app/public/wp-content/plugins/fluent-event`. Requires FluentCommunity.
Last fully audited: 2026-11-12 (first full docs pass, 30 pages).

## Admin screens (route → doc page)

| Route | Screen | Doc page |
|---|---|---|
| `/` | Dashboard | dashboard/admin-dashboard-and-guest-stats |
| `/events` | Events list (All/Upcoming/Past, search, cards/timeline/calendar, filter) | events/manage-events-list-views |
| `/events/new`, `/events/:id/edit` | Event form | events/create-an-event-from-the-admin, events/event-details-and-settings |
| `/events/:id` | Detail: Overview, Description, Guests, Settings (danger zone) | events/edit-or-delete-an-event, guests/* |
| `/calendars*` | Calendars list/create/edit/detail | calendars/* |
| `/settings/general` | Default view, disable view switch, landing pages, portal slug, email sender + footer | settings/general-settings, emails/email-sender-settings |
| `/settings/email-notifications` | Confirmation, cancellation, reminders (max 5, minutes/hours/days, max 30 days) | emails/* |
| Portal `/portal/events`, `/portal/create-new-event`, `/portal/space/<space>/event/<slug>` | FluentCommunity front end | community/*, events/create-an-event-from-the-community-composer |

## Verified facts (code + live UI)

- Entry types: `rsvp` (default), `open` (name + email, no login), `none`. Readme describes "Open" as no registration; the UI/code say otherwise. Docs follow the UI.
- Event visibility: public, unlisted, private, draft. Calendar status: public, private, draft. Guest statuses: going (default), not_going, checked_in, cancelled. Seat statuses: going, checked_in.
- Settings defaults: default view `timeline`, view switch allowed, landing pages `no`, portal slug `events` (`FLUENT_EVENT_PORTAL_SLUG` overrides). Emails all on; reminder default 24 hours.
- Emails via `wp_mail` + Action Scheduler (group `fluent-event`). Not sent for draft events. Subjects: "You are registered for %s", "Your registration for %s is cancelled", "Reminder: %s is coming up".
- Meeting link hidden until registered on rsvp/open ("Please register for the event to see the meeting link."); visible to all on `none`.
- "You're registered" dialog with Google Calendar / Apple-Outlook (.ics) appears only after the Open-event Register form; RSVP shows a notification.
- All REST routes require `manage_options` (admin) except member/visitor registration.

## Gaps / contradictions with readme

- Readme advertises "Team permissions" for editors/authors/contributors; no such UI exists and the policy checks `manage_options`. Docs page `settings/team-permissions` is titled "Who Can Manage Events" and states admin-only. Re-check on each release.
- Not shipped: paid tickets, recurring events, member-created events, use without FluentCommunity.
- Not screenshotted: the "You're registered" dialog and the Open-event confirmation (would create a guest record on the demo site).
