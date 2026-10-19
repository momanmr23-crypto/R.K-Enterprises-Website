#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import re

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'

with io.open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Simple replacement - just the phrase before the em-dash
old = 'across Mumbai through our trusted supplier network '
new = 'across Mumbai through our trusted supplier partner '
if old in content:
    content = content.replace(old, new)
    print('Service schema updated successfully')
else:
    print('Pattern not found')
    # Show what's actually around the pattern
    idx = content.find('through our trusted supplier network')
    if idx > 0:
        print(repr(content[idx-50:idx+100]))

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('DONE')