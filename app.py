from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'HONEY18@vaani25'  # replace with your MySQL root password
app.config['MYSQL_DB'] = 'hospital_db'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Add Patient
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        contact = request.form['contact']
        address = request.form['address']
        disease = request.form['disease']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO patients (name, age, gender, contact, address, disease) VALUES (%s, %s, %s, %s, %s, %s)",
            (name, age, gender, contact, address, disease)
        )
        mysql.connection.commit()
        cur.close()
        return redirect('/view_patients')
    return render_template('add_patient.html')

# View Patients
@app.route('/view_patients')
def view_patients():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patients")
    data = cur.fetchall()
    cur.close()
    return render_template('view_patients.html', patients=data)

# Edit Patient
@app.route('/edit_patient/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        contact = request.form['contact']
        address = request.form['address']
        disease = request.form['disease']

        cur.execute(
            """UPDATE patients SET name=%s, age=%s, gender=%s, contact=%s, 
               address=%s, disease=%s WHERE id=%s""",
            (name, age, gender, contact, address, disease, id)
        )
        mysql.connection.commit()
        cur.close()
        return redirect('/view_patients')

    cur.execute("SELECT * FROM patients WHERE id=%s", (id,))
    patient = cur.fetchone()
    cur.close()
    return render_template('edit_patient.html', patient=patient)

# Delete Patient
@app.route('/delete_patient/<int:id>', methods=['POST'])
def delete_patient(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM patients WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect('/view_patients')

if __name__ == '__main__':
    app.run(debug=True)
