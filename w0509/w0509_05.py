import requests
from bs4 import BeautifulSoup

# url = ""
# headers = ""
# res = requests(url, headers=headers)
# soup = BeautifulSoup(res.text,"lxml")
with open("w0509/a.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")
    
# print(soup)
# print(soup.title)               # <title> 태그 포함 출력
# print(soup.title.get_text())    # 태그 제외 글자만 출력
# print(soup.h2)                  # h2 1개만 출력
# print(soup.find_all("h2"))      # h2 모두 출력
# print(soup.find("p", {"id":"p1"}).get_text())

# print(soup.find_all("ul")[1])
# print(soup.find("div", {"class":"c2"}).find("ul").find("li"))


print(soup.find("div", {"class":"c1"}).find("ul").find_all("li")[1].get_text())
print(soup.find("ul").find_all("li")[1].get_text())

datas = soup.find("ul").find_all("li")
for data in datas:
    print(data.get_text()) 