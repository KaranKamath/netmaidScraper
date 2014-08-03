from bs4 import BeautifulSoup
from urllib2 import urlopen
from pprint import pprint

EX_URL = "http://netmaid.com.sg/maids/273159"    #272739

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
            print childDiv.find_next_sibling(True)
        else:
            maidDict[fieldName] = childDiv.find_next_sibling("div").text

    pprint(maidDict);

def main():
    soup = makeSoup(EX_URL)
    drinkSoup(soup)

if __name__ == "__main__":
    main()
