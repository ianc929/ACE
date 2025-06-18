@echo off
echo Setting up Vercel environment variables...
echo.

cd /d C:\ACE

echo Fixing merge conflicts and committing...
git add .
git commit -m "Fix merge conflicts and prepare for Vercel environment setup

- Resolved merge conflicts in requirements.txt, app.py, vercel.json, index.py
- Clean configuration ready for environment variable setup
- App now working, needs Supabase credentials in Vercel

Generated with Claude Code"

echo Pushing to production...
git checkout production
git merge dev
git push origin production

echo.
echo ========================================
echo MERGE CONFLICTS FIXED!
echo.
echo Now you need to add environment variables in Vercel:
echo.
echo 1. Go to your Vercel dashboard
echo 2. Click on your ACE project
echo 3. Go to Settings → Environment Variables
echo 4. Add these variables:
echo.
echo    SUPABASE_URL = your_supabase_project_url
echo    SUPABASE_KEY = your_supabase_anon_key
echo    FLASK_SECRET_KEY = your_secure_secret_key
echo.
echo 5. Set Environment to: Production
echo 6. Click Save
echo 7. Redeploy your project
echo.
echo Your app will then connect to Supabase!
echo ========================================

pause