from app import app

# This is the handler function Vercel expects
def handler(event, context):
    return app

# Also expose as application for WSGI compatibility
application = app

# For local development
if __name__ == "__main__":
    app.run(debug=True)
