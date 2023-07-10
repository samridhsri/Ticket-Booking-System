# Delete this file after testing

import sqlite3
def connect_db():
    try:
        conn = sqlite3.connect('database.db', timeout=10)
        print("Database connection established successfully")
        return conn
    except sqlite3.Error as e:
        print("Database connection error:", e)
        return None


conn = connect_db()
# venue_name = 'venue_01'
# cursor = conn.execute("SELECT * FROM showDetails WHERE venueName = ?", (venue_name,))
cursor = conn.execute("SELECT venueName FROM venueDetails")
rows1 = cursor.fetchall()
result = {}
for venue in rows1:
    print(venue[0])
    venue_name = venue[0]
    cursor = conn.execute("SELECT * FROM showDetails WHERE venueName = ?", (venue_name,))
    rows = cursor.fetchall()
    if(result.get(venue_name) == None):
        result[venue_name] = []
    for row in rows:
        result[venue_name].append(row)
print(result)
