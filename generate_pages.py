import json

header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    
    <!-- JSON-LD Breadcrumb & Service -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Service",
      "name": "{name}",
      "provider": {{
        "@type": "MedicalOrganization",
        "name": "Deep Care Dental Clinic"
      }},
      "areaServed": {{
        "@type": "Place",
        "name": "Nairobi"
      }}
    }}
    </script>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet">
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="css/tokens.css">
    <link rel="stylesheet" href="css/base.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/service-detail.css">
</head>
<body>

<!-- HEADER START -->
<header class="site-header" id="site-header">
  <div class="header-container">
    <a href="index.html" class="logo-link">
      <img src="assets/images/deep-care-dental-clinic-logo.png" alt="Deep Care Dental Clinic" class="logo-img">
    </a>
    
    <nav class="nav-menu" id="nav-menu">
      <ul class="nav-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="reviews.html">Reviews</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
      
      <div class="header-actions-mobile-only">
        <a href="tel:+254712543781" class="phone-link">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          0712 543781
        </a>
        <a href="contact.html" class="btn btn-primary">Book Appointment</a>
      </div>
    </nav>
    
    <div class="header-actions">
      <div class="header-actions-desktop">
        <a href="tel:+254712543781" class="phone-link">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          0712 543781
        </a>
        <a href="contact.html" class="btn btn-primary">Book Appointment</a>
      </div>
      
      <button class="mobile-toggle" id="mobile-toggle" aria-expanded="false" aria-controls="nav-menu" aria-label="Toggle navigation">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
      </button>
    </div>
  </div>
</header>
<!-- HEADER END -->

<main>
    <!-- 1. BREADCRUMB BAR -->
    <div class="breadcrumb-bar">
        <div class="container breadcrumbs">
            <a href="index.html">Home</a> / <a href="services.html">Services</a> / <span aria-current="page" style="color:var(--color-text); font-weight:600;">{name}</span>
        </div>
    </div>

    <!-- 2. SERVICE HERO -->
    <section class="service-detail-hero">
        <div class="container service-hero-grid">
             <div class="hero-content animate-on-scroll">
                  <div class="service-hero-icon">
                    {icon}
                  </div>
                  <span class="eyebrow">Dental Service</span>
                  <h1>{name}</h1>
                  <p>{desc}</p>
                  <div class="hero-actions">
                      <a href="contact.html" class="btn btn-accent">Book This Treatment</a>
                      <a href="tel:+254712543781" class="btn btn-secondary">Call 0712 543781</a>
                  </div>
             </div>
             <div class="hero-image animate-on-scroll delay-100">
                  <img src="assets/images/service-{slug_img}.jpg" alt="{name}">
             </div>
        </div>
    </section>

    <!-- 3. WHAT TO EXPECT -->
    <section class="what-to-expect bg-surface">
         <div class="container">
              <h2 class="animate-on-scroll">What to Expect</h2>
              <div class="what-to-expect-content animate-on-scroll delay-100">
                    {expect}
              </div>
         </div>
    </section>

    <!-- 4. BENEFITS LIST -->
    <section class="benefits-section">
         <div class="container">
              <h2 class="animate-on-scroll">Benefits</h2>
              <div class="benefits-grid">
{benefits}
              </div>
         </div>
    </section>

    <!-- 6. RELATED SERVICES -->
    <section class="related-services">
         <div class="container">
             <h3 class="animate-on-scroll">You May Also Be Interested In</h3>
             <div class="related-grid">
{related}
             </div>
         </div>
    </section>

    <!-- 7. CTA BANNER -->
    <section class="cta-banner animate-on-scroll">
        <h2>Ready for a Healthier, Confident Smile?</h2>
        <p>Join our family of happy patients. Let's make your dream smile a reality.</p>
        <a href="contact.html" class="btn btn-cta-alt">Book Your Appointment Today</a>
    </section>
