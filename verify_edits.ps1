$c = Get-Content -Raw -Encoding UTF8 'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'
$lines = $c -split '\r?\n'
Write-Host '=== LINES 6-20 ==='
$lines | Select-Object -First 20 | ForEach-Object { Write-Host $_ }
Write-Host ''
Write-Host '=== KEY TERMS CHECK ==='
$patterns = @('Material Sourcing', 'supplier partner', 'Trusted Supplier Partner', 'arranged through a trusted', 'Trusted Supplier Network', 'supplier network')
foreach ($p in $patterns) {
    $hits = @()
    foreach ($i in 0..($lines.Count - 1)) {
        if ($lines[$i] -match $p) {
            $hits += "$($i+1):$($lines[$i].Trim())"
        }
    }
    Write-Host "[$p] -> $($hits.Count) hits"
    foreach ($h in $hits[0..2]) { Write-Host "  $h" }
}