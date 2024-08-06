import sqlite3

def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS insurance_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            driving_experience INTEGER NOT NULL,
            claim_history INTEGER NOT NULL,
            car_make TEXT NOT NULL,
            car_model TEXT NOT NULL,
            car_year INTEGER NOT NULL,
            zipcode TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            additional_info TEXT,
            charges TEXT NOT NULL,
                   charge_status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(name, age, gender, driving_experience, claim_history, car_make, car_model, car_year, zipcode, email, phone, additional_info, charges):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO insurance_data (name, age, gender, driving_experience, claim_history, car_make, car_model, car_year, zipcode, email, phone, additional_info, charges)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, age, gender, driving_experience, claim_history, car_make, car_model, car_year, zipcode, email, phone, additional_info, charges))
    conn.commit()
    conn.close()
