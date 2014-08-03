#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
from pprint import pprint

EX_URL = "http://netmaid.com.sg/maids/273159"    #272739

def non_empty_td_with_field(tag):
    return tag.name == "td" and unicode(tag.string) != u"  -"

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
        elif "Other Information" in fieldName:
            tableRows = childDiv.find_next_sibling(True).find_all("td")
            for i in range(0, len(tableRows), 2):
                maidDict[tableRows[i].text] = "Yes" if "tick" in tableRows[i+1].img["src"] else "No"
        else:
            maidDict[fieldName] = childDiv.find_next_sibling("div").text

    pprint(maidDict);

def main():
    soup = makeSoup(EX_URL)
    drinkSoup(soup)

if __name__ == "__main__":
    main()
