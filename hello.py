from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sqlite3


DEBUG = True

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def connect_db():
    try:
        conn = sqlite3.connect('database.db', timeout=10)
        print("Database connection established successfully")
        return conn
    except sqlite3.Error as e:
        print("Database connection error:", e)
        return None


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test', methods=['GET','POST'])
def register():
    data = request.get_json()
    print(data)
    print(data['email'])
    print(data['password'])
    conn = connect_db()
    conn.execute("INSERT INTO userDetails (email, password) VALUES ('{}', '{}')".format(data['email'], data['password']))
    conn.commit()
    print("Data inserted successfully")
    return 'hello'