from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'test-secret-key-for-demo'

# Simple user database for testing (without Supabase)
USERS = {
    'admin': 'password123',
    'user': 'mypassword'
}

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, username):
        self.id = username
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    if user_id in USERS:
        return User(user_id)
    return None

# Simple file-based storage for testing
def load_addresses():
    try:
        with open('addresses_test.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_addresses(addresses):
    with open('addresses_test.json', 'w') as f:
        json.dump(addresses, f, indent=2)

@app.route('/')
def home():
    if current_user.is_authenticated:
        addresses = load_addresses()
        user_addresses = [addr for addr in addresses if addr.get('username') == current_user.username]
        return render_template('index.html', user=current_user, addresses=user_addresses)
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
        
        if username in USERS and USERS[username] == password:
            user = User(username)
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash('Registration is disabled in test mode. Use demo accounts.', 'error')
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
    try:
        data = request.json
        addresses = load_addresses()
        
        # If this is marked as current address, update other addresses to not be current
        if data.get('is_current', False):
            for addr in addresses:
                if addr.get('username') == current_user.username:
                    addr['is_current'] = False
        
        new_address = {
            'id': len(addresses) + 1,
            'username': current_user.username,
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
        
        addresses.append(new_address)
        save_addresses(addresses)
        
        return jsonify({'success': True, 'message': 'Address added successfully!'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete_address/<int:address_id>', methods=['DELETE'])
@login_required
def delete_address(address_id):
    try:
        addresses = load_addresses()
        addresses = [addr for addr in addresses if not (addr.get('id') == address_id and addr.get('username') == current_user.username)]
        save_addresses(addresses)
        
        return jsonify({'success': True, 'message': 'Address deleted successfully!'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🚀 Starting Address History Tracker (Test Mode)")
    print("📝 Demo accounts:")
    print("   Username: admin | Password: password123")
    print("   Username: user  | Password: mypassword")
    print("🌐 Open: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True)
