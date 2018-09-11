import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

# 登录后才能访问的网页
url = 'https://consumeprod.alipay.com/record/standard.htm'

# 浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'cna=utmnEshgiBMCAWpyWiHw6Rj4; mobileSendTime=-1; credibleMobileSendTime=-1; ctuMobileSendTime=-1; riskMobileBankSendTime=-1; riskMobileAccoutSendTime=-1; riskMobileCreditSendTime=-1; riskCredibleMobileSendTime=-1; riskOriginalAccountMobileSendTime=-1; 3FV_lastvisit=0%091524558456%09%2Fread.php%3Ftid%3D415%26fid%3D5; UM_distinctid=162f6c3f05148c-000ad5dd2a4196-454c092b-1fa400-162f6c3f052880; alipay=K1iSL1Da55J5RQ6I+DnVqNYHGCkmGiiEP4eT+wuWa1sSMsAo; CLUB_ALIPAY_COM=2088912759778331; iw.userid="K1iSL1Da55J5RQ6I+DnVqA=="; ali_apache_tracktmp="uid=2088912759778331"; session.cookieNameId=ALIPAYJSESSIONID; unicard1.vm="K1iSL1Da55J5RQ6I+DnVqA=="; ssl_upgrade=0; spanner=qFe30nWwhRNR4gOG7sVwzeLJksT59Om6; LoginForm=alipay_login_auth; ctoken=ETE3msoKBWRQJe_7; CHAIR_SESS=ZQrP5JQ6VA_3jRZ_q9ZvW4GblNwRgE1ZCpJrBbBJ-KWWF-b_Orzzq-nit74nWvd3c6oQ9mFdeLDIzf24zuKKtECVfPqxTinPFACWMXQoVgYiIxttgNQ8xsCngmhcLI8nvcARRC258jwJOQNAU6GRvA==; zone=GZ00C; ALIPAYJSESSIONID=RZ25OtixeYimrUlIhMD9seadUpe8teauthRZ11GZ00; rtk=bXBkX17jWlsep0rBLXPeV9qmHaBRNTZ+/UzUhBIozGT2BQ8ihe2'

# 把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

# 设置请求头
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# 在发送get请求时带上请求头和cookies
resp = requests.get(url, headers=headers, cookies=cookies)

print(resp.content.decode('utf-8'))