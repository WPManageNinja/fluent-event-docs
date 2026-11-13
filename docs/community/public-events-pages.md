---
title: Public Events Pages
description: Share your events with visitors who are not community members using a public page for each event and an events list on your site.
---

# Public Events Pages

**Public events pages** let anyone open an event, and register for it, without logging in to FluentCommunity. They are normal pages of your WordPress site, shown inside your theme with your header and footer.

## How Public Pages Work

Every event has its own page at `yoursite.com/event/event-name/`. You can also show a list of all events on a page of your own. No switch needs to be turned on.

- **Event page**: One page for each event.
- **Events list**: A list of your public events. Without any setup it is at `yoursite.com/event/`. If you choose an **All Events Page**, that page replaces it.

To change the address or choose the list page, go to **FluentEvent** › **Settings** › **General** › **Public Pages**. See [General settings](/general-settings).

## Opening an Event's Public Page

In the admin, open the event and look at the **Public page** row on the **Overview** tab. It shows the link and a **Copy link** button. See [Edit or delete an event](/edit-or-delete-an-event).

The page shows the event's cover image, its title, the date, time and place, its calendar and **About This Event**. A box beside it holds the date in the event's timezone and in your site's timezone, a **Starts in** note, the registration button, the guest count and the venue.

![An event's public page showing the cover image, details, registration and venue](/images/community/public-pages/1.-Public-Event-Page.webp)

An online event shows a **Join online** button instead of the venue, once the visitor has registered. Before that, a note asks them to register to see the meeting link. See [Meeting link visibility](/meeting-link-visibility).

## Browsing the Events List

The list follows your default view, and visitors can switch the view unless you turned on **Disable view change option**.

- **Calendar chips**: **All** and one chip for each public calendar, so visitors can filter by calendar. A **More** chip holds the rest when there are many.
- **Search events**: Finds an event by name.
- **All**, **Upcoming** and **Past**: Choose which events to list. **Upcoming** is shown first.
- **View icons**: Switch between cards, timeline and calendar. The calendar view has **Month**, **Week** and **Day** buttons.

The list shows ten events at a time, with page links below. When nothing matches, it says "No events match your search."

![The public events list in timeline view with calendar chips, search and the All, Upcoming and Past buttons](/images/community/public-pages/2.-Public-Events-List.webp)

## Showing Events on Any Page

Add the events list to any page or post with the shortcode `[fluent_events]`, or with the events block in the block editor. Show a single event with `[fluent_event]` or the **Fluent Event** block.

The `[fluent_events]` shortcode accepts these options:

- **calendar**: Show one calendar, for example `calendar="workshops"`.
- **view**: Start in `cards`, `timeline` or `calendar`.
- **filter**: Start with `upcoming`, `all` or `past`.
- **view_switch**: Use `no` to hide the view icons.
- **show_calendars**: Use `no` to hide the calendar chips.

In the block editor, the same choices are in the block's **Events list** settings: **First calendar**, **Show calendar pills**, **View**, **View switcher** and **Events shown first**.

## Choosing Which Events Appear

An event has a public page only when both of these are true:

- The event's visibility is **Public** or **Unlisted**.
- The event's calendar is **Public**.

The list shows **Public** events. An **Unlisted** event is not in the list but opens from its direct link, and search engines are asked not to list it. Private and draft events, and events in a private or draft calendar, show a **Page not found** page, the same one as an event that does not exist.

## Registering from a Public Page

Visitors do not need an account. On an **RSVP** event they choose **Interested?** then **Going**. On an **Open** event they click **Register**. Both ask for a **Name** and **Email**.

After registering, the page shows **Going** or **Registered**, and a window with **Add to calendar** links opens. A visitor cannot change the answer afterward, because there is no account to change it from. Guests who register here show **WordPress Pages** as their source in the guest list. See [Manage event guests](/manage-event-guests).

::: warning
Changing the **Event Slug** changes the address of every event and breaks links people already have. Choose it before you share your events.
:::
