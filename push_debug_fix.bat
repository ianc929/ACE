@echo off
echo Pushing debug version to identify Vercel crash...
echo.

cd /d C:\ACE

echo Adding debug files...
git add .

echo Committing debug version...
git commit -m "Add debug logging to identify Vercel crash cause

- Added comprehensive debug logging to index.py
- Created debug_vercel_crash.py for testing
- Added error handling and traceback logging
- Will help identify exact crash location

Generated with Claude Code"

echo.
echo Pushing to production...
git checkout production
git merge dev
git push origin production

echo.
echo ========================================
echo DEBUG VERSION DEPLOYED!
echo.
echo Now check your custom domain:
echo https://www.mycloudgig.com
echo.
echo If it shows an error, it will now tell us exactly what's wrong.
echo Check Vercel Function Logs for detailed debug output.
echo.
echo The error page will show the specific import or runtime error.
echo ========================================

pause