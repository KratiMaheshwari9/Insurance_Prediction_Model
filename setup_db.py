import sqlite3
import os

# Remove the database file if it exists (for testing purposes)
if os.path.exists('insurance_data.db'):
    os.remove('insurance_data.db')

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('insurance_data.db')
cursor = conn.cursor()

# Create a table to store the form data
cursor.execute('''
CREATE TABLE IF NOT EXISTS submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    marital_status TEXT,
    occupation TEXT,
    health_condition TEXT,
    smoking_status TEXT,
    exercise_frequency TEXT,
    email TEXT,
    phone TEXT,
    zipcode TEXT,
    additional_info TEXT,
    total_charge REAL,
    charge_status TEXT
)
''')

conn.commit()
conn.close()

print("Database setup complete.")
