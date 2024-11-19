import psycopg2
from psycopg2 import sql
import os

def create_database():
    # Database connection details
    db_host = os.getenv("DB_HOST", "localhost")  # Default to localhost
    db_user = os.getenv("DB_USER", "postgres")  # Default to postgres user
    db_password = os.getenv("DB_PASSWORD", "password")  # Replace with your password
    db_port = os.getenv("DB_PORT", "5432")  # Default PostgreSQL port
    db_name = os.getenv("DB_NAME", "mobile_phone_recommender")

    try:
        # Connect to PostgreSQL server
        connection = psycopg2.connect(
            dbname="postgres",  # Connect to the default 'postgres' database
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        connection.autocommit = True

        # Create a cursor object
        cursor = connection.cursor()

        # Check if the database already exists
        cursor.execute(
            sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"),
            [db_name],
        )
        exists = cursor.fetchone()

        if not exists:
            # Create the database if it doesn't exist
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
            print(f"Database '{db_name}' created successfully!")
        else:
            print(f"Database '{db_name}' already exists.")

        cursor.close()
        connection.close()

    except psycopg2.Error as e:
        print(f"Error creating database: {e}")
        if connection:
            connection.close()


if __name__ == "__main__":
    create_database()
