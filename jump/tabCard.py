from PyQt5.QtWidgets import *
from selenium import webdriver
from jump import ttt
import sys
import time


class TabDemo(QTabWidget):
    def __init__(self, parent=None):
        super(TabDemo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.addTab(self.tab4, "Tab 4")
        self.addTab(self.tab5, "Tab 5")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.setWindowTitle("布兜网络")
        self.setGeometry(600, 300, 550, 400)

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.setTabText(0, "监控中心")   # 也可以在addTab时进行修改
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        self.zhifubaotitleEdit = QLineEdit(self)
        self.zhifubaoauthorEdit = QLineEdit(self)
        self.zhifubaoauthorEdit.setEchoMode(QLineEdit.Password)
        layout.addRow("用户名", self.zhifubaotitleEdit)
        layout.addRow("密码", self.zhifubaoauthorEdit)
        zhifubaoreviewEdit = QPushButton('确定', self)
        zhifubaoreviewEdit.clicked.connect(self.zhifubaoBtnClickEvent)
        layout.addRow(zhifubaoreviewEdit)
        self.setTabText(1, "支付宝")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QFormLayout()
        self.caifutongtitleEdit = QLineEdit(self)
        self.caifutongauthorEdit = QLineEdit(self)
        self.caifutongauthorEdit.setEchoMode(QLineEdit.Password)
        layout.addRow("用户名", self.caifutongtitleEdit)
        layout.addRow("密码", self.caifutongauthorEdit)
        caifutongreviewEdit = QPushButton('确定', self)
        caifutongreviewEdit.clicked.connect(self.CaifutongBtnClickEvent)
        layout.addRow(caifutongreviewEdit)
        self.setTabText(2, "财付通")
        self.tab3.setLayout(layout)

    def tab4UI(self):
        layout = QFormLayout()
        layout.addRow("用户名", QLineEdit())
        layout.addRow("密码", QLineEdit())
        self.setTabText(3, "微信")  # 也可以在addTab时进行修改
        self.tab4.setLayout(layout)

    def tab5UI(self):
        layout = QFormLayout()
        layout.addRow("55", QLineEdit())
        layout.addRow("55", QLineEdit())
        self.setTabText(4, "充值记录")  # 也可以在addTab时进行修改
        self.tab5.setLayout(layout)

    def zhifubaoBtnClickEvent(self):
        global F_Login
        # self.close()  # 然后窗口关闭
        # ali_num = ''  # 账号密码
        # ali_pad = ''  # 密码
        ali_num = self.zhifubaotitleEdit.text()  # 账号密码
        ali_pad = self.zhifubaoauthorEdit.text()  # 密码
        driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
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
        ttt.keep_safe(driver, F_Login)
        F_Login = 1
        driver.get('https://consumeprod.alipay.com/record/standard.htm')
        time.sleep(2)
        ttt.keep_safe(driver, F_Login)
        ttt.searchDriver(driver)

    def CaifutongBtnClickEvent(self):
        global F_Login
        # self.close()  # 然后窗口关闭
        # ali_num = ''  # 账号密码
        # ali_pad = ''  # 密码
        ali_num = self.caifutongtitleEdit.text()  # 账号密码
        ali_pad = self.caifutongauthorEdit.text()  # 密码
        driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
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
        ttt.keep_safe(driver, F_Login)
        F_Login = 1
        driver.get('https://consumeprod.alipay.com/record/standard.htm')
        time.sleep(2)
        ttt.keep_safe(driver, F_Login)
        ttt.searchDriver(driver)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec_())