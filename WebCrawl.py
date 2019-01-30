import os
# import urllib.request
from urllib import request
import requests
from bs4 import BeautifulSoup
import lxml

def geturl(url):
    folder = "G:\python tutorials\Python-masterclass-course"
    image = "Madonna" + ".jpeg"
    name = os.path.join(folder,image)
    request.urlretrieve(url,name)
    print("Done")

def savecsv(url):
    content = request.urlopen(url)
    csv = content.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'url'
    fx = open(dest_url,"w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

def spider():
    firsturl = r'https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2'
    page = 1;
    while page <= 10:
        if(page == 1):
            source_code = requests.get(firsturl)
        else:
            url = firsturl + "&page=" + str(page)
            print("URL is:" + url)
            source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')
        for link in soup.find_all('div',{'class':'_3wU53n'}):
            #href = link.get('href')
            title = link.text
            print(title)
            #print(href)
        page += 1

def NewReleases():
    url = r'https://www.flipkart.com/offers-list/mobile-new-launches?screen=dynamic&pk=themeViews%3DNewlaunches-whitelisted%3Adesk~widgetType%3DdealCard~contentType%3Dneo&wid=19.dealCard.OMU&otracker=hp_omu_Mobile%2BNew%2BLaunches_7'
    source_code = requests.get(url)
    plain_text = source_code.text
    print(plain_text)
    soup = BeautifulSoup(plain_text,'lxml')
    for link in soup.find_all('div',{'class':'iUmrbN'}):
        title = link.string
        print("Mobile:" + str(title))
    for link in soup.find_all('div',{'class':'_3o3r66'}):
        price = link.string
        print("Price is:" + str(price))

#geturl("https://i.pinimg.com/originals/2e/16/07/2e16070ee6164f0d9b77dec6e977873e.jpg")
#savecsv("http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv")
# spider()
NewReleases()
