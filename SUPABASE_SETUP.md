# Supabase Setup Guide for Address History Tracker

This guide will help you set up Supabase as the database backend for your Address History Tracker application.

## Step 1: Create a Supabase Project

1. Go to [https://supabase.com](https://supabase.com)
2. Sign up for a free account or log in
3. Click "New Project"
4. Choose your organization
5. Fill in project details:
   - **Name**: Address History Tracker
   - **Database Password**: Choose a strong password
   - **Region**: Select the closest region to your users
6. Click "Create new project"
7. Wait for the project to be created (usually takes 1-2 minutes)

## Step 2: Get Your Project Credentials

1. In your Supabase dashboard, go to **Settings** → **API**
2. Copy the following values:
   - **Project URL** (looks like: `https://your-project-id.supabase.co`)
   - **Anon public key** (starts with `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`)

## Step 3: Update Your Environment Variables

1. Open your `.env` file in the project root
2. Replace the placeholder values:

```env
# Supabase Configuration
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...your-anon-key

# Flask Secret Key (already configured)
FLASK_SECRET_KEY=31023335be1b0b1c35c5c549daf6c51f33a3449e40b0e2c1d6e2f26aad00dc4d
```

## Step 4: Create Database Tables

In your Supabase dashboard, go to **SQL Editor** and run the following SQL commands:

### Create Users Table

```sql
-- Create users table
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create index for faster lookups
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
```

### Create Addresses Table

```sql
-- Create addresses table
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

-- Create indexes for better performance
CREATE INDEX idx_addresses_user_id ON addresses(user_id);
CREATE INDEX idx_addresses_created_at ON addresses(created_at DESC);
CREATE INDEX idx_addresses_is_current ON addresses(is_current);
```

### Set Up Row Level Security (RLS)

```sql
-- Enable RLS on users table
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Enable RLS on addresses table
ALTER TABLE addresses ENABLE ROW LEVEL SECURITY;

-- Policy for users table (users can only see their own data)
CREATE POLICY "Users can view own profile" ON users
    FOR SELECT USING (auth.uid()::text = id::text);

CREATE POLICY "Users can update own profile" ON users
    FOR UPDATE USING (auth.uid()::text = id::text);

-- Policy for addresses table (users can only see their own addresses)
CREATE POLICY "Users can view own addresses" ON addresses
    FOR SELECT USING (auth.uid()::text = user_id::text);

CREATE POLICY "Users can insert own addresses" ON addresses
    FOR INSERT WITH CHECK (auth.uid()::text = user_id::text);

CREATE POLICY "Users can update own addresses" ON addresses
    FOR UPDATE USING (auth.uid()::text = user_id::text);

CREATE POLICY "Users can delete own addresses" ON addresses
    FOR DELETE USING (auth.uid()::text = user_id::text);
```

## Step 5: Install Dependencies

Run the following command to install the required Python packages:

```bash
py -m pip install -r requirements.txt
```

## Step 6: Test Your Setup

1. Start your Flask application:
   ```bash
   py app.py
   ```

2. Open your browser and go to `http://localhost:5000`

3. Try registering a new account:
   - Click "Register here" on the login page
   - Fill in the registration form
   - Submit the form

4. If successful, you should be redirected to login

5. Log in with your new account and try adding an address

## Troubleshooting

### Common Issues:

1. **"Database not configured" error**:
   - Check that your `.env` file has the correct SUPABASE_URL and SUPABASE_KEY
   - Make sure the `.env` file is in the same directory as `app.py`

2. **"Permission denied" errors**:
   - Make sure you've set up Row Level Security policies correctly
   - Check that the tables were created successfully

3. **Connection errors**:
   - Verify your Supabase project is active
   - Check your internet connection
   - Ensure the SUPABASE_URL is correct

4. **Import errors**:
   - Make sure all dependencies are installed: `py -m pip install -r requirements.txt`

### Checking Your Setup:

1. In Supabase dashboard, go to **Table Editor**
2. You should see `users` and `addresses` tables
3. Try inserting a test record to verify everything works

## Security Notes

- **Never commit your `.env` file** to version control
- **Use strong passwords** for your Supabase project
- **Enable 2FA** on your Supabase account
- **Regularly rotate your API keys** in production
- **Use environment-specific projects** (separate for dev/staging/production)

## Production Considerations

For production deployment:

1. **Use a custom domain** for your Supabase project
2. **Set up proper backup strategies**
3. **Monitor your database usage**
4. **Implement proper logging**
5. **Use connection pooling** for high-traffic applications
6. **Set up database monitoring and alerts**

## Support

If you encounter issues:

1. Check the [Supabase Documentation](https://supabase.com/docs)
2. Visit the [Supabase Community](https://github.com/supabase/supabase/discussions)
3. Review the application logs for specific error messages
