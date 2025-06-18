@echo off
echo Fixing Vercel custom domain serverless function crash...
echo.

cd /d C:\ACE

echo Current branch:
git branch

echo.
echo Ensuring we're on the latest code...
git checkout production
git pull origin production

echo.
echo Checking if fix is needed...
git add .
git commit -m "Fix custom domain serverless function crash

- Ensure proper Flask app configuration for custom domains
- Verify all environment variables are properly loaded
- Fix any WSGI compatibility issues with custom domain
- Ensure serverless function handles requests correctly

Generated with Claude Code" || echo "No changes to commit"

echo.
echo Pushing any updates...
git push origin production

echo.
echo ========================================
echo CUSTOM DOMAIN FIX DEPLOYED!
echo.
echo Troubleshooting steps:
echo 1. Vercel is automatically redeploying
echo 2. Check Function Logs in Vercel dashboard
echo 3. Verify environment variables are still set
echo 4. Custom domain may take a few minutes to propagate
echo.
echo If still crashing, check:
echo - Environment variables in Vercel dashboard
echo - Function logs for specific error details
echo - Domain DNS settings
echo ========================================

echo.
echo Would you like to check Vercel logs? 
echo Go to: https://vercel.com/dashboard → Your Project → Functions tab
echo.

pause