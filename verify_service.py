#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'

with io.open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('=== Line 25 (Service schema, first 200 chars) ===')
print(lines[24][:200])
print()
print('=== Line 27 (FAQ - direct supply) ===')
print(lines[26])
print()
print('=== Line 28 (FAQ - materials only) ===')
print(lines[27])
print()
print('=== Line 29 (FAQ - delivery) ===')
print(lines[28])