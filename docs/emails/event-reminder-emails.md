---
title: Event Reminder Emails
description: Send guests one or more reminders before an event starts, choose how long before, and learn how reminders react to event changes.
---

# Event Reminder Emails

**Reminder emails** remind registered guests that an event is about to start. You choose how long before the start each reminder goes out.

## Turning On Reminder Emails

Go to **FluentEvent** › **Settings** › **Email Notifications** and turn on **Reminder emails**. They are on by default.

![The Reminders section with a schedule set to 24 hours before](/images/emails/reminders/1.-Reminder-Schedule.webp)

## Setting the Reminder Schedule

The **Schedule** list holds up to 5 reminders. Each has a number and a unit:

- **Minutes before**
- **Hours before**
- **Days before**

The default is one reminder, **24 Hours before**. Click **Add reminder** to add another, for example 1 day and 15 minutes. A reminder can be at most 30 days before the event. Click **Save Settings** when you finish.

## Which Guests Receive a Reminder

Every guest of the event except those whose status is **Not Going** or **Cancelled**. Reminders are sent only for events whose visibility is **Public**, **Unlisted** or **Private**, so a **Draft** event sends none.

The subject is "Reminder:" followed by the event name and "is coming up". The email states the start date, time and timezone.

## How Reminders Respond to Event Changes

- Reminders are scheduled when you create an event.
- If you change an event's start time, its reminders are rescheduled to match.
- If you delete an event, its queued reminders are cancelled.
- If you change the schedule in settings, reminders for upcoming events are rescheduled.

Reminders are sent by a background task, so they go out on the schedule even when nobody is in the admin.
