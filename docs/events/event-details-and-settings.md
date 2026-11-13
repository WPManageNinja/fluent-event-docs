---
title: Event Details and Settings
description: A reference for every field on the FluentEvent event form, including visibility, date and timezone, venue type and registration options.
---

# Event Details and Settings

The event form in the admin (**FluentEvent** › **Events** › **Add Event**) and the form in the community portal share most of their fields. This page explains each section, its default value and what members see.

Two fields exist only in the admin form: **Calendar** and **Visibility**. The portal form has **Where do you want to post this event?** and **Feed post** instead. To see that form, read [Create an event from the community portal](/create-an-event-from-the-community-composer). For a step-by-step walkthrough of the admin form, see [Create an event from the admin](/create-an-event-from-the-admin).

## Adding a Cover Image

The cover image is optional. It shows at the top of the event page and on event cards in the admin and the portal.

1. Click **Click to add a cover image**.
2. Choose an image from the media library, then click **Use this image**.

After you add an image, the same area lets you **Change cover image** or **Remove cover image**. An event without a cover image still works. It just shows no banner.

![The Cover image section with an empty image area](/images/events/event-details/1.-Cover-Image-Section.webp)

## Setting the Event Name and Calendar

- **Event name** (required): The title members see, for example `Friday Q&A`. It can be up to 255 characters.
- **Calendar** (required, admin form only): The calendar the event belongs to. Pick one from the list. A colored dot shows each calendar's color, and a tag marks calendars that are not public.

An event created in the admin does not appear in the community feed. To post an event in a space, use the portal form. If no calendar exists yet, the form asks you to create one first. To learn what a calendar does, see [Calendars overview](/calendars-overview).

## Controlling Who Can Find the Event

The **Visibility** section is in the admin form. **Public** is selected by default. Choose who can find the event:

- **Public**: Anyone can find it.
- **Unlisted**: Only accessible with the direct link.
- **Private**: No public page.
- **Draft**: Not ready yet. Guests do not receive confirmation or reminder emails for a draft event.

Use **Draft** while you prepare an event, then switch to **Public** when it is ready.

An event gets its own public page only when it is **Public** or **Unlisted** and its calendar is public. You can copy the page link from the event's **Overview** tab. See [Edit or delete an event](/edit-or-delete-an-event).

![The Visibility section with Public, Unlisted, Private and Draft options](/images/events/event-details/2.-Visibility-Options.webp)

## Writing the Event Description

The description is optional. It appears on the event page, below the date and place. The editor is a simple writing area, and you format the text as you type.

- Type `/` to open a menu of blocks: **Text**, **Heading 1** to **Heading 6**, **Quote**, **Bullet list**, **Numbered list**, **Image** and **Divider**.
- Select a word to format it, for example to make it bold or add a link.
- Choose **Image** to pick a picture from the media library.

Use the description for the agenda, what to bring or who is speaking. If an event has no description, its admin page shows **No description yet** and offers **Add Description**.

![The Description editor with the slash menu open showing Text, headings and Quote](/images/events/event-details/3.-Description-Editor.webp)

## Setting the Date, Time and Timezone

A new event starts at the next full hour and lasts one hour. Change either value to suit your event.

- **Start** and **End**: Each has a date and a time. The end must be after the start. The end date cannot be earlier than the start date.
- **Timezone**: The timezone the times are entered in. It defaults to your site's timezone. Guests see the event time in that timezone and also in the site's timezone, so they can check it against their own clock.

An event can run for several days. In the calendar view, a multi-day event appears on each day it covers.

![The Date and time section with start, end and timezone fields](/images/events/event-details/4.-Date-And-Time.webp)

## Choosing In Person or Online

**In person** is selected by default. Switch to **Online** for an event with a meeting link.

- **In person**: Enter a **Venue name** (up to 255 characters, for example `Kingsway Hall`) and an **Address** (up to 500 characters, for example street, city and country).

![The Venue type section set to In person with venue name and address fields](/images/events/event-details/5.-In-Person-Venue.webp)

- **Online**: Enter a **Meeting link** (required). Only `http` and `https` links are accepted. Who can see the link depends on the registration type. See [Meeting link visibility](/meeting-link-visibility).

![The Venue type section set to Online with a meeting link field](/images/events/event-details/6.-Online-Venue.webp)

An in-person event with no venue name shows **No venue yet** on its admin page.

## Configuring Event Registration

The **Registration** section decides how guests join and what they see.

- **Entry type**: **RSVP** is selected by default.
    - **RSVP**: Logged-in members say whether they are going.
    - **Open**: Guests register with a name and email, with no login needed.
    - **None**: Nobody registers.
- **Show how many guests are going**: Turned on by default. It displays the going count to members.

To compare the entry types, see [RSVP and Open modes](/event-entry-modes-rsvp-and-open). Click **Create Event** (or **Update Event** when editing) to save.
