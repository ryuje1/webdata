import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time

# 크롬 옵션 설정
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)

# 페이지 접속
url = "https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(3)   # 페이지 로딩 대기

soup = BeautifulSoup(browser.page_source,"lxml")



#### 1-100등 출력하시오
# 순위    곡정보     가수  좋아요  이미지링크
#  1  너에게 닿기를  10cm  59060  https://..
# 합계 : 좋아요 총개수 : 100,000
# 파일 melon1.jpg, ... melon100.jpg


tbody = soup.find("tbody")
trs = tbody.find_all("tr")
# print(trs)

# thead = soup.find("thead")
# ths = thead.find_all("th")
# print(ths[1].find("span", {"class":"rank"}).get_text().strip(), end="\t")
# print(ths[5].find("div", {"class":"wrap pd_l_12"}).get_text().strip(), end="\t")

# title = ['순위', '곡정보', '가수', '좋아요', '이미지링크']
# print("{}\t{}\t{}\t{}\t{}".format(*title))

### 파일 저장
ff = open("w0512/melon1.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(ff)
title = ['순위', '곡제목', '가수', '좋아요']

sum = 0
for tr in trs:
    contents = []
    tds = tr.find_all("td")
    # 순위
    rank = tds[1].find("span", {"class":"rank"}).get_text().strip()
    contents.append(rank)
    print(rank, end="\t")
    # 곡제목
    song = tds[5].find("div", {"class":"ellipsis rank01"}).get_text().strip()
    contents.append(song)
    print(song, end="\t")
    # 가수
    singer = tds[5].find("div", {"class":"ellipsis rank02"}).get_text().strip()
    contents.append(singer)
    print(singer, end="\t")
    # 좋아요
    cnt = tds[7].find("span", {"class":"cnt"}).get_text().strip()[3:].strip()
    contents.append(cnt)
    print(cnt, end="\t")
    
    # 이미지
    print(tds[3].img["src"])
    # 이미지 저장
    imgUrl = tds[3].img["src"]
    img_res = requests.get(imgUrl)
    with open(f"w0512/melonImg/melon{rank}.jpg", "wb") as f:
        f.write(img_res.content)
        
    # 좋아요 합계
    sum += int(int(cnt.replace(",", "")))
    
    writer.writerow(contents)

ff.close()
print(f"좋아요 총 개수 : {sum:,d}")