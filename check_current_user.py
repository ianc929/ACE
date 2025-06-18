"""
Check what user is currently logged in and if they exist in Supabase
"""
import os
from dotenv import load_dotenv

load_dotenv()

def check_current_user():
    try:
        from supabase import create_client, Client
        
        SUPABASE_URL = os.getenv('SUPABASE_URL')
        SUPABASE_KEY = os.getenv('SUPABASE_KEY')
        
        if not SUPABASE_URL or not SUPABASE_KEY:
            print("❌ Environment variables not set")
            return
            
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        print("👥 Users in Supabase database:")
        users_response = supabase.table('users').select('id, username, email').execute()
        
        for user in users_response.data:
            print(f"   - ID: {user['id']} | Username: {user['username']} | Email: {user['email']}")
        
        print("\n🔑 To test address creation, login with one of these users:")
        print("   Username: john_doe    | Password: password123")
        print("   Username: jane_smith  | Password: password123")
        print("   Username: mike_wilson | Password: password123")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🔍 Current User Check")
    print("=" * 30)
    check_current_user()
