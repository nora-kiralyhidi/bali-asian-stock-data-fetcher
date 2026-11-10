import sqlite3
from datetime import date

DB_NAME = 'bali_data.db'

def init_database():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reports
                 (id INTEGER PRIMARY KEY, report_date TEXT, sector TEXT, company TEXT, ticker TEXT, price REAL, change_pct REAL, UNIQUE (report_date, ticker))''')
    conn.commit()
    conn.close()

def save_report(sector, company, ticker, price, change_pct):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO reports (report_date, sector, company, ticker, price, change_pct) VALUES (?, ?, ?, ?, ?, ?)", (date.today().isoformat(), sector, company, ticker, price, change_pct))
    conn.commit()
    conn.close()