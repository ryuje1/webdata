import requests
from bs4 import BeautifulSoup
import csv

with open("w0509/게시판3.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")
    
# -----------------------------  연습 -----------------------------    
# # th 부분
# ths = soup.find("thead").find_all("th")
# for i in range(len(ths)-1):
#     print(ths[i].get_text(), end="\t")
# print()

# # td 부분
# tbody = soup.find("tbody", {"id":"tbody"})
# trs = tbody.find_all("tr")

# for tr in trs:
#     tds = tr.find_all("td")
#     if len(tds) > 1:
#         for i in range(len(tds)-1):
#             print(tds[i].get_text(), end="\t")
#         print()
# ----------------------------------------------------------------

# html 태그 출력
print(soup.title)
print(soup.title.get_text())

# 속성 출력 soup.a['href']
print(soup.a['href'])

## find(), find_all()
# print(soup.find("thead"))
data = soup.find("thead")
ths = data.find_all("th")
print("th 개수 :", len(ths))

# for i in range(len(ths)-1):
#     print(ths[i].get_text(), end="\t")
# print()

# 파일 저장
fileName = "board.csv"
ff = open("w0509/"+fileName, "w", encoding="utf-8-sig", newline="")      # newline="" : enter키 입력X
# with open("w0509/"+fileName, "w", encoding="utf-8-sig", newline="") as ff:
writer = csv.writer(ff)         # csv : 자동으로 ,를 기준으로 구분

# 상단 제목 파일에 저장
topTitle = []
for i, th in enumerate(ths):
    if i<5: 
        print(th.get_text(), end="\t")
        topTitle.append(th.get_text())
writer.writerow(topTitle)       # writerow로는 리스트 타입만 입력 가능
print()


data2 = soup.find("tbody")
trs = data2.find_all("tr")
# print("tr 갯수 :", len(trs))

for tr in trs:
    tds = tr.find_all("td")
    if len(tds)<=1: continue
    bodyData = []   # 게시글 부분 데이터 저장
    for i, td in enumerate(tds):
        if i<5: 
            print(td.get_text(), end="\t")
            bodyData.append(td.get_text())
    writer.writerow(bodyData)   # 파일에 게시글 1개를 저장
    print()

ff.close()
print("파일 저장완료")