import sqlite3
conn = sqlite3.connect('bali_data.db')
print(conn.execute("SELECT COUNT(*) FROM reports").fetchone())
conn.close()