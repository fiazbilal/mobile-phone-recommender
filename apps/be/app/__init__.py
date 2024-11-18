# app/__init__.py

from flask import Flask
from app.extensions.db import db  # Import the db object from extensions
from app.config.config import Config  # Import Config from app/config/config.py

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    return app
