import requests
from bs4 import BeautifulSoup
import pandas as pd
import sklearn
from sklearn.metrics.pairwise import linear_kernel
from gensim.models import Word2Vec
import logging  # Setting up the loggings to monitor gensim
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)
from sklearn.manifold import TSNE
import spacy
#import en_core_web_sm
import numpy as np

data = requests.get("http://catalog.drexel.edu/coursedescriptions/quarter/undergrad/")

link_page_soup = BeautifulSoup(data.text, 'html.parser')

list_link_divs = link_page_soup.find_all("div", class_="qugcourses")

list_links_a = []
for div in list_link_divs:
#     print(div.find_all("a"))
#     print("*"*100)
    for a in div.find_all("a",  href=True):
#         print("http://catalog.drexel.edu/" + a['href'])
        list_links_a.append("http://catalog.drexel.edu/" + a['href'] )

course_name_description_list = []
for course_link in list_links_a:
    course_soup = BeautifulSoup(requests.get(course_link).text, 'html.parser')
    for course in course_soup.find_all("div", class_="courseblock"):
#         print(course.find("p" , class_ = "courseblocktitle").text)
#         print(course.find("p" , class_ = "courseblockdesc").text)        
        course_name_description_list.append([course.find("p" , class_ = "courseblocktitle").text, course.find("p" , class_ = "courseblockdesc").text ])

course_df = pd.DataFrame(course_name_description_list)
course_df.columns = ["TitleBlock" , "DescriptionBlock"]

course_df = pd.concat([course_df,  course_df.TitleBlock.str.extract(r"(.*\s*\d{3,5})\s*(.*)(\d.\d)") ], axis =1 )

course_df.columns = ["TitleBlock" , "DescriptionBlock", "CourseID" , "CourseName" , "Credits" ]

course_df.DescriptionBlock = course_df.DescriptionBlock.str.replace("\n", "")

#comment the line below to print only the first 5 + last 5 lines
pd.set_option("display.max_rows", None, "display.max_columns", None)

print(course_df)
