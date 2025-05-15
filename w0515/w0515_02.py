import requests

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#### 임시 패스워드 : aaa1111
### 본인 + onulee@naver.com


## 메일 발송
# 중요 부분
recvMail = "fbwodms2004@naver.com"      # 받는사람 주소
password = "414W4CPQKXS1"

## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분
# 보낼 내용 (html 문구 포함 가능)
# html img 보낼때 ../a.jpg 로 하면 이미지 안뜸
text = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ko" xml:lang="ko">
<head>
<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<title> 비밀번호 발송 </title>


</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" style="margin:0; padding:0; font:normal 12px/1.5 돋움;">


<table width="700" cellpadding="0" cellspacing="0" align="center">
<tr>
	<td style="width:700px;height:175px;padding:0;margin:0;vertical-align:top;font-size:0;line-height:0;">
		<img src="https://mail.naver.com/read/image/original/?mimeSN=1747272990.405754.173.63232&offset=1767&size=4808542&u=fbwodms2004&cid=2fde3c72f7e9b824bc4a7e1ffd5895b0@cweb007.nm&contentType=image/jpeg&filename=1747272951432.jpeg&org=1" alt="JARDIN" />					
	</td>
</tr>
<tr>
	<td style="width:700px;height:78px;padding:0;margin:0;vertical-align:top;">
		<p style="width:620px;margin:50px 0 40px 38px;text-align:center;font-size:0;line-height:0;"><img src="https://mail.naver.com/read/image/original/?mimeSN=1747273016.964446.174.50944&offset=1916&size=4805124&u=fbwodms2004&cid=58738e6857577f54223185446fe9f@cweb005.nm&contentType=image/jpeg&filename=1747273002330.jpeg&org=1" alt="원두커피의 名家, JARDIN 임시 비밀번호가 발급되었습니다." /></p>
	</td>
</tr>
<tr>
	<td style="width:700px;height:196px;padding:0;margin:0;vertical-align:top;">
		<table width="618" height="194" cellpadding="0" cellspacing="0" align="center" style="margin:0 0 0 40px;border:1px #d9d9d9 solid;">
		<tr>
			<td style="width:618px;height:194px;padding:0;margin:0;vertical-align:top;font-size:0;line-height:0;background:#f9f9f9;">
				<p style="width:620px;margin:30px 0 0 0;padding:0;text-align:center;"><img src="https://mail.naver.com/read/image/original/?mimeSN=1747273016.964446.174.50944&offset=4807337&size=4766834&u=fbwodms2004&cid=7ae2c8196dc4113335fc8bb9dbae6af3@cweb018.nm&contentType=image/jpeg&filename=1747273006145.jpeg&org=1" alt="JARDIN에서 비밀번호 찾기를 요청하셨습니다." /></p>
				<p style="width:620px;margin:10px 0 0 0;padding:0;text-align:center;color:#888888;font-size:12px;line-height:1;">아래의 PASSWORD는 임시 PASSWORD이므로 홈페이지 로그인 후 다시 수정해 주십시오.</p>
				<p style="width:620px;margin:28px 0 0 0;padding:0;text-align:center;color:#666666;font-size:12px;line-height:1;"><strong>임시 패스워드 : <span style="color:#f7703c;line-height:1;">aaa111</span></strong></p>
				<p style="width:620px;margin:30px 0 0 0;padding:0;text-align:center;color:#888888;font-size:12px;line-height:1.4;">쟈뎅샵에서는 고객님께 보다 나은 서비스를 제공하기 위해 항상 노력하고 있습니다.<br/>앞으로 많은 관심 부탁드립니다.</p>
			</td>
		</tr>
		</table>	
	</td>
</tr>
<tr>
	<td style="width:700px;height:120px;padding:0;margin:0;vertical-align:top;">
		<p style="width:700px;margin:30px 0 50px 0;text-align:center;"><a href="#"><img src="https://mail.naver.com/read/image/original/?mimeSN=1747272990.405754.173.63232&offset=4810603&size=4769776&u=fbwodms2004&cid=9e7488531521c67956a38d282ab53@cweb016.nm&contentType=image/jpeg&filename=1747272975334.jpeg&org=1" alt="JARDIN 바로가기" /></a></p>
	</td>
</tr>
<tr>
	<td style="width:700px;height:50px;padding:0;vertical-align:top;font-size:0;line-height:0;text-align:center;">
		<img src="https://mail.naver.com/read/image/original/?mimeSN=1747273016.964446.174.50944&offset=9574466&size=4757162&u=fbwodms2004&cid=7135b652761d6b4c5575e84325dee5@cweb005.nm&contentType=image/jpeg&filename=1747273013704.jpeg&org=1" alt="" />
	</td>
</tr>
<tr>
	<td style="width:700px;height:140px;padding:0;margin:0;vertical-align:top;background-color:#5a524c;">
		<p style="width:620px;margin:20px 0 0 40px;padding:0;text-align:center;line-height:1.5;color:#b2aeac;">메일수신을 원치 않으시는 분은 로그인 후. <span style="color:#ffffff">메일 수신 여부</span>를 변경해주시기 바랍니다.<br/>IF YOU DO NOT WISH TO RECEIVE EMAILS FROM US, PLEASE LOG-IN AND UPDATE<br/> YOUR MEMBERSHIP INFORMATION.</p>

		<p style="width:620px;margin:15px 0 0 40px;padding:0;text-align:center;line-height:1.5;color:#b2aeac;"><span style="color:#ffffff">본 메일에 관한 문의사항은 사이트 내 고객센터를 이용해주시기 바랍니다.</span><br/>COPYRIGHT ©  2014 JARDIN ALL RIGHTS RESERVED.</p>
	</td>
</tr>
</table>



</div>
</body>
</html>
"""
part2 = MIMEText(text, "html")          # html 포함 시 "html" 적어야 함
msg.attach(part2)
msg['From'] = "fbwodms2004@naver.com"                   # 보내는 사람
msg['To'] = recvMail                            # 받는 사람
msg['Subject'] = "임시비밀번호 발급"    # 제목

# ## 파일첨부 부분 ##
# part = MIMEBase('application', "octet-stream")
# ## 파일읽어오기
# with open('w0515/news.csv', "rb") as f:
#     # part 담기
#     part.set_payload(f.read())
    
# # 파일 첨부할 수 있는 형태로 인코딩
# encoders.encode_base64(part)        # 바이너리를 문자화해서 보냄
# ## header 정보
# part.add_header('Content-Disposition', 'attachment', filename='news.csv')
# msg.attach(part)


## 메일 발송 부분 ##
s = smtplib.SMTP("smtp.naver.com", 587)
s.starttls()
s.login("fbwodms2004", password)
### 보내는 주소가 네이버 메일이 아니면 에러 처리
recvMails = ['fbwodms2004@naver.com', 'onulee@naver.com']
for recvMail in recvMails:
    s.sendmail("fbwodms2004@naver.com", recvMail, msg.as_string())   # 보내는사람, 받는사람
s.close()
print("메일 발송 완료")