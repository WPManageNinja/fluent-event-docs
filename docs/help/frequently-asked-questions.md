---
title: Frequently Asked Questions
description: Quick answers about requirements, who can create events, registration types, meeting links, emails and your data in FluentEvent.
---

# Frequently Asked Questions

::: faq
== Does FluentEvent work without FluentCommunity?
No. Events are FluentCommunity posts, so FluentCommunity must be installed and active, and your site needs WordPress 6.7 or newer. The free version of FluentCommunity is enough. See [Install and activate FluentEvent](/install-and-activate-fluent-event).
== Who can create events?
Site administrators. The FluentEvent admin and the **Create new event** page in the portal are for administrators only. See [Who can manage events](/team-permissions).
== Can community members create events?
No. Members can browse events and RSVP, but creating events is limited to administrators.
== What is the difference between RSVP, Open and None?
With **RSVP**, logged-in members choose Going or Not going. With **Open**, anyone registers with a name and email. With **None**, nobody registers. See [RSVP and Open modes](/event-entry-modes-rsvp-and-open).
== Who can see the online meeting link?
On RSVP and Open events, only people who have registered. On events with no registration, everyone who can see the event. See [Meeting link visibility](/meeting-link-visibility).
== Why does my event show a Draft badge or no emails?
A **Draft** event is not ready. It sends no confirmation, cancellation or reminder emails. Change its visibility to **Public**, **Unlisted** or **Private** to publish it.
== Why can't I create an event?
An event needs a calendar. If you have none, the form asks you to create one. See [Create and edit a calendar](/create-and-edit-a-calendar).
== How do I change when reminders are sent?
Go to **Settings** › **Email Notifications** and edit the **Schedule**. You can set up to 5 reminders in minutes, hours or days before the start. See [Event reminder emails](/event-reminder-emails).
== Why do guests not receive emails?
Check that the email is turned on, that the event is not a draft, and that your site can send email. FluentEvent uses WordPress's standard mail function, so an SMTP plugin helps. See [Email notifications overview](/email-notifications-overview).
== Can guests add an event to their calendar?
Yes. After registering for an Open event, guests see **Google Calendar** and **Apple / Outlook** links. See [Add an event to your calendar](/add-an-event-to-your-calendar).
== Does it support paid tickets or recurring events?
Not in version 1.0.0. They are on the roadmap.
== Why does an event link show a page not found?
An event has a public page only when its visibility is **Public** or **Unlisted** and its calendar is **Public**. Private and draft events, and events in a private or draft calendar, show a not-found page. See [Public events pages](/public-events-pages).
== How do I show all my events on a page of my site?
Go to **FluentEvent** › **Settings** › **General** › **Public Pages**, choose or create an **All Events Page** and save. You can also add the `[fluent_events]` shortcode to any page. See [Public events pages](/public-events-pages).
== Can visitors register without an account?
Yes, on the public page of an event. They register with a name and email on **RSVP** and **Open** events. See [Public events pages](/public-events-pages).
== What happens to my data if I delete the plugin?
Your events, guests and settings are kept, so nothing is lost if you reinstall.
:::
