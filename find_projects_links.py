#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

# Find all href links containing index.html#projects (or any index.html anchor that targets #projects)
print('Links to index.html#projects:')
for f in html_files:
    with io.open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    for m in re.finditer(r'href\s*=\s*[\"\']([^\"\']*)[\"\']', content):
        href = m.group(1).strip()
        if 'index.html' in href and 'projects' in href:
            print(f'  [{f}] {href}')

print()
print('Current ids in index.html:')
with io.open(r'd:\Userprofile\ADMIN\Desktop\html\pop\index.html', 'r', encoding='utf-8') as f:
    content = f.read()
ids = re.findall(r'id=["\']([^"\']+)["\']', content)
print(f'  {sorted(set(ids))}')

# Search for #projects anywhere (including in other contexts)
print()
print('Any #projects references anywhere:')
for f in html_files:
    with io.open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    if 'projects' in content:
        # Find all mentions
        for m in re.finditer(r'[^\s>]*projects[^\s>]*', content):
            token = m.group(0)
            if 'href' in token or '#' in token or 'id' in token:
                pass
        # Just check for index.html#projects
        if 'index.html#projects' in content:
            print(f'  [{f}] has index.html#projects')

# Also check for any #projects within href
print()
print('Any href with #projects:')
for f in html_files:
    with io.open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    for m in re.finditer(r'href\s*=\s*[\"\']([^\"\']*)[\"\']', content):
        href = m.group(1).strip()
        if 'projects' in href:
            print(f'  [{f}] {href}')