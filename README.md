# Address History Tracker

A web application for tracking your residential address history over the past 10 years. Built with Flask, Supabase, and modern web technologies.

## Features

- **Secure Authentication**: User registration and login with bcrypt password hashing
- **Address Management**: Add, view, and delete address history
- **Current Address Tracking**: Mark and track your current residence
- **Modern UI**: Responsive design with Tailwind CSS
- **Database Integration**: Powered by Supabase PostgreSQL database
- **Date Range Tracking**: Record start and end dates for each address
- **User Isolation**: Each user can only see their own address data

## Quick Start

### Prerequisites
- Python 3.7+
- A Supabase account (free tier available)

### Installation

1. **Clone this repository**
   ```bash
   git clone <repository-url>
   cd address-history-tracker
   ```

2. **Install dependencies**
   ```bash
   py -m pip install -r requirements.txt
   ```

3. **Set up Supabase** (see detailed guide below)
   - Create a Supabase project
   - Set up database tables
   - Get your project credentials

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your Supabase credentials
   ```

5. **Run the application**
   ```bash
   py app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## Supabase Setup

For detailed Supabase setup instructions, see **[SUPABASE_SETUP.md](SUPABASE_SETUP.md)**

### Quick Setup Summary:
1. Create a Supabase project at [supabase.com](https://supabase.com)
2. Copy your project URL and anon key
3. Update your `.env` file with these credentials
4. Run the SQL commands provided in the setup guide to create tables
5. Test your connection by registering a new user

## Usage

### Getting Started
1. **Register**: Create a new account using the registration form
2. **Login**: Access your account with your credentials
3. **Add Addresses**: Click "Add New Address" to record your address history
4. **Manage Data**: View, edit, or delete your address records

### Adding an Address
Fill in the following information:
- **Street Address**: Your full street address
- **City**: City or town name
- **State/Province**: State, province, or region
- **Postal Code**: ZIP code or postal code
- **Country**: Country name
- **Start Date**: When you moved to this address
- **End Date**: When you moved out (optional for current address)
- **Current Address**: Check if this is your current residence

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: Supabase (PostgreSQL)
- **Authentication**: Flask-Login with bcrypt password hashing
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **Environment**: python-dotenv for configuration

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Row Level Security**: Database-level user data isolation
- **Session Management**: Secure Flask session handling
- **Input Validation**: Server-side validation for all inputs
- **CSRF Protection**: Built-in Flask security features

## Database Schema

### Users Table
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email address
- `password_hash`: Bcrypt hashed password
- `created_at`: Account creation timestamp

### Addresses Table
- `id`: Primary key
- `user_id`: Foreign key to users table
- `street_address`: Street address
- `city`: City name
- `state`: State/province
- `postal_code`: Postal/ZIP code
- `country`: Country name
- `start_date`: Move-in date
- `end_date`: Move-out date (nullable)
- `is_current`: Boolean flag for current address
- `created_at`: Record creation timestamp

## Development

### Local Development
1. Follow the installation steps above
2. Set `debug=True` in `app.py` (already configured)
3. The app will auto-reload on code changes

### Environment Variables
Required environment variables in `.env`:
```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
FLASK_SECRET_KEY=your_secure_secret_key
```

## Deployment

For production deployment:
1. Set up a production Supabase project
2. Configure environment variables on your hosting platform
3. Set `debug=False` in production
4. Use a production WSGI server (e.g., Gunicorn)
5. Enable HTTPS
6. Set up proper logging and monitoring

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

- **Setup Issues**: Check [SUPABASE_SETUP.md](SUPABASE_SETUP.md)
- **Supabase Docs**: [supabase.com/docs](https://supabase.com/docs)
- **Flask Docs**: [flask.palletsprojects.com](https://flask.palletsprojects.com/)
