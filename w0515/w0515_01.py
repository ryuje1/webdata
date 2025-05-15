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


# 신문사 기사
# 한국경제,"지금 계약해도 1년 기다려야 받는다"…인기 폭발한 車
# 파이낸셜뉴스, 머리에 다닥다닥 빨간 물집 생기더니..20대 男 머리 뭉텅이로 빠
# csv 파일 - 멀티메일 발송
# 제목 : 네이버 랭킹뉴스 보냄
# 내용 : 네이버 12개 랭킹 1위 뉴스를 보내드립니다.
# 보내는 주소 : onulee@naver.com

url = 'https://news.naver.com/main/ranking/popularDay.naver'
browser.get(url)

# html 파싱
soup = BeautifulSoup(browser.page_source, 'lxml')

data = soup.find("div", {"class":"rankingnews_box_wrap"})
rNews = data.find_all("div", {"class":"rankingnews_box"})
print(len(rNews))

f = open('w0515/news.csv', "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = ['언론사', '기사제목']
writer.writerow(title)          # csv 리스트 저장

for r in rNews:
    newsName = r.find("strong", {"class":"rankingnews_name"}).get_text().strip()
    print(newsName)
    
    newsContent = r.find("a", {"class":"list_title nclicks('RBP.rnknws')"}).get_text().strip()
    print(newsContent)
    
    writer.writerow([newsName, newsContent])

f.close()

# 파일 생성하는 동안 잠시 대기
time.sleep(2)



## 메일 발송
# 중요 부분
recvMail = "fbwodms2004@naver.com"      # 받는사람 주소
password = "414W4CPQKXS1"

## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분
# 보낼 내용 (html 문구 포함 가능)
# html img 보낼때 ../a.jpg 로 하면 이미지 안뜸
text = """<h2>랭킹뉴스 기사 모음</h2>
<img src='https://mail.naver.com/read/image/original/?mimeSN=1747271418.6918.169.5888&offset=1734&size=4808542&u=fbwodms2004&cid=56a837cffc228b17f4ec728e3415ceb@cweb017.nm&contentType=image/jpeg&filename=1747271405755.jpeg&org=1'>
"""
part2 = MIMEText(text, "html")          # html 포함 시 "html" 적어야 함
msg.attach(part2)
msg['From'] = "fbwodms2004@naver.com"                   # 보내는 사람
msg['To'] = recvMail                            # 받는 사람
msg['Subject'] = "언론사별 랭킹뉴스를 보냅니다."    # 제목

## 파일첨부 부분 ##
part = MIMEBase('application', "octet-stream")
## 파일읽어오기
with open('w0515/news.csv', "rb") as f:
    # part 담기
    part.set_payload(f.read())
    
# 파일 첨부할 수 있는 형태로 인코딩
encoders.encode_base64(part)        # 바이너리를 문자화해서 보냄
## header 정보
part.add_header('Content-Disposition', 'attachment', filename='news.csv')
msg.attach(part)


## 메일 발송 부분 ##
s = smtplib.SMTP("smtp.naver.com", 587)
s.starttls()
s.login("fbwodms2004", password)
### 보내는 주소가 네이버 메일이 아니면 에러 처리
s.sendmail("fbwodms2004@naver.com", recvMail, msg.as_string())   # 보내는사람, 받는사람
s.close()
print("메일 발송 완료")


input("종료 시 ENTER   ")