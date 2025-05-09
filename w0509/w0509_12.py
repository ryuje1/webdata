import requests
from bs4 import BeautifulSoup
import csv

with open('w0509/join02_info_input.html', 'r', encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")

## 파일 저장
ff = open("w0509/join.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(ff)

fds = soup.find_all("fieldset")
for fd in fds:
    fileName = []
    dts = fd.find_all("dt")
    for dt in dts:
        print(dt.get_text().strip())    # strip() : 공백제거
        fileName.append(dt.get_text().strip())
    writer.writerow(fileName)