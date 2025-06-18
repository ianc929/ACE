@echo off
echo Deploying mobile-optimized UI improvements...
echo.

cd /d C:\ACE

echo Current branch:
git branch

echo.
echo Switching to dev branch...
git checkout dev

echo.
echo Adding mobile UI improvements...
git add .

echo.
echo Committing mobile UI optimization...
git commit -m "Optimize UI for mobile devices

- Responsive header with mobile-first design
- Mobile-optimized spacing and font sizes
- Touch-friendly button sizes and padding
- Improved modal form layout for mobile
- Better responsive grid layouts
- Enhanced readability on small screens
- Stack elements vertically on mobile
- Larger tap targets for better UX
- Optimized login and register pages

Generated with Claude Code"

echo.
echo Pushing to dev branch...
git push origin dev

echo.
echo Merging to production for deployment...
git checkout production
git merge dev
git push origin production

echo.
echo ========================================
echo MOBILE UI OPTIMIZATION DEPLOYED!
echo.
echo Mobile improvements made:
echo ✓ Responsive header design
echo ✓ Mobile-friendly font sizes (16px+ inputs)
echo ✓ Touch-optimized button sizes
echo ✓ Better spacing on small screens
echo ✓ Vertical stacking on mobile
echo ✓ Improved modal forms
echo ✓ Enhanced login/register pages
echo ✓ Better text readability
echo.
echo Vercel will automatically redeploy.
echo Test on mobile: https://www.mycloudgig.com
echo ========================================

pause