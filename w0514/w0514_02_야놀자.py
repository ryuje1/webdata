import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import random

# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)     # 설정했던 옵션들을 가지고 크롬 브라우저 실행
browser.maximize_window()                       # 창 최대화

### 1. 야놀자 페이지 접속
url = "https://nol.yanolja.com/"
browser.get(url)
time.sleep(2)

# 2. 팝업창 닫기
elem = browser.find_element(By.XPATH, '/html/body/div[10]/div/div/div/section/div[2]/button[2]').click()
time.sleep(1)

# 3. 호텔/리조트 선택
elem = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/a[11]').click()
time.sleep(1)

# 4. 지역 선택
elem = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div/div/button').click()     # 지역선택
time.sleep(1)
elem = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[1]/button[3]').click()     # 제주
time.sleep(1)
elem = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/a[2]').click()   # 서귀포시/모슬포
time.sleep(1)

# 5. 날짜 선택
elem = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/header/div[2]/div/button[1]').click()    # 날짜
time.sleep(1)
elem = browser.find_element(By.XPATH, '//*[@id="day-picker-2025-06"]/div[2]/div[1]/div[7]/button').click()          # 체크인 6/7
time.sleep(1)
elem = browser.find_element(By.XPATH, '//*[@id="day-picker-2025-06"]/div[2]/div[2]/div[1]/button').click()          # 체크아웃 6/8
time.sleep(1)
elem = browser.find_element(By.XPATH, '//*[@id="pc-dialog-sheet"]/div/div/div[3]/button').click()                   # 적용하기
time.sleep(1)

# 6. 스크롤 내리기
prev_height = browser.execute_script("return document.body.scrollHeight")   # 현재 높이

while True:     # 높이가 더이상 변경되지 않을때까지 무한반복
    # 스크롤 내리기 - 0에서 현재 높이까지
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    
    # 변경된 현재 높이 가져오기
    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    # 높이가 변경되었는지 확인
    if prev_height == curr_height: break
    
    prev_height = curr_height
print("스크롤 종료")


# ▲ Selenium
#---------------------------------------------------------
# ▼ BeautifulSoup


### html 파싱
soup = BeautifulSoup(browser.page_source, "lxml")
## BeautifulSoup 명령어 - find, find_all, next_sibling, previous_sibling, a[href]

# data = soup.find("div", {"class":"flex w-full max-w-legacy-pc-size flex-col bg-static-white pc:px-16 [&>*:first-child]:border-t-0 pc:[&>:first-child]:mt-20"})
# list = data.find_all("a")
# print(len(list))

data = soup.find("div", {"class":"mb-[calc(76px+env(safe-area-inset-bottom))]"})
a_list = data.find_all("a")
# print(a_list[0].find("p", {"class":"mb-4"}))
# print(len(a_list))

for a in a_list:
    title = a.find("p", {"class":"mb-4 line-clamp-2 text-start text-fill-neutral-main typography-subtitle-16-bold"}).get_text().strip()
    print(title)

    # rr = a.find("p", {"class":"flex items-center justify-start gap-2 pl-2"}).find_all("span")
    # rank = rr[0].get_text().strip()
    # rating = rr[1].get_text().strip()
    # print(rank, end="\t")
    # print(rating)
    
    # 평점
    rank = a.find("span", {"class":"typography-body-14-bold"}).get_text()   # 4.2 평점 없을 시 후기 출력
    if rank != "후기":
        rank = float(rank)
    print(rank, end="\t")   # 후기 str타입 / 4.2 float타입
    
    # 평가수
    rating = a.find("span", {"class":"typography-body-14-bold"}).next_sibling   # (10)
    if rating != None: 
        rating = rating.get_text().strip().replace(",", "")  # 평가수 (10)  str타입
        rating = int(rating[1:-1])                           # 10          int타입
        print(rating)                                        # 10

    price = a.find("span", {"class":"shrink-0"})
    if price != None: 
        price = price.get_text().strip().replace(",", "")   # 천단위 표시 제거
        price = int(price)
        print(price)
    else: print("예약마감")
    
    print("-"*50)
print("***출력완료***")


### 파일 저장
with open("w0514/ya1.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())    # html 파일 저장


### 프로그램 종료
input("프로그램 종료 시 Enter키   ")