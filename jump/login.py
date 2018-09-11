import urllib.error, urllib.request, urllib.parse
import http.cookiejar

LOGIN_URL = 'https://www.alipay.com/'
#get_url为使用cookie所登陆的网址，该网址必须先登录才可
get_url = 'https://my.alipay.com/portal/i.htm?referer=https%3A%2F%2Fauth.alipay.com%2Flogin%2FhomeB.htm%3FredirectType%3Dparent'
values = dict(ALIPAYJSESSIONID='RZ25HTfo7ooYEf7eulIQtdkPOtT0hCauthRZ12GZ00', CLUB_ALIPAY_COM='2088912759778331',
              LoginForm='alipay_login_home', UM_distinctid='162f6c3f05148c-000ad5dd2a4196-454c092b-1fa400-162f6c3f052880',
              ali_apache_tracktmp="\"uid=2088912759778331\"", alipay="K1iSL1Da55J5RQ6I+DnVqNYHGCkmGiiEP4eT+wuWa1sSMsAo",
              cna="utmnEshgiBMCAWpyWiHw6Rj4", credibleMobileSendTime="-1",
              ctoken="IJBHQTGWNb_YxIsd", ctuMobileSendTime="-1", userid="\"K1iSL1Da55J5RQ6I+DnVqA==\"",
              mobileSendTime="-1",riskCredibleMobileSendTime="-1",riskMobileAccoutSendTime="-1",
              riskMobileBankSendTime="-1",riskMobileCreditSendTime="-1",riskOriginalAccountMobileSendTime="-1",
              rtk="pMTloWIiI45Oi6ee3MORaRakSrO/gEPgGhwhUO7aw/euS6EjUTu",cookieNameId="ALIPAYJSESSIONID",umt="Lfa694ba84e36883d10d1791faa4cf3d5",
              zone="GZ00C")
postdata = urllib.parse.urlencode(values).encode()
user_agent = r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36' \
             r' (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
#将cookie保存在本地，并命名为cookie.txt
cookie_filename = 'cookie.txt'
cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie_aff)
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(LOGIN_URL, postdata, headers)
try:
    response = opener.open(request)
except urllib.error.URLError as e:
    print(e.reason)

cookie_aff.save(ignore_discard=True, ignore_expires=True)

for item in cookie_aff:
    print('Name ='+ item.name)
    print('Value ='+ item.value)
#使用cookie登陆get_url
get_request = urllib.request.Request(get_url,headers=headers)
get_response = opener.open(get_request)

print(get_response.read().decode())