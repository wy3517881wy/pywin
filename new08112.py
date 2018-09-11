from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Login(object):
    def setupUi(self, MainWindow_Login):
        a = 2

    def retranslateUi(self, MainWindow_Login):
        a = 1


if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    login = Ui_MainWindow_Login()
    login.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())