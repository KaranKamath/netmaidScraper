import sqlite3

conn = sqlite3.connect('scraper.db')

c = conn.cursor()

c.execute('''SELECT urlId FROM maids''')

print c.fetchall()

conn.commit()

conn.close()
