@echo off
echo Deploying modern tech company UI styling...
echo.

cd /d C:\ACE

echo Current branch:
git branch

echo.
echo Switching to dev branch...
git checkout dev

echo.
echo Adding tech styling updates...
git add .

echo.
echo Committing modern tech UI design...
git commit -m "Transform UI to modern tech company design

🚀 Modern Tech Company Redesign:
- Gradient backgrounds with purple/blue theme
- Glass morphism effects with backdrop blur
- Floating particle animations
- FontAwesome icons throughout interface
- Glow button hover effects
- Glassmorphic cards with hover animations
- Tech-style modal with gradient styling
- Enhanced color scheme (emerald/teal/purple)
- Smooth transitions and micro-interactions
- Modern typography and spacing
- Cool hover effects and transformations

Mobile optimizations maintained:
- Responsive design preserved
- Touch-friendly interactions
- Mobile-first approach
- Optimized font sizes and spacing

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
echo MODERN TECH UI DEPLOYED! 🚀
echo.
echo New features:
echo ✓ Gradient backgrounds (purple/blue theme)
echo ✓ Glass morphism effects
echo ✓ Floating animations
echo ✓ FontAwesome icons
echo ✓ Glow button effects
echo ✓ Modern card designs
echo ✓ Smooth transitions
echo ✓ Cool hover animations
echo ✓ Tech company aesthetic
echo ✓ Enhanced visual hierarchy
echo.
echo Your app now looks like a cutting-edge tech startup!
echo Visit: https://www.mycloudgig.com
echo ========================================

pause