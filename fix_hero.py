#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'

with io.open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Print lines 106-130 with full content
for ln in range(105, 130):
    if ln < len(lines):
        print(f'=== Line {ln+1} (full) ===')
        print(repr(lines[ln]))