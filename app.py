from flask import Flask, render_template, request, redirect, url_for  
import sqlite3  

app = Flask(__name__)  

# Connect to SQLite database  
def init_db():  
    conn = sqlite3.connect('database.db')  
    c = conn.cursor()  
    c.execute('''CREATE TABLE IF NOT EXISTS registration  
                 (full_name TEXT, id_number TEXT, nationality TEXT, region TEXT,   
                  zone TEXT, phone_number TEXT, sex TEXT, class_year TEXT,  
                  program TEXT, semester TEXT, academic_type TEXT)''')  
    conn.commit()  
    conn.close()  

init_db()  

@app.route('/')  
def home():  
    return render_template('register.html')  

@app.route('/register', methods=['POST'])  
def register():  
    if request.method == 'POST':  
        full_name = request.form['full_name']  
        id_number = request.form['id_number']  
        nationality = request.form['nationality']  
        region = request.form['region']  
        zone = request.form['zone']  
        phone_number = request.form['phone_number']  
        sex = request.form.get('sex')  
        class_year = request.form.getlist('class_year')  
        program = request.form.getlist('program')  
        semester = request.form.getlist('semester')  
        academic_type = request.form.getlist('academic_type')  

        # Database insertion  
        conn = sqlite3.connect('database.db')  
        c = conn.cursor()  
        c.execute("INSERT INTO registration (full_name, id_number, nationality, region, zone, phone_number, sex, class_year, program, semester, academic_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",  
                  (full_name, id_number, nationality, region, zone, phone_number, sex, ', '.join(class_year), ', '.join(program), ', '.join(semester), ', '.join(academic_type)))  
        conn.commit()  
        conn.close()  
        
        return redirect(url_for('home'))  

if __name__ == "__main__":  
    app.run(debug=True)