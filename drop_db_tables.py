import sqlite3

conn = sqlite3.connect("scraper.db")

c = conn.cursor()

c.execute("DROP TABLE maids")

conn.commit()
c.close()
conn.close()
