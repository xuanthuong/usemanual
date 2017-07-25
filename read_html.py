from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime
import os, glob

client = MongoClient("mongodb://localhost:27017")
db = client.interview


def read_html(file_name):
	guid = file_name.split("/")[-1]
	with open(file_name) as fp:
	 	soup = BeautifulSoup(fp, "lxml")

	for item in soup.findAll('div', { "class" : "content-section" }):
	    content = item.string
	    db.interview.update_one({
			  'guid': guid
			},{
			  '$set': {
			    'content': "this is test content" 
			  }
			}, upsert=True)


html_dir = "/Users/admin/Desktop/interview_senior/html"

if __name__ == "__main__":
	for f in os.listdir(html_dir):
		read_html(os.path.join(html_dir, f))
	# read_html("/Users/admin/Desktop/interview_senior/html/0007b3ef-1624-44a0-9af7-8c4c45ab4a68")

