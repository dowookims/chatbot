import random
import requests as req
import json

url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = req.get(url, verify=False)
lotto_dict = json.loads(res.text)
winner = []
fi = 0
fo = 0
th = 0
tw = 0
on = 0

for i in range(1,7):
    winner.append(lotto_dict[f"drwtNo{i}"])

for i in range(1, 10000000):
    bonus_num = 0
    correct_count = 0
    

    numbers = sorted(random.sample(range(1,46), 6))

    for i in range(6):
        if numbers[i] == winner[i]:
            correct_count +=1
        if numbers[i] == lotto_dict["bnusNo"]:
            bonus_num = 1
    
    if correct_count ==3:
        fi += 1
    elif correct_count ==4:
        fo += 1
    elif correct_count ==5 :
        if bonus_num == 1:
            tw += 1
        else :
            th +=1
    elif correct_count == 6 :
        print(i,'번째에 당첨쓰')
        on +=1


print(f'1등 : {on}')
print(f'2등 : {tw}')
print(f'3등 : {th}')
print(f'4등 : {fo}')
print(f'5등 : {fi}')
