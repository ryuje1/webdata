import requests
from bs4 import BeautifulSoup
import csv

# url = "https://search.daum.net/search?w=tot&q=2024%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
# # headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()          # 에러 시 종료
# print(res.text)

# # 파싱
# soup = BeautifulSoup(res.text, "lxml")

### 파일저장 (잘 안찾아지면 페이지 저장 후 태그 확인)
# with open("w0512/screen.html", "w", encoding="utf-8-sig", newline="") as f:
#     f.write(soup.prettify())

with open("w0512/screen.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")

data = soup.find("div", {"id":"morColl"})
# print(data)
data2 = data.find("c-flicking")
# print(data2)
data3 = data.find_all("c-doc")
# print(data3)

### 영화 30개 가져오기
badge = data3[0].find("c-badge-text")
title = data3[0].find("c-title")
content = data3[0].find("c-contents-desc")
sub = data3[0].find("c-contents-desc-sub")
print(badge.get_text())
print(title)
print(content)
print(sub)

# for dt in data3:
#     badge = dt.find("c-badge-text")
#     title = dt.find("c-title")
#     content = dt.find("c-contents-desc")
#     sub = dt.find("c-contents-desc-sub")
#     print(badge)
#     print(title)
#     print(content)
#     print(sub)