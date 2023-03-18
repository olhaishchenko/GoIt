import json

import requests
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com"


def get_url():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class=quote] span a')
    urls = []
    for tag_a in content:
        urls.append(tag_a['href'])
    return urls


def spider_quotes():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class=quote]')
    result_quotes = []
    for element in content:
        tags = element.find('div', attrs={"class": "tags"}).find('meta')['content'].split(",")
        author = element.find('small', attrs={"class": "author"}).text
        quote = element.find('span', attrs={"class": "text"}).text
        result = {"tags": tags,
                  "author": author,
                  "quote": quote}
        result_quotes.append(result)
    return result_quotes


def spider_authors(urls):
    result_authors = []
    for url in urls:
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('div[class=author-details]')[0]
        fullname = content.find('h3', attrs={"class": "author-title"}).text.split('\n')[0]
        born_date = content.find('span', attrs={"class": "author-born-date"}).text
        born_location = content.find('span', attrs={"class": "author-born-location"}).text
        description = content.find('div', attrs={"class": "author-description"}).text.strip()
        result = {"fullname": fullname,
                  "born_date": born_date,
                  "born_location": born_location,
                  "description": description}
        result_authors.append(result)
    return result_authors


if __name__ == '__main__':
    q = spider_quotes()
    u = get_url()
    a = spider_authors(u)
    with open('quotes.json', 'w', encoding='utf-8') as fd:
        json.dump(q, fd, ensure_ascii=False)
    with open('authors.json', 'w', encoding='utf-8') as fd:
        json.dump(a, fd, ensure_ascii=False)
