@echo off
echo Creating production branch with current code...
echo.

cd /d C:\ACE

echo Current Git status:
git status

echo.
echo Current branches:
git branch -a

echo.
echo Switching to main branch (if it exists) or creating it...
git checkout main 2>nul || git checkout -b main

echo.
echo Ensuring all current files are committed to main...
git add .
git status

echo Making sure main has all current code...
git commit -m "Update main branch with latest code

- Complete Address History Tracker application
- Security improvements and environment management
- All documentation and setup files
- Ready for production deployment

Generated with Claude Code" 2>nul || echo "No changes to commit - main is up to date"

echo.
echo Pushing main branch to GitHub...
git push -u origin main

echo.
echo Creating production branch from main...
git checkout -b production

echo.
echo Production branch created! Pushing to GitHub...
git push -u origin production

echo.
echo ========================================
echo Production branch setup complete!
echo.
echo Branch structure:
echo - main (production-ready code)
echo - dev (development branch)  
echo - production (dedicated production branch)
echo.
echo All branches now exist on GitHub!
echo ========================================

echo.
echo Switching back to dev branch for continued development...
git checkout dev

echo.
echo Current branch:
git branch

pause