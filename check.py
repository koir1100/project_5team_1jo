import sqlite3

conn = sqlite3.connect("./books.db")
cur = conn.cursor()

cur.execute("SELECT * FROM books")
print(cur.fetchall())

cur.close()
conn.close()