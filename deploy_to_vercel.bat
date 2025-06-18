@echo off
echo Deploying ACE to Vercel with proper configuration...
echo.

cd /d C:\ACE

echo Adding Vercel configuration files...
git add vercel.json index.py requirements.txt app.py

echo Committing Vercel deployment files...
git commit -m "Add Vercel deployment configuration

- Add vercel.json for proper Python/Flask deployment
- Create index.py as Vercel entry point  
- Update requirements.txt with pinned versions
- Configure app.py for production deployment

Generated with Claude Code"

echo.
echo Pushing to production branch...
git checkout production
git merge dev
git push origin production

echo.
echo ========================================
echo Vercel Configuration Added!
echo.
echo Next steps:
echo 1. In Vercel dashboard, redeploy your project
echo 2. Set environment variables in Vercel:
echo    - SUPABASE_URL
echo    - SUPABASE_KEY  
echo    - FLASK_SECRET_KEY
echo 3. Make sure you're deploying from 'production' branch
echo ========================================

pause