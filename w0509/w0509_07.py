import requests
from bs4 import BeautifulSoup

# html 파일을 읽어와서 파일 html, css 형태로 파싱(변형)
with open("w0509/게시판3.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")
    
# html 태그 찾는 방법
# print(soup.thead)                   # 태그로 찾기 (해당 태그가 1개만 있을 때 사용)
# soup.find("thead", {"class":""})    # 태그와 속성 값으로 찾기

# # find() : 데이터 1개
# data = soup.find("thead")
# print(data)

# # find_all() : 데이터 여러개 (리스트 타입)
# ths = data.find_all("th")
# for th in ths:
#     print(th.get_text())
    
## find_next_sibling(s)() : 다음 형제 찾기 / find_previous_sibling(s)() : 이전 형제 찾기
# data = soup.find("div", {"id":"input"}).div
# data2 = data.find_next_sibling().find_next_sibling().find_previous_sibling()
# print(data2)

# data = soup.find("div", {"id":"input"})
# print(data.div.get_text())

# 자바스크립트를 읽을 수 없음 html문서만 가능
data = soup.find("tbody", {"id":"tbody"})
trs = data.find_all("tr")
print(trs)
print(len(trs))

for tr in trs:
    tds = tr.find_all("td")
    if len(tds) > 1:    # td가 1개인 것은 출력하지 말것
        for i in range(len(tds)-1):     # 0,1,2,3,4,5
            print(tds[i].get_text(), end="\t")
        print()