#coding=utf-8
import requests
from bs4 import BeautifulSoup
import shutil
import urllib.parse

queryList = ['audi A1','audi A3','audi A4','audi A5','audi A6','audi A7','audi A8','audi Q5','audi Q7','audi TT','audi R8']
location = ['A1','A3','A4','A5','A6','A7','A8','Q5','Q7','TT','R8']
def search_engine(engine,name):
    for q in range(len(queryList)):
    # for querywrd in queryList:
        index = 0
        for x in range(20):
            page = x*21
            url = ('http://www.google.com.sg/search?tbm=isch&source=hp&q=%s&btnG=Search+Images&biw=1920&bih=1075&start=%s&ndsp=21') % (urllib.parse.quote(queryList[q]),page)
            
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            soup_img = soup.findAll('img')

            for img in soup_img:
                fname = name + str(index) + '.jpg'
                res = requests.get(img['src'], stream=True)
                f = open(location[q] + '/' + fname, 'wb')
                shutil.copyfileobj(res.raw, f)
                f.close()
                del res
                index += 1

search_engine('http://www.google.com.sg/search?tbm=isch&source=hp&q=%s&btnG=Search+Images&biw=1920&bih=1075&start=%s&ndsp=21','go')
search_engine('https://www.bing.com/images/search?q=%s&qs=n&form=QBIR&pq=%s&sc=8-8&sp=-1&sk=&undefined=undefined','bi')
search_engine('https://tw.images.search.yahoo.com/search/images;_ylt=A8tUwJuClwFYW0IAztZt1gt.?p=%s&fr=yfp-t-900-tw&fr2=p%3As%2Cv%3Ai','ya')
search_engine('http://search.wow.com/image?v_t=splus-scr&page=1&q=%s&s_it=sb-top&oreq=efde98577c6149de9c4ef218fdcee696','wo')
search_engine('http://search.infospace.com/search/images?fcoid=417&fcop=topnav&fpid=2&q=%s&ql=&topSearchSubmit=Search&topSearchSubmit=Search','inf')