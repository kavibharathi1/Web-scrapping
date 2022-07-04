import requests
from bs4 import Beautifu

def extracting(url):
    response =request.get(url=url).content
    soup =BeatifulSoup(response, 'lxml')
    image=soup.find_all("img" , {"class": "mntl-lightbox__img"})
    print(image)
    for img in image:
        print(img["scr"])
extracting(url ="https://www.lifewire.com/download-free-books-3482754")






















