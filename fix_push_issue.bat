@echo off
echo Fixing push issues...
echo.

cd /d C:\ACE

echo Current status:
git status

echo.
echo Checking remote branches:
git branch -r

echo.
echo Pulling latest changes from dev branch:
git pull origin dev --allow-unrelated-histories

echo.
echo If there are merge conflicts, they will show above.
echo If no conflicts, attempting to push again:
git push origin dev

echo.
echo ========================================
echo If you see merge conflicts above:
echo 1. Edit the conflicted files 
echo 2. Run: git add .
echo 3. Run: git commit -m "Resolve merge conflicts"
echo 4. Run: git push origin dev
echo ========================================
pause