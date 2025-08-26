from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return "Yaahoo! Ahmed have Done it!!!! Flask App is running with MySQL and Nginx!"

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    name = data.get("name")
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="rootpassword",
        database="testdb"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User added!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
