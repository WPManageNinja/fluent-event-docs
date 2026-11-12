import { defineConfig } from 'vitepress'
import { existsSync } from 'node:fs'
import { join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'
import { zoomablePlugin } from './theme/plugin-zoomable'
import { docBlocksPlugin } from './theme/plugin-doc-blocks'

// https://vitepress.dev/reference/site-config
// Canonical origin for this site — reused by the canonical links and the absolute
// og:/twitter: URLs below. Changing the host should only ever mean editing this line.
const SITE_URL = 'https://docs.fluentevent.com'

/**
 * Per-page link-preview cards.
 *
 * `scripts/generate-featured-images.mjs` renders a branded 1200x630 PNG carrying each
 * page's own title into `public/images/featured/`, served at `/images/featured/`.
 *
 * NAMING RULE — kept in sync with that script's cardNameFor(): the card is the page's
 * served path (i.e. `pageData.relativePath`, which VitePress has already passed through
 * any `rewrites`) minus `.md`, with every `/` replaced by `--`, plus `.png`. The home
 * page's `index.md` uses `index.png`.
 *
 * Anything without a generated card falls back to `default.png`, which the generator
 * also emits — so a shared link is never left with no preview at all. The URL must be
 * absolute: relative paths are ignored by Slack/X/LinkedIn/Facebook scrapers.
 */
const FEATURED_DIR = join(dirname(fileURLToPath(import.meta.url)), '..', 'public', 'images', 'featured')

function featuredImageFor(relativePath: string): string {
  const name = `${relativePath.replace(/\.md$/, '').replace(/\//g, '--')}.png`
  const file = existsSync(join(FEATURED_DIR, name)) ? name : 'default.png'
  return `${SITE_URL}/images/featured/${encodeURIComponent(file)}`
}

export default defineConfig({
  title: "FluentEvent",
  description: "Community events, RSVPs and reminders for FluentCommunity.",
  cleanUrls: true,
  // Serve docs/<category>/<slug>.md at /<slug>: the category folder is hidden from the URL
  rewrites: {
    'docs/:category/:slug.md': ':slug.md',
  },
  srcExclude: ['README.md', 'CLAUDE.md', '.claude/**/*.md', 'scripts/**/*.md'],
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/favicon.png' }],
    ['meta', { name: 'theme-color', content: '#12A9B5' }],

    // Open Graph / Twitter values that never vary per page. Every generated card is
    // 1200x630, so the dimensions live here; the image URL itself is per page and
    // is set in transformPageData() below.
    ['meta', { property: 'og:site_name', content: 'FluentEvent' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:locale', content: 'en_US' }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '630' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
  ],
  markdown: {
    config: (md) => {
      md.use(zoomablePlugin)
      md.use(docBlocksPlugin)
    }
  },
  // Per-page SEO tags: canonical URL plus the Open Graph / Twitter values that differ
  // per page, including the page's own featured image (see featuredImageFor above).
  transformPageData(pageData, { siteConfig }) {
    // `relativePath` is the path AFTER `rewrites`, so it matches the public URL.
    const path = pageData.relativePath.replace(/(^|\/)index\.md$/, '$1').replace(/\.md$/, '')
    const url = path ? `${SITE_URL}/${path}` : `${SITE_URL}/`
    const title = pageData.frontmatter.title || pageData.title || siteConfig.site.title
    const description =
      pageData.frontmatter.description || pageData.description || siteConfig.site.description
    const image = featuredImageFor(pageData.relativePath)

    pageData.frontmatter.head ??= []
    pageData.frontmatter.head.push(
      ['link', { rel: 'canonical', href: url }],
      ['meta', { property: 'og:title', content: title }],
      ['meta', { property: 'og:description', content: description }],
      ['meta', { property: 'og:url', content: url }],
      ['meta', { property: 'og:image', content: image }],
      ['meta', { property: 'og:image:alt', content: title }],
      ['meta', { name: 'twitter:title', content: title }],
      ['meta', { name: 'twitter:description', content: description }],
      ['meta', { name: 'twitter:image', content: image }]
    )
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: {
      light: '/images/brand/fluentevent-logo.svg',
      dark: '/images/brand/fluentevent-logo-dark.svg',
      alt: 'FluentEvent'
    },
    siteTitle: false,
    search: {
      provider: 'local'
    },
    nav: [
      { text: 'Home', link: '/' },
      { text: 'User Guide', link: '/fluent-event-introduction' },
      { text: 'Changelog', link: '/change-log' },
      { text: 'Website', link: 'https://fluentevent.com/' }
    ],

    sidebar: [
      {
        text: 'Get Started',
        collapsed: false,
        items: [
          { text: 'Introduction', link: '/fluent-event-introduction' },
          { text: 'Install & activate', link: '/install-and-activate-fluent-event' },
          { text: 'Create your first event', link: '/create-your-first-event' },
          { text: 'Admin overview', link: '/fluent-event-admin-overview' }
        ]
      },
      {
        text: 'Events',
        collapsed: false,
        items: [
          { text: 'Create an event (admin)', link: '/create-an-event-from-the-admin' },
          { text: 'Create an event (composer)', link: '/create-an-event-from-the-community-composer' },
          { text: 'Event details & settings', link: '/event-details-and-settings' },
          { text: 'RSVP and Open modes', link: '/event-entry-modes-rsvp-and-open' },
          { text: 'Events list & views', link: '/manage-events-list-views' },
          { text: 'Edit or delete an event', link: '/edit-or-delete-an-event' }
        ]
      },
      {
        text: 'Guests',
        collapsed: false,
        items: [
          { text: 'Manage event guests', link: '/manage-event-guests' },
          { text: 'Add, edit & remove a guest', link: '/add-edit-and-remove-a-guest' },
          { text: 'Guest statuses & check-in', link: '/guest-statuses-and-check-in' }
        ]
      },
      {
        text: 'Calendars',
        collapsed: true,
        items: [
          { text: 'Calendars overview', link: '/calendars-overview' },
          { text: 'Create & edit a calendar', link: '/create-and-edit-a-calendar' },
          { text: 'Delete a calendar', link: '/delete-a-calendar' }
        ]
      },
      {
        text: 'Dashboard',
        collapsed: true,
        items: [
          { text: 'Dashboard & guest stats', link: '/admin-dashboard-and-guest-stats' }
        ]
      },
      {
        text: 'In the Community',
        collapsed: true,
        items: [
          { text: 'Events in the feed', link: '/events-in-the-community-feed' },
          { text: 'Events page in the portal', link: '/events-page-in-the-community-portal' },
          { text: 'RSVP to an event', link: '/rsvp-to-an-event' },
          { text: 'Add to your calendar', link: '/add-an-event-to-your-calendar' },
          { text: 'Meeting link visibility', link: '/meeting-link-visibility' }
        ]
      },
      {
        text: 'Emails',
        collapsed: true,
        items: [
          { text: 'Email overview', link: '/email-notifications-overview' },
          { text: 'Confirmation & cancellation', link: '/confirmation-and-cancellation-emails' },
          { text: 'Reminder emails', link: '/event-reminder-emails' },
          { text: 'Sender settings', link: '/email-sender-settings' }
        ]
      },
      {
        text: 'Settings',
        collapsed: true,
        items: [
          { text: 'General settings', link: '/general-settings' },
          { text: 'Team permissions', link: '/team-permissions' }
        ]
      },
      {
        text: 'Help & Updates',
        collapsed: true,
        items: [
          { text: 'FAQ', link: '/frequently-asked-questions' },
          { text: 'Changelog', link: '/change-log' }
        ]
      }
    ]
  }
})
