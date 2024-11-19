# run.py
from app import create_app
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = create_app()

if __name__ == '__main__':
    debug = os.getenv('DEBUG', 'False') == 'True'
    host = os.getenv('APP_HOST', '127.0.0.1')
    port = int(os.getenv('APP_PORT', 5000))
    
    app.run(
        debug=debug, 
        host=host, 
        port=port
    )
