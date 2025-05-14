import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time
import random


# 웹스크래핑 - BeautifulSoup

# html 파일 읽어오기
with open("w0514/ya1.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")
# print(soup.prettify())

data = soup.find("div", {"class":"mb-[calc(76px+env(safe-area-inset-bottom))]"})
a_list = data.find_all("a")
print("검색 개수 :", len(a_list))

for i, a in enumerate(a_list):
    # 평점이 4.1 미만 제외, 평가 수 500 미만 제외
    ### 평점 - 있는 경우 평점 출력 / 없는 경우 0 출력
    rank = a.find("span", {"class":"typography-body-14-bold"})
    rank = rank.get_text().strip()
    # 숫자인지 확인
    if rank not in "후기": rank = float(rank)
    else: rank = 0

    rating = a.find("span", {"class":"typography-body-14-bold"}).next_sibling.next_sibling.get_text().strip().replace(",", "")
    rating = int(rating[1:-1])  # 슬라이싱 - 앞뒤 1글자 제거
    
    if rank < 4.1 or rating < 500:
        continue
    print(i+1, end="\t")
    
    
    # 번호 출력
    num = i+1
    print(num, end="\t")
    
    # 제목 출력
    title = a.find("p", {"class":"mb-4"}).get_text().strip()
    print(title, end="\t")
    
    # 평점 출력
    print(rank, end="\t")
    
    # 평가수 출력
    print(rating, end="\t")
    
    price = a.find("span", {"class":"shrink-0"})
    if price != None:
        price = price.get_text().strip().replace(",", "")
        price = int(price)
        print(price)
    else: print("예약마감")
    
    print("-"*30)
print("*** 출력 완료 ***")