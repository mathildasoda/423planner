import re
from re import search as search
from urllib.request import urlopen as uopen
from urllib import parse, error
from bs4 import BeautifulSoup as soup
import pandas as pd

link = "http://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/datascience/#degreerequirementstext"

uclient = uopen(link)
read_html = uclient.read()
uclient.close()

#debug space 
print("""
__________________


i dont wana blind

__________________
""")

ssoup = soup(read_html, "html.parser")

table = ssoup.find("table", {"class":"sc_courselist"})

def cleanScrape(bla):
    bla = str(bla.text)
    todelete = re.findall("<.*?>",bla)
    for c in todelete:
        bla.remove(c,"")
        print(bla)
    return bla

def infoSlot(code,name,hours):
    infoSlot = [code, name, hours]
    return infoSlot


## headers in list --> headers
headers_soup = table.find_all("span", class_="courselistcomment areaheader")
headers = []
for i in headers_soup:
    i = cleanScrape(i)
    if i!="":
        headers.append(i)
# print(headers)


slots = []
code_soup = table.find_all("a", class_="bubblelink code")
codes = []
for c in code_soup:
    n = c.findParent(class_="codecol").findNextSibling("td")
    h = n.findNextSibling(class_="hourscol")       
    c = cleanScrape(c)
    n = cleanScrape(n)
    if h!="" and h!=None:
        h = cleanScrape(h)
    if h==None or h=="":
        h = "N/A"
    if c!="":
        c = c.replace(u"\xa0",u" ")
    # debug print cnh
    print(f"{c}: {n} - {h}")
    
    newSlot = infoSlot(c,n,h)
    slots.append(newSlot)

# print("nubers of classes here:", len(codes))
# print(codes)
# print(slots)


