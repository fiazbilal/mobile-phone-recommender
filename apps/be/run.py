from app import create_app
from app.extensions.db import db
from app.models.mobile_phone import MobilePhone

app = create_app()

def init_db():
    """
    Initialize the database and create the tables.
    """
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")

        # Add a sample mobile phone
        sample_phone = MobilePhone(
            brand="Samsung",
            model="Galaxy S21",
            screen_size=6.2,
            battery_capacity=4000,
            price=799.99
        )
        db.session.add(sample_phone)
        db.session.commit()
        print("Sample mobile phone added to the database.")

if __name__ == "__main__":
    init_db()
