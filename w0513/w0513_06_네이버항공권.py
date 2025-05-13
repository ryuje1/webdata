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

# 네이버 항공권 페이지 접속
url = "https://flight.naver.com/"
browser.get(url)

# 브라우저를 여는 동안 시간이 걸리는데 열리기 전에 선택을 찾으려고 하니까 없어서 에러 발생
time.sleep(2)

### 2. 팝업창 닫기
elem = browser.find_element(By.CLASS_NAME, 'FullscreenPopup_close').click()
# elem = browser.find_element(By.XPATH, '//*[@id="layer"]/button[2]')
# browser.find_element(By.XPATH, '//*[@id="layer"]/button[2]').click()
time.sleep(2)

# 3. 출발지 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]').click()
time.sleep(2)

# 4. 김포 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button').click()
time.sleep(2)

# 5. 도착지 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(2)

# 6. 제주 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button').click()
time.sleep(2)

# 7. 가는날 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)

# 8. 출발 날짜 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[7]/button').click()
time.sleep(2)

# 9. 도착 날짜 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[1]/button').click()
time.sleep(2)

# 10. 항공권 검색 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button').click()
time.sleep(2)

# 11. 항공권 출력할때까지 대기
# 검색버튼 클릭 후 화면이 나타날때까지 대기 (길게는 10초까지 대기)
# WebDriverWait(browser,10).until(EC.presence_of_all_elements_located(By.XPATH, '//*[@id="__next"]/div/main/div[4]/div/div[2]/div[2]/div[1]'))
time.sleep(7)

### 스크롤 내리기
# 현재 사이트 높이를 가져오는 자바스크립트
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 실행
while True:
    # 현재 브라우저의 0에서 현재 높이까지(끝까지) 스크롤 내리기
    # 스크립트 실행
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    # 변동된 현재 문서 높이 가져오기
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 이전 높이와 비교해서 스크롤 높이가 변동이 없을 시 반복문 빠져나옴
    if curr_height == prev_height: break
    prev_height = curr_height   # 현재 높이를 다시 입력해서 스크롤 내리기 재실행
print("스크롤 내리기 종료")

### 웹스크래핑
soup = BeautifulSoup(browser.page_source, "lxml")

## 셀레니움으로 항공사, 출발시간, 도착시간, 편도금액 출력하시오.
data = soup.find("div", {"class":"domestic_flight_content__vYDHd"})
list = data.find_all("div", {"class":"domestic_Flight__8bR_b"})

for i, l in enumerate(list):
    print(i+1, end="\t")
    print(l.find("b", {"class":"airline_name__0Tw5w"}).get_text().strip(), end="\t")
    time = l.find_all("b", {"class":"route_time__xWu7a"})
    print(time[0].get_text().strip(), end="\t")
    print(time[1].get_text().strip(), end="\t")
    print(l.find("i", {"class":"domestic_num__ShOub"}).get_text().strip())


### html 파일 저장
# with open("w0513/fly1.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify())

# print("파일 저장 완료")


### 프로그램 종료
input("프로그램 종료 (Enter키)   ")