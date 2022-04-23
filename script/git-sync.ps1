Set-Location -Path .. -PassThru
git add --all
git commit -m "changes on $(date)"
git pull --all
git push
