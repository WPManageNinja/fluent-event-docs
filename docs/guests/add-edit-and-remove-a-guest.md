---
title: Add, Edit and Remove a Guest
description: Add a guest by hand or from a WordPress user, edit their details and status, and remove them from an event.
---

# Add, Edit and Remove a Guest

Guests usually register themselves, but you can also add, change and remove them from the event's **Guests** tab. Use this to register someone on their behalf, fix a typo in an email or remove a guest who should not be on the list.

## Adding a Guest to an Event

1. Go to **FluentEvent** › **Events** and click **Manage Event** on the event.
2. Open the **Guests** tab.
3. Click **Add Guest**.

![The Guests tab with an arrow pointing to the Add Guest button](/images/guests/add-edit-remove/1.-Add-Guest-Button.webp)

4. Choose how to identify the guest and fill in the form.
    - **Enter manually**: Type the guest's **Name** and **Email**. Both are required.
    - **WordPress user**: Search by name or email and pick an existing user.
5. Choose the guest's **Status**. The default is **Going**.
6. Tick **Send confirmation email** if you want to email the guest.
7. Click **Add Guest**.

The **Send confirmation email** option appears only when the status is **Going** and the confirmation email is turned on in [Email notifications](/email-notifications-overview). Nothing is sent unless you tick it.

![The Add Guest dialog with Enter manually and WordPress user options](/images/guests/add-edit-remove/2.-Add-Guest-Dialog.webp)

## Editing a Guest's Details

1. In the guest list, click **More** on the guest's row.
2. Choose **Edit**.
3. Change the name, email or status.
4. Click **Update Guest**.

![The More menu open on a guest row with View, Edit and Delete](/images/guests/add-edit-remove/3.-Guest-More-Menu.webp)

When you change the status in this dialog, an email option appears if the matching email is turned on.

- **Send confirmation email**: Appears when you change the status to **Going**.
- **Send cancellation email**: Appears when you change the status to **Not Going** or **Cancelled**.

Tick the box to send the email when you save. If you leave it unticked, the status changes and no email is sent.

![The Edit Guest dialog with the guest's name, email and status](/images/guests/add-edit-remove/4.-Edit-Guest-Dialog.webp)

## Viewing Guest Details

Choose **View** in the **More** menu to open **Guest Details**. It shows the guest's name, email and picture, and these facts:

- **Status**: The current status.
- **Source**: How the guest was added, for example **Manual**.
- **Responded**: When the guest registered.
- **Checked in**: When you checked the guest in. It appears only for checked-in guests.
- **Last updated**: When the record last changed.
- **WP User**: **Yes** if the guest is linked to a WordPress user, otherwise **No**.

![The Guest Details dialog showing status, source, responded time and WP user](/images/guests/add-edit-remove/5.-Guest-Details.webp)

## Removing a Guest from an Event

1. Click **More** on the guest's row.
2. Choose **Delete**.
3. Tick **Send cancellation email** if you want the guest to know.
4. Click **Delete**.

The cancellation email option appears only for guests who are **Going** or **Checked In**, and only when the cancellation email is turned on. Removing a guest cannot be undone.

![The Delete Guest dialog with the Send cancellation email option](/images/guests/add-edit-remove/6.-Delete-Guest-Dialog.webp)

If you want to keep a record of the guest, set their status to **Cancelled** instead of deleting. See [Guest statuses and check-in](/guest-statuses-and-check-in).
