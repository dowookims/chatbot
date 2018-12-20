### .csv (Comma Separated Value : 콤마로 구분된 값(들))
### 파일 연다 `import csv`
### 1. 읽기
### 2. 쓰기
### 3. 수정
### 파일 닫기

import csv
# f = open('ssafy1.csv','w', encoding="utf-8")
# ssapy1 = csv.writer(f)
# ssapy1.writerow(["john", "john@hphk.kr", "01012345678", "DoUKnowKimchi","cs"])
# f.close()

# csv 읽기
r = open('ssafy1.csv','r', encoding="utf-8")
ssapy1 = csv.reader(r)
for line in ssapy1:
        print(line)
r.close()
# # csv 수정(추가)
# a = open('ssafy1.csv', 'a', encoding="utf-8")
# ssapy1 = csv.writer(a)
# ssapy1.writerow(["john", "john@hphk.kr", "01012345678", "DoUKnowKimchi","cs"])
# a.close()