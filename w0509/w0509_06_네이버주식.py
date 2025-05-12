import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()      # 에러 시 종료
soup = BeautifulSoup(res.text, "lxml")

print(soup.title)
data = soup.find("div", {"class":"box_type_l"})
trs = data.tbody.find_all("tr")
# print(trs[10])

# 6-10
# i = 5
# for i in range(10):
#     print(trs[i])

# 50개 이름만 출력
# trs[1].find_all("td")[1].find("a")
# for tr in trs:
#     print(tr.get_text()) 