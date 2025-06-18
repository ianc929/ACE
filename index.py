from app import app

# Vercel serverless handler - this is what Vercel calls
def handler(event, context):
    return app

# Also expose as app for direct import
application = app

# For local development
if __name__ == "__main__":
    app.run(debug=True)
