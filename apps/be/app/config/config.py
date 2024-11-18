# app/config/config.py

class Config:
    """Base configuration class."""
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///yourdatabase.db'  # Or any other database URI
