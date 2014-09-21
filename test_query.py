import sqlite3
from db_utils import *

conn = sqlite3.connect('scraper.db')

c = conn.cursor()

c.execute('''SELECT COUNT(urlId) FROM maids''')

print c.fetchall()

c.execute('''SELECT COUNT(urlId) FROM maids WHERE expired_date IS NOT NULL''')

print c.fetchall()

conn.commit()

conn.close()

print getLastUrlId()
