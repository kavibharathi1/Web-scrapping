import requests
from bs4 import BeautifulSoup
import csv
url="https://mdc.mo.gov/fishing/species"
req=requests.get(url).content
soup=BeautifulSoup(req,'lxml')
f=open("C:\\Users\\KARTHIK\\Desktop\\info\\fsh.csv", "w")
headerlist=['Species name' , 'urls']
dw=csv.DictWriter(f,delimiter=',',fieldnames=headerlist)
dw.writeheader()

for i in soup.find_all('div',attrs={'class':"field--field-hunting-species-name"}):
    data1=i.text
    data2=(i.a['href'])
    con=str(data1)+ ',' +str(data2)
    print(con)
    f.write(con)
    f.write("/n")
