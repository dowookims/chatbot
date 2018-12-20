import requests
import bs4
import webbrowser

url = "https://www.bithumb.com/"

res = requests.get(url)
doc = bs4.BeautifulSoup(res.text, "html.parser")

coin_price_list =[]
coin_name_list =[]
coin_korName_list =[]

price_list = doc.select(".sort_real")
name_list = doc.select(".sort_coin")
korName_list = doc.select("#tableAsset > tbody > tr:nth-child(2) > td:nth-child(1) > p > a > strong")

for i in name_list[0:5]:
    coin_name_list.append(i.text)

for i in korName_list[0:5]:
    print(i.text)
    coin_korName_list.append(i.text)

for i in price_list[0:5]:
    coin_price_list.append(i.text)


