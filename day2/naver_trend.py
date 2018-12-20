# 1. requests 에게 naver.com 요청을 보내서
# 2. 응답 받은 문서를 저장하고
# 3. BeautifulSoup 패키지를 통해서
# 4. 우리가 원하는 정보를 뽑아 온다.
# 5. webbrowser를 통해 1위 검색어 페이지를 열어주는 코드.

import requests
import bs4
import webbrowser

url = "https://www.naver.com/"
url1 = "https://search.naver.com/search.naver?query="
result_text_list=[]

response = requests.get(url)
doc = bs4.BeautifulSoup(response.text, "html.parser")

# select로 사용하면 배열로 데이터 변수 저장
result_list = doc.select(".ah_k")

for i in result_list[0:10]:
    result_text_list.append(i.text)

print(result_text_list)
# webbrowser.open_new(url1 + result.text)
