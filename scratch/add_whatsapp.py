import os

html_snippet = """
<a class="wa-float"
   href="https://wa.me/254712543781?text=Hello%2C%20I%20would%20like%20to%20book%20an%20appointment%20at%20Deep%20Care%20Dental%20Clinic."
   target="_blank"
   rel="noopener noreferrer"
   aria-label="Chat with Deep Care Dental Clinic on WhatsApp">

  <svg class="wa-float__icon"
       xmlns="http://www.w3.org/2000/svg"
       viewBox="0 0 24 24"
       aria-hidden="true">
    <path fill="#FFFFFF"
      d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/>
    <path fill="#FFFFFF"
      d="M12 0C5.373 0 0 5.373 0 12c0 2.125.558 4.122 1.532 5.855L.054 23.447a.5.5 0 00.499.553h.056l5.783-1.516A11.95 11.95 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 01-5.006-1.371l-.36-.214-3.732.979.997-3.63-.234-.374A9.818 9.818 0 1112 21.818z"/>
  </svg>

  <span class="wa-float__label">Chat with us</span>

</a>
</body>"""

css_snippet = """
/* ── Floating WhatsApp Button ── */
.wa-float {
  position: fixed;
  bottom: 28px;
  right: 28px;
  z-index: 9999;
  display: flex;
  align-items: center;
  gap: 10px;
  background-color: #25D366;
  color: #FFFFFF;
  text-decoration: none;
  border-radius: 50px;
  padding: 14px 20px 14px 16px;
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.45);
  transition: transform 0.2s ease,
              box-shadow 0.2s ease,
              padding 0.3s ease,
              max-width 0.3s ease;
  max-width: 52px;
  overflow: hidden;
  white-space: nowrap;
}

/* Expand on hover to show label */
.wa-float:hover {
  max-width: 200px;
  padding: 14px 20px 14px 16px;
  box-shadow: 0 6px 24px rgba(37, 211, 102, 0.55);
  transform: translateY(-2px);
}

.wa-float:active {
  transform: scale(0.96);
}

.wa-float:focus-visible {
  outline: 3px solid #25D366;
  outline-offset: 3px;
}

.wa-float__icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.wa-float__label {
  font-family: var(--font-body, 'Inter', sans-serif);
  font-size: 14px;
  font-weight: 600;
  color: #FFFFFF;
  opacity: 0;
  transition: opacity 0.2s ease 0.05s;
  pointer-events: none;
}

/* Show label text when button expands */
.wa-float:hover .wa-float__label {
  opacity: 1;
}

/* Pulse animation to draw attention on page load */
@keyframes wa-pulse {
  0%   { box-shadow: 0 4px 16px rgba(37,211,102,0.45),
                     0 0 0 0 rgba(37,211,102,0.4); }
  70%  { box-shadow: 0 4px 16px rgba(37,211,102,0.45),
                     0 0 0 12px rgba(37,211,102,0); }
  100% { box-shadow: 0 4px 16px rgba(37,211,102,0.45),
                     0 0 0 0 rgba(37,211,102,0); }
}

.wa-float {
  animation: wa-pulse 2.5s ease-in-out 2s 3;
}

/* Stop pulse after hover (user has noticed it) */
.wa-float:hover {
  animation: none;
}

/* Mobile adjustments */
@media (max-width: 480px) {
  .wa-float {
    bottom: 20px;
    right: 16px;
    padding: 13px;
    border-radius: 50%;
    max-width: 52px;
  }

  /* On mobile: icon only, no expand on hover */
  .wa-float:hover {
    max-width: 52px;
    padding: 13px;
    border-radius: 50%;
  }

  .wa-float__label {
    display: none;
  }
}

/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {
  .wa-float {
    animation: none;
    transition: none;
  }
}
"""

files = [
    "index.html", "about.html", "services.html", "reviews.html", 
    "contact.html", "cleaning.html", "teeth-whitening.html", 
    "root-canal-treatment.html", "gum-treatment.html", "dentures.html", 
    "dental-fillings.html", "braces.html", "crowns-and-bridges.html", 
    "tooth-extractions.html"
]

base_dir = r"c:\\My Web Sites\\Deep Care Dental Clinic"

for file in files:
    path = os.path.join(base_dir, file)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "wa-float" not in content:
            content = content.replace("</body>", html_snippet)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")
        else:
            print(f"Skipped {file} (already contains button)")
    else:
        print(f"Warning: {file} not found")

css_path = os.path.join(base_dir, "css", "components.css")
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if ".wa-float" not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\\n" + css_snippet + "\\n")
    print("Updated components.css")
else:
    print("Skipped components.css (already contains button CSS)")
