import pandas as pd
import requests
from bs4 import BeautifulSoup

season_date =[]
species_name =[]


url =("https://mdc.mo.gov/hunting-trapping/seasons?species_topic_filter=All&page=0")
response=requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
data = soup.find_all('div', attrs={'role': 'article'})
#print(data)  # 'id':'-content'


for store in data:

         name_1= store.find('span',class_='field--title').text.replace('\n','')
         species_name.append(name_1)

         name_2 = store.find(class_='field__item').text
         season_date.append(name_2)

list= pd.DataFrame({"species name":species_name,"season date":season_date})
print(list)






