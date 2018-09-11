# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jump-1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication

from PyQt5.QtWidgets import QApplication


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(245, 170)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.changeClick)
        # self.pushButton.clicked.connect(QCoreApplication.instance().quit)

    # QtCore.QMetaObject.connectSlotsByName(Form)

    def changeClick(self):
        sender = self.sender()
        print(sender.text() + ' 被按下了')
        qApp = QApplication.instance()
        qApp.quit()
        Form.jump2

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

