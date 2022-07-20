import requests
from bs4 import BeautifulSoup
import csv
import re

def extractlink(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response,'lxml')
    f = open("C:\\Users\\KARTHIK\\Desktop\\info\\mil.csv", "w" )

    headerlist = ['SPECIES NAME', 'URLs']
    print(headerlist)
    dw = csv.DictWriter(f, delimiter=',', fieldnames=headerlist)
    dw.writeheader()

    for link in soup.find_all('a', href=re.compile("^/hunting-trapping/species/")):

              data1=link.text
              data2=link.get('href')
              content=str(data1)+','+str(data2)
              print(content)
              f.write(content)
              f.write("\n")
    # for link in soup.find_all('a'):
          #print(link.get('href'))
          #print(link.text)
extractlink(url ="https://mdc.mo.gov/hunting-trapping/species")



















'''
filename = "C:\\Users\\KARTHIK\\Desktop\\info\\index.csv"
fo=open(filename,'w', newline="")
content_writer =csv.writer(fo)
content_writer.writerow(['link'])
fo.close()
'''

