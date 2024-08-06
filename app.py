from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def save_to_db(data):
    conn = sqlite3.connect('insurance_data.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO submissions (name, age, gender, marital_status, occupation, health_condition, smoking_status, exercise_frequency, email, phone, zipcode, additional_info, total_charge, charge_status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['name'],
        data['age'],
        data['gender'],
        data['marital_status'],
        data['occupation'],
        data['health_condition'],
        data['smoking_status'],
        data['exercise_frequency'],
        data['email'],
        data['phone'],
        data['zipcode'],
        data['additional_info'],
        data['total_charge'],
        data['charge_status']
    ))
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/project')
def project():
    return render_template('quote_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract form data
    form_data = {
        'name': request.form.get('name'),
        'age': int(request.form.get('age')),
        'gender': request.form.get('gender'),
        'marital_status': request.form.get('marital_status'),
        'occupation': request.form.get('occupation'),
        'health_condition': request.form.get('health_condition'),
        'smoking_status': request.form.get('smoking_status'),
        'exercise_frequency': request.form.get('exercise_frequency'),
        'email': request.form.get('email'),
        'phone': request.form.get('phone'),
        'zipcode': request.form.get('zipcode'),
        'additional_info': request.form.get('additional_info'),
    }

    # Simple logic for determining insurance charges
    base_rate = 100
    age_factor = 0.1 * (form_data['age'] - 25)
    health_factor = 50 if form_data['health_condition'] != 'none' else 0
    smoking_factor = 100 if form_data['smoking_status'] == 'smoker' else 0
    exercise_factor = -20 if form_data['exercise_frequency'] == 'daily' else 0
    
    total_charge = base_rate + age_factor + health_factor + smoking_factor + exercise_factor
    charge_status = 'low' if total_charge < 200 else 'high'
    
    # Update form_data with calculated values
    form_data.update({'total_charge': total_charge, 'charge_status': charge_status})
    
    # Save data to database
    save_to_db(form_data)
    
    # Pass all form data and result to the confirmation page
    return render_template('confirmation.html', **form_data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/view_submissions')
def view_submissions():
    conn = sqlite3.connect('insurance_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, age, gender, marital_status, occupation, health_condition, smoking_status, exercise_frequency, email, phone, zipcode, additional_info, total_charge, charge_status FROM submissions')
    submissions = cursor.fetchall()
    conn.close()
    return render_template('view_submissions.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
