import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

soup = BeautifulSoup(browser.page_source, "lxml")
tbody = soup.find("tbody")
trs = tbody.find_all("tr")
tds = trs[0].find_all("td")

print(tds[1].find("span", {"class":"rank"}).get_text().strip())

print(tds[3].img["src"])
### 이미지 저장
imgUrl = tds[3].img["src"]
img_res = requests.get(imgUrl)
with open("w0512/melon_chart1.jpg", "wb") as f:
    f.write(img_res.content)
    
print(tds[6].find("a").get_text().strip())

cnt = tds[7].find("span", {"class":"cnt"}).get_text().strip()[3:].strip()   # [3:] -> 총건수 3글자 제외
### 천단위 표시 제거, int 타입으로 변경
print(int(cnt.replace(",", "")))

# rank = trs[0].find("div", {"class":"wrap t_center"})
# album = trs[0].find("div", {"class":"ellipsis rank03"})
# g = trs[0].find("span", {"class":"none"})
# print(rank.get_text().strip())
# print(album.get_text().strip())
# print(g.get_text().strip())
# print(g.next_sibling())


input("종료시 enter >>   ")     # 미작성 시 바로 종료됨



# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("window-size=1920x1080")
# options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64),\
#    Accept-Language: ko-KR,ko;q=0.9, Referer: https://www.coupang.com')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
# browser = webdriver.Chrome(options=options)
# browser.maximize_window()
# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
# browser.get(url)

# browser = webdriver.Chrome()
# browser.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")

# input("종료 시 엔터 >>   ")