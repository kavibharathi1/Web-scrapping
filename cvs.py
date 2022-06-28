import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://www.lifewire.com/download-free-books-3482754'
response = requests.get(URL).content
soup = bs(response, 'html.parser')
titles = soup.find_all('a',{'class':'mntl-sc-block-heading__link'})
titles_list = []

count = 1
for title in titles:
    dict = {}
    dict['Title Number'] = f'Title {count}'
    dict['Title Name'] = title.text
    count += 1
    titles_list.append(dict)

filename = "C:\\Users\\KARTHIK\\Desktop\\info\\mo.csv"
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['Title Number', 'Title Name'])
    w.writeheader()

    w.writerows(titles_list)