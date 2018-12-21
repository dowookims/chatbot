import os
import sys
import requests
import json

client_id = os.getenv('CLOVA_ID')
client_secret = os.getenv('CLOVA_CS')
img_file='sana.jpg'
# url = "https://openapi.naver.com/v1/vision/face" // 얼굴감지
url = "https://openapi.naver.com/v1/vision/celebrity" #// 유명인 얼굴인식
files = {'image': open(img_file, 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
result_dict = eval((response.text))
cel_name = (result_dict['faces'][0]['celebrity']['value'])
cel_rate = (result_dict['faces'][0]['celebrity']['confidence'])
if(rescode==200):
    print(cel_name + ' 를 ' + str(cel_rate) + ' 정도 닮았으')
else:
    print("Error Code:" + rescode)