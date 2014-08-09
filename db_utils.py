import sqlite3

def addToMaidsDb(maidDetails):
    conn = sqlite3.connect('scraper.db')
    c = conn.cursor()

    c.close()
    conn.commit()
    conn.close()

def expireInMaidsDb(maidId):
    print "Expiring"
