from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime
import os, glob

client = MongoClient("mongodb://localhost:27017")
db = client.interview

def read_rss(file_name):
	with open(file_name) as fp:
	 	soup = BeautifulSoup(fp, "lxml")

	for item in soup.findAll('item'):
	    artical = {
	    	"guid": item.guid.string,
	    	"link": item.link.string,
			"title": item.title.string,
			"description": item.description.string,
			"pubdate": item.pubdate.string,
			"category": item.category.string
	    }
	    result = db.interview.insert_one(artical)
	    print(result.inserted_id)


rss_dir = "/Users/admin/Desktop/interview_senior/rss"
html_dir = "/Users/admin/Desktop/interview_senior/html"

if __name__ == "__main__":
	for f in os.listdir(rss_dir):
		read_rss(os.path.join(rss_dir, f))

