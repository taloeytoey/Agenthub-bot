import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://propertyhub.in.th/listings/%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B9%80%E0%B8%8A%E0%B9%88%E0%B8%B2-lumpini-ville-prachachuen-phongphet-2-%E0%B8%AB%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%AA%E0%B8%A7%E0%B8%A2-%E0%B8%99%E0%B9%88%E0%B8%B2%E0%B8%AD%E0%B8%A2%E0%B8%B9%E0%B9%88-%E0%B9%80%E0%B8%94%E0%B8%B4%E0%B8%99%E0%B8%97%E0%B8%B2%E0%B8%87%E0%B8%AA%E0%B8%B0%E0%B8%94%E0%B8%A7%E0%B8%81-%E0%B9%80%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%84%E0%B8%A3%E0%B8%9A-%E0%B8%88%E0%B8%9A%E0%B9%83%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%94%E0%B8%B5%E0%B8%A2%E0%B8%A7--bc910a5e---1154268'
response = requests.get(url)

if response.status_code == 200:  
    
    soup = BeautifulSoup(response.text, 'html.parser') 

    title = soup.find_all("h2", {"class": "sc-14haut3-1 ves8oa-14 jPbPgQ"})[0].text
    print (title)


    print ()
    detial_right = soup.find_all("ul", {"class": "ves8oa-4 jHqKOT"})
    for tag in detial_right:
        # print (tag.text)
        print("poster:", tag.find('a').text)#image src
        print("tel:", tag.find('button').text)#image src

    print ()
    detial_left = soup.find_all("div", {"class": "ves8oa-16 bCciqG"})
    for tag in detial_left:
        print (tag.text)

    print ()
    detial_right = soup.find_all("div", {"class": "col-xs-4 sc-1qj7qf1-2 jXJSll"})
    for tag in detial_right:
        print (tag.text)

    print ()
    articles_img = soup.find_all("div", {"class": "image-gallery-thumbnail-inner"})
    for article in articles_img:
        print("Image Source:", article.find('img').attrs['src'])#image src



