import csv
import sqlite3
from datetime import datetime

conn = sqlite3.connect('scraper.db')

c = conn.cursor()

c.execute('''SELECT * FROM maids''')

row = c.fetchone()

strdate = datetime.now().strftime("%d %B, %X")

with open('output-'+ strdate + '.csv', 'wb') as f:
    csv_out = csv.writer(f, dialect='excel')
    header_list = [
            "urlID",
            "Reference Code",
            "Name",
            "Type",
            "Base Salary",
            "Rest Day Preference",
            "Maid Agency",
            "Nationality",
            "Date of Birth",
            "Place of Birth",
            "Siblings",
            "Height",
            "Weight",
            "Religion",
            "Marital Status",
            "Children",
            "Education",
            "Language Skill",
            "Cares For Children",
            "Cares For Elderly",
            "Cares For Disabled",
            "Prefers Housework",
            "Prefers Cooking",
            "Can Handle Pork",
            "Can Eat Pork",
            "Can Handle Beef",
            "Cares for Dogs or Cats",
            "Does Gardening",
            "Does Sewing",
            "Washes Car",
            "Works Off Days For Compensation",
            "Working Experience",
            "Maid Introduction",
            "Image Path",
            "Init Date",
            "As Of Date",
            "Expiry Date"
            ]
    csv_out.writerow(header_list)
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
