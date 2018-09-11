# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

# try:
#     _fromUtf8 = QtCore.QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s):
#         return s
#
# try:
#     _encoding = QApplication.UnicodeUTF8
#
#
#     def _translate(context, text, disambig):
#         return QApplication.translate(context, text, disambig, _encoding)
# except AttributeError:
#     def _translate(context, text, disambig):
#         return QApplication.translate(context, text, disambig)


class Dialog1(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.form = Dialog
        self.label = QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 50, 54, 12))
        self.label.setObjectName("label")
        self.dialog1_pushButton = QPushButton(Dialog)
        self.dialog1_pushButton.setGeometry(QtCore.QRect(160, 130, 75, 23))
        self.dialog1_pushButton.setObjectName("pushButton")

        Dialog.setWindowTitle("WindowTitle")
        self.label.setText("内容")
        self.dialog1_pushButton.setText("返回主窗体")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 信号连接到指定槽
        self.dialog1_pushButton.clicked.connect(self.on_dialog1_pushButton_clicked)


    def on_dialog1_pushButton_clicked(self):
        self.form.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

