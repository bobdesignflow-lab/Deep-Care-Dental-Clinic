import glob

target = """        <li>
          <strong>Address:</strong><br>
          3rd Floor, Room 304, Popman House,<br>
          Moi Avenue, Near Khoja Mosque,<br>
          Nairobi, Kenya
        </li>"""
        
repl = """        <li>
          <strong>Address:</strong><br>
          <address style="font-style: normal; display: inline;">3rd Floor, Room 304, Popman House,<br>
          Moi Avenue, Near Khoja Mosque,<br>
          Nairobi, Kenya</address>
        </li>"""

target2 = """                            <strong>Address</strong>
                            <p>3rd Floor, Room 304, Popman House,<br>Moi Avenue, Near Khoja Mosque,<br>Nairobi, Kenya</p>"""
                            
repl2 = """                            <strong>Address</strong>
                            <address style="font-style: normal;">3rd Floor, Room 304, Popman House,<br>Moi Avenue, Near Khoja Mosque,<br>Nairobi, Kenya</address>"""

files = ['index.html', 'about.html', 'services.html', 'reviews.html', 'contact.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if target in content:
        content = content.replace(target, repl)
        
    if target2 in content:
        content = content.replace(target2, repl2)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("done")
