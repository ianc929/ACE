from app import app

# Vercel entry point
app = app

# For local development
if __name__ == "__main__":
    app.run(debug=True)
