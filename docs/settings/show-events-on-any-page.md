---
title: Show Events on Any Page
description: Add the events list or a single event to any page, post or widget with a shortcode or a block.
---

# Show Events on Any Page

Besides the public event pages, FluentEvent can show events inside your own pages. Use a shortcode anywhere shortcodes work, or a block in the block editor.

## Choosing Shortcode or Block

- **Events list**: Use `[fluent_events]` or the **Fluent Events** block. It shows your public events with search, filters and the card, timeline and calendar views.
- **Single event**: Use `[fluent_event]` or the **Fluent Event** block. It shows one event with its details and registration.

Only events that have a public page appear. See [Public events pages](/public-events-pages).

## Adding the Events List with a Shortcode

Add `[fluent_events]` to a page, post or widget. The shortcode accepts these options:

- **calendar**: Show one calendar, using its slug, for example `calendar="workshops-training"`.
- **view**: Start in `cards`, `timeline` or `calendar`.
- **filter**: Start with `upcoming`, `all` or `past`. The default is `upcoming`.
- **view_switch**: Use `no` to hide the view icons. The default follows **Disable view change option** in [General settings](/general-settings).
- **show_calendars**: Use `no` to hide the calendar chips.

For example, `[fluent_events calendar="workshops-training" view="cards"]` shows only the workshops, as cards. When you leave **view** out, the list uses the default view from General settings.

![A page with the events shortcode showing only the Workshops and Training calendar as cards](/images/settings/show-events/1.-Events-List-Shortcode.webp)

To make a ready-made page, choose or create an **All Events Page** in **FluentEvent** › **Settings** › **General** › **Public Pages**. FluentEvent adds the events list to a page it creates, and shows the shortcode with a **Copy shortcode** button. If the page you pick has no shortcode or block yet, a warning tells you.

## Adding the Events List with the Block

In the block editor, add the **Fluent Events** block to the page. It is described as "A list of your public events, as cards, a timeline or a calendar." Select the block, and its **Events list** settings in the sidebar match the shortcode options:

- **First calendar**: The calendar shown first. Visitors can switch with the calendar pills.
- **Show calendar pills**: Turn off to keep the list on one calendar.
- **View**: **Use the setting**, **Cards**, **Timeline** or **Calendar**.
- **View switcher**: **Use the setting**, **Show** or **Hide**.
- **Events shown first**: **Upcoming**, **All** or **Past**.

In the editor the block shows sample events with the note "Sample events: the page shows your public events here." Visitors see your real events.

![The block editor with the Fluent Events block selected and its Events list settings in the sidebar](/images/settings/show-events/2.-Events-Block-Settings.webp)

## Showing One Event

Add `[fluent_event event="event-slug"]`, using the event's slug, which is the last part of its public address. Or add the **Fluent Event** block and choose the event under **Select an event**.

The event shows its details and the registration button, so visitors can register without leaving your page.

![A page with the single event shortcode showing the cover image, details, registration and venue](/images/settings/show-events/3.-Single-Event-Shortcode.webp)

::: tip
A page that holds the shortcode or a block loads FluentEvent's styles only on that page, so other pages stay fast.
:::
