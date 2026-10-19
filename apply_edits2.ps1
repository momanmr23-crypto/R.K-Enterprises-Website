# Read the file as UTF-8
$c = Get-Content -Raw -Encoding UTF8 'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'
$lines = $c -split '\r?\n'

# Helper: replace text in a specific line
function Replace-Line {
    param([int]$lineNum, [string]$search, [string]$replace)
    $idx = $lineNum - 1
    if ($idx -ge 0 -and $idx -lt $lines.Count) {
        if ($lines[$idx] -match $search) {
            $lines[$idx] = $lines[$idx] -replace $search, $replace
            Write-Host "  Fixed line $lineNum"
        } else {
            Write-Host "  NOT FOUND on line $lineNum: $search"
        }
    }
}

# Helper: replace first occurrence in whole file
function Replace-First {
    param([string]$search, [string]$replace)
    $global:i = 0
    $found = $false
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match $search) {
            $lines[$i] = $lines[$i] -replace $search, $replace
            Write-Host "  Fixed line $($i+1): $search"
            $found = $true
            break
        }
    }
    if (-not $found) { Write-Host "  NOT FOUND: $search" }
}

# 1. Breadcrumb (line 25)
Replace-Line -lineNum 25 -search '"name":"Material Supply"' -replace '"name":"Material Sourcing"'

# 2. Service schema (line 26) - replace "supplier network" with "supplier partner"
Replace-Line -lineNum 26 -search 'through our trusted supplier network \u2014' -replace 'through our trusted supplier partner \u2014'

# 3. FAQ - Do you supply directly? (line 28) - fix duplicate
Replace-Line -lineNum 28 -search 'Brands include Saint-Gobain, Gyproc, USG Boral and Trimurti\. Brands include Saint-Gobain' -replace 'Brands include Saint-Gobain, Gyproc, USG Boral and Trimurti.'

# 4. FAQ - materials only (line 29)
Replace-Line -lineNum 29 -search 'through our supplier network' -replace 'through a trusted supplier partner'

# 5. FAQ - delivery (line 30)
Replace-Line -lineNum 30 -search 'through our supplier partners' -replace 'through our trusted supplier partner'

# 6. Hero paragraph (line 117)
Replace-Line -lineNum 117 -search 'sourced through our trusted supplier network across Mumbai' -replace 'arranged through our trusted supplier partner across Mumbai'

# 7. Overview heading (line 126)
Replace-Line -lineNum 126 -search 'Trusted Supplier Network' -replace 'Trusted Supplier Partner'

# 8. Overview paragraph 2 (line 130)
Replace-Line -lineNum 130 -search 'Through our trusted supplier network, you get ' -replace 'Through our trusted supplier partner, you get '

# 9. FAQ body - delivery (line 174)
Replace-Line -lineNum 174 -search 'through our supplier partners' -replace 'through our trusted supplier partner'

# 10. Meta description main (line 9) - remove duplicate "Call 8082005568"
Replace-Line -lineNum 9 -search 'Call 8082005568. Call 8082005568\.' -replace 'Call 8082005568.'

# 11. Meta description og:description (line 13) - improve wording
Replace-Line -lineNum 13 -search 'sourced via trusted suppliers across Mumbai\. Call for rates\.' -replace 'arranged via our trusted supplier partner. Call for rates.'

# Reconstruct file
$c = $lines -join '\r\n'
$c | Set-Content -Encoding UTF8 'd:\Userprofile\ADMIN\Desktop\html\pop\material-supply-mumbai.html'
Write-Host ''
Write-Host 'DONE'