# FluentEvent User Documentation

VitePress docs for the FluentEvent WordPress plugin (events, RSVPs and reminders for FluentCommunity).

```bash
npm install
npm run docs:dev      # http://localhost:5173
npm run docs:build
```

Project rules, plugin source map, screenshot workflow and skills: see `CLAUDE.md` and `.claude/`.
Screenshots are regenerated with `python3 scripts/screenshots/mkplans.py && npm run shots -- scripts/screenshots/plans/<plan>.json`
(needs the local site at http://localhost:10023 with FluentEvent + FluentCommunity active).
