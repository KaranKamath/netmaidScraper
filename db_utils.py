import sqlite3
import datetime

def addToMaidsDb(maidDetails):
    conn = sqlite3.connect('scraper.db')
    c = conn.cursor()

    try:
        c.execute('''INSERT INTO maids(
                        urlID,
                        ref_code,
                        type,
                        base_salary,
                        rest_day_preference,
                        maid_agency,
                        nationality,
                        date_of_birth,
                        place_of_birth,
                        siblings,
                        height,
                        weight,
                        religion,
                        marital_status,
                        children,
                        education,
                        language_skill,
                        pref_cares_for_children,
                        pref_cares_for_elderly,
                        pref_cares_for_disabled,
                        pref_housework,
                        pref_cooking,
                        other_handles_pork,
                        other_eats_pork,
                        other_handles_beef,
                        other_cares_for_dog_or_cat,
                        other_gardening,
                        other_sewing,
                        other_washes_car,
                        other_works_off_days_for_compensation,
                        working_experience,
                        maid_introduction,
                        img_path,
                        init_date,
                        as_of_date,
                        expired_date)
                        values(
                        ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                        ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''',
                        (maidDetails[u'ID'],
                            maidDetails[u'Ref. Code'],
                            maidDetails[u'Type'],
                            maidDetails[u'Base Salary'],
                            maidDetails[u'Rest Day Preference'],
                            maidDetails[u'Maid Agency'],
                            maidDetails[u'Nationality'],
                            maidDetails[u'Date of Birth'],
                            maidDetails[u'Place of Birth'],
                            maidDetails[u'Siblings'],
                            maidDetails[u'Height'],
                            maidDetails[u'Weight'],
                            maidDetails[u'Religion'],
                            maidDetails[u'Marital Status'],
                            maidDetails[u'Children'],
                            maidDetails[u'Education'],
                            maidDetails[u'Language Skill'],
                            maidDetails[u'Care for Infant/Children'],
                            maidDetails[u'Care for Elderly'],
                            maidDetails[u'Care for Disabled'],
                            maidDetails[u'General Housework'],
                            maidDetails[u'Cooking'],
                            maidDetails[u'Able to handle pork?'],
                            maidDetails[u'Able to eat pork?'],
                            maidDetails[u'Able to handle beef?'],
                            maidDetails[u'Able to care dog/cat?'],
                            maidDetails[u'Able to do gardening work?'],
                            maidDetails[u'Able to do simple sewing?'],
                            maidDetails[u'Willing to wash car?'],
                            maidDetails[u'Willing to work on off days with compensation?'],
                            maidDetails[u'Working Experience'],
                            maidDetails[u'Maid Introduction'],
                            maidDetails[u'Image Path'],
                            maidDetails[u'As Of'],
                            maidDetails[u'As Of'],
                            None));
    except sqlite3.IntegrityError,e:
       c.execute('''UPDATE maids SET as_of_date=? WHERE urlID=? AND expired_date IS NULL;''', (maidDetails[u'As Of'], maidDetails[u'ID']))
    c.execute("SELECT * FROM maids WHERE urlID=?", (maidDetails[u'ID'],))
    print c.fetchall()
    c.close()
    conn.commit()
    conn.close()

def expireInMaidsDb(maidId):
    print "Expiring"

    conn = sqlite3.connect('scraper.db')
    c = conn.cursor()

    c.execute('''UPDATE maids SET expired_date=? WHERE urlID=?;''', (str(datetime.datetime.now()), maidId))
    c.execute('''SELECT * FROM maids WHERE urlID=?''', (maidId,))

    print c.fetchall()

    conn.commit()
    c.close()
    conn.close()
