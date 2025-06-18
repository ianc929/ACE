@echo off
echo Updating all branches with Vercel 404 fix...
echo.

cd /d C:\ACE

echo Step 1: Committing changes to dev branch...
git checkout dev
git add .
git commit -m "Fix Vercel 404 NOT_FOUND error

- Updated vercel.json to use index.py as entry point
- Modified index.py for proper Vercel serverless deployment  
- Exposed Flask app as 'application' for WSGI compatibility
- Fixed routing configuration for Vercel platform

Generated with Claude Code"

echo Pushing dev branch...
git push origin dev

echo.
echo Step 2: Updating main branch...
git checkout main
git merge dev
git push origin main

echo.
echo Step 3: Updating production branch for deployment...
git checkout production  
git merge main
git push origin production

echo.
echo ========================================
echo ALL BRANCHES UPDATED!
echo.
echo Branch Status:
echo ✓ dev - Latest development code
echo ✓ main - Production-ready code  
echo ✓ production - Vercel deployment ready
echo.
echo Vercel will automatically redeploy from production branch.
echo Check your deployment status in Vercel dashboard.
echo ========================================

echo.
echo Switching back to dev for continued development...
git checkout dev

pause