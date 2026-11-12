#!/usr/bin/env python3
"""Generates scripts/screenshots/plans/*.json for the FluentEvent docs (regression fixtures).
Run: python3 scripts/screenshots/mkplans.py   then   npm run shots -- scripts/screenshots/plans/<slug>.json"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'plans')
os.makedirs(OUT, exist_ok=True)
VP = {"width": 1440, "height": 900}

def plan(slug, cat, short, steps, doc=None):
    p = {"doc": f"docs/{cat}/{doc or slug}.md", "outDir": f"public/images/{cat}/{short}", "viewport": VP, "steps": steps}
    json.dump(p, open(os.path.join(OUT, f"{slug}.json"), 'w'), indent=2)

def shot(name, clip="app", **kw):
    d = {"name": name, "clip": clip}; d.update(kw); return {"shot": d}
def arrow(target, frm="left", ln=140): return {"target": target, "from": frm, "len": ln}
def sec(t): return {"selector": "section.fe-form__section", "hasText": t}
def admin(r): return {"admin": r}
def front(u, login=True, **kw): d = {"front": u, "waitUntil": "load", "contentWidth": False, "hideThemeHeader": False, "login": login}; d.update(kw); return d
def vbtn(n): return {"click": f"button.fe-switch__option[aria-label=\"{n}\"]"}
W = {"wait": 900}

# ---------------- getting-started
plan('fluent-event-introduction', 'getting-started', 'introduction', [
  admin('/'), shot('1.-Admin-Dashboard'),
  front('/portal/'), {"wait": 1500}, shot('2.-Event-In-Feed', clip="viewport"),
], 'fluent-event-introduction')

plan('install-and-activate-fluent-event', 'getting-started', 'install-activate', [
  front('/wp-admin/plugins.php?s=fluent'), {"wait": 800},
  {"hideCss": "#wpadminbar, .notice, .update-nag"},
  shot('1.-Plugins-Screen', clip="viewport"),
  admin('/'),
  {"css": "#adminmenumain,#adminmenuback,#adminmenuwrap{visibility:visible!important}"},
  shot('2.-FluentEvent-Menu', clip={"x": 0, "y": 32, "width": 200, "height": 460}),
], 'install-and-activate-fluent-event')

plan('create-your-first-event', 'getting-started', 'first-event', [
  admin('/events'), shot('1.-Add-Event-Button', arrows=[arrow({"text": "Add Event"}, "bottom", 110)]),
  admin('/events/new'),
  {"fill": {"selector": "input[placeholder=\"e.g. Friday Q&A\"]", "value": "Friday Q&A"}},
  shot('2.-New-Event-Form'),
  front('/portal/events'), {"wait": 1200}, shot('3.-Event-In-Portal', clip="viewport"),
], 'create-your-first-event')

plan('fluent-event-admin-overview', 'getting-started', 'admin-overview', [
  admin('/'), shot('1.-Admin-Top-Navigation', badges=[
     {"target": {"selector": ".fe-navbar a", "hasText": "Dashboard"}, "n": 1, "pos": "bottom"},
     {"target": {"selector": ".fe-navbar a", "hasText": "Calendars"}, "n": 2, "pos": "bottom"},
     {"target": {"selector": ".fe-navbar a", "hasText": "Events"}, "n": 3, "pos": "bottom"},
     {"target": {"selector": ".fe-navbar a", "hasText": "Settings"}, "n": 4, "pos": "bottom"}]),
], 'fluent-event-admin-overview')

# ---------------- dashboard
plan('admin-dashboard-and-guest-stats', 'dashboard', 'dashboard', [
  admin('/'), shot('1.-Dashboard-Overview', crop="auto"),
  shot('2.-Guest-Trends-Chart', clip={"element": ".fe-dashboard__chart", "pad": 24}),
], 'admin-dashboard-and-guest-stats')

# ---------------- events
plan('create-an-event-from-the-admin', 'events', 'create-event-admin', [
  admin('/events'), shot('1.-Events-List', arrows=[arrow({"text": "Add Event"}, "bottom", 110)]),
  admin('/events/new'),
  {"fill": {"selector": "input[placeholder=\"e.g. Friday Q&A\"]", "value": "Friday Q&A"}},
  shot('2.-Create-Event-Form'),
  {"scrollTo": sec("Basics")}, shot('3.-Basics-Section', clip={"element": sec("Basics"), "pad": 20}, highlights=[{"row": "Event name", "part": "row"}]),
  {"scrollTo": sec("Registration")}, shot('4.-Registration-Section', clip={"element": sec("Registration"), "pad": 20}),
], 'create-an-event-from-the-admin')

plan('event-details-and-settings', 'events', 'event-details', [
  admin('/events/new'),
  {"scrollTo": sec("Cover image")}, shot('1.-Cover-Image-Section', clip={"element": sec("Cover image"), "pad": 20}),
  {"scrollTo": sec("Visibility")}, shot('2.-Visibility-Options', clip={"element": sec("Visibility"), "pad": 20}),
  {"scrollTo": sec("Date and time")}, shot('3.-Date-And-Time', clip={"element": sec("Date and time"), "pad": 20}),
  {"scrollTo": sec("Venue type")}, shot('4.-In-Person-Venue', clip={"element": sec("Venue type"), "pad": 20}),
  {"click": {"selector": "section.fe-form__section :is(label,button,[role=radio])", "hasText": "Online"}}, W,
  {"scrollTo": sec("Venue type")}, shot('5.-Online-Venue', clip={"element": sec("Venue type"), "pad": 20}),
], 'event-details-and-settings')

plan('event-entry-modes-rsvp-and-open', 'events', 'entry-modes', [
  admin('/events/new'),
  {"scrollTo": sec("Registration")}, shot('1.-Entry-Type-Options', clip={"element": sec("Registration"), "pad": 20}),
  admin('/events/1'), shot('2.-Registration-Type-On-Event', clip={"element": ".fe-event-overview", "pad": 20},
        highlights=[".fe-event-overview__badges"]),
], 'event-entry-modes-rsvp-and-open')

plan('manage-events-list-views', 'events', 'list-views', [
  admin('/events'), vbtn('Cards'), W, shot('1.-Cards-View'),
  vbtn('Timeline'), W, shot('2.-Timeline-View'),
  vbtn('Calendar'), W, shot('3.-Calendar-View'),
  {"click": {"text": "Past"}}, W, vbtn('Timeline'), W, shot('4.-Past-Events'),
  {"click": {"text": "Upcoming"}}, W,
  {"click": ".fe-events-view__toolbar button[aria-label=\"Filter\"], .fe-events-view__toolbar .el-button:last-child"}, W,
  shot('5.-Filter-Panel', clip="viewport"),
], 'manage-events-list-views')

plan('edit-or-delete-an-event', 'events', 'edit-delete', [
  admin('/events/1'), shot('1.-Event-Detail', crop="auto", arrows=[arrow({"text": "Edit Event"}, "left", 150)]),
  {"click": "#fe-tab-settings"}, W, shot('2.-Event-Settings-Tab', crop="auto"),
  admin('/events/1/edit'), shot('3.-Edit-Event-Form'),
], 'edit-or-delete-an-event')

plan('create-an-event-from-the-community-composer', 'events', 'portal-composer', [
  front('/portal/events'), {"wait": 1200},
  shot('1.-Create-New-Event-Button', clip="viewport", arrows=[arrow({"text": "Create new event"}, "left", 150)]),
  front('/portal/create-new-event'), {"wait": 1800},
  shot('2.-Create-Event-Page', clip="viewport"),
], 'create-an-event-from-the-community-composer')

# ---------------- calendars
plan('calendars-overview', 'calendars', 'overview', [
  admin('/calendars'), shot('1.-Calendars-List', crop="auto"),
  admin('/calendars/1'), shot('2.-Calendar-Detail', crop="auto"),
], 'calendars-overview')

plan('create-and-edit-a-calendar', 'calendars', 'create-edit', [
  admin('/calendars'), shot('1.-Create-Calendar-Button', arrows=[arrow({"text": "Create Calendar"}, "left", 150)]),
  admin('/calendars/new'), shot('2.-Create-Calendar-Form', crop="auto"),
  admin('/calendars/1/edit'), shot('3.-Edit-Calendar-Form', crop="auto"),
], 'create-and-edit-a-calendar')

plan('delete-a-calendar', 'calendars', 'delete', [
  admin('/calendars/1'), {"click": "#fe-tab-settings"}, W, shot('1.-Calendar-Danger-Zone', crop="auto"),
], 'delete-a-calendar')

# ---------------- guests
plan('manage-event-guests', 'guests', 'manage', [
  admin('/events/1'), {"click": "#fe-tab-guests"}, {"wait": 1200}, shot('1.-Guests-Tab'),
  shot('2.-Status-Filters', clip={"element": ".fe-guests__table", "pad": 16}),
], 'manage-event-guests')

plan('add-edit-and-remove-a-guest', 'guests', 'add-edit-remove', [
  admin('/events/1'), {"click": "#fe-tab-guests"}, {"wait": 1200},
  shot('1.-Add-Guest-Button', arrows=[arrow({"text": "Add Guest"}, "left", 150)]),
  {"click": {"text": "Add Guest"}}, W, shot('2.-Add-Guest-Dialog', clip={"element": ".el-dialog", "pad": 32}),
], 'add-edit-and-remove-a-guest')

plan('guest-statuses-and-check-in', 'guests', 'statuses', [
  admin('/events/1'), {"click": "#fe-tab-guests"}, {"wait": 1200},
  shot('1.-Guest-Status-Tabs'),
], 'guest-statuses-and-check-in')

# ---------------- settings & emails
plan('general-settings', 'settings', 'general', [
  admin('/settings/general'), shot('1.-General-Settings', crop="auto"),
], 'general-settings')
plan('email-notifications-overview', 'emails', 'overview', [
  admin('/settings/email-notifications'), shot('1.-Email-Notifications-Screen', crop="auto"),
], 'email-notifications-overview')
plan('confirmation-and-cancellation-emails', 'emails', 'confirm-cancel', [
  admin('/settings/email-notifications'),
  shot('1.-Registration-Email-Toggles', crop="auto", arrows=[arrow({"text": "Confirmation email"}, "left", 120)]),
], 'confirmation-and-cancellation-emails')
plan('event-reminder-emails', 'emails', 'reminders', [
  admin('/settings/email-notifications'), shot('1.-Reminder-Schedule', crop="auto", arrows=[arrow({"text": "Add reminder"}, "right", 120)]),
], 'event-reminder-emails')
plan('email-sender-settings', 'emails', 'sender', [
  admin('/settings/general'), {"scrollTo": {"text": "From name"}}, shot('1.-Email-Sender-Fields', crop="auto"),
], 'email-sender-settings')

# ---------------- community (front end)
plan('events-in-the-community-feed', 'community', 'feed', [
  front('/portal/'), {"wait": 1800}, shot('1.-Event-Post-In-Feed', clip="viewport"),
], 'events-in-the-community-feed')
plan('events-page-in-the-community-portal', 'community', 'portal-events', [
  front('/portal/events'), {"wait": 1500}, vbtn('Cards'), W, shot('1.-Events-Cards', clip="viewport"),
  vbtn('Timeline'), W, shot('2.-Events-Timeline', clip="viewport"),
  vbtn('Calendar'), W, shot('3.-Events-Calendar', clip="viewport"),
  front('/portal/space/events-meetups/home'), {"wait": 1500}, shot('4.-Space-Events', clip="viewport"),
], 'events-page-in-the-community-portal')
plan('rsvp-to-an-event', 'community', 'rsvp', [
  {"viewport": {"width": 1440, "height": 1150}},
  front('/portal/space/events-meetups/event/monthly-community-call-november', login=False), {"wait": 1800},
  shot('1.-Log-In-To-RSVP', clip="viewport"),
  front('/portal/space/events-meetups/event/holiday-virtual-mixer', login=False), {"wait": 1800},
  {"click": {"selector": "button", "hasText": "Register"}}, W,
  shot('2.-Open-Event-Register-Form', clip="viewport"),
  front('/portal/space/events-meetups/event/monthly-community-call-november'), {"wait": 1800},
  {"click": {"text": "Interested?"}}, W, shot('3.-Going-Or-Not-Going', clip="viewport"),
], 'rsvp-to-an-event')
plan('meeting-link-visibility', 'community', 'meeting-link', [
  {"viewport": {"width": 1440, "height": 1150}},
  front('/portal/space/events-meetups/event/monthly-community-call-november', login=False), {"wait": 1800},
  shot('1.-Meeting-Link-Hidden', clip="viewport"),
  front('/portal/space/events-meetups/event/monthly-community-call-november'), {"wait": 1800},
  shot('2.-Join-Online-Button', clip="viewport"),
], 'meeting-link-visibility')
print("plans:", len(os.listdir(OUT)))
