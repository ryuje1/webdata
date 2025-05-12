import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
# 쿠팡 접근 헤더
headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
   "Accept-Language": "ko-KR,ko;q=0.9",
   "Referer": "https://www.coupang.com/",
}
res = requests.get(url, headers=headers)
res.raise_for_status()          # 에러 시 종료
soup = BeautifulSoup(res.text, "lxml")

with open("w0512/coupang1.html", "w", encoding="utf-8-sig", newline="") as f:
    f.write(soup.prettify())

print("파일 저장 완료")