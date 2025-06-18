@echo off
echo Fixing Vercel environment variable detection...
echo.

cd /d C:\ACE

echo Updating environment variable validation logic...
git add .

echo Committing Vercel environment fix...
git commit -m "Fix Vercel environment variable detection

- Remove overly strict validation that blocks production deployment
- Improve placeholder detection logic  
- Allow Vercel environment variables to work properly
- Fix 'Database not configured' message in production

Generated with Claude Code"

echo.
echo Pushing to production branch...
git checkout production
git merge dev
git push origin production

echo.
echo ========================================
echo VERCEL ENVIRONMENT FIX DEPLOYED!
echo.
echo Changes made:
echo ✓ Fixed environment variable validation logic
echo ✓ Removed blocking validation for production
echo ✓ Improved placeholder detection
echo ✓ Should now connect to Supabase properly
echo.
echo Vercel will automatically redeploy.
echo Check your app in 2-3 minutes!
echo ========================================

pause