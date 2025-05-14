import smtplib
from email.mime.text import MIMEText

smtpName = "smtp.naver.com"             # smtp 서버명
smtpPort = 587                          # smtp 포트

sendEmail = "aaa"               # 아이디
# 중요 정보
recvEmail = "aaa@gmail.com"     # 받는사람 이메일주소
password = "1111"               # 네이버 로그인 비밀번호를 입력해도 되지만 파일이 노출 -> 어플리케이션 비밀번호 설정 가능
text = "날씨정보 오늘날씨:맑음, 내일날씨:흐리고 비"

msg = MIMEText(text)
msg['Subject'] = "웹스크래핑 이메일 보내기"
msg['From'] = "aaa@naver.com"   # 보내는 주소
msg['To'] = recvEmail                   # 받는주소

s = smtplib.SMTP("smtp.naver.com", 587)
s.starttls()
s.login("aaa@naver.com", password)
### 보내는 주소가 네이버 메일이 아니면 에러 처리
s.sendmail("aaa@naver.com", recvEmail, msg.as_string())   # 보내는사람, 받는사람
s.close()

print("메일발송 완료")