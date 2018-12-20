import requests as req
from bs4 import BeautifulSoup as bs
import datetime
#from time import sleep
HTTP_API_key ="환경변수"
user_id = '환경변수'

url = f"https://api.telegram.org/bot{HTTP_API_key}/"
url_weather = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
res_weather = req.get(url_weather)
#travel_date = datetime.datetime.now() => 최저가 비행기 자동으로 보내기
#url_buyTickets = f"https://store.naver.com/flights/v2/results?trip=OW&scity1=ICN&ecity1=BKK&sdate1={travel_date}.&adult=1&child=0&infant=0&fareType=Y&airlineCode=&nxQuery=%ED%95%AD%EA%B3%B5%EA%B6%8C"
doc = bs(res_weather.text, "html.parser")
today_temp = doc.select(".todaytemp")
today_weat = doc.select(".cast_txt")

msg = f"오늘 서울의 기온은 {today_temp[0].text}도. {today_weat[0].text}."

def botSendTempMsg(text):
    msg = text
    url2 = f"https://api.telegram.org/bot684427904:AAFR-JTyhuf--wZiosr_IMdu9lggDp-F1VU/sendMessage?chat_id={user_id}&text={msg}"
    req.get(url2)

#botSendTempMsg(msg)