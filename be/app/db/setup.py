from flask import Flask
from . import db

def init_db(app: Flask):
    """Bind SQLAlchemy to the Flask app and initialize the database."""
    db.init_app(app)
    with app.app_context():
        db.create_all()
