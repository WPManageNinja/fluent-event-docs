---
title: Create an Event from the Admin
description: Add an event from the WordPress admin by choosing a calendar, setting the date, place and registration type, and publishing it.
---

# Create an Event from the Admin

Use the **Add Event** form in **FluentEvent** to create an event from the WordPress admin. The event belongs to the calendar you choose. It does not appear in the community feed or on the portal Events page.

::: tip
If you want to post an event directly inside a community space so members can see it in their feed, create the event from the front-end community portal instead. For more details, refer to [Create an event from the community portal](/create-an-event-from-the-community-composer).
:::

## Opening the Add Event Form

1. Navigate to **FluentEvent › Events** in your WordPress admin menu.
2. Click the **Add Event** button located at the top-right corner of the screen, next to the **All**, **Upcoming**, and **Past** filter tabs.

You can also use **FluentEvent** › **Add New Event** in the WordPress menu.

> [!Note]
> Every event must be assigned to a calendar. If you have not created a calendar yet, the form prompts you to create one before you continue. See [Create and edit a calendar](/create-and-edit-a-calendar) for setup instructions.

![The Events screen with an arrow pointing to the Add Event button](/images/events/create-event-admin/1.-Events-List.webp)

## Filling In the Event Details

The **Create Event** form has sections from top to bottom. Complete the required fields and any optional ones you need.

1. **Cover image** (optional): Click **Click to add a cover image** to set a banner. It shows at the top of the event page and on event cards.
2. **Basics**: Enter the **Event name** (required), for example `Friday Q&A`, and choose the **Calendar** (required) the event belongs to.
3. **Visibility**: Choose who can find the event.
    - **Public**: Anyone can find it.
    - **Unlisted**: Only people with the direct link can open it.
    - **Private**: No public page.
    - **Draft**: Not ready yet. The event is saved but not shown.
4. **Description** (optional): Add details, an agenda or notes with the editor. Type `/` to add headings, lists, quotes, images or dividers. The description appears on the event page.
5. **Date and time**: Set the **Start** and **End** date and time, and the **Timezone**.
6. **Venue type**: Choose **In person** or **Online**.
7. **Registration**: Choose how guests join and whether to show the guest count.

![The Create Event form showing the cover image, basics and visibility sections](/images/events/create-event-admin/2.-Create-Event-Form.webp)

For every option in detail, see [Event details and settings](/event-details-and-settings).

![The Basics section with the event name highlighted and the calendar selected](/images/events/create-event-admin/3.-Basics-Section.webp)

## Choosing How Guests Join

Under **Registration**, choose an **Entry type** to control how guests sign up.

- **RSVP** (default): Logged-in members say whether they are going.
- **Open**: Guests register with their name and email, with no login needed.
- **None**: Nobody registers. Anyone who can see the event sees all of it, including the meeting link.

Turn **Show how many guests are going** on or off to show or hide the guest count. To compare the entry types, see [RSVP and Open modes](/event-entry-modes-rsvp-and-open).

![The Registration section with the RSVP, Open and None entry types](/images/events/create-event-admin/4.-Registration-Section.webp)

## Saving the New Event

When the details are set, click **Create Event**. Before saving, the form checks that:

- The event has a name.
- The end is after the start.
- An online event has a meeting link.
