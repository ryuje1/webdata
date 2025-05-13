import requests
from bs4 import BeautifulSoup

### fly1.html 불러오기
## 항공사, 출발시간, 도착시간, 편도금액 출력하시오.
with open("w0513/fly1.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")


data = soup.find("div", {"class":"domestic_flight_content__vYDHd"})
list = data.find_all("div", {"class":"domestic_Flight__8bR_b"})

d_list = []     # List 정렬
for i, l in enumerate(list):
    # 번호
    num = i+1
    print(num, end="\t")
    # 항공사
    airline = l.find("b", {"class":"airline_name__0Tw5w"}).get_text().strip()
    print(airline, end="\t")
    # 출발시간, 도착시간
    time = l.find_all("b", {"class":"route_time__xWu7a"})
    startTime = time[0].get_text().strip()
    endTime = time[1].get_text().strip()
    print(startTime, end="\t")
    print(endTime, end="\t")
    # 금액
    price = l.find("i", {"class":"domestic_num__ShOub"}).get_text().strip()
    print(price, end="\t")
    print()

    price = int(price.replace(",", ""))
    d_list.append([airline, startTime, endTime, price])
    
### 최저가 List 정렬
dd_list = sorted(d_list, key=lambda x:x[3])
print(dd_list)