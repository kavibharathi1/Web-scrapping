import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://mdc.mo.gov/discover-nature/field-guide/american-badger"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

data = soup.find_all('div', attrs={'class': 'dialog-off-canvas-main-canvas'})  # 'div',attrs={'class':'field__items'})

for store in data:
    link = store.find(class_='block-field-blocknodespeciesfield-species-media').img
    print(link['src'])

    species_name = store.find('span', class_='field--hidden').text
    print(species_name)

    scientific_name = store.find(class_='field--field-species-scientific-name').text
    print(scientific_name)

    family = store.find(class_='field--field-species-family').text
    print(family)

    desc = store.find(class_='field--field-species-description').text
    print(desc)

    size = store.find(class_='field--field-species-size').text
    print(size)

    habit = store.find(class_='field--field-species-habitat').text
    print(habit)

    food = store.find(class_='block-field-blocknodespeciesfield-species-food').text
    print(food)

    status = store.find(class_='block-field-blocknodespeciesfield-species-status-text').text
    print(status)

    find = store.find(class_='field--field-species-distribution').text
    print(find)

