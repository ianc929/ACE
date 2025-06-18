# Test Supabase Data Flow

Your Supabase integration is working! Here's how to test that data is being saved and deleted:

## ✅ Current Status
- **Supabase Connected**: ✅ Successfully connected
- **Database Tables**: ✅ Created and accessible
- **App Running**: ✅ http://localhost:5000

## 🧪 Test Steps

### Step 1: Register a New User
1. **Go to**: http://localhost:5000
2. **Click**: "Login" → "Register here"
3. **Fill in the form**:
   - Username: `testuser`
   - Email: `test@example.com`
   - Password: `password123`
   - Confirm Password: `password123`
4. **Click**: "Register"
5. **Expected**: "Registration successful! Please log in."

### Step 2: Login with New User
1. **Login with**:
   - Username: `testuser`
   - Password: `password123`
2. **Expected**: Successfully logged in and redirected to main page

### Step 3: Add an Address
1. **Click**: "Add New Address"
2. **Fill in the form**:
   - Street Address: `123 Test Street`
   - City: `Test City`
   - State: `TC`
   - Postal Code: `12345`
   - Country: `Test Country`
   - Start Date: Pick any date
   - Check: "This is my current address"
3. **Click**: "Add Address"
4. **Expected**: Address appears on the main page

### Step 4: Verify Data in Supabase
Run the verification script:
```bash
py verify_supabase.py
```

**Expected Output**:
```
👥 Users in database: 1
   - User: testuser (test@example.com) - Created: [timestamp]
🏠 Addresses in database: 1
   - Address 1: 123 Test Street, Test City, TC, Test Country (CURRENT)
     User ID: 1 - Created: [timestamp]
```

### Step 5: Test Address Deletion
1. **In the web app**, click the "Delete" button next to your address
2. **Confirm deletion**
3. **Run verification again**: `py verify_supabase.py`
4. **Expected**: `🏠 Addresses in database: 0`

### Step 6: Add Multiple Addresses
1. **Add another address** (different details)
2. **Don't check "current address"** this time
3. **Run verification**: `py verify_supabase.py`
4. **Expected**: Shows both addresses, only one marked as current

## 🔍 Alternative Verification Methods

### Method 1: Supabase Dashboard
1. **Go to**: Your Supabase project dashboard
2. **Click**: "Table Editor"
3. **View**: `users` and `addresses` tables
4. **See**: Your data directly in the database

### Method 2: Check Server Logs
Watch the terminal where `py app.py` is running:
- `POST /register` - User registration
- `POST /login` - User login
- `POST /add_address` - Address creation
- `DELETE /delete_address/[id]` - Address deletion

## ✅ Success Indicators

If everything is working correctly, you should see:
- ✅ Users can register and login
- ✅ Addresses are saved to Supabase
- ✅ Addresses can be deleted from Supabase
- ✅ Each user sees only their own addresses
- ✅ Data persists between app restarts
- ✅ Verification script shows correct data counts

## 🚨 Troubleshooting

If data isn't appearing:
1. **Check**: Are you using the Supabase app (`py app.py`) not the test app?
2. **Verify**: Your `.env` file has correct Supabase credentials
3. **Confirm**: Database tables were created with the SQL script
4. **Test**: Registration works (creates new users)

Your Supabase integration is ready and working! 🎉
