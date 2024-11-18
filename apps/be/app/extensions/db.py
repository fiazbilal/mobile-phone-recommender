from flask_sqlalchemy import SQLAlchemy

# Create the database instance
db = SQLAlchemy()

# Example model for reference
class BaseModel(db.Model):
    """
    Base model with common fields for all models.
    Other models can inherit from this.
    """
    __abstract__ = True  # This makes it an abstract base class and not create a table for it
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

# Add other database-related utilities here as needed
