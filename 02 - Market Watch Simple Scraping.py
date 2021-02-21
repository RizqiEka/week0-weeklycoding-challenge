#Import Required Library

import requests
from bs4 import BeautifulSoup

#Locating the main HTML block to scrape
#For Example: BRIS stock

url = "https://www.marketwatch.com/investing/stock/bris?countrycode=ID"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
containers = soup.find_all('li', {'class': 'kv__item'})

#Scraping through Container & Writing to .txt file

with open('BRIS Market Watch.txt', 'w') as creator:
    for i in containers:
        name = i.contents[1].text
        value = i.contents[3].text
        creator.write(f'{name} : {value} \n')