from selenium import webdriver as wd
import time
import datetime
import webbrowser as wb
import requests as req

driver = wd.Chrome("C:\\Users\\student\\Desktop\\study\\chatbot\\day3\\chromedriver")
driver.implicitly_wait(3)

url = "https://edu.ssafy.com/comm/login/SecurityLoginForm.do"
url2 = "https://edu.ssafy.com/edu/board/notice/list.do"

driver.get(url)
driver.find_element_by_name('userId').send_keys('userId')
driver.find_element_by_name('userPwd').send_keys('userPw')
driver.find_element_by_css_selector('#wrap > div > div > div.section > form > div > div.field-set.log-in > div.form-btn > a').click()
driver.get(url2)
result = driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div.board-wrap > table.default-tbl.type2 > tbody > tr > td.link > a').click()

days = driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(4)').text
menu0 = days.split('\n')
menu_list=[]
# 현재 공지사항 까지 들어갔고

# 추후에 공지사항에서 게시글 텍스트 뽑아내고, 그 중 [중식] 있는 것 중에, 최근에 있는 것을 뽑아낸다.

# 이후 날짜를 확인해서, 오늘에 맞는 것을 뽑아내서 작업한다.

dt = datetime.datetime.now()
nowDt = dt.strftime('%Y-%m-%d')
wtdy = dt.weekday()
ktdy =""
tmrw = dt.weekday()+1
tmrDt = dt.strftime('%Y-%m-%d')
print("내일은"+tmrDt)

menu_list.append(menu0)
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(5)').text.split('\n')[7:])
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(6)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(7)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(8)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(9)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(10)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(11)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(12)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(13)').text.split('\n')[1:])
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(14)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(15)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(16)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(17)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(18)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(19)').text.split('\n'))
menu_list.append(driver.find_element_by_css_selector('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb > table:nth-child(4) > tbody > tr:nth-child(20)').text.split('\n'))

def print_menu(wtdy):
    for i in range(0,len(menu_list)):
        if i==0:
            print(nowDt+" "+menu_list[i][wtdy])
            continue
        if i==1:
            print("*****A형*******\n"+menu_list[i][wtdy])
            continue
        if i==9:
            print("*****B형*******\n"+menu_list[i][wtdy])
            continue
        print(menu_list[i][wtdy])

# 내일 메뉴도 출력
#print_menu(wtdy)
# 이번주 메뉴도 출력
