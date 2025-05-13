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

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)

url = "https://nol.yanolja.com/"
browser.get(url)
time.sleep(2)

# 1. 호텔/리조트 클릭
# 2. 지역 선택 > 제주 > 서귀포시/모슬포 클릭
# 3. 날짜 > 체크인 6/7, 체크아웃 6/8 선택 후 적용하기 클릭
# 4. 스크롤 내리기
# 5. 호텔, 호텔이름, 평점(없으면 없음 출력), 후기(개수), 금액 출력하시오.

# 1. 호텔/리조트 클릭
elem = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/button').click()
time.sleep(2)
elem = browser.find_element(By.XPATH, '/html/body/div[9]/div/div/aside/div/div[1]/div[2]/div[1]/button[1]').click()
time.sleep(2)
# 2. 지역 선택 > 제주 > 서귀포시/모슬포 클릭
elem = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/button').click()
time.sleep(2)
elem = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[1]/button[3]').click()
time.sleep(1)
elem = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/a[2]').click()
time.sleep(2)
# 3. 날짜 > 체크인 6/7, 체크아웃 6/8 선택 후 적용하기 클릭
elem = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/header/div[2]/div/button[1]').click()
time.sleep(2)
elem = browser.find_element(By.XPATH, '//*[@id="day-picker-2025-06"]/div[2]/div[1]/div[7]/button').click()
time.sleep(1)
elem = browser.find_element(By.XPATH, '//*[@id="day-picker-2025-06"]/div[2]/div[2]/div[1]/button').click()
time.sleep(1)
elem = browser.find_element(By.XPATH, '//*[@id="pc-dialog-sheet"]/div/div/div[3]/button').click()
time.sleep(2)
# 4. 스크롤 내리기
# 출력대기
time.sleep(5)

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height: break
    prev_height = curr_height
print("스크롤 종료")


## 웹스크래핑
soup = BeautifulSoup(browser.page_source, "lxml")
datas = soup.find_all("div", {"class":"flex w-full max-w-legacy-pc-size flex-col bg-static-white pc:px-16 [&>*:first-child]:border-t-0 pc:[&>:first-child]:mt-20"})
for dt in datas:
    data = dt.find("a", {"class":"flex w-full min-w-[320px] flex-col p-16 pc:w-1/2"})
    print(data.find("p", {"class":"text-text-neutral-sub typography-body-12-regular"}).get_text().strip())
    print(data.find("p", {"class":"mb-4 line-clamp-2 text-start text-fill-neutral-main typography-subtitle-16-bold"}).get_text().strip())


input("Enter키 누르면 종료   ")