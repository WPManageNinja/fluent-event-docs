---
title: Guest Statuses and Check-In
description: Learn what Going, Not Going, Checked In and Cancelled mean, how a status changes and how to check guests in at the event.
---

# Guest Statuses and Check-In

Each guest has one of four statuses. The status decides who is counted as coming and who receives reminders. You see the number of guests in each status on the tabs of the event's **Guests** tab.

![The status tabs on the Guests tab showing how many guests have each status](/images/guests/statuses/1.-Guest-Status-Tabs.webp)

## Understanding the Four Guest Statuses

- **Going**: The guest is registered and expected. This is the default for guests you add.
- **Not Going**: The guest said they cannot come.
- **Checked In**: The guest arrived and you checked them in. The check-in time is saved and shown on the guest row.
- **Cancelled**: The registration was cancelled, by the guest or by you.

Guests who are **Going** or **Checked In** hold a seat. Both count in the going numbers on your [dashboard](/admin-dashboard-and-guest-stats) and in the going count members see.

## Checking a Guest In

Check guests in as they arrive, so you know who attended.

1. Open the event and go to the **Guests** tab.
2. Click the guest's status.
3. Choose **Checked In**.

FluentEvent saves the time and shows it under the status, for example "at: November 13, 2026 5:49 am". The **Checked In** tab lists everyone you have checked in, and **Guest Details** shows the time as **Checked in**.

![The Checked In tab listing guests with their check-in times](/images/guests/statuses/2.-Checked-In-Guests.webp)

If you check in the wrong guest, change the status back to **Going**. FluentEvent clears the check-in time.

## Changing a Guest's Status

You can set any status from the same menu, or from the **Edit** dialog. Members and visitors change their own status by RSVPing. See [RSVP to an event](/rsvp-to-an-event) and [Manage event guests](/manage-event-guests).

## How Status Changes Trigger Emails

When a guest changes their own status, FluentEvent sends emails automatically, if the matching email is turned on.

- **Confirmation email**: A guest who becomes **Going** gets it.
- **Cancellation email**: A guest who moves from **Going** to **Not Going** or **Cancelled** gets it.

When you change a status as an admin, FluentEvent sends an email only if you ask for it. Tick **Send confirmation email** or **Send cancellation email** in the **Add Guest**, **Edit Guest** or **Delete Guest** dialog. Changing a status from the guest list and checking a guest in never send an email.

Reminders go only to guests who are **Going** or **Checked In**. Guests who are **Not Going** or **Cancelled** do not get them. See [Email notifications](/email-notifications-overview) for the full picture.
