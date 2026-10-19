#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import glob
import io
from collections import Counter

base = os.path.abspath('.')
html_files = glob.glob('**/*.html', recursive=True)
print(f'Found {len(html_files)} HTML files')
print()

# Collect all hrefs
all_links = []
goto = []
for f in html_files:
    with io.open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    for m in re.finditer(r'href\s*=\s*[\"\']([^\"\']*)[\"\']', content):
        href = m.group(1).strip()
        if href and not href.startswith(('javascript:', 'tel:', 'mailto:', '#')):
            all_links.append((f, href))

# Classify
external = [l for l in all_links if l[1].startswith(('http://', 'https://'))]
anchor_html = [l for l in all_links if l[1].startswith('#')]
anchor_index = [l for l in all_links if 'index.html#' in l[1]]
internal = [l for l in all_links if not l[1].startswith(('http://', 'https://', '#'))]

print(f'External: {len(external)} | Internal(#): {len(anchor_html)} | index.html anchors: {len(anchor_index)} | Other internal: {len(internal)}')
print()

# Check internal links that go to .html or .pdf etc (not anchors)
missing = []
for file, href in internal:
    if href.endswith('.html') or href.endswith('.pdf'):
        target = os.path.normpath(os.path.join(base, href))
        if not os.path.exists(target):
            missing.append((file, href))

print(f'External .html/.pdf targets: {len(missing)}')
for file, href in missing:
    print(f'  MISSING: [{file}] {href}')

print()

# Anchor links - check which anchors exist on target pages
print('Anchor link verification:')
# Gather all ids from all pages
page_ids = {}
for f in html_files:
    with io.open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    page_ids[f] = set(re.findall(r'id=["\']([^"\']+)["\']', content))

broken_anchors = []
for file, href in anchor_index + anchor_html:
    if '#' not in href:
        continue
    # Parse: target file + anchor
    parts = href.split('#', 1)
    target_file = parts[0]
    anchor = parts[1]
    
    # If target file is a full path (like blog.html, privacy.html), check it
    if target_file in page_ids:
        if anchor not in page_ids[target_file]:
            broken_anchors.append((file, href, target_file, anchor))
    elif target_file in ('index.html',):
        # index.html anchors
        if anchor not in page_ids['index.html']:
            broken_anchors.append((file, href, 'index.html', anchor))

print(f'Broken anchor links: {len(broken_anchors)}')
for file, href, target, anchor in broken_anchors:
    print(f'  [{file}] href="{href}" -> target "{target}" missing id="{anchor}"')

print()
print('Summary:')
print(f'  Total links: {len(all_links)}')
print(f'  External: {len(external)}')
print(f'  Internal anchors: {len(anchor_index) + len(anchor_html)}')
print(f'  Internal page links: {len(internal)}')
print(f'  Missing targets: {len(missing)}')
print(f'  Broken anchors: {len(broken_anchors)}')
print()
print('ALL CHECKS PASSED' if not missing and not broken_anchors else 'SOME ISSUES FOUND')