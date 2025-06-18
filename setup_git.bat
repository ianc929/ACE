@echo off
echo Setting up Git repository for Address History Tracker...
echo.

:: Change to the project directory
cd /d C:\ACE

:: Initialize Git repository
echo Initializing Git repository...
git init
git branch -M main

:: Configure Git (you'll need to edit these with your actual details)
echo Please edit this file to add your name and email before running!
echo git config --global user.name "Ian"
echo git config --global user.email "ianc929@gmail.com"
pause

:: Add files and commit
echo Adding files to Git...
git add .
git status
echo.
echo Creating initial commit...
git commit -m "Initial commit: Address History Tracker with dev/prod setup"

:: Create development branch
echo Creating development branch...
git checkout -b dev
echo Switching back to main branch...
git checkout main

echo.
echo ========================================
echo Git setup complete!
echo.
echo Branches created:
echo - main (production)
echo - dev (development)
echo.
echo Next steps:
echo 1. Create repository on GitHub
echo 2. Run: git remote add origin https://github.com/yourusername/repo-name.git
echo 3. Run: git push -u origin main
echo 4. Run: git push -u origin dev
echo ========================================
pause