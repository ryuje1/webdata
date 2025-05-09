import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# th 출력, 파일 저장
# ff = open("w0509/stock.csv", "w", encoding="utf-8-sig", newline="")
# writer = csv.writer(ff)
# ths = soup.thead.find_all("th")
# fileName = []
# for th in ths:
#     print(th.get_text(), end="\t")
#     fileName.append(th.get_text())
# writer.writerow(fileName)
# print()


## 내용부분 5개 
trs = soup.tbody.find_all("tr")
for tr in trs:
    tds = tr.find_all("td")
    count = 0
    if len(tds)<=1: continue
    for td in tds:
        if td.find("span", {"class":"blind"}):continue
        print(td.get_text().strip(), end="\t")
    print()

## 50개 저장
trs = soup.tbody.find_all("tr")
for tr in trs:
    tds = tr.find_all("td")
    if len(tds)<=1: continue
    for td in tds:
        if td.find("span", {"class":"blind"}):continue
        print(td.get_text().strip(), end="\t")
        # fileName.append(td.get_text().strip())
    # writer.writerow(fileName)
    print()