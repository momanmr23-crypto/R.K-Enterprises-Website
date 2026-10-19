#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import re

with io.open(r'd:\Userprofile\ADMIN\Desktop\html\pop\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find context around #commercial-projects
print('=== Context around #commercial-projects in index.html ===')
for m in re.finditer(r'[^\n]*#commercial-projects[^\n]*', content):
    print(f'  {m.group(0)[:200]}')

print()
print('=== Context around #commercial-projects near section (50 lines back) ===')
lines = content.split('\n')
found = False
for i, line in enumerate(lines):
    if '#commercial-projects' in line:
        start = max(0, i-10)
        end = min(len(lines), i+5)
        print(f'  (line {i+1})')
        for j in range(start, end):
            marker = '>>>' if j == i else '   '
            print(f'  {marker} L{j+1}: {lines[j][:120]}')
        found = True
        break

if not found:
    print('  #commercial-projects not found as line match, searching...')
    # Find where the last comment "PROJECTS" or similar is
    for i, line in enumerate(lines):
        if 'commercial-projects' in line:
            print(f'  Found at line {i+1}: {line[:120]}')