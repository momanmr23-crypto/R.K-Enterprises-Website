#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\index.html'

with io.open(path, 'r', encoding='utf-8') as f:
    content = f.read()

terms = ['supplier network', 'Trusted Supplier Network', 'Material Supply', 'reliable supplier', 'our suppliers']
for t in terms:
    print(f'"{t}" -> {content.count(t)} occurrences')

# Show all lines containing "supplier" or "Material Supply"
print('\n--- Lines with supplier/company mentions ---')
for i, line in enumerate(content.split('\n'), 1):
    if 'supplier' in line.lower() or 'Material Supply' in line or 'material supply' in line:
        print(f'L{i}: {line[:130]}')

print('\n--- Line 1476 area (services section) ---')
lines = content.split('\n')
if len(lines) >= 1476:
    for j in range(1474, min(1482, len(lines))):
        print(f'L{j+1}: {lines[j][:130]}')