</main>
"""

footer = """
<!-- FOOTER START -->
<footer class="site-footer">
  <div class="footer-container">
    <div class="footer-col">
      <img src="assets/images/deep-care-dental-clinic-logo.png" alt="Deep Care Dental Clinic" style="height: 40px; margin-bottom: 16px; filter: brightness(0) invert(1);">
      <p>Providing exceptional dental care and beautiful smiles in Nairobi, Kenya.</p>
      <div class="social-icons">
        <a href="#" aria-label="Facebook">
          <svg viewBox="0 0 24 24"><path d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5C10 7.57 11.57 6 13.5 6H16v3h-2c-.55 0-1 .45-1 1v2h3v3h-3v6.95c5.05-.5 9-4.76 9-9.95z"/></svg>
        </a>
        <a href="#" aria-label="Instagram">
          <svg viewBox="0 0 24 24"><path d="M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2zm-.2 2A3.6 3.6 0 0 0 4 7.6v8.8C4 18.39 5.61 20 7.6 20h8.8a3.6 3.6 0 0 0 3.6-3.6V7.6C20 5.61 18.39 4 16.4 4H7.6zm9.65 1.5a1.25 1.25 0 0 1 1.25 1.25A1.25 1.25 0 0 1 17.25 8 1.25 1.25 0 0 1 16 6.75a1.25 1.25 0 0 1 1.25-1.25zM12 7a5 5 0 0 1 5 5 5 5 0 0 1-5 5 5 5 0 0 1-5-5 5 5 0 0 1 5-5zm0 2a3 3 0 0 0-3 3 3 3 0 0 0 3 3 3 3 0 0 0 3-3 3 3 0 0 0-3-3z"/></svg>
        </a>
      </div>
    </div>
    
    <div class="footer-col">
      <h4>Quick Links</h4>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="reviews.html">Reviews</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    
    <div class="footer-col">
      <h4>Contact Info</h4>
      <ul class="footer-links">
        <li>
          <strong>Address:</strong><br>
          3rd Floor, Room 304, Popman House,<br>
          Moi Avenue, Near Khoja Mosque,<br>
          Nairobi, Kenya
        </li>
        <li style="margin-top: 8px;">
          <strong>Phone:</strong><br>
          <a href="tel:+254712543781">0712 543781</a>
        </li>
        <li style="margin-top: 8px;">
          <strong>Hours:</strong><br>
          Mon–Sat: 8:00 AM – 5:30 PM
        </li>
      </ul>
    </div>
    
    <div class="footer-col">
      <h4>Ready for a new smile?</h4>
      <p style="margin-bottom: 16px;">Book your appointment today and let us take care of your dental health.</p>
      <a href="contact.html" class="btn btn-primary" style="width: 100%;">Book an Appointment</a>
    </div>
  </div>
  
  <div class="footer-bottom">
    <p>&copy; <span id="current-year">2026</span> Deep Care Dental Clinic. All rights reserved.</p>
  </div>
</footer>
<!-- FOOTER END -->

