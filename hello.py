from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sqlite3
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


DEBUG = True

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'abcdefgh'  # Change this to a secure secret key
jwt = JWTManager(app)
CORS(app)

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

@app.route('/api/auth/register', methods=['GET','POST'])
def register():
    data = request.get_json()
    print(data)
    print(data['email'])
    print(data['password'])
    try:
        conn = connect_db()
        conn.execute("INSERT INTO userDetails (email, password) VALUES ('{}', '{}')".format(data['email'], data['password']))
        conn.commit()
        return jsonify({"message": "success"})
    except:
        return jsonify({"message": "error"})

@app.route('/api/auth/admin-login', methods=['GET','POST'])
def adminlogin():
    data = request.get_json()
    print(data)
    print(data['email'])
    print(data['password'])
    try:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM adminDetails WHERE email = '{}' AND password = '{}'".format(data['email'], data['password']))
        rows = cursor.fetchall()
        if(len(rows) == 1):
            access_token = create_access_token(identity=data['email'])
            return jsonify({"message": "success",
                            "access_token": access_token})
        else:
            return jsonify({"message": "error"})
    except:
        return jsonify({"message": "error"})

@app.route('/api/auth/login', methods=['GET','POST'])
def login():
    data = request.get_json()
    print(data)
    print(data['email'])
    print(data['password'])
    try:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM userDetails WHERE email = '{}' AND password = '{}'".format(data['email'], data['password']))
        rows = cursor.fetchall()
        if(len(rows) == 1):
            access_token = create_access_token(identity=data['email'])
            return jsonify({"message": "success",
                            "access_token": access_token})
        else:
            return jsonify({"message": "error"})
    except:
        return jsonify({"message": "error"})

@app.route('/api/all-details', methods=['GET','POST'])
def venueAndShowDetails():
    try:
        conn = connect_db()
        cursor = conn.execute('SELECT * FROM venueDetails')
        rows1 = cursor.fetchall()
        print(rows1)
        cursor = conn.execute('SELECT * FROM showDetails')
        rows2 = cursor.fetchall()
        print(rows2)
        cursor = conn.execute("SELECT venueName FROM venueDetails")
        venueNames = cursor.fetchall()
        result_VenueAndShow = {}
        for venue in venueNames:
            print(venue[0])
            venue_name = venue[0]
            cursor = conn.execute("SELECT * FROM showDetails WHERE venueName = ?", (venue_name,))
            showName = cursor.fetchall()
            if(result_VenueAndShow.get(venue_name) == None):
                result_VenueAndShow[venue_name] = []
            for row in showName:
                result_VenueAndShow[venue_name].append(row)

        return jsonify({"venueList": rows1,
                        "showList": rows2,
                        "venueAndShow": result_VenueAndShow})
    except:
        return jsonify({'message': 'There was an error'})

@app.route('/api/createVenue', methods=['GET','POST'])
def createVenue():
    data = request.get_json()
    print(data)
    print(data['name'])
    print(data['place'])
    print(data['location'])
    print(data['capacity'])

    try:
        conn = connect_db()
        conn.execute("INSERT INTO venueDetails (venueName, place, location, capacity) VALUES ('{}', '{}', '{}', '{}')".format(data['name'], data['place'], data['location'], data['capacity']))
        conn.commit()
        return jsonify({"message": "success"})
    except:
        return jsonify({"message": "error"})

@app.route('/api/createshow', methods=['GET','POST'])
def createShow():
    data = request.get_json()
    print(data)

    try:
        conn = connect_db()
        conn.execute("INSERT INTO showDetails (showName, rating, time, tags, price, venueName) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(data['name'], data['rating'], data['time'], data['tags'], data['price'], data['venuename']))
        conn.commit()
        return jsonify({"message": "success"})
    except:
        return jsonify({"message": "error"})

# @app.route('/api/auth/protected', methods=['GET','POST'])
# @jwt_required
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify({"message": "success",
#                     "current_user": current_user})
    