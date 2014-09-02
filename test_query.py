import sqlite3

conn = sqlite3.connect('scraper.db')

c = conn.cursor()

c.execute('''SELECT * FROM maids
WHERE place_of_birth LIKE '%ALBAY%' and type='Transfer'
and height like '%158%' ''')

print c.fetchall()

conn.commit()

conn.close()
