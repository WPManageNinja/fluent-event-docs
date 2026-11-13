---
title: Event Details and Settings
description: A reference for every field on the FluentEvent event form, including visibility, date and timezone, venue type and registration options.
---

# Event Details and Settings

The event form in the admin (**FluentEvent** › **Events** › **Add Event**) and the form in the community portal share most of their fields. This page explains each section.

Two fields exist only in the admin form: **Calendar** and **Visibility**. The portal form has **Where do you want to post this event?** and **Feed post** instead. To see that form, read [Create an event from the community portal](/create-an-event-from-the-community-composer).

## Adding a Cover Image

An optional image shown at the top of the event page and on event cards. Click **Click to add a cover image** to choose one from the media library. After you add one, you can change or remove it.

![The Cover image section with an empty image area](/images/events/event-details/1.-Cover-Image-Section.webp)

## Setting the Event Name and Calendar

- **Event name** (required): the title members see, for example `Friday Q&A`.
- **Calendar** (required, admin form only): the calendar the event belongs to. An event created in the admin does not appear in the community feed. To post an event in a space, use the portal form. See [Calendars overview](/calendars-overview) to learn what a calendar does.

## Controlling Who Can Find the Event

The **Visibility** section is in the admin form. Choose who can find the event:

- **Public**: anyone can find it.
- **Unlisted**: only accessible with the direct link.
- **Private**: no public page.
- **Draft**: not ready yet. Guests do not receive confirmation or reminder emails for a draft event.

![The Visibility section with Public, Unlisted, Private and Draft options](/images/events/event-details/2.-Visibility-Options.webp)

## Writing the Event Description

An optional description shown on the event page. It uses the WordPress editor with **Visual** and **Code** tabs and an **Add media** button.

## Setting the Date, Time and Timezone

- **Start** and **End**: each has a date and a time. The end must be after the start.
- **Timezone**: the timezone the times are entered in. Guests see the event time in that timezone and also in the site's timezone.

![The Date and time section with start, end and timezone fields](/images/events/event-details/3.-Date-And-Time.webp)

## Choosing In Person or Online

Choose **In person** or **Online**.

- **In person**: enter a **Venue name** and an **Address**.

![The Venue type section set to In person with venue name and address fields](/images/events/event-details/4.-In-Person-Venue.webp)

- **Online**: enter a **Meeting link** (required). Only `http` and `https` links are accepted. Who can see the link depends on the registration type. See [Meeting link visibility](/meeting-link-visibility).

![The Venue type section set to Online with a meeting link field](/images/events/event-details/5.-Online-Venue.webp)

## Configuring Event Registration

- **Entry type**: choose how guests join.
    - **RSVP**: logged-in members say whether they are going.
    - **Open**: guests register with a name and email.
    - **None**: nobody registers.
- **Show how many guests are going**: turn this on to display the going count to members.

To compare the entry types, see [RSVP and Open modes](/event-entry-modes-rsvp-and-open). Click **Create Event** (or **Update Event** when editing) to save.
