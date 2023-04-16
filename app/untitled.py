# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from threading import Timer
from cfg import *
import psycopg2
from Laborant_main_window import Ui_Dialog_2 as UiL

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(365, 40, 270, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(73, 140, 81);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 270, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 310, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(330, 230, 170, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 270, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 310, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 400, 600, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 440, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 180, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(73, 140, 81);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setLineWidth(5)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(550, 270, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_2.close()
        self.label_3.close()

        self.pushButton.pressed.connect(lambda: log(self))

        self.time_error = 0

        def log(self):
            connection = False

            try:
                connection = psycopg2.connect(
                    host=host,
                    user=user,
                    database=db_name,
                    password=password
                )

            except Exception as _ex:
                print("[ИНФО] Ошибка при работе с PostrgeSQL", _ex)

            self.user_login = self.lineEdit.text()
            self.user_password = self.lineEdit_2.text()

            if len(self.user_login) == 0:
                return

            if len(self.user_password) == 0:
                return

            cur = connection.cursor()
            cur.execute(f"SELECT login FROM public.users WHERE login = '{self.user_login}'")
            check_login = cur.fetchone()
            cur.execute(f"SELECT password FROM public.users WHERE login = '{self.user_login}'")
            check_pass = cur.fetchone()


            try:
                if str(check_pass[0]) == str(self.user_password) and str(check_login[0]) == str(self.user_login):
                    Dialog.close()
                    ui2 = UiL()
                    ui2.setupUi(Dialog=Dialog)
                    Dialog.show()

            except Exception as _ex:
                if self.time_error != 2:
                    self.time_error += 1
                    self.label_2.setText("Неверные данные для авторизации")
                    self.label_2.show()
                    timer = Timer(3.00, self.label_2.close)
                    self.label_3.close()
                    timer.start()
                elif self.time_error == 2:
                    self.label_2.setText("Вы ввели не верные данные, блокировка на 10 сек.")
                    self.label_2.show()
                    self.label_3.show()
                    timer = Timer(10.00, self.label_2.close)
                    timer.start()
                    self.time_error = 0
                else:
                    self.time_error += 1
                    print(_ex)
                    self.label_2.setText("Неверные данные для авторизации")
                    self.label_2.show()
                    timer = Timer(3.00, self.label_2.close)
                    timer.start()




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Авторизация"))
        self.pushButton.setText(_translate("Dialog", "Войти"))
        self.pushButton_2.setText(_translate("Dialog", "*"))
        self.pushButton_3.setText(_translate("Dialog", "Заменить каптчу"))
        self.lineEdit.setText(_translate("Dialog", "chacking0"))
        self.lineEdit_2.setText(_translate("Dialog", "4tzqHdkqzo4"))
        self.lineEdit_3.setText(_translate("Dialog", "Капча"))
        self.label_2.setText(_translate("Dialog", "Вы ввели не правильные данные"))
        self.label_3.setText(_translate("Dialog", "10 сек."))
        self.label_5.setText(_translate("Dialog", "Показать пароль"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
