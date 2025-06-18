import sys
import traceback
import os

# Debug logging for Vercel
print(f"=== Vercel Handler Starting ===")
print(f"Python version: {sys.version}")
print(f"Environment variables loaded: {len(os.environ)}")

try:
    print("Importing Flask app...")
    from app import app
    print("✓ App imported successfully")
    
    # Vercel expects this exact variable name
    application = app
    
    print("✓ Application configured for Vercel")
    
except Exception as e:
    print(f"❌ IMPORT ERROR: {e}")
    traceback.print_exc()
    # Create a minimal error app
    from flask import Flask
    application = Flask(__name__)
    
    @application.route('/')
    def error():
        return f"Import Error: {str(e)}", 500

# For local development
if __name__ == "__main__":
    print("Running in local development mode")
    application.run(debug=True)
