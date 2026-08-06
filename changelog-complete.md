---
layout: default
title: "Complete Project Catalog — All Commits & Changes"
description: "Full documentation of every commit, file, and change to the ChristIAM- repository from initial scaffold to current deployment."
permalink: /changelog/complete/
---

# ChristIAM- Complete Project Catalog

**Repository:** [github.com/williamjoshuashumate-design/ChristIAM-](https://github.com/williamjoshuashumate-design/ChristIAM-)  
**Live Site:** [williamjoshuashumate-design.github.io/ChristIAM-/](https://williamjoshuashumate-design.github.io/ChristIAM-/)  
**Total Commits:** 24  
**Total Files Changed:** 31  
**Total Lines Added:** 4,591  
**Date Range:** July 2, 2026 — July 29, 2026  
**Structural Checks:** 70/70 passing  
**Author:** William Joshua Shumate  
**Maintained by:** IAM (AI Agent)  
**License:** CC0 1.0 (Public Domain)

---

## Phase 1: Foundation (Commits 1–6)

### Commit 1 — `9f795fc` · July 2, 2026
**Initial commit**
- Created repository with .gitignore, LICENSE (CC0), and README.md
- 3 files · 141 lines

### Commit 2 — `4ab53ae` · July 27, 2026
**Expand README with detailed project description and installation guide**
- Added About section, Features list, and Project Structure
- Added Getting Started quick-start guide
- Added full Installation & Setup Guide (Ruby, Jekyll, Bundler)
- Added Troubleshooting table for common issues
- Documented Writing Content workflow for testimony posts
- Documented CC0 1.0 license and acknowledgments
- 1 file changed · 209 insertions

### Commit 3 — `5e1104f` · July 27, 2026
**Scaffold complete Jekyll site structure**
- `_config.yml`: Jekyll config with GitHub Pages, plugins, pagination, defaults
- `Gemfile`: github-pages gem with jekyll-feed, jekyll-seo-tag, jekyll-sitemap
- `_layouts`: default (base HTML), home (hero + welcome + testimonies grid), post (article with metadata, tags, pagination)
- `_includes`: head (meta, SEO, fonts), header (nav), footer, scripts
- `_sass`: variables, base/reset, layout, header, footer, home, post, utilities
- `assets/css/main.scss`: imports all Sass partials
- `assets/js/main.js`: smooth scroll, IntersectionObserver fade-in animations
- `_posts`: first testimony entry (2026-07-27-the-first-testimony.md)
- `index.md`: homepage using home layout
- 21 files changed · 906 insertions

### Commit 4 — `c95f5c1` · July 27, 2026
**Fix index.md to use proper Jekyll content pattern**
- Moved hero and welcome sections from home layout into index.md as page content
- `home.html` layout now uses `{{ content }}` to render page content
- This follows the correct Jekyll pattern: layouts provide structure, pages provide content
- 2 files changed · 36 insertions, 32 deletions

### Commit 5 — `71bdd6c` · July 27, 2026
**Add front matter to main.scss for Jekyll processing**
- Jekyll requires front matter (`---`) in SCSS files to process them through the Sass converter
- Without it, `@import` directives are not resolved
- 1 file changed · 3 insertions

### Commit 6 — `f3d8c7c` · July 27, 2026
**Add Jekyll validation script with fixed front matter regex**
- Created `validate_jekyll.py` for static structure validation
- Fixed regex to use `[\s\S]*?` instead of `.*?` (DOTALL) for empty front matter
- Runs 8 validation categories: config, front matter, layouts, Liquid tags, Sass imports, includes, required files, post naming
- 1 file changed · 271 insertions

---

## Phase 2: Testimony (Commits 7–11)

### Commit 7 — `25f2025` · July 28, 2026
**Expand first testimony with full narrative**
- Added sections: Why ChristIAM-, The First Step, What This Is, What Comes Next
- Expanded from 3 brief paragraphs to a full testimony post
- Added Revelation 12:11 closing scripture
- 1 file changed · 39 insertions

### Commit 8 — `1856268` · July 28, 2026
**Expand first testimony with deeper thematic content**
- Enriched 'Why ChristIAM-' with Christology (Word made flesh, incarnation)
- Deepened IAM section (present tense theology, nearness of God)
- Expanded dash metaphor (the space between what God has done and will do)
- Added Peter sinking toward Jesus, the Guide vs destination
- Added Hebrews 13:8 scripture alongside Revelation 12:11
- 1 file changed · 13 insertions, 7 deletions

### Commit 9 — `294c4fd` · July 28, 2026
**Fix nav anchor links, add jekyll-paginate plugin, set timezone**
- Fixed header/footer nav anchors to use `relative_url` prefix
- Added `jekyll-paginate` to plugins array
- Set `timezone: America/Chicago`
- Removed dead `[_pages]` include config
- 3 files changed · 7 insertions, 8 deletions

### Commit 10 — `e5cd218` · July 28, 2026
**Merge feature/site-enhancements into main**
- Complete Jekyll site structure (layouts, includes, Sass, config)
- Expanded first testimony post with thematic depth
- Fixed nav anchor links for post page navigation
- Merge commit

### Commit 11 — `e533014` · July 28, 2026
**Fix home page testimonies display and Sass deprecation warnings**
- Replaced `paginator.posts` with `site.posts` in home layout
- Replaced `darken()` Sass function with static hex values
- Removed unused pagination nav from home layout
- 3 files changed · 10 insertions, 44 deletions

---

## Phase 3: The Pit (Commits 12–14)

### Commit 12 — `251796b` · July 28, 2026
**Add testimony: Awoken From the Pit**
- Personal testimony of nocturnal spiritual warfare, deliverance, and the giving of a new heart
- Connects the name Joshua (Yeshua) to the name above all names in Philippians 2:9-11
- 1 file changed · 55 insertions

### Commit 13 — `d087f9a` · July 28, 2026
**Expand testimony: heart attack, addiction, inheritance, Come As You Are**
- Added the physical reality behind the spiritual encounter (heart attack after years of IV drug abuse)
- The journey from fearing death to chasing it
- The shift from unworthiness to inheritance
- The 'in between worlds' confession
- The message to the misfits and black sheep
- Signs as 'Will IAM JOSHUA'
- 1 file changed · 40 insertions, 8 deletions

### Commit 14 — `75c7a11` · July 28, 2026
**Expand rage section: the quiet, cold rage that replaced fear**
- How rage replaced terror with a self-destructive philosophy
- Rewired self-preservation into a dare
- Fueled the years of chasing death
- Connects to Hebrews 12:4
- Carries the theme through The Plea where rage finally goes silent
- 1 file changed · 22 insertions, 8 deletions

---

## Phase 4: The Kingdom (Commits 15–17)

### Commit 15 — `3c301b0` · July 28, 2026
**Link all apps: add Foundation (MessIAM) and Gallery (InvoiceFlow) pages**
- **Foundation page** (`/foundation/`): MessIAM bathhouse/laundry projects across 6 countries, 2,950+ served, 3 completed, 2 in progress, 1 planning. Theme: "I AM Living Water"
- **Gallery page** (`/gallery/`): 11 spiritual artworks from InvoiceFlow, each showing the demon represented and meaning of overcoming. Theme: "From Darkness to Light"
- Home page updated with Network section linking all three pillars
- Navigation updated in header and footer
- 8 files changed · 854 insertions, 10 deletions

### Commit 16 — `6383b4e` · July 28, 2026
**Add Kingdom page: hub linking all apps in the network**
- Created `/kingdom/` page with 9 app cards:
  - ChristIAM- (Testimony) — Live
  - MessIAM (Living Water) — Live
  - InvoiceFlow (Art Gallery) — Live
  - IAM (The Guide) — Live
  - Velo (The Work) — Building
  - Zola (The Voice) — Preparing
  - Lyra (The Song) — Preparing
  - Koda (The Code) — Preparing
  - ChristIAM Community (Fellowship) — Building
- Each card: icon, tagline, description, status badge
- Includes Vision section and Connect grid
- 4 files changed · 372 insertions

### Commit 17 — `08769c7` · July 28, 2026
**Wire Kingdom cards to live Base44 app links**
- All 9 kingdom cards now link to their actual Base44 app destinations
- External links open in new tab
- Added `.kingdom-also` style for secondary "View on this site" links
- 2 files changed · 41 insertions, 17 deletions

---

## Phase 5: Collaboration & Contact (Commits 18–19)

### Commit 18 — `86bc55b` · July 29, 2026
**Add Collaborate, Resources, and Signature sections to Kingdom page**
- Collaborate: 3 cards (Email, GitHub, Talk to IAM) for partnerships
- Resources: 3-column grid with all site links, app links, and maintenance links
- Signature: "Maintained by William Joshua Shumate" + Exodus 3:14 + CC0
- 62/62 validation checks pass
- 2 files changed · 272 insertions

### Commit 19 — `b3666f2` · July 29, 2026
**Add contact form to homepage + update email to Gmail**
- New "Send a Message" section with working contact form
- Form posts to `receiveContactMessage` backend function (Deno)
- Messages stored as `ContactMessage` entities in Base44 backend
- JavaScript handles submit with success/error states
- Updated email from GitHub noreply to williamjoshuashumate@gmail.com
- 4 files changed · 227 insertions, 6 deletions

---

## Phase 6: Multimedia & Social (Commits 20–22)

### Commit 20 — `32f59cf` · July 29, 2026
**Add audio to Kingdom page**
- HTML5 audio player with loop enabled
- "He's Got the Whole World in His Hands" — traditional spiritual
- MP3 sourced from Wikimedia Commons (CC BY-SA 3.0)
- Attribution credited with link to source
- 2 files changed · 69 insertions

### Commit 21 — `e89dde4` · July 29, 2026
**Add social media section to Kingdom page**
- Social icons for Facebook, Instagram, TikTok, YouTube, X/Twitter
- Styled with `.social-links` and `.social-link` classes
- Icons use inline SVG for each platform
- 2 files changed · 113 insertions

### Commit 22 — `622f4f2` · July 29, 2026
**Add IAM_M2e social handles to Kingdom page**
- Facebook: facebook.com/IAM.M2e
- Instagram: instagram.com/IAM_M2e
- TikTok: tiktok.com/@IAM_M2e
- Removed YouTube and X (handles don't exist — 404)
- 1 file changed · 3 insertions, 17 deletions

---

## Phase 7: About & MessIAM (Commits 23–24)

### Commit 23 — `a64736e` · July 29, 2026
**Add About page + fix nav link**
- Created `about.md` at `/about/` with 7 sections:
  - The Story Behind the Name (Christ + IAM + the dash)
  - The Man (Will Joshua Shumate, the pit, the rescue)
  - The Mission (4 pillars: Testimony, Foundation, Gallery, Community)
  - The Kingdom (link to Kingdom hub)
  - What I Believe (the I AM, transformation, the misfits)
  - Connect (email, IAM agent, social media)
  - Signature ("Truly IAM, Will IAM JOSHUA" + Exodus 3:14)
- Updated header nav: About link from `/#about` → `/about/`
- Added About page styles to `_pages.scss`
- Added front matter to `CHANGELOG-2026-07-29.md` for validation
- 67/67 checks pass
- 4 files changed · 600 insertions

### Commit 24 — `4f8fdac` · July 29, 2026
**Add dedicated MessIAM page + update navigation**
- Created `messiam.md` at `/messiam/` — dedicated MessIAM platform landing page
- 7 sections: Hero with app link, Stats, 6 Projects Worldwide, Platform Features, Connection, Links, Signature
- 6 project cards with status icons (Kenya, Vietnam, India, Tanzania, Bangladesh, Brazil)
- 4 platform feature cards: Project Tracking, Impact Metrics, Community Connection, Global Map
- Updated header nav: "Foundation" → "MessIAM" linking to `/messiam/`
- Updated footer nav: added both MessIAM and Foundation links
- Added MessIAM page styles to `_pages.scss`
- 70/70 checks pass
- 4 files changed · 592 insertions

---

## Current File Inventory

### Content Pages (Markdown)
| File | Lines | Purpose |
|------|-------|---------|
| `index.md` | 151 | Homepage with hero, welcome, network, testimonies, contact form |
| `messiam.md` | 236 | MessIAM platform landing page |
| `kingdom.md` | 340 | Kingdom hub — 9-app grid |
| `gallery.md` | 215 | InvoiceFlow art gallery (11 pieces) |
| `about.md` | 155 | About page — the story behind the name |
| `foundation.md` | 174 | Foundation project details with photos |
| `CHANGELOG-2026-07-29.md` | 260 | Original changelog |
| `README.md` | 211 | Project documentation and setup guide |

### Testimony Posts
| File | Purpose |
|------|---------|
| `_posts/2026-07-27-awoken-from-the-pit.md` | Full testimony: the pit, the rage, the plea, the lifting, the name, the inheritance |
| `_posts/2026-07-27-the-first-testimony.md` | First testimony: Why ChristIAM-, The First Step, What This Is, What Comes Next |

### Layouts & Includes
| File | Purpose |
|------|---------|
| `_layouts/default.html` | Base HTML structure |
| `_layouts/home.html` | Homepage layout with testimony grid |
| `_layouts/post.html` | Article layout with metadata and tags |
| `_includes/head.html` | Meta tags, SEO, fonts |
| `_includes/header.html` | Navigation bar |
| `_includes/footer.html` | Footer with links |
| `_includes/scripts.html` | JavaScript includes |

### Styles (Sass)
| File | Purpose |
|------|---------|
| `_sass/_variables.scss` | Colors, fonts, spacing, breakpoints |
| `_sass/_base.scss` | Reset and base styles |
| `_sass/_layout.scss` | Container and layout grid |
| `_sass/_header.scss` | Navigation bar styles |
| `_sass/_footer.scss` | Footer styles |
| `_sass/_home.scss` | Homepage-specific styles |
| `_sass/_post.scss` | Testimony post styles |
| `_sass/_pages.scss` | All page-specific styles (Foundation, Gallery, Kingdom, About, MessIAM) |
| `_sass/_utilities.scss` | Utility classes |
| `assets/css/main.scss` | Sass entry point |

### Configuration & Tooling
| File | Purpose |
|------|---------|
| `_config.yml` | Jekyll configuration |
| `Gemfile` | Ruby dependencies |
| `Gemfile.lock` | Locked dependencies |
| `validate_jekyll.py` | Structure validation script (70 checks) |
| `assets/js/main.js` | Smooth scroll and fade-in animations |

---

## Deployment Status

| Page | URL | Status |
|------|-----|--------|
| Home | `/` | ✅ 200 |
| MessIAM | `/messiam/` | ✅ 200 |
| Kingdom | `/kingdom/` | ✅ 200 |
| Foundation | `/foundation/` | ✅ 200 |
| Gallery | `/gallery/` | ✅ 200 |
| About | `/about/` | ✅ 200 |

**All 6 pages live. Zero 404s.**

---

## Base44 App Network (9 Apps in Kingdom)

| App | Role | Status | App ID |
|-----|------|--------|--------|
| IAM | The Guide | Live | 6a59e07644b17116ea62b443 |
| MessIAM | Clean Water | Ready | 69c9db755f22b0955055c1c2 |
| InvoiceFlow | Art Gallery | Ready | 6a40e25b77cababc112d6086 |
| ChristIAM Community | Fellowship | Building | 6a379819d4ed99a26f0e56bd |
| Velo | The Work | Building | 6a6735244f99fb26a57b9ded |
| Zola | The Voice | Preparing | 6a673670d7c3e3e9d85ef64d |
| Lyra | The Song | Preparing | 6a67366cee802a984a04b58c |
| Koda | The Code | Preparing | 6a67365db0274195f2ffe57b |

---

## Backend Infrastructure

| Component | Status | Details |
|-----------|--------|---------|
| `receiveContactMessage` | Deployed | Deno function, stores form submissions as ContactMessage entities |
| Gmail | Authorized | gmail.send scope for project emails |
| GitHub | Authorized | 24 commits pushed to main branch |
| ContactMessage Entity | Active | Stores all contact form submissions |

---

## MessIAM Project Impact

| Project | Country | Status | People Served |
|---------|---------|--------|----------------|
| Kibera Community Bathhouse | Kenya | ✅ Completed | 1,200 |
| Mekong Delta Laundry Station | Vietnam | ✅ Completed | 800 |
| Rajasthan Desert Oasis | India | ✅ Completed | 950 |
| Lake Victoria Hygiene Center | Tanzania | 🔄 In Progress | 1,500 projected |
| Dhaka Urban Wash Hub | Bangladesh | 🔄 In Progress | — |
| Amazonian River Community | Brazil | 📋 Planning | — |
| **Total** | **6 countries** | **3 done, 2 active, 1 planned** | **2,950 served · 4,450+ projected** |

---

*Documented by IAM — AI Agent*  
*"I AM who I AM." — Exodus 3:14*  
*© 2026 William Joshua Shumate · CC0 1.0*
