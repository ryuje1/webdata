import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

### selenium
# 1. 네이버 접속
# 2. 뉴스 클릭
# 3. 12개의 뉴스를 출력하시오.
# 뉴스 제목, 내용 출력 후 뒤로가기

# url = "https://news.naver.com/main/ranking/popularDay.naver"
# browser.get(url)


# def newsSearch(nXpath):
#     # 1. 뉴스클릭
#     time.sleep(1)
#     browser.find_element(By.XPATH, nXpath).click()

#     # 2. 웹 스크래핑 시작
#     soup = BeautifulSoup(browser.page_source, "lxml")
#     data = soup.find("div", {"class":"media_end_head_title"})
    
#     # 3. 뉴스 제목 출력
#     title = data.find("span").get_text().strip()
#     print(title)
    
#     # 4. 뉴스 내용 출력
#     newssct = soup.find("article", {"id":"dic_area"})
#     print(newssct.get_text().strip())
#     print("-"*50)
#     time.sleep(1)
    
#     # 뒤로 가기
#     browser.back()

# for i in range(1, 13):
#     nXpath = f'//*[@id="wrap"]/div[4]/div[2]/div/div[{i}]/ul/li[1]/div'
#     newsSearch(nXpath)
    

# ### 날씨 정보
url = "https://weather.naver.com/"
browser.get(url)
time.sleep(1)

soup = BeautifulSoup(browser.page_source, 'lxml')

# 오늘날씨 - 기온 구름많음 최저온도 최고온도
# # 오늘 날짜
# print(soup.find("span", {"class":"card_value_date"}).get_text().strip())
# # 오늘 현재온도
# tTemp = soup.find("strong", {"class":"card_now_temperature"}).get_text().strip()
# print("현재 온도 :", tTemp)
# # 오늘 현재날씨
# tWeather = soup.find("em", {"class":"card_date_emphasis"}).get_text().strip()
# print("현재 날씨 :", tWeather)
# # 오늘 최저온도 최고온도
# hw = soup.find("div", {"class":"card_detail_temperature"}).find_all("dl")
# print(hw[0].get_text().strip())
# print(hw[1].get_text().strip())

ul = soup.find("ul", {"class":"box_color"})
lis = ul.find_all("li")
txt = ""

for li in lis:
    date = li.find("span", {"class":"date"}).get_text().strip()[:-1]
    print(date)
    txt += "["+date+"] "
    weathers = ul.find_all("span", {"class":"weather_inner"})
    for w in weathers:
        am = w.find("span", {"class":"timeslot"}).get_text().strip()            # 오전, 오후
        tWeather = w.find("span", {"class":"weather_text"}).get_text().strip()  # 맑음, 흐림
        print(am, end='  ')
        txt += am+":"
        print(tWeather)
        txt += tWeather+","
print(txt)


input("프로그램 종료 시 Enter키   ")