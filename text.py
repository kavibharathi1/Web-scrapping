import requests
from bs4 import BeautifulSoup

def ExtractData(url):
    response = requests.get(url=url).content
    #print(response)
    soup = BeautifulSoup(response, 'lxml')
    div = soup.div("a",{"class" : "mntl-sc-block-heading__link"})
    for each in div:
       print(each.text)
    #lines = div.find_all('t')
    #print(lines)

ExtractData(url ="https://www.lifewire.com/download-free-books-3482754")
























