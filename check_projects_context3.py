#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import re

files = ['blog.html', 'privacy.html', 'terms.html']

for fname in files:
    path = r'd:\Userprofile\ADMIN\Desktop\html\pop\\' + fname
    with io.open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    print(f'=== {fname} - index.html#projects contexts ===')
    for m in re.finditer(r'[^\n]*index\.html#projects[^\n]*', content):
        line = m.group(0).strip()
        if 'href' in line:
            print(f'  {line[:150]}')
    print()