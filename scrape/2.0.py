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
headers = []
codes = []
titles = []
hours = []

## headers in list --> [headers]
header_soup = table.find_all("span", class_="courselistcomment areaheader")
for hed in header_soup:
    hed = str(hed.text)
    s = re.findall("<.*?>",hed)
    for n in s:
        hed.remove(n,"")
    headers.append(hed)

def clean_title(title):
    print(title)

clean_title("MATH 101& MATH 102& MATH 180")


code_soup = table.find_all("td", class_="codecol")
for cod in code_soup:
    cod = str(cod.text)
    s = re.findall("<.*?>",cod)
    for n in s:
        cod.remove(n,"")
    if cod!="":
        cod = cod.replace(u"\xa0",u" ")
        codes.append(cod)
    else:
        codes.append(cod)
# print(codes)
    

