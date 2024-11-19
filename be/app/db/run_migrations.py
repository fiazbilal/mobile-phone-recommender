import psycopg2
from psycopg2 import sql
import os

def get_applied_migrations(cursor):
    # Query the migrations table to get the list of applied migrations
    cursor.execute("SELECT migration_name FROM migrations;")
    applied_migrations = cursor.fetchall()
    return {migration[0] for migration in applied_migrations}

def run_migrations():
    # Database connection details
    db_host = os.getenv("DB_HOST", "localhost")
    db_user = os.getenv("DB_USER", "postgres")
    db_password = os.getenv("DB_PASSWORD", "password")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "mobile_phone_recommender")

    try:
        # Connect to the database (already created)
        connection = psycopg2.connect(
            dbname=db_name,  # Connect to your application database
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        connection.autocommit = True

        cursor = connection.cursor()

        # Ensure migrations table exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS migrations (
                id SERIAL PRIMARY KEY,
                migration_name VARCHAR(255) NOT NULL UNIQUE,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        connection.commit()

        # Get the list of applied migrations
        applied_migrations = get_applied_migrations(cursor)

        # Loop through all migration files in the 'migrations' folder
        migration_files = sorted([f for f in os.listdir('./app/db/migrations') if f.endswith('.sql')])

        for migration_file in migration_files:
            # Check if the migration has already been applied
            if migration_file not in applied_migrations:
                # Open and execute the migration SQL file
                with open(f'./app/db/migrations/{migration_file}', 'r') as file:
                    migration_sql = file.read()
                    try:
                        cursor.execute(migration_sql)
                        print(f"Applied migration: {migration_file}")

                        # Insert record into the migrations table
                        cursor.execute(
                            sql.SQL("INSERT INTO migrations (migration_name) VALUES (%s)"),
                            [migration_file]
                        )
                        connection.commit()

                    except psycopg2.errors.DuplicateTable as e:
                        # Skip the migration if the table already exists
                        print(f"Skipping migration {migration_file}: Table already exists.")
                    except psycopg2.errors.DuplicateColumn as e:
                        # Skip the migration if the column already exists
                        print(f"Skipping migration {migration_file}: Column already exists.")
                    except psycopg2.Error as e:
                        print(f"Error applying migration {migration_file}: {e}")
                        connection.rollback()

        cursor.close()
        connection.close()

    except psycopg2.Error as e:
        print(f"Error running migrations: {e}")
        if connection:
            connection.close()

if __name__ == "__main__":
    run_migrations()
