---
title: General Settings
description: Set the default events view, choose the All Events page and event address for your public pages, and set the email sender details.
---

# General Settings

**FluentEvent** › **Settings** › **General** controls how events are listed, where your public events pages live and who the event emails come from. The screen has three sections, each with its own **Save Settings** button.

![The General settings screen with the events view options, public pages and email fields](/images/settings/general/1.-General-Settings.webp)

## Choosing the Default Events List View

- **Default events list view**: Choose **Cards**, **Timeline** or **Calendar**. The default is **Timeline**. This view is used in the admin, on the community Events page and on your public events list.
- **Disable view change option**: When on, everyone sees the selected view and cannot switch. When off (default), users can switch to the view they prefer.

Click **Save Settings** in this section to keep your changes.

## Setting Up Public Pages

The **Public Pages** section controls the pages visitors can open without logging in to FluentCommunity. Event pages work without any setup. This section lets you choose where the list of all events lives. See [Public events pages](/public-events-pages).

- **All Events Page**: Choose the WordPress page that lists your events. Click the select and search for a page, or click **+** to create one.
- **Event Slug**: The first part of every event's address. The default is `event`, so each event opens at `/event/event-name/`. The text under the field shows the address.

To create a page, click **+**, enter a **Page Title** and click **Add**. FluentEvent creates the page and adds the events list to it.

![The Add Page dialog with the page title Events typed in](/images/settings/general/2.-Add-Page-Dialog.webp)

Here is an example with a page called **Events Shortcode Demo** picked. Under the field, FluentEvent shows the shortcode `[fluent_events]` with a **Copy shortcode** button and a **Preview** link. The **Event Slug** below keeps the default `event`, and the text under it shows the address, `/event/event-name/`. Nothing is saved until you click **Save Settings**.

![The Public Pages section with the page Events Shortcode Demo picked and the shortcode shown beneath it](/images/settings/general/3.-Public-Pages-Example.webp)

The shortcode and **Preview** link appear as soon as you pick a page. If the page does not hold the events list yet, a warning says "This page doesn't contain the shortcode or block yet." Add the shortcode or the events block to the page to fix it.

::: tip
Only events with the **Public** or **Unlisted** visibility in a **Public** calendar have a public page. See [Calendars overview](/calendars-overview).
:::

Click **Save Settings** in this section to keep your changes. Changing the **Event Slug** changes the address of every event, so links people already have stop working.

## Finding the Email Sender and Footer Settings

The same screen holds the sender details for event emails. Read [Email sender settings](/email-sender-settings) for each field.

Click **Save Settings** in the **Email** section to keep your changes.
