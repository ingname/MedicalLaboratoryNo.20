import sys
from PyQt5 import QtWidgets
from untitled import Ui_Dialog as Ui1
from Laborant_main_window import Ui_Dialog_2 as Ui2L
from Laborant_add_paccient import Ui_Laborant_add_paccient as Ui3L
import psycopg2
from threading import Timer
from PyQt5.QtCore import QTimer
from cfg import *


app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui1()
ui.setupUi(Dialog)
Dialog.show()


def open_paccient_add():
    global paccient_add
    paccient_add = QtWidgets.QDialog()
    ui3 = Ui3L()
    ui3.setupUi(paccient_add)
    return_window2()
    ui3.pushButton_14.clicked.connect(lambda: return_window3())


def return_window3():
    paccient_add.close()
    OtherDialog.show()


def return_window2():
    OtherDialog.close()
    paccient_add.show()
def open_window():
    global OtherDialog
    OtherDialog = QtWidgets.QDialog()
    ui2 = Ui2L()
    ui2.setupUi(OtherDialog)

    def log():
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

        user_login = ui.lineEdit.text()
        user_password = ui.lineEdit_2.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        cur = connection.cursor()
        cur.execute(f"SELECT login FROM public.users WHERE login = '{user_login}'")
        check_login = cur.fetchone()
        cur.execute(f"SELECT password FROM public.users WHERE login = '{user_login}'")
        check_pass = cur.fetchone()

        try:
            if str(check_pass[0]) == str(user_password) and str(check_login[0]) == str(user_login):
                with open("data_user.txt", 'w') as f:
                    f.write(f"{str(user_login)}")
                with open("data_pass.txt", 'w') as f:
                    f.write(f"{str(user_password)}")

                ui2.insert()

                Dialog.close()
                OtherDialog.show()

            else:
                if ui.time_error != 2:
                    ui.time_error += 1
                    ui.label_2.setText("Неверные данные для авторизации")
                    ui.label_2.show()
                    timer2 = Timer(3.00, ui.label_2.close)
                    ui.label_3.close()
                    timer2.start()
                elif ui.time_error == 2:
                    ui.label_2.setText("Вы ввели не верные данные, блокировка на 10 сек.")
                    ui.label_2.show()
                    ui.label_3.show()
                    timer2 = Timer(10.00, ui.label_2.close)
                    timer2.start()
                    ui.time_error = 0
                else:
                    ui.time_error += 1
                    ui.label_2.setText("Неверные данные для авторизации")
                    ui.label_2.show()
                    timer2 = Timer(3.00, ui.label_2.close)
                    timer2.start()

        except Exception as _ex:
            ui.time_error += 1
            ui.label_2.setText("Неверные данные для авторизации")
            ui.label_2.show()
            timer2 = Timer(3.00, ui.label_2.close)
            timer2.start()
            print(_ex)
    log()

    def return_window():
        OtherDialog.close()
        Dialog.show()
        timers.disconnect()

    def timer():
        try:
            if ui2.now_m - 1 == 0 and ui2.now_s == 0:
                end_of_session()
                return False
            if ui2.now % 60 == 0:
                ui2.now_m = ui2.now / 60
                ui2.label_2.setText(f'{int(ui2.now_m - 1)}:{int(ui2.now_s)}')
                ui2.now2 = 59
            if ui2.now2 % 1 == 0:
                ui2.now_s = ui2.now2
                ui2.label_2.setText(f'{int(ui2.now_m - 1)}:{int(ui2.now_s)}')
                ui2.now2 -= 1
                ui2.now -= 1
            if ui2.now_s < 10:
                ui2.now_s = ui2.now2 + 1
                ui2.label_2.setText(f'{int(ui2.now_m - 1)}:0{int(ui2.now_s)}')
            if ui2.now_m <= 5:
                ui2.label_13.setText(f'Окончание сенса через: {int(ui2.now_m - 1)}:{int(ui2.now_s)}')
                if ui2.now_s < 10:
                    ui2.label_13.setText(f'Окончание сенса через: {int(ui2.now_m - 1)}:0{int(ui2.now_s)}')
                ui2.label_13.show()
        except:
            pass

    def end_of_session():
        timers.disconnect()
        ui.label_2.setText('Отдохните минуту')
        ui.label_2.show()
        ui.pushButton.hide()
        timer2 = Timer(5.00, huiny)
        timer2.start()
        return_window3()
        return_window()


    def huiny():
        ui.label_2.close()
        ui.pushButton.show()

    timer()
    timers = QTimer()
    timers.timeout.connect(timer)
    timers.start(1000)




    ui2.pushButton_8.clicked.connect(lambda: return_window())
    ui2.pushButton_10.clicked.connect(lambda: open_paccient_add())

ui.pushButton.pressed.connect(lambda: open_window())


sys.exit(app.exec_())

