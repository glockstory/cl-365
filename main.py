from bs4 import BeautifulSoup
import requests
import re
from getHTML import get_html
from get_all_links import get_all_links
from pymongo import MongoClient


def putinfo(links):
    for url in links:
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        newsTimes = soup.find('div', {'class': 'col-md-9 main-content'}).find('div', {'class': 'date'})
        bigline = soup.find('div', {'id': 'full_text'})
        headline = soup.find('h1').text
        newsLine = bigline.text
        newsLine = re.sub("^\s+|\n|\r|\s+$", '', newsLine)  # 2 текст новости
        newsTime = newsTimes.text.strip()  # 4   дата
        news_ = {
            "headline": headline,
            "text": newsLine,
            "url": url,
            "time": newsTime
        }
        if news.find_one({'headline': headline}) is None:
            if news.find_one({'url': url}) is None:
                if news.find_one({'time': newsTime}) is None:
                    news.insert_one(news_)
                    print('added entry to the database', url)
        else:
            print('entry already exists', url)


client = MongoClient()
db = client.news_volgograd
news = db.news_vlg

for i in range(11, 20):
    url = 'https://www.volgograd.ru/news/' + '?PAGEN_1=' + str(i)
    all_links = get_all_links(get_html(url))
    putinfo(all_links)
