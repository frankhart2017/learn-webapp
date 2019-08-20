import mysql.connector

db = mysql.connector.connect(
    user="root",
    passwd="root",
    host="localhost",
    database="learn"
)

cursor = db.cursor()
