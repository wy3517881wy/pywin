# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys


class MyWindow(QWidget):
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())