<script src="js/main.js"></script>
</body>
</html>
"""

SVG_MAPPING = {
    "Professional Teeth Cleaning": '<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 12s1.5 2 4 2 4-2 4-2"/></svg>',
    "Teeth Whitening": '<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    "Root Canal Treatment": '<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 22h20L12 2z"/></svg>',
    "Gum Treatment": '<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>',
    "Dentures": '<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/></svg>',
    "Dental Fillings": '<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>',
    "Braces": '<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
    "Crowns and Bridges": '<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18"/><path d="M3 6h18"/><path d="M3 18h18"/></svg>',
    "Tooth Extractions": '<svg class="service-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>'
}

SLUGS_MAPPING = {
    "Professional Teeth Cleaning": "cleaning.html",
    "Teeth Whitening": "teeth-whitening.html",
    "Root Canal Treatment": "root-canal-treatment.html",
    "Gum Treatment": "gum-treatment.html",
    "Dentures": "dentures.html",
    "Dental Fillings": "dental-fillings.html",
    "Braces": "braces.html",
    "Crowns and Bridges": "crowns-and-bridges.html",
    "Tooth Extractions": "tooth-extractions.html"
}

services = [
    {
        "name": "Professional Teeth Cleaning",
        "desc": "Routine cleaning to remove plaque and tartar buildup, polish teeth, and support long-term gum health. Recommended every 6 months.",
        "expect": "<p>A typical professional teeth cleaning takes about 30 to 45 minutes and is a virtually painless process ideal for nervous first-time patients. First, one of our dental professionals will examine your mouth with a small mirror to check your overall oral health.</p><p>Next, we use gentle, specialized tools to remove any hardened plaque (tartar) around your gum line and between your teeth. Once the tartar is cleared, we brush your teeth with a high-powered electric brush and special gritty toothpaste to gently scrub away stains and polish the enamel. The final step is expert flossing to ensure every spot is clean.</p>",
        "benefits": [
            "Plaque & Tartar Removal", "Fresher Breath", "Gum Disease Prevention"
        ],
        "related": ["Teeth Whitening", "Gum Treatment", "Dental Fillings"]
    },
    {
        "name": "Teeth Whitening",
        "desc": "Safe, professional whitening treatment to brighten smiles and remove surface staining, more effective and even than over-the-counter kits.",
        "expect": "<p>Our professional teeth whitening process is safe, highly effective, and tailored to give you a brighter smile without causing discomfort. First, we'll perform a quick check to make sure your teeth and gums are healthy enough for whitening.</p><p>Then, we protect your lips and gums before carefully applying a professional-grade whitening gel directly to your teeth. A specialized light may be used to enhance the gel's effectiveness. The entire process takes about an hour, allowing you to walk out with a noticeably whiter and more confident smile the very same day.</p>",
        "benefits": [
            "Brighter, Confident Smile", "Safe for Tooth Enamel", "Immediate Results"
        ],
        "related": ["Professional Teeth Cleaning", "Crowns and Bridges", "Braces"]
    },
    {
        "name": "Root Canal Treatment",
        "desc": "Gentle treatment to save an infected or badly decayed tooth by removing damaged pulp, cleaning the canal, and sealing it \u2014 relieves pain and preserves the natural tooth.",
        "expect": "<p>The idea of a root canal often makes people nervous, but with modern anesthetics, it feels very similar to getting a standard cavity filling. We prioritize your comfort every step of the way. First, we completely numb the area around the affected tooth so you won't feel any pain.</p><p>Next, we create a tiny opening in the tooth to gently remove the infected or damaged tissue inside. After thoroughly cleaning and disinfecting the inner space, we fill and seal it to prevent any future infection. You'll leave the clinic with your natural tooth saved and free of the pain that brought you in.</p>",
        "benefits": [
            "Stops Tooth Pain", "Saves Natural Tooth", "Prevents Further Infection"
        ],
        "related": ["Dental Fillings", "Crowns and Bridges", "Tooth Extractions"]
    },
    {
        "name": "Gum Treatment",
        "desc": "Treatment for gum disease ranging from deep cleaning to more advanced periodontal care, focused on protecting gum and bone health.",
        "expect": "<p>Gum treatment is essential for reversing early signs of gum disease, such as bleeding or swollen gums, and is designed to restore your gums to a healthy, pink, and firm state. The process begins with a careful evaluation of the health of your gum tissue.</p><p>For mostly mild cases, we perform a deep cleaning called scaling and root planing. This involves gently numbing your gums and meticulously clearing away bacteria and tartar buildup deep below the gumline. By smoothing the tooth roots, we help your gums reattach securely to the teeth, promoting natural healing and stopping disease progression.</p>",
        "benefits": [
             "Stops Bleeding Gums", "Protects Tooth Roots", "Reverses Early Disease"
        ],
        "related": ["Professional Teeth Cleaning", "Tooth Extractions", "Dentures"]
    },
    {
        "name": "Dentures",
        "desc": "Custom-fitted full or partial dentures to replace missing teeth, restore chewing function, and support natural facial structure.",
        "expect": "<p>Getting dentures is a step-by-step process focused completely on your comfort and getting the perfect fit. During your first visit, we will take precise impressions (molds) and measurements of your mouth to ensure your new teeth look natural and fit securely.</p><p>Once the dentures are custom-made in the lab, you will return for a fitting. We will have you try them on and make small, careful adjustments to ensure they feel comfortable when you speak and chew. We'll also take the time to teach you exactly how to care for your new smile at home.</p>",
        "benefits": [
            "Restores Chewing Ability", "Supports Facial Shape", "Custom, Natural Look"
        ],
        "related": ["Tooth Extractions", "Crowns and Bridges", "Gum Treatment"]
    },
    {
        "name": "Dental Fillings",
        "desc": "Durable, tooth-colored fillings to repair cavities and restore damaged teeth, blending naturally with your smile.",
        "expect": "<p>Getting a dental filling is a very straightforward and routine procedure aimed at fixing a cavity before it causes pain or further damage. Before we start, we use a local anesthetic to gently numb the tooth and the surrounding area so you remain completely comfortable.</p><p>Once you are numb, we carefully remove the decayed portion of the tooth. We then thoroughly clean the space and fill it with a completely safe, tooth-colored resin material. The material is hardened quickly with a special blue light and then smoothed out so your bite feels completely natural.</p>",
        "benefits": [
            "Stops Cavity Growth", "Tooth-Colored Blending", "Strengthens Damaged Tooth"
        ],
        "related": ["Root Canal Treatment", "Tooth Extractions", "Professional Teeth Cleaning"]
    },
    {
        "name": "Braces",
        "desc": "Orthodontic treatment to gradually straighten teeth and correct bite issues for a healthier, more confident smile, suitable for teens and adults.",
        "expect": "<p>Starting your journey with braces is an exciting step toward an incredible smile. Your first appointment is all about planning. We take digital photos, X-rays, and molds of your teeth to figure out exactly how they need to move over time.</p><p>When it's time to get the braces on, the procedure is entirely painless. We clean your teeth and carefully bond small brackets to the front of each tooth. We then connect them with a thin wire held in place with tiny bands. Because we use light, continuous pressure, you may feel some normal tenderness an hour or so later as your teeth begin to adjust.</p>",
        "benefits": [
            "Straightens Crooked Teeth", "Corrects Bite Alignment", "Long-term Confidence"
        ],
        "related": ["Teeth Whitening", "Professional Teeth Cleaning", "Gum Treatment"]
    },
    {
        "name": "Crowns and Bridges",
        "desc": "Custom crowns to restore damaged teeth and bridges to replace missing teeth, both designed to match your natural teeth in shape and color.",
        "expect": "<p>Crowns and bridges are excellent ways to rebuild your smile securely and beautifully, usually taking two visits. In the first visit, we numb the area completely to ensure your comfort, then gently shape the affected teeth so the crown or bridge will fit perfectly over them.</p><p>We then take a highly accurate mold to send to our lab, and provide you with a temporary artificial tooth to protect your smile in the meantime. During your second visit usually a couple of weeks later, we remove the temporary piece and permanently cement your custom-made, natural-looking final piece into place.</p>",
        "benefits": [
             "Protects Weak Teeth", "Fills Missing Gaps", "Matches Natural Teeth"
        ],
        "related": ["Root Canal Treatment", "Dentures", "Dental Fillings"]
    },
    {
        "name": "Tooth Extractions",
        "desc": "Safe, gentle removal of severely damaged, decayed, or problematic teeth when other treatments aren't viable, performed with patient comfort as priority.",
        "expect": "<p>While hearing you need a tooth extraction can be intimidating, we specialize in making the process fast, safe, and as stress-free as possible. First and foremost, we use highly effective local anesthesia to ensure the entire area is completely numb — you'll only feel a bit of pressure, never pain.</p><p>Using specialized instruments, the dentist will gently loosen the tooth and carefully lift it out. After the tooth is removed, we place a simple gauze pad over the site to help clean, natural healing begin. Before you leave, we provide extremely clear, easy-to-follow instructions on exactly how to care for your mouth over the next few days to ensure a smooth recovery.</p>",
        "benefits": [
            "Removes Source of Pain", "Prevents Infection Spread", "Fast & Gentle Process"
        ],
        "related": ["Dentures", "Gum Treatment", "Crowns and Bridges"]
    }
]

BENEFIT_SVG = '<svg class="benefit-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>'


for service in services:
    slug = SLUGS_MAPPING[service["name"]]
    slug_img = slug.replace(".html", "")
    
    # Generate Benefits
    benefits_html = ""
    for b in service["benefits"]:
        benefits_html += f'''                  <div class="benefit-card animate-on-scroll">
                      <div class="benefit-icon">{BENEFIT_SVG}</div>
                      <h4>{b}</h4>
                  </div>\n'''
                  
    # Generate Related
    related_html = ""
    for r in service["related"]:
        r_slug = SLUGS_MAPPING[r]
        r_icon = SVG_MAPPING[r].replace('class="service-icon"', 'class="related-icon-svg"')
        related_html += f'''                 <a href="{r_slug}" class="related-card animate-on-scroll">
                     <div class="related-icon">{r_icon}</div>
                     <span class="related-title">{r}</span>
                 </a>\n'''
                 
    title = f"{service['name']} in Nairobi | Deep Care Dental Clinic"
    
    page_content = header.format(
        title=title,
        desc=service["desc"],
        name=service["name"],
        icon=SVG_MAPPING[service["name"]],
        slug_img=slug_img,
        expect=service["expect"],
        benefits=benefits_html,
        related=related_html
    ) + footer
    
    with open(slug, "w", encoding="utf-8") as f:
        f.write(page_content)

print("Generated 9 service files successfully!")
