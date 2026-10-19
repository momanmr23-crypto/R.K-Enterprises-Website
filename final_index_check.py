#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

for path in [
    r'd:\Userprofile\ADMIN\Desktop\html\pop\index.html',
    r'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html',
]:
    print(f'\n{"="*50}')
    print(f'CHECKING: {path}')
    print('='*50)
    with io.open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    checks = {
        'No "supplier network"': 'supplier network',
        'No "Trusted Supplier Network"': 'Trusted Supplier Network',
        'Has "supplier partner"': 'supplier partner',
        'Service schema is "Material Sourcing & Arrangement"': 'Material Sourcing & Arrangement',
    }

    for label, pattern in checks.items():
        count = content.count(pattern)
        if 'No' in label:
            status = 'PASS' if count == 0 else 'FAIL'
        else:
            status = 'PASS' if count > 0 else 'FAIL'
        print(f'  [{status}] {label} (found {count})')

print('\nDone.')