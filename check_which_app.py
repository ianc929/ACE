"""
Quick script to check which app is running on port 5000
"""
import requests

try:
    response = requests.get('http://localhost:5000')
    content = response.text
    
    if "Registration is disabled in test mode" in content:
        print("❌ You're using the TEST APP (app_test.py)")
        print("🔄 You need to switch to the SUPABASE APP (app.py)")
        print("\n📝 To fix this:")
        print("1. Stop the test app (Ctrl+C in the terminal running app_test.py)")
        print("2. Make sure the Supabase app is running (py app.py)")
        print("3. Go to http://localhost:5000")
    elif "Address History Tracker" in content:
        print("✅ You're using the SUPABASE APP (app.py)")
        print("🎉 This is correct! You can register new users and add addresses.")
    else:
        print("❓ Unknown app running")
        
except Exception as e:
    print(f"❌ Error checking app: {e}")
    print("Make sure an app is running on http://localhost:5000")
