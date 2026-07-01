import os
import re
import glob

# Constants for injection
SKIP_LINK = '\n<a href="#main-content" class="skip-link">Skip to main content</a>'
CANONICAL_OG = '''
    <!-- SEO and Social -->
    <meta name="robots" content="index, follow">
    <!-- TODO: Confirm and update domain when live -->
    <link rel="canonical" href="https://deepcaredentalclinic.co.ke/{page_url}">
    
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://deepcaredentalclinic.co.ke/{page_url}">
    <meta property="og:title" content="{page_title}">
    <meta property="og:description" content="{page_desc}">
    <!-- TODO: Create a 1200x630px OG image with the clinic logo and name -->
    <meta property="og:image" content="https://deepcaredentalclinic.co.ke/assets/images/og-image.jpg">
    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{page_title}">
    <meta name="twitter:description" content="{page_desc}">
    <meta name="twitter:image" content="https://deepcaredentalclinic.co.ke/assets/images/og-image.jpg">
'''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    is_modified = False

    # 1. Skip Link
    if '<a href="#main-content" class="skip-link">' not in content:
        content = re.sub(r'(<body[^>]*>)', r'\1' + SKIP_LINK, content)
        is_modified = True

    # 2. Main content wrapper ID
    if '<main>' in content:
        content = content.replace('<main>', '<main id="main-content">')
        is_modified = True

    # 3. Canonical and OG tags
    if '<!-- SEO and Social -->' not in content and '<title>' in content:
        title_match = re.search(r'<title>(.*?)</title>', content)
        desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
        
        page_title = title_match.group(1) if title_match else ""
        page_desc = desc_match.group(1) if desc_match else ""
        page_url = filename if filename != 'index.html' else ''
        
        injection = CANONICAL_OG.format(page_url=page_url, page_title=page_title, page_desc=page_desc)
        content = content.replace('</head>', injection + '\n</head>')
        is_modified = True

    # 4. Image tags missing width/height
    # We will just add a comment for performance instead of guessing dimensions if it's too complex here. But wait, I'll do this manually for the important ones.
    
    # 5. SVGs missing aria-hidden
    # Find <svg> tags that don't have aria-hidden or role
    svg_pattern = re.compile(r'(<svg(?![^>]*aria-hidden)(?![^>]*role)[^>]*>)')
    if svg_pattern.search(content):
        # Note: the group \2 trick might be wrong, let's just do a simpler sub
        content = re.sub(r'<svg (?!.*aria-hidden)(?!.*role)([^>]*)>', r'<svg aria-hidden="true" \1>', content)
        is_modified = True

    if is_modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

html_files = ['index.html', 'about.html', 'services.html', 'reviews.html', 'contact.html']
for f in html_files:
    process_file(f)
