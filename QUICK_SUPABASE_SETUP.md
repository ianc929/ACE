# Quick Supabase Setup - Step by Step

Follow these exact steps to get your Address History Tracker working with Supabase database.

## Step 1: Create Supabase Account & Project

1. **Go to** [https://supabase.com](https://supabase.com)
2. **Click "Start your project"** and sign up (free)
3. **Click "New Project"**
4. **Fill in:**
   - Name: `Address History Tracker`
   - Database Password: `YourSecurePassword123!` (remember this)
   - Region: Choose closest to you
5. **Click "Create new project"** (takes 1-2 minutes)

## Step 2: Get Your Credentials

1. **In your Supabase dashboard**, click **Settings** → **API**
2. **Copy these two values:**
   - **Project URL**: `https://xxxxxxxxxxxxx.supabase.co`
   - **Anon public key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` (long string)

## Step 3: Update Your .env File

1. **Open your `.env` file** in the project
2. **Replace the placeholder values:**

```env
# Supabase Configuration
SUPABASE_URL=https://xxxxxxxxxxxxx.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...your-actual-key

# Flask Secret Key (already configured)
FLASK_SECRET_KEY=31023335be1b0b1c35c5c549daf6c51f33a3449e40b0e2c1d6e2f26aad00dc4d
```

## Step 4: Create Database Tables

1. **In Supabase dashboard**, go to **SQL Editor**
2. **Click "New query"**
3. **Copy and paste this SQL** (run each block separately):

### Create Users Table:
```sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
```

### Create Addresses Table:
```sql
CREATE TABLE addresses (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
    street_address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_current BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_addresses_user_id ON addresses(user_id);
CREATE INDEX idx_addresses_created_at ON addresses(created_at DESC);
```

## Step 5: Install Compatible Supabase Version

```bash
py -m pip uninstall supabase -y
py -m pip install supabase==1.0.4
```

## Step 6: Test Your Setup

1. **Stop the current test app** (Ctrl+C in terminal)
2. **Run the Supabase version:**
   ```bash
   py app.py
   ```
3. **Open browser:** http://localhost:5000
4. **Register a new account** (not the demo ones)
5. **Add an address** and verify it saves to Supabase

## Step 7: Verify in Supabase

1. **Go to Supabase dashboard** → **Table Editor**
2. **Click on "users" table** - you should see your registered user
3. **Click on "addresses" table** - you should see your added address

## Troubleshooting

### If you get import errors:
```bash
py -m pip uninstall supabase gotrue postgrest realtime storage3 supafunc -y
py -m pip install supabase==1.0.4
```

### If you get "Database not configured":
- Double-check your `.env` file has the correct SUPABASE_URL and SUPABASE_KEY
- Make sure there are no extra spaces or quotes around the values

### If you get "Permission denied":
- Make sure you created the tables with the exact SQL above
- Check that your Supabase project is active (not paused)

## Success Indicators

✅ **App starts without errors**
✅ **You can register a new user**
✅ **You can add addresses**
✅ **Addresses appear in Supabase Table Editor**
✅ **You can delete addresses**
✅ **Different users see different data**

Once this works, your app is fully integrated with Supabase!
