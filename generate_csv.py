import csv
import sqlite3

conn = sqlite3.connect('scraper.db')

c = conn.cursor()

c.execute('''SELECT * FROM maids''')

row = c.fetchone()

with open('output.csv', 'wb') as f:
    csv_out = csv.writer(f, dialect='excel')

    while row:
        formatted_row = []
        for r in row:
            if isinstance(r, basestring):
                formatted_row.append(r.encode('utf-8'))
            else:
                formatted_row.append(r)

        csv_out.writerow(formatted_row)
        row = c.fetchone()

conn.commit()
conn.close()
