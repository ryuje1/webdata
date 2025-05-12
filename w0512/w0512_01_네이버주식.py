# **중요 외우기

import requests
from bs4 import BeautifulSoup   # 파싱할때 사용
import csv

sum = 0     # 총 합계
### 파일 저장
ff = open("w0512/stock.csv", "a", encoding="utf-8-sig", newline="")
writer = csv.writer(ff)

for j in range(1, 6):
    url = f"https://finance.naver.com/sise/sise_market_sum.naver?&page={j}"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()          # 에러 시 종료

    # 파싱
    soup = BeautifulSoup(res.text, "lxml")
    data = soup.find("tbody")
    trs = data.find_all("tr")

    ### 상단 타이틀 저장 부분
    if j == 1:
        title = []
        tdata = soup.find("thead")
        ths = tdata.find_all("th")
        for th in ths[:-1]:
            title.append(th.get_text().strip())
        ## 파일저장
        writer.writerow(title)

    for tr in trs:
        tds = tr.find_all("td")
        contents = []
        if len(tds) <= 1: continue
        for i, td in enumerate(tds):
            if i == 12: break
            if i == 2:  # 현재가 합계 출력
                number = td.get_text().strip()
                contents.append(number)
                price = int(number.replace(",", ""))   # 천단위 표시 제거, 타입변경
                sum += price
                print(price, end="\t")
                continue
            if i == 3: 
                em1 = td.find("em").get_text().strip()
                span1 = td.find("span", {"class":"tah"}).get_text().strip()
                contents.append(em1+span1)
                print(em1+span1, end="\t")
                continue
            tcontent = td.get_text().strip()
            contents.append(tcontent)
            print(tcontent, end="\t")
        writer.writerow(contents)       # 내용 파일 저장
        print()

print(f"현재가 총 합계 : {sum:,d}")
ff.close()
print("프로그램을 종료합니다.")


# trs = data.find_all("tr")
# print(trs[1])
    
# td 여러개
# tds = trs[1].find_all("td")
# print(tds)

# 여러개일때 for문 사용
# for td in tds:
#     print(td.get_text().strip())
# print("-"*50)

# tds = trs[2].find_all("td")
# for td in tds:
#     print(td.get_text().strip())
# print("-"*50)


# data = soup.find("thead")
# print("-"*50)

# # 값이 있으면 출력, 없으면 None
# th1 = data.find("th")                   # 1. 1개 찾기
# ths = data.find_all("th")               # 2. 여러개 찾기 (리스트 타입)
# tr1 = data.find("th", {"class":"tr"})   # 3. 클래스 또는 아이디에 맞는 항목 찾기
# print(th1)
# print("-"*50)
# print(ths)
# print("-"*50)
# print(tr1.get_text())                   # get_text() : 태그 제외 글자만 출력
# print("-"*50)

