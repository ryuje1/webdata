import requests

## 사이트 접속해서 html 소스 가져옴
# res = requests.get("https://www.google.com/") # 접근 가능
# 파이썬에서 웹스크래핑 -> 웹 접근 제한을 진행
# 접근을 할 수 없음.
# res = requests.get("https://www.melon.com/")    # 접근 제한
res = requests.get("https://www.naver.com/")

if res.status_code == 200:
    print("정상적인 프로그램 진행")
    print(res)
    # 응답코드 200 - 정상코드 / 400-404 - 페이지 없음 또는 접근제한 / 500 - 프로그램 에러
    print("응답코드 :", res.status_code)
    res.raise_for_status()  # 에러 시 종료
    print(res.text)     # text 글자 타입으로 출력
else:
    print("프로그램 종료") 