# naver webtoon 화요일 긁어오기

import requests
#import bs4
from bs4 import BeautifulSoup as bs
import webbrowser
import datetime
import os
import codecs

url ='https://m.comic.naver.com/webtoon/weekday.nhn?week='
goto_url="https://comic.naver.com/webtoon/weekdayList.nhn?week="
result_comics_name_list = []
result_comics_imgUrl_list = []

dt = datetime.datetime.now()
today =""
if dt.weekday() == 0:
    today ='mon'
elif dt.weekday() == 1:
    today ='tue'
elif dt.weekday() == 2:
    today ='wed'
elif dt.weekday() == 3:
    today ='thu'
elif dt.weekday() == 4:
    today ='fri'
elif dt.weekday() == 5:
    today ='sat'
else:
    today ='sun'

response = requests.get(url+today)
doc = bs(response.text, 'html.parser')

result_list = doc.select('.toon_name')
result_img_list = doc.select('.im_br')

for e in result_img_list:
    print(e.select_one('img')['src'])

for i in result_list:
    result_comics_name_list.append(i.text)

file = codecs.open(today+"_comics_name.txt", 'w', encoding='utf-8')

for i in result_comics_name_list:
    file.write(i+"\n")

file.close()