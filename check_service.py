#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import re

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'

with io.open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for the service schema description
m = re.search(r'description":"We arrange and source[^"]*"', content)
if m:
    print(f'Service description: {m.group()[:200]}')
else:
    # Try with escaped quotes
    m = re.search(r'description":"We arrange and source[^"]*', content)
    if m:
        print(f'Found: {m.group()[:200]}')

# Search for any "supplier network" in the file
if 'supplier network' in content:
    print('\n"supplier network" still present:')
    for i, line in enumerate(content.split('\n'), 1):
        if 'supplier network' in line:
            print(f'  Line {i}: {line[:120]}')
else:
    print('\n"supplier network" not found - clean!')