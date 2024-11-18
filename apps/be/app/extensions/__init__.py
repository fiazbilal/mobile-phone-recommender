from flask_sqlalchemy import SQLAlchemy

# Initialize the extensions here
db = SQLAlchemy()

# If you are using other extensions like Flask-Migrate or Flask-Login, you can also initialize them here
# Example:
# from flask_migrate import Migrate
# migrate = Migrate()

# Add more extensions as needed
# Example:
# from flask_login import LoginManager
# login_manager = LoginManager()

__all__ = ["db"]
