from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from selenium import webdriver

import time, sqlite3
from selenium.webdriver.chrome.options import Options
from jump import caifutongUtill

N = 1
F_Login = 0
count = 0


def __init__(self):
    super().__init__()
    title = QLabel('用户名：', self)
    author = QLabel('密码：', self)

    self.titleEdit = QLineEdit(self)
    self.authorEdit = QLineEdit(self)
    reviewEdit = QPushButton('确定', self)

    title.move(80, 70)  # 左 上
    self.titleEdit.move(140, 70)
    author.move(80, 130)
    self.authorEdit.move(140, 130)
    reviewEdit.move(140, 190)

    self.authorEdit.setEchoMode(QLineEdit.Password)

    self.setGeometry(300, 300, 350, 300)
    self.setWindowTitle('登录')
    self.show()
    reviewEdit.clicked.connect(self.btnClickEvent)


def keep_safe(driver):
    try:
        F = 1
        while F:
            if F_Login == 1:
                QR_Code = driver.find_element_by_xpath('//*[@id="container"]/h2').text
                txt = '安全校验';[[]]
            else:
                QR_Code = driver.find_element_by_xpath('/html/body/div/div[1]/div/h1/a[2]').text  # 1
                txt = '登录'
            if QR_Code == txt:
                print(txt)
                print('请在15s内扫码')
                if txt == '安全校验':
                    time.sleep(15)
                    QR_Code_2 = driver.find_element_by_xpath('//*[@id="container"]/h2').text
                    if QR_Code_2 == QR_Code:
                        F = 1
                    else:
                        F = 0
                elif txt == '登录':
                    time.sleep(15)
                    QR_Code_2 = QR_Code = driver.find_element_by_xpath('/html/body/div/div[1]/div/h1/a[2]').text
                    if QR_Code_2 == QR_Code:
                        F = 1
                    else:
                        F = 0
    except:
        pass


def btnClickEvent(self, e):
    global F_Login
    # self.close()  # 然后窗口关闭
    # ali_num = '771331973@qq.com'  # 账号密码
    # ali_pad = ''  # 密码
    ali_num = self.titleEdit.text()  # 账号密码
    ali_pad = self.authorEdit.text()  # 密码
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='D:\chromedriver.exe', chrome_options=chrome_options)
    driver.get(
        "https://auth.alipay.com/login/index.htm?goto=https%3A%2F%2Fmy.alipay.com%2Fportal%2Fi.htm%3Freferer%3Dhttps%253A%252F%252Fauthet15.alipay.com%252Flogin%252FhomeB.htm")
    driver.find_element_by_xpath('//*[@id="J-loginMethod-tabs"]/li[2]').click()
    driver.find_element_by_xpath('//*[@id="J-input-user"]').clear()
    time.sleep(2)
    for i in ali_num:
        driver.find_element_by_xpath('//*[@id="J-input-user"]').send_keys(i)
        time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="password_rsainput"]').clear()
    driver.find_element_by_xpath('//*[@id="password_rsainput"]').click()
    for i in ali_pad:
        driver.find_element_by_xpath('//*[@id="password_rsainput"]').send_keys(i)
        time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="password_rsainput"]').text
    driver.find_element_by_xpath('//*[@id="J-login-btn"]').click()
    time.sleep(2)
    caifutongUtill.keep_safe(driver, F_Login)
    F_Login = 1
    driver.get('https://consumeprod.alipay.com/record/standard.htm')
    time.sleep(2)
    caifutongUtill.keep_safe(driver, F_Login)
    caifutongUtill.searchDriver(driver)

