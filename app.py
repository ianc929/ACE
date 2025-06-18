from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime
import bcrypt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Validate required environment variables
required_env_vars = ['SUPABASE_URL', 'SUPABASE_KEY', 'FLASK_SECRET_KEY']
missing_vars = [var for var in required_env_vars if not os.getenv(var) or os.getenv(var).startswith('your_')]

if missing_vars:
    print("❌ Missing or placeholder environment variables:")
    for var in missing_vars:
        print(f"   - {var}")
    print("📝 Please update your .env file with actual values")
    print("💡 Run setup_env.bat to configure your environment")

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', os.urandom(24))

# Supabase configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

supabase = None
if SUPABASE_URL and SUPABASE_KEY and SUPABASE_URL != 'your_supabase_project_url_here':
    try:
        from supabase import create_client, Client
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("✅ Supabase connected successfully!")
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        print("📝 Running in fallback mode. Check QUICK_SUPABASE_SETUP.md for setup instructions.")
else:
    print("📝 Supabase not configured. Check QUICK_SUPABASE_SETUP.md for setup instructions.")

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, email=None):
        self.id = str(id)
        self.username = username
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    if not supabase:
        return None
    try:
        response = supabase.table('users').select('*').eq('id', user_id).execute()
        if response.data:
            user_data = response.data[0]
            return User(user_data['id'], user_data['username'], user_data.get('email'))
    except Exception as e:
        print(f"Error loading user: {e}")
    return None

def hash_password(password):
    """Hash a password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed):
    """Check if password matches the hashed version"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

@app.route('/')
def home():
    if current_user.is_authenticated and supabase:
        try:
            # Get user's addresses from Supabase
            response = supabase.table('addresses').select('*').eq('user_id', current_user.id).order('created_at', desc=True).execute()
            addresses = response.data if response.data else []
            return render_template('index.html', user=current_user, addresses=addresses)
        except Exception as e:
            flash(f'Error loading addresses: {str(e)}', 'error')
            return render_template('index.html', user=current_user, addresses=[])
    return render_template('index.html', user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('Please enter both username and password!', 'error')
            return render_template('login.html')
        
        if not supabase:
            flash('Database not configured. Please set up Supabase.', 'error')
            return render_template('login.html')
        
        try:
            # Check if user exists in Supabase
            response = supabase.table('users').select('*').eq('username', username).execute()
            
            if response.data and len(response.data) > 0:
                user_data = response.data[0]
                if check_password(password, user_data['password_hash']):
                    user = User(user_data['id'], user_data['username'], user_data.get('email'))
                    login_user(user)
                    flash('Logged in successfully!', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Invalid username or password!', 'error')
            else:
                flash('Invalid username or password!', 'error')
                
        except Exception as e:
            flash(f'Login error: {str(e)}', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not all([username, email, password, confirm_password]):
            flash('Please fill in all fields!', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return render_template('register.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long!', 'error')
            return render_template('register.html')
        
        if not supabase:
            flash('Database not configured. Please set up Supabase.', 'error')
            return render_template('register.html')
        
        try:
            # Check if username already exists
            response = supabase.table('users').select('username').eq('username', username).execute()
            if response.data:
                flash('Username already exists!', 'error')
                return render_template('register.html')
            
            # Check if email already exists
            response = supabase.table('users').select('email').eq('email', email).execute()
            if response.data:
                flash('Email already registered!', 'error')
                return render_template('register.html')
            
            # Create new user
            hashed_password = hash_password(password)
            user_data = {
                'username': username,
                'email': email,
                'password_hash': hashed_password,
                'created_at': datetime.now().isoformat()
            }
            
            response = supabase.table('users').insert(user_data).execute()
            
            if response.data:
                flash('Registration successful! Please log in.', 'success')
                return redirect(url_for('login'))
            else:
                flash('Registration failed. Please try again.', 'error')
                
        except Exception as e:
            flash(f'Registration error: {str(e)}', 'error')
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/add_address', methods=['POST'])
@login_required
def add_address():
    if not supabase:
        return jsonify({'error': 'Database not configured'}), 500
    
    try:
        data = request.json
        print(f"🔍 DEBUG: Received data: {data}")
        print(f"🔍 DEBUG: Current user ID: {current_user.id}")
        
        # Validate required fields
        required_fields = ['street_address', 'city', 'state', 'postal_code', 'country', 'start_date']
        for field in required_fields:
            if not data.get(field):
                print(f"❌ DEBUG: Missing field: {field}")
                return jsonify({'error': f'{field.replace("_", " ").title()} is required'}), 400
        
        # If this is marked as current address, update other addresses to not be current
        if data.get('is_current', False):
            print("🔍 DEBUG: Updating other addresses to not current")
            update_response = supabase.table('addresses').update({'is_current': False}).eq('user_id', current_user.id).execute()
            print(f"🔍 DEBUG: Update response: {update_response}")
        
        address_data = {
            'user_id': int(current_user.id),  # Ensure it's an integer
            'street_address': data.get('street_address'),
            'city': data.get('city'),
            'state': data.get('state'),
            'postal_code': data.get('postal_code'),
            'country': data.get('country'),
            'start_date': data.get('start_date'),
            'end_date': data.get('end_date') if data.get('end_date') else None,
            'is_current': data.get('is_current', False),
            'created_at': datetime.now().isoformat()
        }
        
        print(f"🔍 DEBUG: Address data to insert: {address_data}")
        
        response = supabase.table('addresses').insert(address_data).execute()
        print(f"🔍 DEBUG: Insert response: {response}")
        print(f"🔍 DEBUG: Response data: {response.data}")
        
        if response.data:
            print("✅ DEBUG: Address inserted successfully")
            return jsonify({'success': True, 'message': 'Address added successfully!'})
        else:
            print("❌ DEBUG: No data returned from insert")
            return jsonify({'error': 'Failed to add address - no data returned'}), 500
    
    except Exception as e:
        print(f"❌ DEBUG: Exception in add_address: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/delete_address/<int:address_id>', methods=['DELETE'])
@login_required
def delete_address(address_id):
    if not supabase:
        return jsonify({'error': 'Database not configured'}), 500
    
    try:
        # Verify the address belongs to the current user before deleting
        response = supabase.table('addresses').delete().eq('id', address_id).eq('user_id', current_user.id).execute()
        
        return jsonify({'success': True, 'message': 'Address deleted successfully!'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Expose app for Vercel deployment
application = app

if __name__ == '__main__':
    app.run(debug=True)
