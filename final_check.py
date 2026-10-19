#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'

with io.open(path, 'r', encoding='utf-8') as f:
    content = f.read()

checks = {
    'Material Sourcing (schema)': 'Ceiling Material Sourcing & Arrangement',
    'Material Sourcing (breadcrumb)': '"name":"Material Sourcing"',
    'supplier partner (meta desc)': 'trusted supplier partners',
    'supplier partner (og:description)': 'trusted supplier partner',
    'supplier partner (FAQ-direct)': 'from a trusted supplier partner',
    'supplier partner (FAQ-materials)': 'through a trusted supplier partner',
    'supplier partner (FAQ-delivery)': 'through our trusted supplier partner',
    'supplier partner (Hero)': 'sourced through our trusted supplier partner',
    'supplier partner (Overview)': 'Through our trusted supplier partner',
    'Trusted Supplier Partner (heading)': 'Trusted Supplier Partner',
    'No "supplier network"': 'supplier network',  # expect 0
    'No "Network" (Trusted)': 'Trusted Supplier Network',  # expect 0
    'Meta - no duplicate phone': 'Call 8082005568. Call 8082005568',  # expect 0
    'FAQ - no duplicate brands': 'Brands include Saint-Gobain, Gyproc, USG Boral and Trimurti. Brands include',  # expect 0
}

print('=== VALIDATION ===')
all_ok = True
for label, pattern in checks.items():
    count = content.count(pattern)
    status = 'PASS' if count == 0 or (label.startswith('No') and count == 0) or (not label.startswith('No') and count > 0) else 'FAIL'
    if status == 'FAIL':
        all_ok = False
    print(f'[{status}] {label}: found {count}')

print(f'\nOverall: {"ALL PASS" if all_ok else "SOME FAILURES"}')

# Show Service schema full description
import re
m = re.search(r'description":"We arrange and source[^"]*"', content)
if m:
    print(f'\nService schema description: {m.group()[:250]}')

# Show all occurrences of "supplier partner"
print(f'\nAll "supplier partner" occurrences:')
for i, line in enumerate(content.split('\n'), 1):
    if 'supplier partner' in line:
        print(f'  L{i}: {line[:120]}')