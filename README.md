# ChristIAM-

> A personal testimony website built with Jekyll and deployed on GitHub Pages.

## About

ChristIAM- is a personal testimony project — sharing stories of faith, transformation, and the journey of walking with Christ. The name reflects the identity found in the One who said "I AM" (Exodus 3:14).

This site is built using [Jekyll](https://jekyllrb.com/), a static site generator, and hosted on [GitHub Pages](https://pages.github.com/).

## Features

- 📖 Personal testimony and faith stories
- 🌐 Hosted free on GitHub Pages
- ⚡ Fast, static, and lightweight
- 📱 Responsive design out of the box
- 📝 Easy content updates via Markdown

## Getting Started

### Prerequisites

- [Ruby](https://www.ruby-lang.org/) (version 2.7.0 or higher)
- [Jekyll](https://jekyllrb.com/docs/installation/)
- [Git](https://git-scm.com/)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/williamjoshuashumate-design/ChristIAM-.git
   cd ChristIAM-
   ```

2. **Install dependencies:**
   ```bash
   bundle install
   ```

3. **Run the site locally:**
   ```bash
   bundle exec jekyll serve
   ```

4. **View the site:**
   Open your browser to `http://localhost:4000`

### Deployment

The site deploys automatically when changes are pushed to the `main` branch. GitHub Pages handles the build and hosting — no manual deployment needed.

## Installation & Setup Guide

This section walks through setting up a local development environment for the ChristIAM- site from scratch, including installing Ruby, Jekyll, and all required dependencies.

### Step 1: Install Ruby

Jekyll requires Ruby version 2.7.0 or higher.

#### macOS (using Homebrew)
```bash
brew install ruby
```
After installation, add the Ruby bin directory to your PATH (add to `~/.zshrc` or `~/.bash_profile`):
```bash
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

#### Ubuntu / Debian
```bash
sudo apt-get update
sudo apt-get install ruby-full build-essential zlib1g-dev
```

#### Windows
Download and run [Ruby Installer for Windows](https://rubyinstaller.org/). Use the recommended default options, including installing MSYS2.

#### Verify Ruby installation
```bash
ruby -v
```
You should see output like `ruby 3.x.x`.

### Step 2: Install Jekyll and Bundler

Jekyll is a Ruby gem. Install it along with Bundler (which manages Ruby project dependencies):

```bash
gem install jekyll bundler
```

#### Verify Jekyll installation
```bash
jekyll -v
```

### Step 3: Clone the Repository

```bash
git clone https://github.com/williamjoshuashumate-design/ChristIAM-.git
cd ChristIAM-
```

### Step 4: Install Project Dependencies

The project uses a `Gemfile` to manage its Ruby gem dependencies (including the `github-pages` gem that matches the version GitHub Pages uses in production).

```bash
bundle install
```

> **Note:** If you get a permissions error on macOS, do **not** use `sudo`. Instead, configure your gem install directory:
> ```bash
> bundle config set --local path 'vendor/bundle'
> bundle install
> ```

### Step 5: Run the Site Locally

Start the Jekyll development server:

```bash
bundle exec jekyll serve
```

This builds the site and serves it at `http://localhost:4000`. The server watches for file changes and automatically regenerates the site — just refresh your browser to see updates.

#### Useful serve flags
- `--livereload` — auto-reload the browser on changes:
  ```bash
  bundle exec jekyll serve --livereload
  ```
- `--open` — automatically open the browser:
  ```bash
  bundle exec jekyll serve --open
  ```
- `--port 4001` — use a different port:
  ```bash
  bundle exec jekyll serve --port 4001
  ```

### Step 6: Build for Production

To generate a production-ready static site (output goes to `_site/`):

```bash
bundle exec jekyll build
```

To build with production environment variables:
```bash
JEKYLL_ENV=production bundle exec jekyll build
```

### Troubleshooting

| Issue | Solution |
|-------|----------|
| `bundle: command not found` | Run `gem install bundler` |
| Permission errors on `gem install` | Configure a user gem directory (see Step 4 note) |
| `jekyll: command not found` | Run via `bundle exec jekyll serve` instead of `jekyll serve` |
| Port 4000 already in use | Use `--port 4001` or another free port |
| Build errors after updating gems | Run `bundle update` to refresh dependencies |
| `__DIR__` or encoding errors | Ensure Ruby version is 2.7.0 or higher (`ruby -v`) |

## Project Structure

```
ChristIAM-/
├── _posts/          # Blog posts and testimony entries (Markdown)
├── _layouts/        # Page layout templates
├── _includes/       # Reusable page components
├── _config.yml      # Jekyll configuration file
├── index.md         # Homepage content
├── README.md        # This file
└── LICENSE          # CC0 1.0 Universal (Public Domain)
```

## Writing Content

To add a new testimony or post, create a new Markdown file in `_posts/` using the naming convention:

```
YYYY-MM-DD-title-of-post.md
```

Each post should include front matter:

```yaml
---
layout: post
title: "Your Title Here"
date: YYYY-MM-DD
---
```

## License

This project is licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) — released into the public domain. You are free to use, share, and adapt this work without restriction.

## Acknowledgments

- [Jekyll](https://jekyllrb.com/) — the static site generator that powers this site
- [GitHub Pages](https://pages.github.com/) — free hosting and automatic deployment
- Every person who shares their testimony — your story matters

---

*"I AM who I AM." — Exodus 3:14*
