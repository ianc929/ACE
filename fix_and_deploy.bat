@echo off
echo Fixing merge conflicts and deploying to Vercel...
echo.

cd /d C:\ACE

echo Step 1: Adding resolved files...
git add .

echo Step 2: Committing merge conflict resolution...
git commit -m "Resolve merge conflicts and fix Vercel 404 error

- Fixed merge conflicts in app.py, vercel.json, and index.py
- Proper Vercel configuration with index.py entry point
- Exposed Flask app as 'application' for WSGI compatibility
- Ready for automatic Vercel deployment

Generated with Claude Code"

echo Step 3: Pushing to dev branch...
git push origin dev

echo.
echo Step 4: Updating production branch for Vercel...
git checkout production
git merge dev
git push origin production

echo.
echo ========================================
echo DEPLOYMENT COMPLETE!
echo.
echo ✓ Merge conflicts resolved
echo ✓ Code pushed to production branch  
echo ✓ Vercel will automatically redeploy
echo.
echo Check your Vercel dashboard in 2-3 minutes.
echo Your 404 error should be fixed!
echo ========================================

pause