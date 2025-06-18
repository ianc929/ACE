# Git Workflow Guide - Address History Tracker

## Branch Structure

- **main** - Production-ready code (stable releases)
- **dev** - Development branch (integration and testing)

## Initial Setup Commands

Run these commands in **Command Prompt/PowerShell** from your `C:\ACE` directory:

### 1. Initialize Git Repository
```cmd
cd C:\ACE
git init
git branch -M main
```

### 2. Configure Git (if not done before)
```cmd
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Add Files and Initial Commit
```cmd
git add .
git commit -m "Initial commit: Address History Tracker with dev/prod setup"
```

### 4. Create Development Branch
```cmd
git checkout -b dev
git push -u origin dev
git checkout main
```

### 5. Connect to GitHub
```cmd
# Create repository on GitHub first, then:
git remote add origin https://github.com/yourusername/ACE.git
git push -u origin main
git push -u origin dev
```

## Daily Development Workflow

### Working on Features (Development)

1. **Switch to dev branch:**
   ```cmd
   git checkout dev
   git pull origin dev
   ```

2. **Make your changes and test locally:**
   ```cmd
   # Start development server
   py app_test.py
   # or
   py app.py
   ```

3. **Stage and commit changes:**
   ```cmd
   git add .
   git commit -m "Add feature: description of what you built"
   ```

4. **Push to dev branch:**
   ```cmd
   git push origin dev
   ```

### Merging to Production

When dev branch is stable and ready for production:

1. **Switch to main branch:**
   ```cmd
   git checkout main
   git pull origin main
   ```

2. **Merge dev into main:**
   ```cmd
   git merge dev
   ```

3. **Push to production:**
   ```cmd
   git push origin main
   ```

4. **Tag the release (optional but recommended):**
   ```cmd
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

## Environment Management

### Development Environment
- Use `.env.development` template to create your `.env`
- Run `py app_test.py` for file-based testing
- Or use development Supabase project with `py app.py`

### Production Environment
- Use `.env.production` template for production deployment
- Set `FLASK_DEBUG=False`
- Use separate production Supabase project

## Common Git Commands

### Viewing Status and History
```cmd
git status                    # See current changes
git log --oneline            # View commit history
git branch -a                # List all branches
```

### Creating Feature Branches (Advanced)
```cmd
git checkout dev
git checkout -b feature/new-feature-name
# Work on feature
git add .
git commit -m "Implement new feature"
git checkout dev
git merge feature/new-feature-name
git branch -d feature/new-feature-name
```

### Emergency Hotfixes
```cmd
git checkout main
git checkout -b hotfix/critical-bug-fix
# Fix the bug
git add .
git commit -m "Fix critical bug"
git checkout main
git merge hotfix/critical-bug-fix
git push origin main
# Also merge into dev
git checkout dev
git merge hotfix/critical-bug-fix
git push origin dev
git branch -d hotfix/critical-bug-fix
```

## Deployment Considerations

### Development Deployment
- Deploy from `dev` branch
- Use development environment variables
- Enable debug mode for testing

### Production Deployment
- Deploy only from `main` branch
- Use production environment variables
- Disable debug mode
- Use production database

## Best Practices

1. **Never work directly on main branch**
2. **Always test on dev before merging to main**
3. **Write descriptive commit messages**
4. **Pull before pushing to avoid conflicts**
5. **Use tags for releases**
6. **Keep sensitive data in .env files (never commit them)**

## Troubleshooting

### Merge Conflicts
```cmd
# When merge conflicts occur:
git status                   # See conflicted files
# Edit files to resolve conflicts
git add .
git commit -m "Resolve merge conflicts"
```

### Undo Last Commit (if not pushed)
```cmd
git reset --soft HEAD~1      # Keep changes staged
git reset --hard HEAD~1      # Discard changes completely
```

### View Differences
```cmd
git diff                     # See unstaged changes
git diff --staged            # See staged changes
git diff main dev            # Compare branches
```