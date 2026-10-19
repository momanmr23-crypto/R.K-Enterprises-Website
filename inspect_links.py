#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import glob
import urllib.parse

base = os.path.abspath('.')
html_files = glob.glob('**/*.html', recursive=True)
print(f'Found {len(html_files)} HTML files')
print()

all_links = []
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    for m in re.finditer(r'href\s*=\s*[\"\']([^\"\']*)[\"\']', content):
        href = m.group(1).strip()
        # Skip javascript:, tel:, mailto:, anchors
        if href and not href.startswith(('javascript:', 'tel:', 'mailto:', '#')):
            all_links.append((f, href))

print(f'Found {len(all_links)} href links across all HTML files')
print('=' * 80)

# Classify links
internal = []
external = []
anchor = []
other = []
for file, href in all_links:
    if href.startswith(('http://', 'https://')):
        external.append((file, href))
    elif href.startswith('#'):
        anchor.append((file, href))
    elif href.startswith(('javascript:', 'tel:', 'mailto:')):
        other.append((file, href))
    else:
        internal.append((file, href))

print(f'  Internal: {len(internal)}')
print(f'  External: {len(external)}')
print(f'  Anchor:   {len(anchor)}')
print(f'  Other:    {len(other)}')
print()

# Check internal links
missing = []
broken = []
for file, href in internal:
    # Normalize the href
    if href.startswith('/'):
        target = os.path.normpath(os.path.join(base, href.lstrip('/')))
    elif href.startswith('./') or href.startswith('../'):
        target = os.path.normpath(os.path.join(base, href))
    else:
        target = os.path.normpath(os.path.join(base, href))

    if not os.path.exists(target):
        missing.append((file, href, target))
    elif target.endswith('.html') == False and not target.endswith('/'):
        # It's a directory or file without extension - check if directory exists
        if not os.path.exists(target + '.html'):
            broken.append((file, href, target))

print(f'Missing target files: {len(missing)}')
for file, href, target in missing:
    print(f'  [{file}] {href} -> MISSING: {target}')

print(f'Non-HTML targets: {len(broken)}')
for file, href, target in broken:
    print(f'  [{file}] {href} -> {target}')

print()
print('=' * 80)
print('All external URLs:')
for file, href in external:
    print(f'  [{file}] {href}')

print()
print('All internal links grouped by target file:')
from collections import Counter
links_by_target = Counter()
for file, href in internal:
    if href.startswith('/'):
        target = href.lstrip('/')
    elif href.startswith('./') or href.startswith('../'):
        target = href
    else:
        target = href
    links_by_target[target] += 1

for target, count in sorted(links_by_target.items()):
    exists = '✓' if os.path.exists(os.path.normpath(os.path.join(base, target))) else '✗ MISSING'
    print(f'  {target}  ({count}x) {exists}')

print()
print('Done.')