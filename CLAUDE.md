# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Address History Tracker - A Flask web application for tracking residential address history over the past 10 years. Uses Supabase as the backend database with secure authentication and address management features.

## Common Commands

### Development
- **Start main application**: `py app.py` (runs on http://localhost:5000)
- **Start test version**: `py app_test.py` (file-based storage, no Supabase required)
- **Install dependencies**: `py -m pip install -r requirements.txt`

### Database & Testing
- **Verify Supabase connection**: `py verify_supabase.py`
- **Seed test data**: `py seed_test_data.py`
- **Check current user**: `py check_current_user.py`

## Architecture

### Core Components
- **Flask Application** (`app.py`): Main application with Supabase integration
- **Test Version** (`app_test.py`): Standalone version using file-based storage
- **Database Setup** (`database_setup.sql`): PostgreSQL schema for Supabase
- **Authentication**: Flask-Login with bcrypt password hashing
- **Frontend**: HTML templates with Tailwind CSS, vanilla JavaScript

### Database Schema
- **users table**: id, username, email, password_hash, created_at
- **addresses table**: id, user_id, street_address, city, state, postal_code, country, start_date, end_date, is_current, created_at

### Key Features
- Row Level Security (RLS) for data isolation
- Current address tracking (only one per user)
- Secure password hashing with bcrypt
- User session management

## Environment Setup

### Required Environment Variables (.env)
- `SUPABASE_URL`: Supabase project URL
- `SUPABASE_KEY`: Supabase anon key
- `FLASK_SECRET_KEY`: Flask session secret

### Database Setup
1. Create Supabase project
2. Run SQL from `database_setup.sql` or follow `SUPABASE_SETUP.md`
3. Set up Row Level Security policies
4. Configure environment variables

## Git Workflow

### Branch Structure
- **main**: Production-ready code (stable releases)
- **dev**: Development branch (integration and testing)

### Development Workflow
- Work on `dev` branch: `git checkout dev`
- Push changes: `git push origin dev`
- Merge to production: `git checkout main && git merge dev && git push origin main`
- See `GIT_WORKFLOW.md` for detailed commands

### Environment Configuration
- **Development**: Use `.env.development` template, run `py app_test.py`
- **Production**: Use `.env.production` template, run `py app.py`

## Development Notes

### Application Modes
- **Production Mode**: Uses Supabase database (`app.py`)
- **Test Mode**: Uses local JSON file storage (`app_test.py`)
- **Fallback**: Main app runs without database if Supabase not configured

### Security Features
- Bcrypt password hashing
- Flask-Login session management
- Supabase RLS for data isolation
- Input validation on all forms

### File Structure
- `templates/`: HTML templates (index.html, login.html, register.html)
- `addresses.json` / `addresses_test.json`: Test data storage
- `*_test.py`: Testing and verification utilities
- `*SETUP.md`: Documentation files
- `GIT_WORKFLOW.md`: Complete Git workflow documentation