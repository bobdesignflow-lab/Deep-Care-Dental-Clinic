import glob
import re
import os

files = glob.glob('*.html') + ['sitemap.xml', 'robots.txt']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and remove all HTML style <!-- TODO: ... --> comments
    new_content = re.sub(r'<!--\s*TODO:.*?-->\n?', '', content, flags=re.DOTALL)
    
    # Also remove any hash style # TODO: ... if it exists in robots.txt
    new_content = re.sub(r'#\s*TODO:.*?\n', '', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed TODOs from {filepath}")

# Also replace them in generate_pages.py to prevent them from being regenerated
with open('generate_pages.py', 'r', encoding='utf-8') as f:
    gen_content = f.read()
    
gen_new = re.sub(r'<!--\s*TODO:.*?-->\n?', '', gen_content, flags=re.DOTALL)
gen_new = re.sub(r'#\s*TODO:.*?\n', '', gen_new)

if gen_new != gen_content:
    with open('generate_pages.py', 'w', encoding='utf-8') as f:
        f.write(gen_new)
    print("Removed TODOs from generate_pages.py")

print("done")
