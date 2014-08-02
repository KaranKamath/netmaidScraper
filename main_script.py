from bs4 import BeautifulSoup
from urllib2 import urlopen
from pprint import pprint

EX_URL = "http://netmaid.com.sg/maids/272739"

def makeSoup(URL):
    html = urlopen(URL).read()
    soup = BeautifulSoup(html, "lxml")
    return soup;

def drinkSoup(soup):
    maidDetails = soup.find(id="maid_detail")

    maidDict = {}

    for childDiv in maidDetails.find_all("div", "title"):
        maidDict[childDiv.string] = "somevalue"

    pprint(maidDict.keys());

def main():
    soup = makeSoup(EX_URL)
    drinkSoup(soup)

if __name__ == "__main__":
    main()
