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

## headers in list --> headers
headers_soup = table.find_all("span", class_="courselistcomment areaheader")
headers = []
for i in headers_soup:
    i = str(i.text)
    s = re.findall("<.*?>",i)
    for n in s:
        i.remove(n,"")
    if i!="":
        headers.append(i)
# print(headers)

## cred hours converted to floats in list --> hours 
hours_soup = table.find_all("td", class_="hourscol")
hours = []
for i in hours_soup:
    i = str(i.text)
    s = re.findall("<.*?>",i)
    for n in s:
        i.remove(n,"")
    if i!="":
        i = float(i)
        hours.append(i)
    else:
        hours.append("N/A")
hours.pop(0)
# print(hours)

code_soup = table.find_all("a", class_="bubblelink code")
codes = []
for i in code_soup:
    i = str(i.text)
    s = re.findall("<.*?>",i)
    for n in s:
        i.remove(n,"")
    if i!="":
        i = i.replace(u"\xa0",u" ")
        codes.append(i)
# print(codes)

# for i in range(len(codes)):
#     print(f"{codes[i]}: {hours[i]}")

