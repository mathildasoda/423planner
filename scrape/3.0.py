import re
from re import search as search
from urllib.request import urlopen as uopen
from urllib import parse, error
from bs4 import BeautifulSoup as soup
import pandas as pd

ds_url = "http://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/datascience/#degreerequirementstext"

uclient = uopen(ds_url)
ds_html = uclient.read()
uclient.close()

#debug space 
print("""
__________________


i dont wana blind

__________________
""")

ds_soup = soup(ds_html, "html.parser")

table = ds_soup.find("table", {"class":"sc_courselist"})

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

# # debug infoSlot func
# c = "INFO 101"
# n = "Introduction to Computing and Security Technology"
# h = 3.0
# print(f"slot looks like this: {infoSlot(c,n,h)[0]}")
# print(f"display looks like this: {infoSlot(c,n,h)[1]}")



## headers in list --> headers
headers_soup = table.find_all("span", class_="courselistcomment areaheader")
headers = []



code_soup = table.find_all("a", class_="bubblelink code")
codes = []

for i in headers_soup:
    i = cleanScrape(i)
    if i!="":
        headers.append(i)


# print(headers)

## cred hours converted to floats in list --> hours 

# hours_soup = table.find_all("td", class_="hourscol")
# hours = []
# for i in hours_soup:
#     i = str(i.text)
#     s = re.findall("<.*?>",i)
#     for n in s:
#         i.remove(n,"")
#     if i!="":
#         i = float(i)
#         hours.append(i)
#     else:
#         hours.append("N/A")
# hours.pop(0)
# print(hours)

slots = []
class no_hourscol_error(Exception):
    pass
for c in code_soup:
    n = c.findParent(class_="codecol").findNextSibling()
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
    # print(f"{c}: {n} - {h}")
    
    newSlot = infoSlot(c,n,h)
    slots.append(newSlot)

# print("nubers of classes here:", len(codes))
# print(codes)
print(slots)


