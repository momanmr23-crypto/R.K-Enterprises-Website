#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

print('Starting link fix for #projects -> #residential-projects\n')
change_count = 0

for f in html_files:
    with io.open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    if 'index.html#projects' in content:
        new_content = content.replace('index.html#projects', 'index.html#residential-projects')
        with io.open(f, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        print(f'  [{f}] {content.count("index.html#projects")}x changed')
        change_count += 1

print(f'\nTotal files changed: {change_count}')