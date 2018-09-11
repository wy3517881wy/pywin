#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
pyu40 PyQt5 tutorial

In this example, we reimplement an
event handler.

author: Jan Bodnar
website: py40.com
last edited: January 2015
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication, QLabel, QLineEdit,QPushButton,QMainWindow)

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.qle = QLineEdit(self)
        qbtn = QPushButton('clickBtn', self)
        qbtn.clicked.connect(self.buttonClicked)
        qbtn.resize(qbtn.sizeHint())
        self.qle.setText("sadasdsad")

        self.qle.move(60, 100)
        self.lbl.move(60, 40)
        self.statusBar()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()


    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        print(self.qle.text())
        # self.lbl.setText(self.lbl,"asdsadsad")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())