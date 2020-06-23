
import sys
import re
from urllib.request import urlopen as uopen
from urllib import parse, error
from bs4 import BeautifulSoup as soup

#datasci cred req url
ds_url = "http://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/datascience/#degreerequirementstext"
#someone pls debuG THIS MF

uclient = uopen(ds_url)
ds_html = uclient.read()
uclient.close()

ds_soup = soup(ds_html, "html.parser")
print("""


space


""")
ds_raw = ds_soup.find_all(id="degreerequirementstextcontainer")
print(ds_raw)
