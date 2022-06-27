import requests
from bs4 import BeautifulSoup

def ExtractData(url):
    response = requests.get(url=url).content
    #print(response)
    soup = BeautifulSoup(response, 'lxml')
    div = soup.div("div",{"class" : "loc article-content"})
    print(div)
    #lines = div.find_all('t')
    #print(lines)

ExtractData(url ="https://www.lifewire.com/download-free-books-3482754")
























