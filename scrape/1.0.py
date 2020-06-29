import sys
import re
from re import search as search
from urllib.request import urlopen as uopen
from urllib import parse, error
from bs4 import BeautifulSoup as soup

#datasci cred req url
ds_url = "http://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/datascience/#degreerequirementstext"

uclient = uopen(ds_url)
ds_html = uclient.read()
uclient.close()

ds_soup = soup(ds_html, "html.parser")

#debug space 
print("""
__________________


i dont wana blind

__________________
""")

ds_raw = ds_soup.find(id="degreerequirementstextcontainer")
# print(ds_raw)

# get headers by class="courselistcomment areaheader", remove html tags, print
ds_headers = ds_soup.find_all("span", class_="courselistcomment areaheader")
headers = []
for i in ds_headers:
    i = str(i.text)
    s = re.findall("<.*?>",i)
    for n in s:
        i.remove(n,"")
    if i!="":
        headers.append(i)
        print(i)


# get credit hours by class="hourscol", remove html tags, print
ds_hours = ds_soup.find_all("td", class_="hourscol")
for i in ds_hours:
    i = str(i.text)
    s = re.findall("<.*?>",i)
    for n in s:
        i.remove(n,"")
    # if i!="":
    #     print(i)


# get course codes by class="hourscol", remove html tags, print
ds_code = ds_soup.find_all("a", class_="bubblelink code")
for i in ds_code:
    i = str(i.text)
    s = re.findall("<.*?>",i)
    for n in s:
        i.remove(n,"")
    # if i!="":
    #     print(i)

# get course name??
# ds_name = ds_soup.find("td", class_="hourscol")
# name = ds_name.find_previous_sibling("td")
# print(name)

# for i in ds_name:
#     print(i)

