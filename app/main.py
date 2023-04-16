import datetime
import sys
from PyQt5 import QtWidgets
from untitled import Ui_Dialog as Ui1
from Laborant_main_window import Ui_Dialog_2 as Ui2L
from Laborant_add_paccient import Ui_Laborant_add_paccient as Ui3L
from Laborant_barcode_window import Ui_Laborant_barcode as Ui4L
import psycopg2
from threading import Timer
from PyQt5.QtCore import QTimer
from cfg import *
# import pyglet


app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui1()
ui.setupUi(Dialog)
Dialog.show()
# mus = pyglet.resource.media("ballin.mp3")
# mus.play()


def open_barcode_add():
    global barcode_add
    barcode_add = QtWidgets.QDialog()
    ui4 = Ui4L()
    ui4.setupUi(barcode_add)
    open_window_barcode()
    ui4.pushButton_16.clicked.connect(lambda: return_window13414())
    ui4.pushButton_12.clicked.connect(lambda: podschet_hueti())
    ui4.pushButton_13.clicked.connect(lambda: podschet_huinu())
    ui4.pushButton_14.clicked.connect(lambda: huynaaa())
    ui4.lineEdit.setText('')

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


    cur = connection.cursor()
    cur.execute(f"SELECT order_id FROM public.orders;")
    Check = cur.fetchall()
    ui4.label_15.setText(f'')
    ui4.lineEdit.setText('')
    ui4.label_20.close()

    def podschet_hueti():
        try:
            hueta_polnaya = int(ui4.lineEdit.text())
        except:
            hueta_polnaya = ''
            ui4.label_20.show()
            ui4.label_20.setText('Фигня')
        if hueta_polnaya == '' or hueta_polnaya == 0:
            ui4.label_20.show()
            ui4.label_20.setText('Фигня')
        else:
            ui4.label_20.setText('Нормас')
            cur.execute(f"SELECT order_id FROM public.orders WHERE order_id = {hueta_polnaya}")
            Hui = cur.fetchall()
            try:
                if str(Hui[0][0]) == str(hueta_polnaya):
                    timer2 = Timer(3.00, ui4.label_20.close)
                    timer2.start()
                    ui4.label_20.show()
                    ui4.label_20.setText('Занято')

            except:
                datahui = f'{hueta_polnaya}{datetime.date.today().day}0{datetime.date.today().month}{datetime.date.today().year}{Check[-1][0] + int(hueta_polnaya) * 1231}'
                if int(datahui) > 10000000000000:
                    datahui = str(datahui)[:13]
                ui4.lineEdit.setText(f'{datahui}')
                ui4.label_15.setText(f'{datahui}')

    def podschet_huinu():
        datahui = f'{datetime.date.today().day + datetime.datetime.now().second * 35}0{datetime.date.today().month + datetime.datetime.now().second * 12}{datetime.date.today().year + datetime.datetime.now().second * 17}{Check[-1][0] + datetime.datetime.now().second * 1231}'
        if int(datahui) > 10000000000000:
            datahui = str(datahui)[:13]
        ui4.lineEdit.setText(f'{datahui}')
        ui4.label_15.setText(f'{datahui}')

    def huynaaa():
        global qr_code
        qr_code = int(ui4.label_15.text())
        ui2.label_23.setText(str(qr_code))
        return_window13414()



def open_paccient_add():
    global paccient_add
    paccient_add = QtWidgets.QDialog()
    ui3 = Ui3L()
    ui3.setupUi(paccient_add)
    return_window2()
    ui3.pushButton_14.clicked.connect(lambda: return_window3())
    ui3.pushButton_13.clicked.connect(lambda: ui3.data_insert())

def return_window13414():
    barcode_add.close()
    OtherDialog.show()

def open_window_barcode():
    OtherDialog.close()
    barcode_add.show()

def return_window3():
    paccient_add.close()
    OtherDialog.show()

def return_window4():
    paccient_add.hide()


def return_window2():
    OtherDialog.close()
    paccient_add.show()
def open_window():
    global OtherDialog
    OtherDialog = QtWidgets.QDialog()
    global ui2
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
        barcode_add.hide()
        return_window4()

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
    ui2.pushButton_12.clicked.connect(lambda: open_barcode_add())

ui.pushButton.pressed.connect(lambda: open_window())


sys.exit(app.exec_())

