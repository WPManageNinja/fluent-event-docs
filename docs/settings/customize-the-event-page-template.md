---
title: Customize the Event Page Template
description: Change the layout of the public event page and the events archive with the Site Editor and the FluentEvent blocks.
---

# Customize the Event Page Template

Each public event page and the events archive use a template. On block themes you can rearrange them in the Site Editor. On classic themes FluentEvent wraps its pages in your theme's header and footer.

## Understanding the Two Templates

FluentEvent adds two templates to your site. Both sit between your theme's header and footer.

- **Single Event**: The page for one event, at `yoursite.com/event/event-name/`.
- **Events Archive**: The events list, at `yoursite.com/event/`. When you choose an **All Events Page** in [General settings](/general-settings), the archive address sends visitors to that page instead.

An administrator who opens a public event page sees an **Edit Event** link in the toolbar. It opens the event in the FluentEvent admin.

## Editing the Templates on a Block Theme

1. Go to **Appearance** › **Editor**.
2. Open **Templates**. Type `Event` in the search box to find the two templates. Their author is **FluentEvent**.
3. Choose **Single Event** or **Events Archive**.
4. Rearrange, remove or style the blocks, then click **Save**.

![The Site Editor Templates list filtered to Events Archive and Single Event from FluentEvent](/images/settings/customize-template/1.-Event-Templates-List.webp)

The **Single Event** template is built from one block for each piece of the page:

- **Event Cover**: The cover image.
- **Event Title**: The event's title.
- **Event Meta**: The date, time and place.
- **Event Calendar**: A link to the event's calendar.
- **Event Description**: The description, under **About This Event**.
- **Event Registration**: The box with the date in both timezones, the registration button, the guest count and the venue.

The default layout puts the cover on top, the title, meta, calendar and description in a wide column and the registration box in a narrow column beside it. Drop a block you do not need, or move the registration box above the description. Open **List View** to see the blocks as a tree and select any of them.

![The Single Event template in the Site Editor with the List View open and the Event Registration block selected](/images/settings/customize-template/2.-Single-Event-Template.webp)

The **Events Archive** template holds the **Fluent Events** block. Select it to change its settings, the same as on any page. See [Show events on any page](/show-events-on-any-page).

![The Events Archive template in the Site Editor with the Fluent Events block selected and its settings](/images/settings/customize-template/3.-Events-Archive-Template.webp)

## Using FluentEvent on a Classic Theme

A classic theme has no Site Editor, so FluentEvent shows its pages inside your theme's header and footer. Style them with your theme's CSS.

If your theme has its own template for events, for example `single-fe_event.php` or `archive-fe_event.php`, WordPress uses that template instead.

## What Visitors Can Never See

Whatever the template, the same visibility rules apply. Draft and private events, and events in a private or draft calendar, show a **Page not found** page. See [Public events pages](/public-events-pages).
