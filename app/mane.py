import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from window_ui.untitled import Ui_Dialog


class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        # Присоединение окна
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Interface()
    win.setFixedSize(1000, 600)
    win.show()
    sys.exit(app.exec_())
