
import sys
from urllib import request 
from urllib.request import urlopen as uopen
from bs4 import BeautifulSoup as soup

#datasci cred req url
ds_url = "http://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/datascience/#degreerequirementstext"

uclient = uopen(ds_url)
ds_html = uclient.read()
uclient.close()

ds_soup = soup(ds_html, "html.parser")
print(ds_soup.h1)
print(ds_soup.h2)
print(ds_soup.h3)