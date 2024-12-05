import os
from todo_app import create_app

app = create_app()

if __name__ == '__main__':
    # Get the port from the environment variable or use 5000 as a default
    port = int(os.environ.get("PORT", 5000))
    
    # Run the app with host="0.0.0.0" so it can be accessed from outside the container
    app.run(host="0.0.0.0", port=port)
