"""
Supabase Data Verification Script
Run this to check if data is being stored in your Supabase database
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def verify_supabase_connection():
    try:
        from supabase import create_client, Client
        
        SUPABASE_URL = os.getenv('SUPABASE_URL')
        SUPABASE_KEY = os.getenv('SUPABASE_KEY')
        
        if not SUPABASE_URL or not SUPABASE_KEY:
            print("❌ Environment variables not set")
            return False
            
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        print("🔍 Checking Supabase connection...")
        
        # Check users table
        users_response = supabase.table('users').select('id, username, email, created_at').execute()
        print(f"👥 Users in database: {len(users_response.data)}")
        
        for user in users_response.data:
            print(f"   - User: {user['username']} ({user['email']}) - Created: {user['created_at']}")
        
        # Check addresses table
        addresses_response = supabase.table('addresses').select('id, user_id, street_address, city, state, country, is_current, created_at').execute()
        print(f"🏠 Addresses in database: {len(addresses_response.data)}")
        
        for addr in addresses_response.data:
            current_text = " (CURRENT)" if addr['is_current'] else ""
            print(f"   - Address {addr['id']}: {addr['street_address']}, {addr['city']}, {addr['state']}, {addr['country']}{current_text}")
            print(f"     User ID: {addr['user_id']} - Created: {addr['created_at']}")
        
        print("\n✅ Supabase verification complete!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Supabase Data Verification")
    print("=" * 40)
    verify_supabase_connection()
