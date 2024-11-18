from app.extensions.db import db
from app.extensions.db import BaseModel

class MobilePhone(BaseModel):
    """
    A model for storing mobile phone details.
    """
    __tablename__ = 'mobile_phones'

    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    screen_size = db.Column(db.Float, nullable=False)
    battery_capacity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=True)
