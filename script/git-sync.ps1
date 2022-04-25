cd $(Get-Location) && cd ..
git add --all
git commit -m "changes on $(date)"
git pull --all
git push
