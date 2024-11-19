# app/__init__.py
from flask import Flask
from .config import Config
from app.db.setup import init_db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize the database
    init_db(app)

    # Import and register blueprints
    # from .routes import health, scraping, recommendation
    from .routes import health

    app.register_blueprint(health.bp)
    # app.register_blueprint(scraping.bp)
    # app.register_blueprint(recommendation.bp)

    return app
