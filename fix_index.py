#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\index.html'

with io.open(path, 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# 1. Service schema - supplier network -> supplier partner
content = content.replace(
    'through our trusted supplier network across Mumbai',
    'through our trusted supplier partner across Mumbai'
)

# 2. Services heading - Material Supply -> Material Sourcing & Arrangement
content = content.replace('<h3 class="font-bold text-2xl mb-4">Material Supply</h3>',
                          '<h3 class="font-bold text-2xl mb-4">Material Sourcing &amp; Arrangement</h3>')

# 3. Navigation link "Material Supply" -> "Material Sourcing & Arrangement"
content = content.replace('<a href="material-supply-mumbai.html" class="hover:text-amber-400 transition-colors">Material Supply</a>',
                          '<a href="material-supply-mumbai.html" class="hover:text-amber-400 transition-colors">Material Sourcing &amp; Arrangement</a>')

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
print('Changes applied:')
print(f'  supplier network -> {content.count("supplier network")} (was {original.count("supplier network")})')
print(f'  Material Sourcing -> {content.count("Material Sourcing")} (was {original.count("Material Sourcing")})')
print(f'  "Material Supply" -> {content.count("Material Supply")} (was {original.count("Material Supply")})')