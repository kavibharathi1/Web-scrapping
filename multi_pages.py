import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

season_date =[]
species_name =[]
pages = np.arange(0,7)
url="https://mdc.mo.gov/hunting-trapping/seasons?species_topic_filter=All&page=0"

for page in pages:
     page =requests.get(url+str(page))
     soup=BeautifulSoup(page.text,'lxml')
     data =soup.find_all('div',attrs={'class':'views-row'})#'id':'-content'

     for store in data:

         name_1= store.h2.a.find('span', class_ ='field--title').text
         species_name.append(name_1)
         name_2 = store.find(class_='field__items').text.replace('\n', '')
         season_date.append(name_2)

dict=({"SPECIES NAME" : species_name ,"SEASONS DATE" : season_date})
df = pd.DataFrame(dict)
df.to_csv(r"C:\\Users\\KARTHIK\\Desktop\\info\\doc.csv", index=False )













