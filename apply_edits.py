#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

path = r'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'

with io.open(path, 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# 1. Breadcrumb
content = content.replace('"name":"Material Supply"', '"name":"Material Sourcing"')

# 2. Service schema - supplier network -> supplier partner
content = content.replace('through our trusted supplier network across Mumbai', 'through our trusted supplier partner across Mumbai')

# 3. FAQ duplicate "Brands include"
content = content.replace('Brands include Saint-Gobain, Gyproc, USG Boral and Trimurti. Brands include Saint-Gobain', 'Brands include Saint-Gobain, Gyproc, USG Boral and Trimurti.')

# 4. FAQ - materials only
content = content.replace('through our supplier network', 'through a trusted supplier partner')

# 5. FAQ - delivery
content = content.replace('through our supplier partners', 'through our trusted supplier partner')

# 6. Hero paragraph
content = content.replace('sourced through our trusted supplier network across Mumbai', 'arranged through our trusted supplier partner across Mumbai')

# 7. Overview heading
content = content.replace('Trusted Supplier Network', 'Trusted Supplier Partner')

# 8. Overview paragraph 2
content = content.replace('Through our trusted supplier network, you get', 'Through our trusted supplier partner, you get')

# 9. FAQ body - delivery
content = content.replace('through our supplier partners', 'through our trusted supplier partner')

# 10. Meta description duplicate
content = content.replace('Call 8082005568. Call 8082005568.', 'Call 8082005568.')

# 11. og:description
content = content.replace('sourced via trusted suppliers across Mumbai. Call for rates.', 'arranged via our trusted supplier partner. Call for rates.')

if content != original:
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('DONE - changes applied')
else:
    print('NO CHANGES - content already matches')