from selenium import webdriver
import time


url = 'http://www.kfc.com.cn/kfccda/storelist/index.aspx'
#driver = webdriver.PhantomJS(executable_path='/home/guowei/bin/phantomjs/bin/phantomjs')
driver = webdriver.PhantomJS('D://phantomjs-2.1.1-windows//bin//phantomjs.exe')
driver.get(url)

time.sleep(2)

for i in range(1, 11):
    shopName_xpath = '//tr[' + str(i + 1) + ']/td[1]'
    shopAddress_xpath = '//tr[' + str(i + 1) + ']/td[2]'
    shopName = driver.find_element_by_css_selector('#listhtml').find_element_by_xpath(shopName_xpath).text
    shopAddress = driver.find_element_by_css_selector('#listhtml').find_element_by_xpath(shopAddress_xpath).text
    print(shopName)

    print(shopAddress)