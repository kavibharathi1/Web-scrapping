import requests
from bs4 import BeautifulSoup
from htmldate import find_date


response = requests.get("https://myfwc.com/hunting/season-dates/").content
find_date=find_date("https://myfwc.com/hunting/season-dates/")
    #print(response)
soup = BeautifulSoup(response, 'lxml')
htmldate = soup.div("div",{"class" : "col-md"})
for each in htmldate:
    print(each.text)
#print(htmldate)
    #lines = div.find_all('t')
    #print(lines)
