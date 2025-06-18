"""
Seed Test Data for Address History Tracker
This script adds sample users and addresses to your Supabase database for testing
"""

import os
import bcrypt
from datetime import datetime, date
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def hash_password(password):
    """Hash a password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def seed_test_data():
    try:
        from supabase import create_client, Client
        
        SUPABASE_URL = os.getenv('SUPABASE_URL')
        SUPABASE_KEY = os.getenv('SUPABASE_KEY')
        
        if not SUPABASE_URL or not SUPABASE_KEY:
            print("❌ Environment variables not set")
            return False
            
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        print("🌱 Seeding test data to Supabase...")
        
        # Test users data
        test_users = [
            {
                'username': 'john_doe',
                'email': 'john.doe@example.com',
                'password_hash': hash_password('password123'),
                'created_at': datetime.now().isoformat()
            },
            {
                'username': 'jane_smith',
                'email': 'jane.smith@example.com',
                'password_hash': hash_password('password123'),
                'created_at': datetime.now().isoformat()
            },
            {
                'username': 'mike_wilson',
                'email': 'mike.wilson@example.com',
                'password_hash': hash_password('password123'),
                'created_at': datetime.now().isoformat()
            }
        ]
        
        # Insert test users
        print("👥 Adding test users...")
        for user in test_users:
            try:
                # Check if user already exists
                existing = supabase.table('users').select('username').eq('username', user['username']).execute()
                if not existing.data:
                    response = supabase.table('users').insert(user).execute()
                    if response.data:
                        print(f"   ✅ Added user: {user['username']}")
                    else:
                        print(f"   ❌ Failed to add user: {user['username']}")
                else:
                    print(f"   ⚠️  User already exists: {user['username']}")
            except Exception as e:
                print(f"   ❌ Error adding user {user['username']}: {e}")
        
        # Get user IDs for addresses
        users_response = supabase.table('users').select('id, username').execute()
        user_map = {user['username']: user['id'] for user in users_response.data}
        
        # Test addresses data
        test_addresses = [
            # John Doe's addresses
            {
                'user_id': user_map.get('john_doe'),
                'street_address': '123 Main Street',
                'city': 'New York',
                'state': 'NY',
                'postal_code': '10001',
                'country': 'United States',
                'start_date': '2020-01-15',
                'end_date': '2022-06-30',
                'is_current': False,
                'created_at': datetime.now().isoformat()
            },
            {
                'user_id': user_map.get('john_doe'),
                'street_address': '456 Oak Avenue',
                'city': 'Brooklyn',
                'state': 'NY',
                'postal_code': '11201',
                'country': 'United States',
                'start_date': '2022-07-01',
                'end_date': None,
                'is_current': True,
                'created_at': datetime.now().isoformat()
            },
            # Jane Smith's addresses
            {
                'user_id': user_map.get('jane_smith'),
                'street_address': '789 Pine Road',
                'city': 'Los Angeles',
                'state': 'CA',
                'postal_code': '90210',
                'country': 'United States',
                'start_date': '2019-03-10',
                'end_date': '2021-12-15',
                'is_current': False,
                'created_at': datetime.now().isoformat()
            },
            {
                'user_id': user_map.get('jane_smith'),
                'street_address': '321 Beach Boulevard',
                'city': 'Santa Monica',
                'state': 'CA',
                'postal_code': '90401',
                'country': 'United States',
                'start_date': '2021-12-16',
                'end_date': None,
                'is_current': True,
                'created_at': datetime.now().isoformat()
            },
            # Mike Wilson's addresses
            {
                'user_id': user_map.get('mike_wilson'),
                'street_address': '555 Tech Drive',
                'city': 'Austin',
                'state': 'TX',
                'postal_code': '73301',
                'country': 'United States',
                'start_date': '2021-08-01',
                'end_date': '2023-05-30',
                'is_current': False,
                'created_at': datetime.now().isoformat()
            },
            {
                'user_id': user_map.get('mike_wilson'),
                'street_address': '777 Innovation Way',
                'city': 'Seattle',
                'state': 'WA',
                'postal_code': '98101',
                'country': 'United States',
                'start_date': '2023-06-01',
                'end_date': None,
                'is_current': True,
                'created_at': datetime.now().isoformat()
            }
        ]
        
        # Insert test addresses
        print("🏠 Adding test addresses...")
        for addr in test_addresses:
            if addr['user_id']:  # Only add if user exists
                try:
                    response = supabase.table('addresses').insert(addr).execute()
                    if response.data:
                        current_text = " (CURRENT)" if addr['is_current'] else ""
                        print(f"   ✅ Added address: {addr['street_address']}, {addr['city']}{current_text}")
                    else:
                        print(f"   ❌ Failed to add address: {addr['street_address']}")
                except Exception as e:
                    print(f"   ❌ Error adding address {addr['street_address']}: {e}")
        
        print("\n🎉 Test data seeding complete!")
        print("\n📋 Test Login Credentials:")
        print("   Username: john_doe    | Password: password123")
        print("   Username: jane_smith  | Password: password123") 
        print("   Username: mike_wilson | Password: password123")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🌱 Address History Tracker - Test Data Seeder")
    print("=" * 50)
    seed_test_data()
    print("\n🔍 Run 'py verify_supabase.py' to see the data!")
