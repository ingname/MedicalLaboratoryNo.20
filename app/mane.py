import sys  # Необходимо для завершения программы без происшествий, см. ласт строчку кода
from PyQt5 import QtWidgets, QtGui  # Основные классы из библиотеки
from untitled import Ui_Dialog # Импорт окна из QT designer файла

from PyQt5 import QtCore

# Стандартный кусок кода, в котором создаем класс окна и наследуем его от класса QtWidgets.QMainWindow
# __init__ необходимо для передачи аргументов, если такие есть, и эта функция выполняется сразу при обьявлении класса
class Interface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Interface, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Medic')


        icon = QtGui.QIcon("img/1.png")
        self.setWindowIcon(icon)


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=None):
        super(MyTableModel, self).__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0])

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self._data[row][col]
            return str(value)
        return None
class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=None):
        super(MyTableModel, self).__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0])

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self._data[row][col]
            return str(value)
        return None

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Interface()
    win.resize(1011, 637)
    win.show()
    sys.exit(app.exec_())

