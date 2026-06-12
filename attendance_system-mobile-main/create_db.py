import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mvkarthikeya@07"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS attendance_system")

print("Database created successfully!")

conn.close()