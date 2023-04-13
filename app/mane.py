import sys  # Необходимо для завершения программы без происшествий, см. ласт строчку кода
from PyQt5 import QtWidgets, QtGui  # Основные классы из библиотеки
from window_ui.untitled import Ui_Dialog  # Импорт окна из QT designer файла

# Стандартный кусок кода, в котором создаем класс окна и наследуем его от класса QtWidgets.QMainWindow
# __init__ необходимо для передачи аргументов, если такие есть, и эта функция выполняется сразу при обьявлении класса
class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Medic')

        icon = QtGui.QIcon("img/1.png")
        self.setWindowIcon(icon)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Interface()
    win.resize(1000, 600)
    win.show()
    sys.exit(app.exec_())

