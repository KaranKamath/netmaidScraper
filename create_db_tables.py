import sqlite3

conn = sqlite3.connect('scraper.db')

c = conn.cursor()

c.execute('''CREATE TABLE maids(
                urlID INTEGER PRIMARY KEY,
                ref_code TEXT,
                type TEXT,
                base_salary TEXT,
                rest_day_preference TEXT,
                maid_agency TEXT,
                nationality TEXT,
                date_of_birth TEXT,
                place_of_birth TEXT,
                siblings TEXT,
                height TEXT,
                weight TEXT,
                religion TEXT,
                marital_status TEXT,
                children TEXT,
                education TEXT,
                language_skill TEXT,
                pref_cares_for_children TEXT,
                pref_cares_for_elderly TEXT,
                pref_cares_for_disabled TEXT,
                pref_housework TEXT,
                pref_cooking TEXT,
                other_handles_pork TEXT,
                other_eats_pork TEXT,
                other_handles_beef TEXT,
                other_cares_for_dog_or_cat TEXT,
                other_gardening TEXT,
                other_sewing TEXT,
                other_washes_car TEXT,
                other_works_off_days_for_compensation TEXT,
                working_experience TEXT,
                img_path TEXT)''')
