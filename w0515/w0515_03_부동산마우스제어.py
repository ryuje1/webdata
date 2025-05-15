# 웹스크래핑

# 1. request - find, find_all
# soup = Beautiful(res.text, 'lxml')

# 2. selenium - find_element(By. XPATH/ID/CLASS_NAME)
# soup = Beautiful(browser.page_source, 'lxml')


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import time
import csv
import random
import pyautogui        # 마우스 제어



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


url = 'https://new.land.naver.com/complexes/102737?ms=37.5373434,127.0100999,17&a=APT:PRE:ABYG:JGC&e=RETAIL'
browser.get(url)
time.sleep(1)

pyautogui.moveTo(50, 700)
time.sleep(1)

pre_height = browser.execute_script("return articleListArea.scrollHeight")
# print("처음 화면 높이 :", pre_height)
### 자바 스크립트의 스크롤 내리기를 사용해서 진행
browser.execute_script("window.scroll(0, articleListArea.scrollHeight)")
pyautogui.moveTo(50, 700)
time.sleep(2)
while True:
    pyautogui.scroll(-pre_height)       # 마우스 휠로 스크롤 내리기
    time.sleep(2)
    # 변화된 현재 높이
    curr_height = browser.execute_script("return articleListArea.scrollHeight")
    # print("변화된 현재 높이 :", curr_height)
    if curr_height == pre_height: break
    pre_height = curr_height

soup = BeautifulSoup(browser.page_source, 'lxml')
data = soup.find_all("div", {"class":"item_inner"})

### 30억 이하 전세만 출력하시오.

for dt in data:
    price = dt.find("div", {"class":"price_line"})
    price_type = price.find("span", {"class":"type"}).get_text().strip()
    price_line = price.find("span", {"class":"price"}).get_text().strip()

    p_line = price_line.split("억")
    price_line = int(p_line[0])
        
    if price_type == "전세" and price_line <= 30:
        # 상단 타이틀
        title = dt.find("span", {"class":"text"}).get_text().strip()
        print(title)
        # 가격 타입 - 전세, 월세, 매매
        print(price_type)
        # 가격 - 109억, 109 -> int타입으로 변경
        print(price_line)
        # 스펙 내용
        spec = dt.find("span", {"class":"spec"}).get_text().strip()
        print(spec)
    else: continue
    print("-"*50)

input("종료 시 Enter   ")