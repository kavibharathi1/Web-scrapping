import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

season_date =[]
species_name =[]
pages = np.arange(1,2,10)
for page in pages:
     page =requests.get("https://mdc.mo.gov/hunting-trapping/seasons?species_topic_filter=All&page=0")
     soup=BeautifulSoup(page.text,'html.parser')
     data =soup.find_all('div',attrs={'role':'article'})#'id':'-content'

     for store in data:

         name_1= store.h2.a.find('span', class_ ='field--title').text
         species_name.append(name_1)
         name_2 = store.find(class_='field__items').text.replace('\n', '')
         season_date.append(name_2)

list= pd.DataFrame({"species name":species_name,"season date":season_date})
print(list)