def getInfor(driver):
    global N
    for num in range(10):
        num = num + 1
        al_day_xpath = '//*[@id="trade_list_ul"]/li[' + str(num) + ']/div[1]'  # 创建时间
        al_time_xpath = '//*[@id="trade_list_ul"]/li[' + str(num) + ']/div[2]'  # 类型
        al_way_xpath = '//*[@id="trade_list_ul"]/li[' + str(num) + ']/div[3]'   # 交易单号
        al_payee_xpath = '//*[@id="trade_list_ul"]/li[' + str(num) + ']/div[4]'   # 交易对方
        al_snum_xpath = '//*[@id="trade_list_ul"]/li[' + str(num) + ']/div[5]'  # 收入
        al_figure_xpath = '//*[@id="trade_list_ul"]/li[' + str(num) + ']/div[6]'  # 支出
        al_status_xpath = '//*[@id="trade_list_ul"]/li[' + str(num) + ']/div[7]'  # 操作

        if isElementExist(driver, al_day_xpath):
            al_day = driver.find_element_by_xpath(al_day_xpath).text
            al_time = driver.find_element_by_xpath(al_time_xpath).text
            al_way = driver.find_element_by_xpath(al_way_xpath).text
            al_payee = driver.find_element_by_xpath(al_payee_xpath).text
            al_snum = driver.find_element_by_xpath(al_snum_xpath).get_attribute("title")
            al_figure = driver.find_element_by_xpath(al_figure_xpath).text
            al_status = driver.find_element_by_xpath(al_status_xpath).text
            conn = sqlite3.connect('caifutongDatabase.db')
            cursor = conn.cursor()

            cursor.execute(
                'create table if not exists records(recordid INTEGER PRIMARY KEY NOT NULL,createtime text,'
                'gender char(100),ordernum int(40),expend char(50),operation char(50),output char(50))')
            selectsql = "select sum(recordid) from records where ordernum = '" + al_way + "'"
            cursor.execute(selectsql)
            values = cursor.fetchall()
            if values[0][0] == None:
                sqlss = "insert into records (createtime,gender,ordernum,expend,operation,output)" \
                        " values('" + al_day + "','" + al_time + "','" + al_way + "','" + al_payee + "','" + al_snum + "','" + al_figure + "')"
                cursor.execute(sqlss)
            cursor.close()
            conn.commit()
            conn.close()
            print(str(N) + '.' + '创建时间' + ':' + al_day + '\t类型' + ':' + al_time + '\t交易单号' + ':' + al_way + '\t交易对方' + ':' + al_payee + '\t收入（元）' + ':' + al_snum + '\t支出（元）' + ':' + al_figure + '\t操作' + ':' + al_status)
            N = N + 1



driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
driver.get(
    "https://www.tenpay.com/v3/index.shtml?target=https%3A%2F%2Fwww.tenpay.com%2Fv3%2Ftrade%2Ftrade_details_list.shtml%3FADTAG%3Dtenpay_v3.trade.query.details")


def isElementExistBySelector(self, element):
    flag = True
    try:
        self.find_element_by_css_selector(element)
        return flag

    except Exception as e:
        flag = False
        return flag


def isElementExist(driver, element):
    flag = True
    try:
        driver.find_element_by_xpath(element)
        return flag
    except:
        flag = False
        return flag

def searchDriver():
    cnt = 0
    global count

    if count > 0:
        time.sleep(60)
    count = count + 1

    for i in range(8):
        time.sleep(1)
        flag = isElementExist(driver, '//*[@id="next"]/a[1]')
        if cnt == 1:
            if flag:
                cnt = cnt + 1
                print("存在1")
                js = "document.getElementById('next').click();"
                driver.execute_script(js)
                # elem = driver.find_element_by_xpath('//*[@id="next"]/a[1]')
                # elem.click()
            else:
                print("没有下一页1")
                break
        elif cnt == 0:
            cnt = cnt + 1
        else:
            if flag:
                print("存在2")
                js = "document.getElementById('trans_time_container').children[3].children[0].click();"
                driver.execute_script(js)
                break
            else:
                print("没有下一页2")
                break
        time.sleep(2)
        getInfor(driver)
#        keep_safe(driver)
    searchDriver()


searchDriver()
