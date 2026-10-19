#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'

with io.open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Check specific patterns
patterns = {
    'Material Sourcing': 'Material Sourcing',
    'supplier partner': 'supplier partner',
    'Trusted Supplier Partner': 'Trusted Supplier Partner',
    'Trusted Supplier Network': 'Trusted Supplier Network',
    'Call 8082005568': 'Call 8082005568',
    'sourced through our': 'sourced through our',
    'arranged through our': 'arranged through our',
    'Brands include': 'Brands include',
}

for pattern in patterns:
    hits = []
    for i, line in enumerate(lines, 1):
        if patterns[pattern] in line:
            hits.append(i)
    status = 'OK' if pattern != 'Trusted Supplier Network' else ('STILL PRESENT' if hits else 'removed')
    print(f'[{pattern}]: {status} -> lines {hits}')