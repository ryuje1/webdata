import requests

# url = "https://finance.naver.com/sise/sise_market_sum.naver"
url = "https://n.news.naver.com/article/011/0004483132?ntype=RANKING"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
with open("w0509/test3.html", "w", encoding="utf-8") as f:
    f.write(res.text)
res.raise_for_status()
print(res.text) 