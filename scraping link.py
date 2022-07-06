import requests
from bs4 import BeautifulSoup

def extractlink(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response,'lxml')
    for link in soup.find_all('a'):
     print(link.get('href'))
extractlink(url ="https://mdc.mo.gov/hunting-trapping/regulations")





















