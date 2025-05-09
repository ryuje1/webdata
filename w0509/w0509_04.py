import requests
from bs4 import BeautifulSoup

# url = "https://finance.naver.com/sise/sise_market_sum.naver"
url = "https://n.news.naver.com/article/011/0004483132?ntype=RANKING"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
with open("w0509/test3.html", "w", encoding="utf-8") as f:
    f.write(res.text)
res.raise_for_status()
# print(res.text)     # 문자열
# 문자열을 html, css으로 파싱(변경)
soup = BeautifulSoup(res.text,"lxml")
# print(soup)           # html, css 파일
# <title> 태그에 접근해서 가져옴
# print(soup.title)
# print(soup.title.get_text())
# print(soup.header)
# print(soup.header.div)
# print(soup.header.a)
## 태그ㄴ 속성을 출력
# print(soup.header.a.attrs)          # 속성의 전체 출력
# print(soup.header.a['href'])        # 해당 속성 값 1개 출력
# print(soup.header.a['class'])       # 해당 속성 값 1개 출력

## id, class 속성 출력
# find() : 해당 태그의 속성 값을 가지고 검색 가능

# data1 = soup.find("a", attrs={"class":"ofhd_float_back"})
# print(data1)
# data1 = soup.find("a", {"class":"ofhd_float_back"})
# print(data1)
# data1 = soup.find("a", class_= "ofhd_float_back")
# print(data1)

# data2 = soup.find("h2", attrs={"id":"title_area"})
# print(data2)
# print(data2.get_text())
# data2 = soup.find("h2", {"id":"title_area"})
# print(data2.get_text())
# data2 = soup.find("h2", id ="title_area")
# print(data2.get_text())


### find() : 1개만 검색 / find_all() : 복수 개를 검색
ul_data = soup.find("ul", {"class":"ranking_list"})
# li_data = ul_data.find("li", {"class":"rl_item"}) 
# print(li_data)
li_datas = ul_data.find_all("li", {"class":"rl_item"}) 
print(len(li_datas))    # 길이 출력 (갯수)
# print(li_datas[1])      # 2번째 항목 출력
# print(li_datas)         # 모두 출력 (리스트 형태)

for li_data in li_datas:    # 제목만 출력
    print(li_data.find("p", {"class":"rl_txt"}).get_text())