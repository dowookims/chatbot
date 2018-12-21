import os
import requests as req
from pprint import pprint as pp


# String 수술
# 1. f-string
# 2. format()
#print("Hello, {}".format("Asheley"))
# res = req.get(url_u)
# doc = res.json()
#user_id = pp(doc['result'][0]['message']['chat']['id'])
#user_name = pp(doc['result'][0]['message']['chat']['first_name'])

# 아젠다 : 텔레그램 메세지를 보낼 예정
## chat_id 받아오는 과정
# 1. 환경변수 호출
#   - 토큰 환경변수를 불러온다.
# 2. url 만듦
#   - base url을 만들어서
#   - base url + token + method
# 3. getUpdates
# 4. chat_id get
# ***********************************
# 5. url 재 구성
# 6. 메시지를 보냄

msg = input()
token = os.getenv('TELEGRAM_TOKEN')
default_id = os.getenv('USERID')
name = os.getenv('NAMES')
url = f"https://api.telegram.org/bot{token}/"

def showJson(token=token):
    method = "getUpdates"
    url_s = f"{url}{method}"
    return req.get(url_s).json()
    
def showIdNames(token = token, index = 0):
    doc = showJson()
    user_id = doc['result'][index]['message']['chat']['id']
    user_nm = doc['result'][index]['message']['chat']['first_name']
    return [user_id, user_nm]
    
def sendMessage(msg, token = token, chat_id = default_id):
    method = "sendMessage"
    url_m = f"{url}{method}?chat_id={chat_id}&text={msg}"
    req.get(url_m)
    return True

sendMessage(msg)