import sqlite3

conn = sqlite3.connect('trends.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS trends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    platform TEXT,
    keyword TEXT,
    timestamp DATETIME
)
''')
conn.commit()
conn.close() 