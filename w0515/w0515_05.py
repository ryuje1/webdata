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
from datetime import datetime

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

#### 네이버 항공권
# 김포, 제주 5/31 - 6/1
# 출발 비행기표 금액 90,000 이하 제외
# 김포 출발시간 17:00 이후 제외


url = "https://flight.naver.com/"
browser.get(url)
time.sleep(2)

# 팝업 닫기
elem = browser.find_element(By.XPATH, '//*[@id="layer"]/button[2]').click()
time.sleep(1)

# 출발지 김포 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]').click()
time.sleep(1)
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button').click()
time.sleep(1)

# 도착지 제주 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(1)
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button').click()
time.sleep(1)

# 가는날 5/31 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[5]/td[7]/button').click()
time.sleep(1)

# 오는날 6/4 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[4]/button').click()
time.sleep(1)

# 검색하기 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button').click()
time.sleep(5)

# 스크롤 내리기
pre_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == pre_height: break
    pre_height = curr_height


soup = BeautifulSoup(browser.page_source, 'lxml')
data = soup.find("div", {"class":"domestic_results__gp5WB"})
list = data.find_all("div", {"class":"domestic_Flight__8bR_b"})

for i, l in enumerate(list):
    # 순번
    num = i+1
    # 항공사 이름
    airline = l.find("b", {"class":"airline_name__0Tw5w"}).get_text().strip()
    # 출발시간
    f_time = l.find_all("b", {"class":"route_time__xWu7a"})     # 06:15
    startTime = f_time[0].get_text().strip()
    sh = int((startTime.split(":"))[0])
    sm = int((startTime.split(":"))[1])
    standard_time = datetime(2025,5,31,17,00,00)
    now_time = datetime(2025,5,31,sh,sm,00)
    # 도착시간
    endTime = f_time[1].get_text().strip()
    # 금액
    price = l.find("i", {"class":"domestic_num__ShOub"}).get_text().strip().replace(",", "")
    price = int(price)
    
    ## 조건 : 110,000 이상이거나 출발 시간이 17:00 이후면 제외 대상
    if price >= 140000 or standard_time<now_time: continue
    
    print(num, end="\t")
    print(airline, end="\t")
    print(startTime, end="\t")
    print(endTime, end="\t")
    print(price)
    print("-"*50)
 
 
input("종료 시 Enter   ")