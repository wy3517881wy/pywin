# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication,QMessageBox,QLCDNumber, QSlider , QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a <b>QWidge212132132121321</b> widget')
        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b style="color:red;font-size:20px;">QPushButton</b> widget')
        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())
        # 移动窗口的位置
        btn.move(100, 100)

        # 创建一个PushButton并为他设置一个tooltip
        qbtn = QPushButton('close Panel', self)
        qbtn.setToolTip('This is a <b style="color:red;font-size:20px;">delete this</b> widget')
        # btn.sizeHint()显示默认尺寸
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        # 移动窗口的位置
        btn.move(200, 100)

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(500, 300, 600, 500)
        self.setWindowTitle('Tooltips')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'title',
                                     "确定关闭?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())