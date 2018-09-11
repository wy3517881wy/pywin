from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='D:\chromedriver.exe', chrome_options=chrome_options)
driver.get("https://auth.alipay.com/login/index.htm")

sss = driver.find_element_by_class_name("authcenter-body-login")
# html = driver.page_source   #获取整个页面的html代码
InnerElement = sss.get_attribute('innerHTML')  #获取某个元素里面的html代码
print(InnerElement)
# 无头浏览器模式