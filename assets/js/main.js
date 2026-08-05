// ChristIAM- — main JavaScript
// Lightweight, no dependencies

document.addEventListener('DOMContentLoaded', function () {
  // === Theme Management ===
  var html = document.documentElement;
  var themeToggle = document.getElementById('theme-toggle');
  var savedTheme = null;

  try {
    savedTheme = localStorage.getItem('theme');
  } catch (e) {}

  // Apply saved theme on load (before render would be better, but this works)
  if (savedTheme === 'dark') {
    html.setAttribute('data-theme', 'dark');
  } else if (savedTheme === 'light') {
    html.setAttribute('data-theme', 'light');
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      var current = html.getAttribute('data-theme');
      var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      var isDark = current === 'dark' || (!current && prefersDark);

      if (isDark) {
        html.setAttribute('data-theme', 'light');
        try { localStorage.setItem('theme', 'light'); } catch (e) {}
      } else {
        html.setAttribute('data-theme', 'dark');
        try { localStorage.setItem('theme', 'dark'); } catch (e) {}
      }
    });
  }

  // === Navigation Dropdown ===
  var navDropdown = document.getElementById('nav-more');
  if (navDropdown) {
    var navTrigger = navDropdown.querySelector('.nav-trigger');

    navTrigger.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var isOpen = navDropdown.classList.toggle('is-open');
      navTrigger.setAttribute('aria-expanded', isOpen);
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function (e) {
      if (!navDropdown.contains(e.target)) {
        navDropdown.classList.remove('is-open');
        navTrigger.setAttribute('aria-expanded', 'false');
      }
    });

    // Close on Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navDropdown.classList.contains('is-open')) {
        navDropdown.classList.remove('is-open');
        navTrigger.setAttribute('aria-expanded', 'false');
        navTrigger.focus();
      }
    });
  }

  // === Mobile Hamburger ===
  var hamburger = document.getElementById('nav-hamburger');
  var nav = document.getElementById('site-nav');

  if (hamburger && nav) {
    hamburger.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('is-open');
      hamburger.classList.toggle('is-open', isOpen);
      hamburger.setAttribute('aria-expanded', isOpen);
    });
  }

  // === Smooth Scroll for Anchor Links ===
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;
      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // === Intersection Observer for Fade-in Animations ===
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.fade-in').forEach(function (el) {
    observer.observe(el);
  });
});
