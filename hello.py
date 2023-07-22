from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import sqlite3
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from pdf_generate_script import generate_pdf_file_venue, generate_pdf_file_show
import traceback
import uuid
from datetime import datetime

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

@app.route('/api/auth/login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    print(data)
    print(data['email'])
    print(data['password'])

    try:
        conn = connect_db()
        cursor = conn.execute(
            "SELECT * FROM userDetails WHERE email = '{}' AND password = '{}'".format(data['email'], data['password']))
        rows = cursor.fetchall()
        if len(rows) == 1:
            access_token = create_access_token(identity=data['email'])

            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            conn.execute("UPDATE userDetails SET loginTime = '{}' WHERE email = '{}'".format(current_time, data['email']))
            conn.commit()
            return jsonify({
                "message": "success",
                "access_token": access_token,
                "email": data['email']
            })
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

@app.route('/api/getvenuecapacity', methods=['GET','POST'])
def getVenueCapacity():
    data = request.get_json()
    print(data)

    try:
        conn = connect_db()
        cursor = conn.execute("SELECT capacity FROM venueDetails WHERE venueName = '{}'".format(data))
        capacity = cursor.fetchall()
        print(capacity)
        return jsonify({"capacity": capacity[0][0]})
    except:
        return jsonify({"message": "error"})

@app.route('/api/createshow', methods=['GET','POST'])
def createShow():
    data = request.get_json()
    print(data)

    try:
        conn = connect_db()
        conn.execute("INSERT INTO showDetails (showName, rating, time, tags, price, venueName, showCapacity) VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}')".format(data['name'], data['rating'], data['time'], data['tags'], data['price'], data['venuename'], data['showcapacity']))
        conn.commit()
        return jsonify({"message": "success"})
    except:
        return jsonify({"message": "error"})

@app.route('/api/editShowDetails', methods=['GET','POST'])
def editShowDetails():
    data = request.get_json()
    print(data)
    try:
        conn = connect_db()
        query = "UPDATE showDetails SET rating = ?, time = ?, tags = ?, price = ?, venueName = ? WHERE showName = ?"
        parameters = (data['rating'], data['time'], data['tags'], data['price'], data['venuename'], data['showname'])
        print(parameters)
        conn.execute(query, parameters)
        conn.commit()
        return jsonify({"message": "success"})
    except:
        return jsonify({"message": "error"})

@app.route('/api/deleteShow', methods=['GET','POST'])
def deleteShow():
    data = request.get_json()
    try:
        conn = connect_db()
        conn.execute("DELETE FROM showDetails WHERE showName = ? AND time = ?", (data['showname'],data['time']))
        conn.commit()
        return jsonify({"message": "success"})
    except:
        return jsonify({"message": "error"})

@app.route('/api/showDetails', methods=['GET','POST'])
def showDetails():
    data = request.get_json()
    print(data)
    print(data['showname'])
    showName = data['showname']
    try:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM showDetails WHERE showName = ?", (showName,))
        rows = cursor.fetchall()
        print(rows)
        return jsonify({"showDetails": rows})
    except:
        return jsonify({"message": "error"})

@app.route('/api/bookticket', methods=['GET', 'POST'])
def bookTicket():
    data = request.get_json()
    print(data)

    try:
        conn = connect_db()
        cursor = conn.execute("SELECT time, showCapacity FROM showDetails WHERE showName = ?", (data['showName'],))
        showTiming = cursor.fetchall()
        print(showTiming[0][0])
        showtiming = showTiming[0][0]
        showCapacity = showTiming[0][1]
        if(int(data['numberOfSeats']) > int(showCapacity)):
            return jsonify({"message": "error", "error_details": "Number of seats requested is more than the show capacity"})
        conn.execute("INSERT INTO userBookingDetails (username, showName, venueName, numberOfTickets, totalPrice, showTiming) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(data['username'], data['showName'], data['venueName'], int(data['numberOfSeats']), int(data['totalPrice']), showtiming))
        conn.commit()
        conn.execute("UPDATE showDetails SET showCapacity = showCapacity - ? WHERE showName = ?", (data['numberOfSeats'], data['showName']))
        conn.commit()
        return jsonify({"message": "success"})
    except Exception as e:
        print("Error occurred:", str(e))
        traceback.print_exc()  # This will print the traceback for detailed error information.
        return jsonify({"message": "error", "error_details": str(e)})

@app.route('/api/getUserBookingDetails', methods=['GET', 'POST'])
def getUserBookingDetails():
    data = request.get_json()
    # print(data)

    try:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM userBookingDetails WHERE username = ?", (data['username'],))
        rows = cursor.fetchall()
        print(rows)
        return jsonify({"userBookingDetails": rows})
    except:
        return jsonify({"message": "error"})

@app.route('/api/exportVenuePDF', methods=['POST'])
def exportVenuePDF():
    data = request.get_json()

    try:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM venueDetails")
        rows = cursor.fetchall()

        # Generate a unique filename for the PDF using UUID
        pdf_file = str(uuid.uuid4()) + '.pdf'

        generate_pdf_file_venue(rows, pdf_file)

        return jsonify({"pdf_file": pdf_file})
    except:
        return jsonify({"message": "error"})

@app.route('/api/exportShowPDF', methods=['POST'])
def exportShowPDF():
    data = request.get_json()

    try:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM showDetails")
        rows = cursor.fetchall()
        print(rows)

        # Generate a unique filename for the PDF using UUID
        pdf_file = str(uuid.uuid4()) + '.pdf'

        generate_pdf_file_show(rows, pdf_file)

        return jsonify({"pdf_file": pdf_file})
    except:
        return jsonify({"message": "error"})

@app.route('/api/downloadVenuePDF/<pdf_file>', methods=['GET'])
def downloadVenuePDF(pdf_file):
    try:
        return send_file(pdf_file, as_attachment='venue_details.pdf', download_name='venue_details.pdf')
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": str(e)})

@app.route('/api/downloadShowPDF/<pdf_file>', methods=['GET'])
def downloadShowPDF(pdf_file):
    try:
        return send_file(pdf_file, as_attachment='show_details.pdf', download_name='show_details.pdf')
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": str(e)})
    
@app.route('/api/show-search', methods=['GET', 'POST'])
def showSearch():
    data = request.get_json()
    print(data)
    print(data['showName'])

    try:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM showDetails WHERE showName LIKE ?", ('%' + data['showName'] + '%',))
        rows = cursor.fetchall()
        print(rows)
        return jsonify({"showDetails": rows})
    except:
        return jsonify({"message": "error"})


@app.route('/api/deleteUserBooking', methods=['GET', 'POST'])

def deleteUserBooking():
    data = request.get_json()
    
    print(data)
    

    try:
        conn = connect_db()
        conn.execute("DELETE FROM userBookingDetails WHERE username = ? AND showName = ? AND numberOfTickets = ?", (data['username'], data['showname'], data['numberOfTickets']))
        conn.commit()
        conn.execute("UPDATE showDetails SET showCapacity = showCapacity + ? WHERE showName = ?", (data['numberOfTickets'], data['showname']))
        conn.commit()
        return jsonify({"message": "success"})
    except:
        return jsonify({"message": "error"})

