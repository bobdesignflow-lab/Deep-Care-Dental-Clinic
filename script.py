import re
import os

root_dir = r"c:\My Web Sites\Deep Care Dental Clinic"
index_path = os.path.join(root_dir, "index.html")
services_path = os.path.join(root_dir, "services.html")
components_css_path = os.path.join(root_dir, "css", "components.css")
home_css_path = os.path.join(root_dir, "css", "home.css")
services_css_path = os.path.join(root_dir, "css", "services.css")

slugs = {
    "Professional Teeth Cleaning": "cleaning",
    "Teeth Whitening": "teeth-whitening",
    "Root Canal Treatment": "root-canal-treatment",
    "Gum Treatment": "gum-treatment",
    "Dentures": "dentures",
    "Dental Fillings": "dental-fillings",
    "Braces": "braces",
    "Crowns and Bridges": "crowns-and-bridges",
    "Tooth Extractions": "tooth-extractions"
}

def fix_html_cards(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Find the cards, they all start with <div...class="service-card..." or <a...class="service-card-link..."
    # The end of the card is either </div>\s*</div>\s*</div> for index or </div>\s*</a> for services
    out_html = ""
    idx = 0
    while True:
        # Search for a card start
        m1 = re.search(r'<(div|a)[^>]*?class="(service-card animate-on-scroll|service-card-link animate-on-scroll)[^"]*"[^>]*?>', html[idx:])
        if not m1:
            out_html += html[idx:]
            break
            
        start_pos = idx + m1.start()
        out_html += html[idx:start_pos]
        
        # We know next elements are image container and content string
        tag_type = m1.group(1) # div or a
        classes = m1.group(2)
        
        # Extract the delay if it exists
        m_delay = re.search(r'delay-\d+', html[start_pos:start_pos+m1.end()])
        delay_cls = (" " + m_delay.group(0)) if m_delay else ""
        
        # Find the end of this card block
        if tag_type == "div":
            # in index.html, ends with </div> just before the next card or end of grid
            # easiest is to find "Learn More" link which is at the end of content
            m_end = re.search(r'<a href="([^"]+)".*?Learn More.*?</a>\s*</div>\s*</div>', html[start_pos:])
            if m_end:
                end_pos = start_pos + m_end.end()
                link_href = m_end.group(1)
            else:
                break
        else:
            # in services.html, ends with </a>
            m_end = re.search(r'(<div class="learn-more">Learn More.*?</div>\s*</div>\s*)</a>', html[start_pos:])
            link_href_m = re.search(r'href="([^"]+)"', html[start_pos:start_pos+100])
            link_href = link_href_m.group(1) if link_href_m else "index.html"
            end_pos = start_pos + m_end.end()
            
        card_html = html[start_pos:end_pos]
        
        # extract SVG and H3
        m_header = re.search(r'(<svg[^>]*>.*?</svg>)\s*<h3>(.*?)</h3>', card_html, re.DOTALL)
        svg_icon = m_header.group(1)
        h3_text = m_header.group(2)
        slug = slugs.get(h3_text, "missing")
        
        # extract description (p tags)
        m_desc = re.search(r'<p>(.*?)</p>', card_html, re.DOTALL)
        desc_text = m_desc.group(1)
        
        new_card = f"""<a class="service-card animate-on-scroll{delay_cls}" href="{link_href}">
                <div class="service-card__img-wrap">
                    <picture>
                        <source srcset="assets/images/{slug}.png" type="image/png">
                        <img src="assets/images/{slug}.jpg" alt="{h3_text} at Deep Care Dental Clinic, Nairobi" width="400" height="220" loading="lazy">
                    </picture>
                </div>
                <div class="service-card__content">
                    <div class="service-card__header">
                        {svg_icon}
                        <h3>{h3_text}</h3>
                    </div>
                    <p>{desc_text}</p>
                    <span class="learn-more">Learn More <span>→</span></span>
                </div>
            </a>"""
            
        # For index.html, we need to respect the original indentation, maybe just prepend "            "
        new_card = "\n".join("            " + line if i>0 else line for i, line in enumerate(new_card.split("\n")))
        # But wait, services.html indentation is 16 spaces deep. It's fine to just be slightly loose on space
        
        out_html += new_card
        idx = end_pos

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(out_html)

fix_html_cards(index_path)
fix_html_cards(services_path)

# Handle CSS
with open(components_css_path, "r", encoding="utf-8") as f:
    css = f.read()

unified_css = """
/* Service card unified layout */
.service-card {
  background: #FFFFFF;
  border: 0.5px solid #E3E7EE;
  border-radius: 12px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  height: 100%;
}
.service-card:hover, .service-card:focus-visible {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(26, 86, 174, 0.12);
  outline: none;
}
.service-card:focus-visible {
  box-shadow: 0 0 0 3px rgba(26, 86, 174, 0.5);
}
.service-card__img-wrap {
  width: 100%;
  height: 220px;
  overflow: hidden;
  border-radius: 12px 12px 0 0;
  background-color: #E6F1FB;
  flex-shrink: 0;
}
.service-card__img-wrap picture {
  display: block;
  width: 100%;
  height: 100%;
}
.service-card__img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.3s ease;
}
.service-card:hover .service-card__img-wrap img,
.service-card:focus-visible .service-card__img-wrap img {
  transform: scale(1.04);
}
.service-card__content {
  padding: 1.25rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.service-card__header {
  display: flex;
  align-items: center;
  gap: 10px;
}
.service-card__header .service-icon {
  width: 24px;
  height: 24px;
  color: #1A56AE;
  flex-shrink: 0;
  margin-bottom: 0;
}
.service-card__content h3 {
  color: #16223A;
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0;
}
.service-card__content p {
  color: #4B5563;
  font-size: 0.875rem;
  line-height: 1.5;
  margin-bottom: 0;
  flex-grow: 1;
}
.service-card .learn-more {
  margin-top: auto;
  font-weight: 500;
  color: #1A56AE;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.875rem;
}
.service-card .learn-more span {
  transition: transform 0.3s ease;
}
.service-card:hover .learn-more {
  text-decoration: underline;
}
.service-card:hover .learn-more span,
.service-card:focus-visible .learn-more span {
  transform: translateX(4px);
}
"""
if "/* Service card unified layout */" not in css:
    with open(components_css_path, "a", encoding="utf-8") as f:
        f.write("\n" + unified_css)

# Remove duplicates from css
def remove_css_block(path, start_marker, end_marker):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # It's easier to just use regex to strip out .service-card blocks
    # Home.css lines 195 to 282
    content = re.sub(r'/\* Service card — image-on-top layout \*/.*?\.service-card \.learn-more:hover {[^}]*}', '/* Service card styles moved to components.css */', content, flags=re.DOTALL)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def remove_css_block_services(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r'\.service-card-link {.*?\.service-card-link:hover \.learn-more span {[^}]*}', '/* Service card styles moved to components.css */', content, flags=re.DOTALL)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

remove_css_block(home_css_path, "", "")
remove_css_block_services(services_css_path)
print("ALL DONE")
