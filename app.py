
from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
import mysql.connector
from mysql.connector import Error
import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@#$123Bangtan'
app.config['MYSQL_DB'] = 'portfolio'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/certifications")
def get_certifications():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM certifications")
    rows = cur.fetchall()

    result = []

    for r in rows:
        result.append({
            "id": r[0],
            "name": r[1],
            "platform": r[2],
            "image": r[3]
        })

    return jsonify(result)

@app.route('/api/contact', methods=['POST'])
def save_contact():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        # Validate inputs
        if not name or not email or not message:
            return jsonify({'success': False, 'error': 'All fields are required'})
        
        cur = mysql.connection.cursor()
        query = "INSERT INTO contact_messages (name, email, message) VALUES (%s, %s, %s)"
        values = (name, email, message)
        cur.execute(query, values)
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
        
    except Exception as e:
        print("Error:", e)
        return jsonify({'success': False, 'error': str(e)})
    


from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
import mysql.connector
from mysql.connector import Error
import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = '${{RAILWAY_PRIVATE_DOMAIN}}'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '${{MYSQL_ROOT_PASSWORD}}'
app.config['MYSQL_DB'] = 'railway'
app.config['MYSQLPORT'] = '3306'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/certifications")
def get_certifications():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM certifications")
    rows = cur.fetchall()

    result = []

    for r in rows:
        result.append({
            "id": r[0],
            "name": r[1],
            "platform": r[2],
            "image": r[3]
        })

    return jsonify(result)

@app.route('/api/contact', methods=['POST'])
def save_contact():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        # Validate inputs
        if not name or not email or not message:
            return jsonify({'success': False, 'error': 'All fields are required'})
        
        cur = mysql.connection.cursor()
        query = "INSERT INTO contact_messages (name, email, message) VALUES (%s, %s, %s)"
        values = (name, email, message)
        cur.execute(query, values)
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
        
    except Exception as e:
        print("Error:", e)
        return jsonify({'success': False, 'error': str(e)})
    
import os



