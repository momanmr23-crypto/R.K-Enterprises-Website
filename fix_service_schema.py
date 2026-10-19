#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'

with io.open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Service schema - the description might still say "supplier network"
# Look for the specific Service schema field that might still say "network"
old_service = 'through our trusted supplier network \u2014 PVC ceiling panels'
new_service = 'through our trusted supplier partner \u2014 PVC ceiling panels'
if old_service in content:
    content = content.replace(old_service, new_service)
    print('Fix 1: Service schema updated')
else:
    # Check what's actually there
    import re
    m = re.search(r'description":"We arrange and source.*?PVC ceiling panels[^"]*"', content)
    if m:
        print(f'Current: {m.group()[:100]}...')
    else:
        print('Pattern not found - need to investigate')

# Fix 2: FAQ line 27 duplicate "Brands include"
old_faq = 'Brands include Saint-Gobain, Gyproc, USG Boral and Trimurti., Gyproc, USG Boral and Trimurti.'
new_faq = 'Brands include Saint-Gobain, Gyproc, USG Boral and Trimurti.'
if old_faq in content:
    content = content.replace(old_faq, new_faq)
    print('Fix 2: FAQ duplicate brands removed')
else:
    import re
    m = re.search(r'Brands include[^,]+, Gyproc[^,]*, Trimurti\.', content)
    if m:
        print(f'Found: {m.group()[:80]}')
    else:
        print('FAQ duplicate pattern not found')

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('DONE')