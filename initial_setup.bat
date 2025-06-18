@echo off
echo Setting up ACE repository from scratch...
echo.

cd /d C:\ACE

echo Checking if this is a git repository...
if not exist .git (
    echo Initializing Git repository...
    git init
    git branch -M main
) else (
    echo Git repository already exists.
)

echo Configuring Git user...
git config user.name "Ian"
git config user.email "ianc929@gmail.com"

echo Current Git status:
git status

echo.
echo Adding all files...
git add .

echo Current status after adding:
git status

echo.
echo Making initial commit to main branch...
git commit -m "Initial commit: Address History Tracker with security features

- Complete Flask web application for address history tracking
- Supabase database integration with authentication
- Secure environment variable management
- Development and production environment templates
- Comprehensive documentation and setup guides
- Git workflow with dev/main branch structure

Generated with Claude Code"

echo.
echo Checking if remote origin exists...
git remote -v

echo.
echo Setting remote origin (if not already set)...
git remote add origin https://github.com/ianc929/ACE.git 2>nul || echo Remote origin already exists

echo.
echo Pushing to main branch...
git push -u origin main

echo.
echo Creating and switching to dev branch...
git checkout -b dev

echo.
echo Pushing dev branch...
git push -u origin dev

echo.
echo ========================================
echo Repository setup complete!
echo.
echo Branches created:
echo - main (pushed to GitHub)
echo - dev (pushed to GitHub)
echo.
echo Your code is now on GitHub!
echo ========================================
pause