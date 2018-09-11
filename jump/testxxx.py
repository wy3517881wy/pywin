from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.uic.properties import QtWidgets

from selenium import webdriver
import sys, time, sqlite3

from jump import ttt


class MyWindow(QWidget):
    global F_Login
    global N
    global count
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


    # def closeEvent(self, e):
    #     reply = QMessageBox.question(self, 'title',
    #                                  "确定关闭?", QMessageBox.Yes |
    #                                  QMessageBox.No, QMessageBox.No)
    #
    #     if reply == QMessageBox.Yes:
    #         e.accept()
    #     else:
    #         e.ignore()

    def btnClickEvent(self, e):
        global F_Login
        # self.close()  # 然后窗口关闭
        # ali_num = '771331973@qq.com'  # 账号密码
        # ali_pad = ''  # 密码
        ali_num = self.titleEdit.text()  # 账号密码
        ali_pad = self.authorEdit.text()  # 密码
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
    ex = MyWindow()
    sys.exit(app.exec_())