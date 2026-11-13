---
title: Enable FluentEvent in FluentCommunity
description: Turn on FluentEvent in FluentCommunity so members can see events, the Events page and the Events tab in your community.
---

# Enable FluentEvent in FluentCommunity

**FluentEvent** adds nothing to your community portal until you turn it on in FluentCommunity. Until then, the FluentEvent admin works, but members cannot see events, the **Events** page or the **Events** tab in spaces, and you cannot post events from the portal.

## Before You Turn It On

- Install and activate both plugins. See [Install and activate FluentEvent](/install-and-activate-fluent-event).
- Log in as a site administrator.
- Use a version of FluentCommunity that shows a **FluentEvent** card in its features list. If you do not see the card, update FluentCommunity.

## Opening the FluentEvent Settings

1. In the community portal, open **Portal Settings** and choose **Features & Addons**.
2. Scroll to **Recommended Plugins and Addons**.
3. Find **FluentEvent** and click **View Settings**.

The card shows an **Installed** badge when the plugin is active. It reads "Publish events as posts in your discussion spaces and collect RSVPs and registrations."

![The FluentEvent card in Features and Addons with an arrow pointing to View Settings](/images/getting-started/enable-fluent-event/1.-FluentEvent-Feature-Card.webp)

## Enabling FluentEvent

The **FluentEvent Settings** panel opens on the right.

1. Tick **Enable FluentEvent**.
2. Check the **Events URL slug**. The default is `events`, so the Events page is at `yoursite.com/portal/events`.
3. Click **Save Settings**.

The slug is used for the community events pages and the **Events** tab in spaces. Choose a word the community is not already using. FluentCommunity refuses an empty slug, a slug it already uses for another page, and the words it reserves for space tabs (`home`, `about`, `post`, `members`, `invitations`, `documents`, `media`, `page` and `settings`).

![The FluentEvent Settings panel with Enable FluentEvent ticked and the Events URL slug field](/images/getting-started/enable-fluent-event/2.-FluentEvent-Settings-Drawer.webp)

The panel also has an **Open Admin** button next to the note "Manage calendars, events and guests in the FluentEvent admin."

## Finishing the Setup

After you enable FluentEvent, the panel shows **Next steps**:

1. Turn on **Events** in **Menu Settings**, so the link shows in the portal menu.
2. Turn on **Events** under **Space Settings** › **Menu**, so each space shows its own **Events** tab.
3. Use **Create new event** in the feed or the space menu to post your first event.

See [Turn on Events in your community](/turn-on-events-in-your-community) for the first two steps and [Create an event from the community portal](/create-an-event-from-the-community-composer) for the third.

## Turning FluentEvent Off Again

Clear **Enable FluentEvent** and click **Save Settings**. FluentEvent then adds nothing to your community again. Your events, guests and settings stay in the FluentEvent admin.

::: warning
Changing the **Events URL slug** changes the address of the Events page, so links people already have stop working.
:::
