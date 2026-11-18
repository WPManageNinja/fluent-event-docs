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

In the admin, go to **FluentEvent** › **Events**, click **Manage Event** and stay on the **Overview** tab. The **Public page** row at the bottom shows the event's link, with a **Copy link** button next to it. Click the link to open the page in a new tab, or copy it to share. See [Edit or delete an event](/edit-or-delete-an-event).

![The event Overview tab with the Public page row highlighted showing the link and Copy link button](/images/settings/public-pages/1.-Public-Page-Row.webp)

If the row has no link, it explains why. Only **Public** and **Unlisted** events in a **Public** calendar have a public page.

The page shows the event's cover image, its title, the date, time and place, its calendar and **About This Event**. A box beside it holds the date in the event's timezone and in your site's timezone, a **Starts in** note, the registration button, the guest count and the venue.

![An event's public page showing the cover image, details, registration and venue](/images/settings/public-pages/2.-Public-Event-Page.webp)

The page is built from a template you can change. See [Customize the event page template](/customize-the-event-page-template).

An online event shows a **Join online** button instead of the venue, once the visitor has registered. Before that, a note asks them to register to see the meeting link. See [Meeting link visibility](/meeting-link-visibility).

## Browsing the Events List

The list follows your default view, and visitors can switch the view unless you turned on **Disable view change option**.

- **Calendar chips**: **All** and one chip for each public calendar, so visitors can filter by calendar. A **More** chip holds the rest when there are many.
- **Search events**: Finds an event by name.
- **All**, **Upcoming** and **Past**: Choose which events to list. **Upcoming** is shown first.
- **View icons**: Switch between cards, timeline and calendar. The calendar view has **Month**, **Week** and **Day** buttons.

The list shows ten events at a time, with page links below. When nothing matches, it says "No events match your search."

![The public events list in timeline view with calendar chips, search and the All, Upcoming and Past buttons](/images/settings/public-pages/3.-Public-Events-List.webp)

## Showing Events on Any Page

You can put the events list on any page or post of your site, and show a single event anywhere. See [Show events on any page](/show-events-on-any-page).

## Choosing Which Events Appear

An event has a public page only when both of these are true:

- The event's visibility is **Public** or **Unlisted**.
- The event's calendar is **Public**.

The list shows **Public** events. An **Unlisted** event is not in the list but opens from its direct link, and search engines are asked not to list it. Private and draft events, and events in a private or draft calendar, show your theme's "page not found" (404) page, the same one as an event that does not exist. Visitors cannot tell whether the event exists.

![The page not found message of the site theme shown for a private event](/images/settings/public-pages/4.-Page-Not-Found.webp)

## Registering from a Public Page

Visitors do not need an account. On an **RSVP** event they choose **Interested?**, and the menu offers **Going**. On an **Open** event they click **Register** instead.

![The Interested? menu on an RSVP event showing the Going option](/images/settings/public-pages/5.-RSVP-Going-Menu.webp)

Both ask for a **Name** and **Email**, then **Register**.

![The Register window with Name and Email fields and a Register button](/images/settings/public-pages/6.-Register-Form.webp)

After registering, the page shows **Going** or **Registered**, and a window with **Add to calendar** links opens. A visitor cannot change the answer afterward, because there is no account to change it from. Guests who register here show **WordPress Pages** as their source in the guest list. See [Manage event guests](/manage-event-guests).

::: warning
Changing the **Event Slug** changes the address of every event and breaks links people already have. Choose it before you share your events.
:::
