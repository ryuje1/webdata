import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

## 중요 부분
recvMail = "aaa@naver.com"      # 받는사람 주소
password = "1111"

## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분
text = "이메일 글자 발송"
part2 = MIMEText(text)
msg.attach(part2)
msg['From'] = "aaa@naver.com"
msg['To'] = recvMail
msg['Subject'] = "시가총액 250개 주식정보를 보냅니다."

## 파일첨부 부분 ##
part = MIMEBase('application', "octet-stream")
## 파일읽어오기
with open('w0514/stock.csv', "rb") as f:
    # part 담기
    part.set_payload(f.read())
    
# 파일 첨부할 수 있는 형태로 인코딩
encoders.encode_base64(part)        # 바이너리를 문자화해서 보냄
## header 정보
part.add_header('Content-Disposition', 'attachment', filename='stock.csv')
msg.attach(part)


## 메일 발송 부분 ##
s = smtplib.SMTP("smtp.naver.com", 587)
s.starttls()
s.login("aaa", password)
### 보내는 주소가 네이버 메일이 아니면 에러 처리
recvMails = ['aaa@naver.com', 'aaa@gmail.com']
for recvMail in recvMails:
    s.sendmail("aaa@naver.com", recvMail, msg.as_string())   # 보내는사람, 받는사람
s.close()
print("메일 발송 완료")