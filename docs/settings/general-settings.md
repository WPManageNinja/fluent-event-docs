---
title: General Settings
description: Set the default events view, control view switching, turn public landing pages on or off and set the email sender details.
---

# General Settings

**FluentEvent** › **Settings** › **General** controls how events are listed for everyone and who the event emails come from.

![The General settings screen with the events view options, landing pages and email fields](/images/settings/general/1.-General-Settings.webp)

## Events list view

- **Default events list view**: choose **Cards**, **Timeline** or **Calendar**. The default is **Timeline**. This view is used on the community Events page and in the admin.
- **Disable view change option**: when on, everyone sees the selected view and cannot switch. When off (default), users can switch to the view they prefer.

## Public landing pages

- **Enable landing pages**: when on, visitors can browse your public calendars and their events on public pages. When off (default), calendars have no public pages and their links show a not-found page.
- **Portal slug**: where the public calendars page lives. The default is `events`. Leave it empty to use the site root. Changing it breaks links people already have. If your site sets `FLUENT_EVENT_PORTAL_SLUG` in `wp-config.php`, that value is used and the field is read-only.

::: tip
Only calendars with the **Public** status appear on landing pages. See [Create and edit a calendar](/create-and-edit-a-calendar).
:::

## Email sender and footer

The same screen holds the sender details for event emails. Read [Email sender settings](/email-sender-settings) for each field.

Click **Save Settings** to keep your changes.
