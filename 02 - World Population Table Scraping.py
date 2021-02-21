#Import Required Library

import requests
from bs4 import BeautifulSoup

#Locating the table to scrape

url = "https://www.worldometers.info/world-population/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
table = soup.find('table', {'class': 'table table-striped table-bordered table-hover table-condensed table-list'})
table = table.find_all('tr')

with open('Worldometer Word Population.txt', 'w') as creator:
    for row in table:

        #Scrape the Table Heading
        headcolumn = row.find_all('th')
        for entry in headcolumn:
            creator.write(f'{entry.text} ')

        #Scrape the Table Content
        column = row.find_all('td')
        for entry in column:
            creator.write(f'{entry.text} ')
        creator.write('\n')