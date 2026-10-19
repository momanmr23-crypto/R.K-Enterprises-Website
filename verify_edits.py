#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'

with io.open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('=== KEY LINES ===')
# lines are 0-indexed, so line N = index N-1
key_line_numbers = [6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 25, 26, 27, 28, 29, 30, 115, 116, 117, 124, 125, 126, 129, 130, 170, 171, 172]
for ln in key_line_numbers:
    if 0 < ln <= len(lines):
        txt = lines[ln-1].rstrip()
        print(f'--- Line {ln} ---')
        print(txt[:150] + ('...' if len(txt) > 150 else ''))