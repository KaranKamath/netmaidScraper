#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
from pprint import pprint

EX_URL = "http://netmaid.com.sg/maids/273159"    #272739

def non_empty_td_with_field(tag):
    return tag.name == "td" and unicode(tag.string) != u"  -"

def not_a_title_class(tag):
    return tag.name == 'div' and tag.get('class') == None

def makeSoup(URL):
    html = urlopen(URL).read()
    soup = BeautifulSoup(html, "lxml")
    return soup;

def drinkSoup(soup):
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
            maidDict["Working Experience"] = workExVal[:-1]
        else:
            maidDict[fieldName] = childDiv.find_next_sibling("div").text

    pprint(maidDict);

def main():
    soup = makeSoup(EX_URL)
    drinkSoup(soup)

if __name__ == "__main__":
    main()
