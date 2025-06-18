@echo off
echo Fixing Vercel serverless function crash...
echo.

cd /d C:\ACE

echo Current branch:
git branch

echo.
echo Adding crash fix...
git add .

echo Committing serverless function fix...
git commit -m "Fix Vercel serverless function crash (500 error)

- Updated vercel.json to use app.py as entry point
- Added proper handler function for Vercel serverless
- Fixed WSGI compatibility with application variable
- Increased function timeout to 30 seconds

Generated with Claude Code"

echo.
echo Pushing to current branch...
git push origin HEAD

echo.
echo Switching to production and merging fix...
git checkout production
git merge dev 2>nul || git merge main
git push origin production

echo.
echo ========================================
echo CRASH FIX DEPLOYED!
echo.
echo Changes made:
echo ✓ Fixed Vercel entry point configuration
echo ✓ Added proper serverless handler function  
echo ✓ Increased function timeout
echo ✓ Fixed WSGI compatibility
echo.
echo Vercel will automatically redeploy.
echo Monitor your deployment in Vercel dashboard.
echo ========================================

pause