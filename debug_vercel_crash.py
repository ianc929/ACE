#!/usr/bin/env python3
"""
Debug script to test what's causing the Vercel crash
"""

import sys
import traceback

try:
    print("=== Starting Vercel Debug ===")
    print(f"Python version: {sys.version}")
    
    print("1. Testing basic imports...")
    import os
    print("✓ os imported")
    
    print("2. Testing Flask import...")
    from flask import Flask
    print("✓ Flask imported")
    
    print("3. Testing flask-login import...")
    from flask_login import LoginManager
    print("✓ flask-login imported")
    
    print("4. Testing environment variables...")
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')
    flask_secret = os.getenv('FLASK_SECRET_KEY')
    
    print(f"SUPABASE_URL exists: {bool(supabase_url)}")
    print(f"SUPABASE_KEY exists: {bool(supabase_key)}")
    print(f"FLASK_SECRET_KEY exists: {bool(flask_secret)}")
    
    print("5. Testing Supabase import...")
    from supabase import create_client
    print("✓ Supabase imported")
    
    print("6. Testing app import...")
    from app import app
    print("✓ App imported successfully")
    
    print("=== All tests passed! ===")
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    print("Full traceback:")
    traceback.print_exc()
    
if __name__ == "__main__":
    print("Debug script completed")