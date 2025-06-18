from app import app

# Vercel serverless function handler
def handler(request):
    return app(request.environ, lambda status, headers: None)

# For local development
if __name__ == "__main__":
    app.run(debug=True)