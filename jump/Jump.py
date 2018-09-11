import sys
from PyQt5 import QtWidgets
from jump.j1 import Ui_Form
from jump.j1 import Ui_Form as u2
from jump.j2dialog import Ui_Dialog

class Mywindow(QtWidgets.QWidget, Ui_Form):

    def jump2(self):
        print("kkkk")
        m2 = W2()
        m2.show()
        m2.exec_()
        print("zzzzz")

    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Window2(QtWidgets.QWidget, u2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class W2(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Mywindow()
    main.show()
    sys.exit(app.exec_())
