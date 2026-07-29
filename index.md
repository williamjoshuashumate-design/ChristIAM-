---
layout: home
title: "ChristIAM-"
description: "A personal testimony of faith, transformation, and the journey of walking with Christ."
---

<!-- Hero Section -->
<section class="hero">
  <div class="hero-content">
    <h1 class="hero-title">I AM</h1>
    <p class="hero-subtitle">A testimony of faith, transformation, and the One who makes all things new.</p>
    <div class="hero-cta">
      <a href="#testimonies" class="btn btn-primary">Read Testimonies</a>
      <a href="#about" class="btn btn-secondary">Learn More</a>
    </div>
  </div>
  <div class="hero-scripture">
    <p class="scripture-text">"I AM who I AM."</p>
    <p class="scripture-ref">— Exodus 3:14</p>
  </div>
</section>

<!-- Welcome Section -->
<section id="about" class="welcome">
  <div class="welcome-content">
    <h2>Welcome</h2>
    <p>
      ChristIAM- is more than a project — it's a testimony. A space to share stories of how
      God's grace has moved, healed, and transformed lives. Here you'll find personal
      accounts of faith, reflections on Scripture, and the journey of walking with the One
      who calls Himself "I AM."
    </p>
    <p>
      Whether you're seeking encouragement, exploring faith, or have a story of your own to
      share, you're welcome here.
    </p>
  </div>
</section>

<!-- The Network -->
<section class="network-section">
  <h2>The Network</h2>
  <div class="network-grid">
    <a href="{{ '/foundation/' | relative_url }}" class="network-card">
      <h3>The Foundation</h3>
      <p class="network-tagline">I AM Clean Water</p>
      <p>Bathhouse and laundry facilities bringing clean water access to remote communities across 6 countries. 2,950+ people served.</p>
    </a>
    <a href="{{ '/gallery/' | relative_url }}" class="network-card">
      <h3>The Gallery</h3>
      <p class="network-tagline">From Darkness to Light</p>
      <p>Spiritual warfare on canvas. Each piece a demon faced and overcome — despair, self-hatred, isolation, and more.</p>
    </a>
    <a href="{{ '/kingdom/' | relative_url }}" class="network-card">
      <h3>The Kingdom</h3>
      <p class="network-tagline">One Story · Many Rooms</p>
      <p>Every project, every app, every creative work — all connected under one name. Click any room to enter.</p>
    </a>
  </div>
</section>

<!-- Featured Testimonies -->
<section id="testimonies" class="featured-testimonies">
  <h2>Featured Testimonies</h2>
  <div class="testimony-grid">
    <!-- Testimony cards will be dynamically populated from _posts/ -->
    <p class="coming-soon">New testimony entries coming soon.</p>
  </div>
</section>

<!-- Contact / Message Section -->
<section id="contact" class="home-contact">
  <h2>Send a Message</h2>
  <p class="contact-intro">
    Have a question, a story to share, or want to collaborate? Send a message directly — it goes straight to Will's inbox.
  </p>

  <form id="contact-form" class="contact-form">
    <div class="form-row">
      <div class="form-group">
        <label for="contact-name">Name</label>
        <input type="text" id="contact-name" name="name" required maxlength="200" placeholder="Your name" autocomplete="name">
      </div>
      <div class="form-group">
        <label for="contact-email">Email</label>
        <input type="email" id="contact-email" name="email" required maxlength="200" placeholder="you@example.com" autocomplete="email">
      </div>
    </div>
    <div class="form-group">
      <label for="contact-message">Message</label>
      <textarea id="contact-message" name="message" required maxlength="5000" rows="5" placeholder="What's on your heart?"></textarea>
    </div>
    <button type="submit" class="btn btn-primary contact-submit" id="contact-submit">Send Message</button>
    <p class="contact-status" id="contact-status"></p>
  </form>

  <div class="contact-alt">
    <p>Prefer to reach out directly?</p>
    <a href="mailto:williamjoshuashumate@gmail.com" class="contact-email-link">williamjoshuashumate@gmail.com</a>
    <span class="contact-sep">·</span>
    <a href="https://app.base44.com/superagent/6a59e07644b17116ea62b443" target="_blank" rel="noopener" class="contact-email-link">Talk to IAM &rarr;</a>
  </div>
</section>

<script>
(function() {
  var form = document.getElementById('contact-form');
  var status = document.getElementById('contact-status');
  var submitBtn = document.getElementById('contact-submit');
  var endpoint = 'https://untitled-copy-ea62b443.base44.app/functions/receiveContactMessage';

  form.addEventListener('submit', function(e) {
    e.preventDefault();
    submitBtn.disabled = true;
    submitBtn.textContent = 'Sending...';
    status.className = 'contact-status';
    status.textContent = '';

    var data = {
      name: document.getElementById('contact-name').value.trim(),
      email: document.getElementById('contact-email').value.trim(),
      message: document.getElementById('contact-message').value.trim()
    };

    fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    })
    .then(function(res) { return res.json(); })
    .then(function(result) {
      if (result.ok) {
        status.className = 'contact-status contact-success';
        status.textContent = 'Message sent. Will get back to you soon.';
        form.reset();
      } else {
        status.className = 'contact-status contact-error';
        status.textContent = result.error || 'Something went wrong. Please try again.';
      }
    })
    .catch(function() {
      status.className = 'contact-status contact-error';
      status.textContent = 'Could not send. Please email williamjoshuashumate@gmail.com directly.';
    })
    .finally(function() {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Send Message';
    });
  });
})();
</script>
