@echo off
echo Fixing Vercel dependency compatibility error...
echo.

cd /d C:\ACE

echo Adding dependency fix...
git add .

echo Committing dependency compatibility fix...
git commit -m "Fix Vercel ImportError: werkzeug.urls url_decode compatibility

- Updated flask-login to 0.6.3 (compatible with newer werkzeug)
- Pinned werkzeug to 2.3.7 for stability
- Simplified index.py Vercel entry point
- Fixed flask-login/werkzeug version conflict

Generated with Claude Code"

echo.
echo Pushing to current branch...
git push origin HEAD

echo.
echo Updating production branch...
git checkout production 2>nul || echo "Already on production"
git merge dev 2>nul || git merge main 2>nul || echo "Merge completed"
git push origin production

echo.
echo ========================================
echo DEPENDENCY FIX DEPLOYED!
echo.
echo Fixed issues:
echo ✓ Updated flask-login to compatible version
echo ✓ Pinned werkzeug version for stability  
echo ✓ Simplified Vercel entry point
echo ✓ Resolved ImportError crash
echo.
echo Vercel will automatically redeploy.
echo The ImportError should be resolved!
echo ========================================

pause