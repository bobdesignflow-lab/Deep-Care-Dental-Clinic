document.addEventListener('DOMContentLoaded', () => {
  // Set Active Navigation State
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-links a');
  navLinks.forEach(link => {
    // Handle local paths or deployed paths robustly
    const linkPath = new URL(link.href, window.location.href).pathname;
    
    // Check exact path match, or if root matches index.html
    if (currentPath === linkPath || 
       (currentPath.endsWith('/') && linkPath.endsWith('index.html')) ||
       (currentPath.endsWith('index.html') && linkPath.endsWith('/'))) {
      link.setAttribute('aria-current', 'page');
      link.classList.add('active');
    }
  });

  // Mobile Navigation Toggle
  const mobileToggle = document.getElementById('mobile-toggle');
  const navMenu = document.getElementById('nav-menu');
  
  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = mobileToggle.getAttribute('aria-expanded') === 'true';
      mobileToggle.setAttribute('aria-expanded', !isExpanded);
      mobileToggle.setAttribute('aria-label', !isExpanded ? 'Close navigation menu' : 'Open navigation menu');
      mobileToggle.classList.toggle('is-open');
      navMenu.classList.toggle('is-active');
    });
  }

  // Sticky Header on Scroll
  const header = document.getElementById('site-header');
  if (header) {
    const attachStickyHeader = () => {
      if (window.scrollY > 50) {
        header.classList.add('is-scrolled');
      } else {
        header.classList.remove('is-scrolled');
      }
    };
    
    // Attach listener and trigger immediately
    window.addEventListener('scroll', attachStickyHeader);
    attachStickyHeader();
  }

  // Dynamic Year in Footer
  const yearElement = document.getElementById('current-year');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }

  // Scroll Animations using IntersectionObserver
  const animatedElements = document.querySelectorAll('.animate-on-scroll');
  if (animatedElements.length > 0) {
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            // stop observing once it's visible so it doesn't animate out and in forever
            observer.unobserve(entry.target);
          }
        });
      }, {
        rootMargin: '0px 0px -50px 0px',
        threshold: 0.1
      });

      animatedElements.forEach(el => observer.observe(el));
    } else {
      animatedElements.forEach(el => el.classList.add('is-visible'));
    }
  }
  
  // Accordion Logic
  const accordions = document.querySelectorAll('.accordion');
  if (accordions.length > 0) {
    accordions.forEach(accordion => {
      const triggers = accordion.querySelectorAll('.accordion-trigger');
      
      triggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
          const isExpanded = trigger.getAttribute('aria-expanded') === 'true';
          const contentId = trigger.getAttribute('aria-controls');
          const content = document.getElementById(contentId);
          
          // Close all other items in this accordion
          triggers.forEach(otherTrigger => {
            if (otherTrigger !== trigger) {
              otherTrigger.setAttribute('aria-expanded', 'false');
              const otherContentId = otherTrigger.getAttribute('aria-controls');
              const otherContent = document.getElementById(otherContentId);
              if (otherContent) otherContent.setAttribute('aria-hidden', 'true');
            }
          });
          
          // Toggle current item
          trigger.setAttribute('aria-expanded', !isExpanded);
          if (content) content.setAttribute('aria-hidden', isExpanded ? 'true' : 'false');
        });
      });
    });
  }
});
