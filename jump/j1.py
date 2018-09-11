# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jump-1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QLineEdit
from PyQt5 import QtCore, QtWidgets
from functools import partial
from jump.j2dialog import Ui_Dialog
from PyQt5.QtCore import QCoreApplication


class Ui_Form(object):
    def setupUi(self, Form):

        qle = QLineEdit(self)
        qle.move(60, 100)

        Form.setObjectName("Form")
        Form.resize(245, 170)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        #self.pushButton.clicked.connect(Form.jump2)
        #self.pushButton.clicked.connect(lambda: self.changeClick(Form))
        self.pushButton.clicked.connect(partial(self.changeClick, Form, qle))
        #self.pushButton.clicked.connect(Form.close)



    def changeClick(self, ff, app):
        qApp = QApplication.instance()
        qApp.closeAllWindows()

        print(app.text())

        m2 = W2(app)
        m2.show()
        m2.exec_()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

class W2(QtWidgets.QDialog, Ui_Dialog,app):
    def __init__(self):
        super().__init__()
        self.setupUi(self)