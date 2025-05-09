import requests
from bs4 import BeautifulSoup
import csv      # csv 파일 저장

with open("w0509/notice_list.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")

## 파일 저장
ff = open("w0509/list.csv", "w", encoding="utf-8-sig", newline="")      # utf-8-sig : 엑셀파일에서 한글깨짐 방지, newline="" : enter키 입력X
writer = csv.writer(ff)     # csv 파일 list 타입으로 저장

trs = soup.table.find_all("tr")
for i, tr in enumerate(trs):
    fileName = []
    # 상단 타이틀
    if i==0:
        ths = soup.table.find_all("th")
        for th in ths:
            print(th.get_text(), end="\t")
            fileName.append(th.get_text())
        writer.writerow(fileName)       # 상단 타이틀 list 타입으로 저장
        print()
        continue
    # 내용 부분
    tds = tr.find_all("td")
    for td in tds:
        print(td.get_text(), end="\t")
        fileName.append(td.get_text())
    writer.writerow(fileName)           # 내용 부분 list 타입으로 저장
    print()