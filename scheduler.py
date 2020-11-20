import time
import schedule
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import requests
import os
from dotenv import load_dotenv
import pymongo
import datetime
load_dotenv()

KEY = os.getenv('KEY')
MONGO_URL = os.getenv('MONGO_URL')
client = pymongo.MongoClient(MONGO_URL)

db = client["badnews"]
collection = db["articles"]


def analyze_news():
    data = {}
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           f'apiKey={KEY}')
    response = requests.get(url)
    json = response.json()

    titles = []
    for i in json['articles']:
        pol = TextBlob(i['title']).sentiment.polarity
        titles.append({"title": i['title'], "pol": pol})

    five_worst = sorted((i for i in titles), key=lambda k: k['pol'])[0:6]
    data['title'] = five_worst[0]['title']
    response = collection.insert_one(data)


if __name__ == "__main__":
    job()
