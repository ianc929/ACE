@echo off
echo Pushing security improvements to dev branch...
echo.

cd /d C:\ACE

echo Checking current branch...
git branch

echo Switching to dev branch...
git checkout dev

echo Adding all changes...
git add .

echo Committing changes...
git commit -m "Implement comprehensive security system for API key management

- Add secure environment variable validation in app.py
- Create SECURITY_GUIDE.md with best practices  
- Add setup_env.bat for easy secure configuration
- Update .gitignore with clear security documentation
- Sanitize .env file (removed exposed credentials)
- Implement template-based environment management

Generated with Claude Code"

echo Pushing to dev branch...
git push origin dev

echo.
echo ========================================
echo Push to dev branch complete!
echo Check GitHub to see the changes.
echo ========================================
pause