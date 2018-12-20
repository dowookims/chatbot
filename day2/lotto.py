import random
import requests as req
import json

#1. 나눔로또 api를 통해 우승 번호를 가져온다.
#2. Random으로 생성된 번호와 우승 번호를 비교해서 등수를 알려준다.
# - 1등 : 6개
# - 2등 : 5개 맞고 + 보너스 번호
# - 3등 : 5개
# - 4등 : 4개
# - 5등 : 3개

numbers = sorted(random.sample(range(1,46), 6))
my_numbers = ' '.join(str(e) for e in numbers)
print(numbers)
bonus_num = 0
success_nums = 0
winner = []
ranks = ""

url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837"

res = req.get(url, verify=False)
lotto_dict = json.loads(res.text)

drwNo = lotto_dict['drwNo']

for i in range(1,7):
    winner.append(lotto_dict[f"drwtNo{i}"])

    if numbers[i-1] == lotto_dict[f"drwtNo{i}"]:
        success_nums +=1
    if numbers[i-1] == lotto_dict['bnusNo']:
        bonus_num == 1

winner_txtNum = ' '.join(str(e) for e in winner)

if success_nums == 3:
    ranks = "5등"
elif success_nums == 4:
    ranks = "4등"
elif success_nums == 5:
    if bonus_num == 1:
        ranks = "2등"
    else :
        ranks = "3등"
elif success_nums == 6:
    ranks ="1등"
else :
    ranks ="꽝"


print('***********************************************************')
print(f'이번 {drwNo} 회차 당첨번호는 {winner} 입니다.')
print('***********************************************************')
print(f'당신의 순위는 {ranks} 당신의 번호는 {numbers} 입니다. 로또와 맞는 숫자는 {str(success_nums)} 입니다.')
print('***********************************************************')