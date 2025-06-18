@echo off
echo Setting up secure environment for ACE project...
echo.

cd /d C:\ACE

echo Checking if .env file exists...
if exist .env (
    echo .env file already exists. Backing up as .env.backup
    copy .env .env.backup
    echo.
)

echo Creating .env file from development template...
copy .env.development .env

echo.
echo ========================================
echo IMPORTANT: Edit your .env file now!
echo ========================================
echo.
echo 1. Open .env in Notepad
echo 2. Replace placeholder values with your actual:
echo    - Supabase URL
echo    - Supabase API Key  
echo    - Flask Secret Key
echo.
echo 3. NEVER commit the .env file to Git
echo    (It's already in .gitignore)
echo.
echo Your .env file is now ready for editing.
echo.
pause

notepad .env