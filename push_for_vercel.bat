@echo off
echo Pushing Vercel configuration to trigger automatic deployment...
echo.

cd /d C:\ACE

echo Current branch:
git branch

echo.
echo Switching to dev branch to commit changes...
git checkout dev

echo Adding Vercel configuration files...
git add .

echo Committing Vercel deployment configuration...
git commit -m "Add Vercel deployment configuration

- Add vercel.json for proper Flask deployment routing
- Create index.py as Vercel serverless entry point
- Pin dependency versions in requirements.txt  
- Configure app.py for production environment
- Ready for automatic Vercel deployment

Generated with Claude Code"

echo.
echo Pushing to dev branch...
git push origin dev

echo.
echo Merging dev into production for deployment...
git checkout production
git merge dev
git push origin production

echo.
echo ========================================
echo Code pushed to GitHub!
echo.
echo Vercel should automatically:
echo 1. Detect the push to production branch
echo 2. Start a new deployment
echo 3. Use the new vercel.json configuration
echo.
echo Check your Vercel dashboard for deployment status.
echo ========================================

echo.
echo IMPORTANT: Set these environment variables in Vercel:
echo - SUPABASE_URL (your Supabase project URL)
echo - SUPABASE_KEY (your Supabase anon key) 
echo - FLASK_SECRET_KEY (a secure random string)
echo.

pause