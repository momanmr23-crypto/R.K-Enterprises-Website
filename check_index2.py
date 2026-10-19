#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\index.html'

with io.open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('=== Line 162 (Service schema) ===')
print(lines[161][:400])
print()
print('=== Line 1477 (service description) ===')
print(lines[1476][:250])
print()
print('=== Line 17 (about/main text) ===')
print(lines[16][:300])
print()
print('=== All lines with "supplier" ===')
for i, line in enumerate(lines, 1):
    if 'supplier' in line.lower():
        print(f'L{i}: {line[:150]}')