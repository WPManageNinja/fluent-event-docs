---
title: Email Notifications Overview
description: See which emails FluentEvent sends to guests, when each is sent and where to turn them on or off.
---

# Email Notifications Overview

**FluentEvent** emails guests when they register, when they cancel and before an event starts. Manage all three in **FluentEvent** › **Settings** › **Email Notifications**.

## The Three Emails FluentEvent Sends

- **Confirmation email**: sent when a guest registers as going. See [Confirmation and cancellation emails](/confirmation-and-cancellation-emails).
- **Cancellation email**: sent when a guest cancels, or when an admin cancels their registration.
- **Reminder emails**: sent before the event starts, at times you choose. See [Event reminder emails](/event-reminder-emails).

All three are on by default. Each has its own switch, so you can turn any off. Click **Save Settings** after changing them.

![The Email Notifications screen with confirmation, cancellation and reminder settings](/images/emails/overview/1.-Email-Notifications-Screen.webp)

## Previewing an Email

Click the eye icon next to a switch to see what guests receive. The **Email Preview** window shows the **Subject** and the email as a guest sees it, with your footer. The preview uses sample details, such as a guest called Jane Doe, so no real guest is emailed.

- **Preview the confirmation email**: The email guests get when they register.
- **Preview the cancellation email**: The email guests get when a registration is cancelled.
- **Preview the reminder email**: The email guests get before the event starts.

![The Email Preview window showing the subject and the confirmation email](/images/emails/overview/2.-Email-Preview.webp)

## Sending Rules for Event Emails

- Emails go only to guests of events that are not drafts.
- Emails are sent with WordPress's standard mail function, so they use whatever email delivery your site has, such as an SMTP plugin.
- The sender name, reply-to address and footer are set once for all event emails. See [Email sender settings](/email-sender-settings).
- Emails are sent in the background, so they can arrive a short time after the action that triggered them.
