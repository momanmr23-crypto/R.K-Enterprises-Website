#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import re

with io.open(r'd:\Userprofile\ADMIN\Desktop\html\pop\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all "commercial" mentions
print('=== All "commercial" mentions in index.html ===')
for m in re.finditer(r'[^\n]*commercial[^\n]*', content):
    line = m.group(0).strip()
    # Only show lines with actual HTML attributes (not CSS)
    if any(attr in line for attr in ['<div', '<section', '<h', 'id=', 'class=', '<a']):
        print(f'  {line[:200]}')

print()
print('=== All section/elements with "projects" in id/class ===')
for m in re.finditer(r'[^\n]*\bprojects\b[^\n]*', content):
    line = m.group(0).strip()
    if '<' in line:
        print(f'  {line[:200]}')

print()
print('=== Lines mentioning id with "project" (not classes) ===')
for m in re.finditer(r'<[^>]*\b(?:id|class)=["\'][^"\']*\bprojects\b[^"\']*["\'][^>]*>', content):
    print(f'  {m.group(0)[:200]}')