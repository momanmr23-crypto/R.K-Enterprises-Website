#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import re

# All anchor links found across all pages that start with index.html#
anchor_links = [
    'index.html#services',
    'index.html#residential-projects',
    'index.html#process',
    'index.html#contact',
    'index.html#faq',
    'index.html#projects',
    'index.html#calculator',
]

# Read index.html and find all ids
with io.open(r'd:\Userprofile\ADMIN\Desktop\html\pop\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

ids_in_index = re.findall(r'id=["\']([^"\']+)["\']', content)

print('IDs present in index.html:')
for i in sorted(set(ids_in_index)):
    print(f'  #{i}')

print()
print('Anchor targets that need verification:')
for link in anchor_links:
    # Extract the anchor part
    if '#' in link:
        _, anchor = link.split('#', 1)
        if anchor in ids_in_index:
            print(f'  [{link}] ✓ EXISTS as id="{anchor}"')
        else:
            print(f'  [{link}] ✗ MISSING - id="{anchor}" not found in index.html')
    else:
        print(f'  [{link}] (no anchor)')