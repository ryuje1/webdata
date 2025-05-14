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

# 네이버 항공권 페이지 접속
url = "https://www.naver.com/"
browser.get(url)

elem = browser.find_element(By.ID, 'query')     # input창
elem.send_keys("시가 총액")                      # input창에 글자 입력
elem.send_keys(Keys.ENTER)                      # Enter키 입력

elem = browser.find_element(By.XPATH, '//*[@id="main_pack"]/section[1]/div/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[1]/th/a')
elem.click()

# 탭 변경
browser.switch_to.window(browser.window_handles[0])     # 첫번째 탭으로 변경
browser.get("https://www.naver.com")

### 프로그램 종료
input("프로그램 종료 시 (Enter키)   ")