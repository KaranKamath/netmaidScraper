from bs4 import BeautifulSoup
from urllib2 import urlopen

EX_URL = "http://netmaid.com.sg/maids/272739"

def makeSoup(URL):
    html = urlopen(URL).read()
    soup = BeautifulSoup(html, "lxml")
    return soup;

def drinkSoup(soup):
    maidDetails = soup.find(id="maid_detail")

    for detailDiv in maidDetails.stripped_strings:
        print repr(detailDiv)
    #print maidDetails

def main():
    soup = makeSoup(EX_URL)
    drinkSoup(soup)

if __name__ == "__main__":
    main()
