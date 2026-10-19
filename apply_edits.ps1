# Read the file as UTF-8
$c = Get-Content -Raw -Encoding UTF8 'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'

# 1. Breadcrumb in JSON-LD
$c = $c -replace '"name":"Material Supply"', '"name":"Material Sourcing"'

# 2. Service schema description
$c = $c -replace 'We arrange and source genuine branded ceiling and POP line materials across Mumbai through our trusted supplier network\.', 'We arrange and source genuine branded ceiling and POP line materials across Mumbai through a trusted supplier partner.'

# 3. FAQ answer about direct supply
$c = $c -replace 'We source genuine branded ceiling materials .*?We do not hold stock or sell directly; we arrange supply through our supplier partners\.', 'We source genuine branded ceiling materials from a trusted supplier partner — PVC panels, gypsum boards, POP, GI channels, putty, cornice profiles. We do not hold stock or sell materials directly; we arrange sourcing and delivery. Brands include Saint-Gobain, Gyproc, USG Boral and Trimurti.'

# 4. FAQ answer - materials only
$c = $c -replace 'Yes\. We arrange material-only sourcing for contractors, carpenters and self-managed projects through our supplier network, or supply \+ installation as a complete package\. We connect you to suppliers and coordinate delivery\.', 'Yes. We arrange material-only sourcing for contractors, carpenters and self-managed projects through a trusted supplier partner, or supply + installation as a complete package. We connect you to the supplier partner and coordinate delivery.'

# 5. FAQ answer - delivery
$c = $c -replace 'Yes\. We coordinate delivery across Mumbai, Thane and Navi Mumbai through our supplier partners\.', 'Yes. We coordinate delivery across Mumbai, Thane and Navi Mumbai through our trusted supplier partner.'

# 6. Hero paragraph
$c = $c -replace 'All kinds of POP line materials, PVC ceilings, gypsum boards, channels, putty &amp; more \u2014 sourced through our trusted supplier network across Mumbai\.', 'All kinds of POP line materials, PVC ceilings, gypsum boards, channels, putty &amp; more \u2014 arranged through a trusted supplier partner across Mumbai.'

# 7. Overview heading
$c = $c -replace 'All Kinds of Ceiling &amp; POP Line Materials \u2014 Trusted Supplier Network', 'All Kinds of Ceiling &amp; POP Line Materials \u2014 Trusted Supplier Partner'

# 8. Overview paragraph 2
$c = $c -replace 'Through our trusted supplier network, you get <strong>genuine branded materials \(Saint-Gobain, Gyproc, USG Boral, Trimurti, Armstrong\) at competitive rates</strong>\.', 'Through our trusted supplier partner, you get <strong>genuine branded materials (Saint-Gobain, Gyproc, USG Boral, Trimurti, Armstrong) at competitive rates</strong>.'

# 9. FAQ body - delivery
$c = $c -replace 'Yes\. We coordinate delivery across Mumbai, Thane and Navi Mumbai through our supplier partners\. Delivery charges depend on order size and location\.', 'Yes. We coordinate delivery across Mumbai, Thane and Navi Mumbai through our trusted supplier partner. Delivery charges depend on order size and location.'

# 10. Meta description - main
$c = $c -replace 'Ceiling material sourcing and arrangement in Mumbai, Thane &amp; Navi Mumbai .*We source genuine branded materials through our trusted suppliers\.', 'Ceiling material sourcing and arrangement in Mumbai, Thane &amp; Navi Mumbai \u2014 PVC ceilings, gypsum boards, POP, channels, putty &amp; more. R.K Ceiling Solutions arranges genuine branded materials through trusted supplier partners. Call 8082005568.'

# 11. Meta description - og:title
$c = $c -replace 'We arrange genuine branded ceiling materials.*through our trusted supplier network across Mumbai\. Best rates\.', 'We arrange genuine branded ceiling materials \u2014 PVC, gypsum boards, POP, channels &amp; putty \u2014 through our trusted supplier partner. Best rates.'

# Write back
$c | Set-Content -Encoding UTF8 'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'
Write-Host 'DONE'