#coding=utf-8
import requests
from bs4 import BeautifulSoup
import shutil
import urllib
# import urllib.request
from time import sleep

# queryList = ['bmw2series','bmw3series','bmw4series','bmw5series','bmw6series','bmw7series']
# queryList = ['bmwx1','bmwx3','bmwx4','bmwx5','bmwx6','bmwm2','bmwm3','bmwm4','bmwm5','bmwm6']
queryList = ['bmw logo','benz logo','lexus logo','audi logo']
location = ['bmw','benz','lexus','audi']

for q in range(len(queryList)):

# for querywrd in queryList:
    # querywrd='bmw1series'
    index = 0
    for x in range(20):
        page = x*21
        url = ('http://www.google.com.sg/search?tbm=isch&source=hp&q=%s&btnG=Search+Images&biw=1920&bih=1075&start=%s&ndsp=21')% (urllib.quote(queryList[q]),page)
        # url = ('http://www.google.com.sg/search?tbm=isch&source=hp&q=%s&btnG=Search+Images&biw=1920&bih=1075&start=%s&ndsp=21')% (urllib.quote(querywrd),page)
        # url = 'https://www.google.com.sg/search?biw=1680&bih=395&tbm=isch&sa=2&q='


        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        shop_img = soup.findAll('img')
        # print len(shop_img)

        for img in shop_img:
            # print img['src']
            fname = str(index) + '.jpg'

            res2 = requests.get(img['src'], stream=True)
            f = open( 'car/' + location[q] + '/' + fname, 'wb')
            shutil.copyfileobj(res2.raw, f)
            f.close()
            del res2
            index += 1

        sleep(1)