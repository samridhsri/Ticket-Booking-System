from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import sqlite3
import traceback
import json
from hello import connect_db

def send_google_chat_notification(email):
    return "something"


def check_login_status():
    try:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM userDetails")
        rows = cursor.fetchall()

        current_time = datetime.now()
        for row in rows:
            uID, email, password, loginTime = row

            # Convert loginTime to a datetime object
            login_time = datetime.strptime(loginTime, '%Y-%m-%d %H:%M:%S')

            # Calculate the time difference
            time_difference = current_time - login_time

            # If the time difference is greater than 24 hours (86400 seconds), send notification
            if time_difference.total_seconds() > 86400:
                # Call a function to send the notification via Google Chat webhook
                send_google_chat_notification(email)

    except Exception as e:
        traceback.print_exc()


scheduler = BackgroundScheduler()
scheduler.add_job(check_login_status, 'interval', hours=24)  # Run every 24 hours
scheduler.start()