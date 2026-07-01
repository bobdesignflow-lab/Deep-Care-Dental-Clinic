import os
import re

root_dir = r"c:\My Web Sites\Deep Care Dental Clinic"
index_path = os.path.join(root_dir, "index.html")
services_path = os.path.join(root_dir, "services.html")
img_dir = os.path.join(root_dir, "assets", "images")

slugs = [
    "cleaning", "teeth-whitening", "root-canal-treatment", 
    "gum-treatment", "dentures", "dental-fillings", 
    "braces", "crowns-and-bridges", "tooth-extractions"
]

def fix_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    for slug in slugs:
        png_exists = os.path.exists(os.path.join(img_dir, f"{slug}.png"))
        jpg_exists = os.path.exists(os.path.join(img_dir, f"{slug}.jpg"))
        
        # If PNG doesn't exist, we must remove the <source> tag to prevent broken images
        if not png_exists:
            source_pattern = r'\s*<source[^>]*?srcset="assets/images/' + re.escape(slug) + r'\.png"[^>]*?>'
            html = re.sub(source_pattern, '', html)
            
        # If JPG doesn't exist but PNG does, we should point the <img> src to the PNG to be safe
        if not jpg_exists and png_exists:
            img_pattern = r'(<img[^>]*?src="assets/images/' + re.escape(slug) + r')\.jpg'
            html = re.sub(img_pattern, r'\1.png', html)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

fix_html_file(index_path)
fix_html_file(services_path)
print("HTML fixed.")
