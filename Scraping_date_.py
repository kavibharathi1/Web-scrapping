import requests
import re
from bs4 import BeautifulSoup
url="https://myfwc.com/hunting/season-dates/"
data=requests.get(url).content
soup=BeautifulSoup(data,'lxml')

for list in re.finditer(r'<li>(.*?)</li>',str(soup)):
    print(list.group(1))
    print()
    #<h1 class="page-title">(.*?)</h1>


