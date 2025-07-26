import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="chatdb"
)
cursor = conn.cursor()

users = [("Alice", "alice@example.com"), ("Bob", "bob@example.com")]
cursor.executemany("INSERT INTO chat_user (name, email) VALUES (%s, %s)", users)
conn.commit()
conn.close()
