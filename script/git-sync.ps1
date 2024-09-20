#Requires -Version 5

$gitRoot = git rev-parse --show-toplevel 2> $null

if ($?) {
    Set-Location -Path $gitRoot

    git add .
    git commit -m "changes on $(Get-Date)"
    git pull
    git push
} else {
    Write-Warning "error: not fond .git"
}
