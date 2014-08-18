#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen, URLError
from urllib import urlretrieve
from pprint import pprint
from db_utils import *
import datetime
import os
import sys
import time
import random

log_name = ""

KEY_LIST = [u'Able to do gardening work?',
            u'Cooking',
            u'Religion',
            u'General Housework',
            u'Language Skill',
            u'Siblings',
            u'Type',
            u'Willing to wash car?',
            u'Care for Infant/Children',
            u'Working Experience',
            u'Date of Birth',
            u'Able to handle pork?',
            u'Care for Elderly',
            u'Able to handle beef?',
            u'Able to do simple sewing?',
            u'Nationality',
            u'Base Salary',
            u'Willing to work on off days with compensation?',
            u'Care for Disabled',
            u'Maid Name',
            u'Able to care dog/cat?',
            u'Ref. Code',
            u'Rest Day Preference',
            u'ID',
            u'Weight',
            u'Image Path',
            u'Height',
            u'Marital Status',
            u'Place of Birth',
            u'Maid Agency',
            u'Able to eat pork?',
            u'Education',
            u'Children',
            u'As Of']

BASE_URL = "http://netmaid.com.sg/maids/"

def non_empty_td_with_field(tag):
    return tag.name == "td" and (u"  " not in unicode(tag.string))

def not_a_title_class(tag):
    return tag.name == 'div' and tag.get('class') == None

def div_preceding_intro(tag):
    return tag.name == 'div' and tag.string == u'Maid Introduction'

def makeSoup(URL_ID):
    URL = BASE_URL + URL_ID
    try:
        openUrl = urlopen(URL)

        log(URL, openUrl.getcode())

        html = openUrl.read()
        soup = BeautifulSoup(html, "lxml")
        return soup;
    except URLError, e:
        log_error(e)

        try:
            if e.code == 404:
                return None
        except:
            print "Something went wrong"
            print e
            print sys.exc_info()[0]
            print "Check Internet Settings"
            sys.exit()

def log_error(e, URL):
    with open("./logs/errors.txt", "a") as errorFile:
        errorFile.write(str(datetime.datetime.now()) + "\t" + str(URL) + "\n" + str(e) + "\n")

def log(url, code):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    with open(("./logs/" + log_name), "a") as logFile:
        logFile.write(str(datetime.datetime.now()) + "\t" + str(code) + "\t" + url + "\n")

def drinkSoup(soup, maidId):
    maidDetails = soup.find(id="maid_detail")

    maidDict = {}

    for childDiv in maidDetails.find_all("div", "title"):
        fieldName = childDiv.text.replace("&"," &")

        if "& Experience" in fieldName:
            tableRows = childDiv.find_next_sibling(True).find_all(non_empty_td_with_field)
            for i in range(0, len(tableRows), 2):
                maidDict[tableRows[i].text] = tableRows[i+1].img["src"][-5]
        elif "Height/Weight" in fieldName:
            rawValue = childDiv.find_next_sibling(True).text
            height = rawValue[:rawValue.index('/')]
            weight = rawValue[rawValue.index('/') + 1:]
            maidDict[u'Height'] = height.strip()
            maidDict[u'Weight'] = weight.strip()
        elif "Language Skill" in fieldName:
            languageDivs = childDiv.find_parent().find_all(not_a_title_class)
            langVal = ""
            for i in range(0, len(languageDivs)):
                langVal += languageDivs[i].text + ","
            maidDict[fieldName] = langVal[:-1]
        elif "Other Information" in fieldName:
            tableRows = childDiv.find_next_sibling(True).find_all("td")
            for i in range(0, len(tableRows), 2):
                maidDict[tableRows[i].text] = "Yes" if "tick" in tableRows[i+1].img["src"] else "No"
        elif "Working Experience" in fieldName:
            tableRows = childDiv.find_next_sibling(True).find_all("td")
            workExVal = ""
            for i in range(0, len(tableRows), 2):
               workExVal += tableRows[i].text + '-' + tableRows[i+1].text + ','
            maidDict[fieldName] = workExVal[:-1]
        else:
            maidDict[fieldName] = childDiv.find_next_sibling("div").text

    maidDict[u"As Of"] = str(datetime.datetime.now())
    maidDict[u"ID"] = maidId
    maidDict[u"Image Path"] = extractImage(maidDetails, maidId)
    maidDict[u"Maid Introduction"] = getMaidIntroduction(soup)

    #pprint(maidDict)
    return maidDict

def getMaidIntroduction(soup):
    previousDiv = soup.find(div_preceding_intro)
    introductionString = ""

    introDiv = previousDiv.find_next_sibling('div')

    for text in introDiv.stripped_strings:
        introductionString += '\n' + text

    introductionString = introductionString.strip()

    return unicode(introductionString)

def extractImage(maidDetails, imageName):
    directory = "photos"
    if not os.path.exists(directory):
        os.makedirs(directory)
    localPath = "./" + directory + "/" + imageName + ".jpg"
    urlretrieve(maidDetails.div.img["src"], localPath)
    return localPath

def orderSoup(maidId):
    soup = makeSoup(str(maidId))

    if soup != None:
        maidDetails = drinkSoup(soup, str(maidId))
        for keyName in KEY_LIST:
            if keyName not in maidDetails.keys():
                maidDetails[keyName] = None
        #pprint(maidDetails.keys())
        addToMaidsDb(maidDetails)
    else:
        expireInMaidsDb(str(maidId))

def main():
    #maidId = 221550
    #maidId = 273161
    maidId = 273159
    global log_name
    log_name = "logfile - " + datetime.datetime.now().strftime("%d %B, %X") + ".txt"

    #orderSoup(maidId)
    while True:
        try:
            print maidId, "\n"
            orderSoup(maidId)
            time.sleep(4 + random.uniform(-3, 3))
            maidId = maidId + 1
        except:
            log_error(sys.exc_info()[0], maidId)
            maidId = maidId + 1
            time.sleep(3 + random.uniform(-2, 2))

if __name__ == "__main__":
    main()
