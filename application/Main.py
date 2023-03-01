from PyQt5 import QtCore, QtGui, QtWidgets
#import Invetory_list
#import DF_method

#import Invetory_list
#import DF_method

import methods.Invetory_list as Invetory_list
import methods.DF_method as DF_method

from methods import CreateQR
from prettytable import PrettyTable
import time
import os


'''

FAQ - информация

'''





'''

Удалить предмет из бд

'''

class Ui_Form_scr_4(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1118, 701)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("background-color: rgb(49, 49, 50);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 111, 61))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "border: 2px solid rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "border: 4px solid #A52A2A;\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "border: 4px solid #A52A2A;\n"
                                      "}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("methods/Group 3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(160, 160))
        self.pushButton.setShortcut("")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(590, 170, 201, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 450, 359, 64))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 2px solid rgb(255, 255, 255);\n"
                                        "border-radius: 15px;\n"
                                        "margin-top:10px;\n"
                                        "height: 50px;\n"
                                        "background-color: #778899;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: #2F4F4F;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color: #2F4F4F;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(340, 190, 201, 201))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 18px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 18px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.return_scr)
        self.pushButton_2.clicked.connect(self.del_val)


    def return_scr(self):
        MainWindow.show()
        Form_4.close()

    def del_val(self):
        try:
            data_start = DF_method.data.copy()

            DF_method.del_values(str(self.lineEdit_2.text()), int(self.lineEdit_3.text()))

            data_final = DF_method.data.copy()

            if data_start.equals(data_final) == False:
                dlg = QtWidgets.QMessageBox()
                dlg.setText(f'Предмет с инфентарником {str(self.lineEdit_2.text())} удалён в кабинете {self.lineEdit_3.text()}')
                correct_button = QtWidgets.QPushButton('Ок')
                dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
                dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
                button = dlg.exec()

            else:
                dlg = QtWidgets.QMessageBox()
                dlg.setText(f'Ошибка\nПредмет с инфентарником {str(self.lineEdit_2.text())} НЕ УДАЛЁН в кабинете {self.lineEdit_3.text()}'
                            f'\nПроверьте правильность написания кабинета и инвентарника')
                correct_button = QtWidgets.QPushButton('Ок')
                dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
                dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
                button = dlg.exec()
            print('Пися')

        except Exception as e:
            print(e)

            dlg = QtWidgets.QMessageBox()
            dlg.setWindowTitle("Ошибка!")
            dlg.setText('Ошибка в набранных значениях\nПроверьте правильность написания кабинета и инвентарника!')
            correct_button = QtWidgets.QPushButton('Ок')

            dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
            dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            button = dlg.exec()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "      инвентарник"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "      кабинет"))
        self.pushButton_2.setText(_translate("Form", "Удалить"))
        self.label_2.setText(_translate("Form", "Инвентарник"))
        self.label_4.setText(_translate("Form", "Кабинет"))




'''

Подвести итоги

'''

class to_sum_up:
    def __init__ (self, data, log_txt, last_duplicate, errors, comp_data, phone_data):
        self.data = data

        self.data = data
        self.log_txt = log_txt
        self.last_duplicate = last_duplicate
        self.errors = errors
        self.comp_data = comp_data
        self.phone_data = phone_data

    def check_count_cab(self, phone_line, comp_line):
        # проверяем, правильное ли количество
        if phone_line['count'].values[0] != comp_line['count'].values[0]:
            dlg = QtWidgets.QMessageBox()
            dlg.setWindowTitle("I have a question!")
            dlg.setText(
                f'В кабинете {phone_line["num_cab"].values[0]} неправильное количество предметов.\nДолжно быть:\n'
                  f'{comp_line}\nСейчас:\n{phone_line}\n\n' + 'Если вы выберете "исправлю", то нужно будет найти недостающие предметы или убрать лишние. '
                  'Если вы выберете "перезаписать бд", то теперь это число предметов актуально и общая бд перезапишется.')


            correct_button = QtWidgets.QPushButton('Исправлю')
            overwrite_button = QtWidgets.QPushButton('Перезаписать бд')

            dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
            dlg.addButton(overwrite_button, QtWidgets.QMessageBox.NoRole)
            dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            button = dlg.exec()


            if button == 0:
                self.log_txt.write(
                    f'Ошибка № {self.errors}.\nВ кабинете {phone_line["num_cab"].values[0]} неправильное количество предметов:\nДолжно быть:\n'
                    f'{comp_line}\nСейчас:\n{phone_line}\n\n\n')
                self.errors += 1
            else:
                # вызываем фукцию для замены количества в общей
                DF_method.update_count(phone_line['count'].values[0], comp_line['invent'].values[0],
                             comp_line['num_cab'].values[0])

        if phone_line['num_cab'].values[0] != comp_line['num_cab'].values[0]:

            dlg = QtWidgets.QMessageBox()
            dlg.setWindowTitle("I have a question!")
            dlg.setText(f'Найден неправильный кабинет.\nДолжно быть:\n{comp_line}\nСейчас:\n{phone_line}\n'+
                        'Если вы выберете "исправлю", перенести предмет/предметы на свое место. Если вы выберете\n'
                        ' "перезаписать бд", то кабинеты в общей базе данных перезапишутся на текущие.\n'
                        'Надо напечатать новый QrCode!!!')
            correct_button = QtWidgets.QPushButton('Исправлю')
            overwrite_button = QtWidgets.QPushButton('Перезаписать бд')

            dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
            dlg.addButton(overwrite_button, QtWidgets.QMessageBox.NoRole)
            dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            button = dlg.exec()


            if button == 0:
                self.log_txt.write(
                    f'Ошибка № {self.errors}.\nНайден неправильный кабинет.\nДолжно быть:\n{comp_line}\nСейчас:\n{phone_line}\n\n\n')
                self.errors += 1
            else:
                # обновляем кабинет в общей бд
                DF_method.update_cab(phone_line['num_cab'].values[0], comp_line['invent'].values[0],
                           comp_line['num_cab'].values[0])

    def sum_up(self):
        for invent in self.comp_data['invent']:
            if invent != self.last_duplicate:
                # найден ли элемент в локальной бд
                if self.phone_data.loc[self.phone_data['invent'] == invent].empty:

                    dlg = QtWidgets.QMessageBox()
                    dlg.setWindowTitle("I have a question!")
                    dlg.setText(f'На кафедре не обнаружен предмет:\n{self.comp_data.loc[self.comp_data["invent"] == invent]}\n'+
                                'Если вы выберете "исправлю", то нужно будет найти и принести предмет на кафедру.'
                                ' Если вы выберете "перезаписать бд", то предмет списан или утерян и теперь не числится на кафедре.'
                                )

                    correct_button = QtWidgets.QPushButton('Исправлю')
                    overwrite_button = QtWidgets.QPushButton('Перезаписать бд')

                    dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
                    dlg.addButton(overwrite_button, QtWidgets.QMessageBox.NoRole)
                    dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
                    button = dlg.exec()

                    if button == 0:
                        self.log_txt.write(
                            f'Ошибка № {self.errors}.\nНа кафедре не обнаружен предмет:\n{self.data.loc[self.data["invent"] == invent]}\n\n\n')
                        self.errors += 1
                    else:
                        # вызываем ф-ию для удаления из общей бд
                        DF_method.del_values(invent, self.comp_data.loc[self.comp_data['invent'] == invent]['num_cab'].values[0])
                else:
                    phone_slice = self.phone_data.loc[self.phone_data['invent'] == invent].sort_values(by='num_cab').reset_index(
                        drop=True)
                    comp_slice = self.comp_data.loc[self.comp_data['invent'] == invent].sort_values(by='num_cab').reset_index(
                        drop=True)
                    # одна ли строка с этим инвентарником
                    if len(phone_slice) == 1:
                        self.check_count_cab(phone_slice, comp_slice)
                    else:
                        for i, j in zip(phone_slice.index, comp_slice.index):
                            self.check_count_cab(phone_slice.iloc[[i]], comp_slice.iloc[[j]])
                        self.last_duplicate = invent

        if self.errors == 1:
            ui.flag = True
'''

Создать ведомость 

'''
class Ui_Form_scr_3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1118, 701)
        Form.setTabletTracking(False)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setStyleSheet("background-color: rgb(49, 49, 50);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 111, 61))
        self.pushButton.setStyleSheet('''QPushButton {
                                        border: 2px solid rgb(255, 255, 255);
                                        }
                                        QPushButton:hover {
                                           border: 4px solid #A52A2A;
                                        }
                                        QPushButton:pressed {
                                            border: 4px solid #A52A2A;
                                        }''')
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("methods/Group 3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(160, 160))
        self.pushButton.setShortcut("")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(380, 230, 361, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet('''QPushButton {
                                        color: rgb(255, 255, 255);
                                        border: 2px solid rgb(255, 255, 255);
                                        border-radius: 15px;
                                        margin-top:10px;
                                        height: 50px;
                                        background-color: #778899;
                                        }
                                        QPushButton:hover {
                                            background-color: #2F4F4F;
                                        }
                                        QPushButton:pressed {
                                            background-color: #2F4F4F;
                                        }''')
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.return_scr)
        self.pushButton_2.clicked.connect(self.creat_list)



    def return_scr(self):
        MainWindow.show()
        Form_3.close()


    def creat_list(self):
        try:
            inventory = Invetory_list.report()
            inventory.InputData(int(self.lineEdit.text()))
            dlg = QtWidgets.QMessageBox()
            dlg.setText(f'Ведомость для кабинета {self.lineEdit.text()} создана')
            correct_button = QtWidgets.QPushButton('Ок')

            dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
            dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            button = dlg.exec()

        except Exception as e:
            print('Это не номер кабинета', e)

            inventory = Invetory_list.report()
            inventory.InputData(int(self.lineEdit.text()))
            dlg = QtWidgets.QMessageBox()
            dlg.setText(f'Ошибка! Это не номер кабинета')
            correct_button = QtWidgets.QPushButton('Ок')

            dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
            dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            button = dlg.exec()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "      Номер кабинета"))
        self.pushButton_2.setText(_translate("Form", "Создать ведомость"))




'''

Создать QR 

'''
class Ui_Form_scr_2(object):  #инвертарник и кабинет
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1118, 701)
        Form.setStyleSheet("background-color: rgb(49, 49, 50);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 111, 61))
        self.pushButton.setStyleSheet('''QPushButton {
                                        border: 2px solid rgb(255, 255, 255);
                                        }
                                        QPushButton:hover {
                                           border: 4px solid #A52A2A;
                                        }
                                        QPushButton:pressed {
                                            border: 4px solid #A52A2A;
                                        }''')
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("methods/Group 3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(160, 160))
        self.pushButton.setShortcut("")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(440, 230, 131, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 470, 359, 64))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet('''QPushButton {
                                        color: rgb(255, 255, 255);
                                        border: 2px solid rgb(255, 255, 255);
                                        border-radius: 15px;
                                        margin-top:10px;
                                        height: 50px;
                                        background-color: #778899;
                                        }
                                        QPushButton:hover {
                                            background-color: #2F4F4F;
                                        }
                                        QPushButton:pressed {
                                            background-color: #2F4F4F;
                                        }''')
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(620, 210, 131, 211))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.return_scr)
        self.pushButton_2.clicked.connect(self.create_qr)

    def return_scr(self):
        MainWindow.show()
        #Form_1.close()
        Form_2.close()

    def create_qr(self):
        try:
            s_1 = self.lineEdit_3.text()
            s_2 = self.lineEdit_4.text()
            val_df = DF_method.find_invent(s_1, int(s_2))
            print(val_df)
            print(val_df)
            #CreateQR.createQrCode(s)
            #print((str(val_df[0][1]), str(val_df[0][0]), str(val_df[0][2])))
            if not list(val_df):
                dlg = QtWidgets.QMessageBox()
                dlg.setText('Такого предмета нет')
                correct_button = QtWidgets.QPushButton('Ок')
                dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
                dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
                button = dlg.exec()
            else:
                CreateQR.itog(str(val_df[0][1]), str(val_df[0][0]), str(val_df[0][2]))  #314_с001

                dlg = QtWidgets.QMessageBox()
                dlg.setText('Qr создан')
                correct_button = QtWidgets.QPushButton('Ок')
                dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
                dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
                button = dlg.exec()

        except Exception as e:
            print('Ошибка в создании ', e)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Инвентарник"))
        self.label_2.setText(_translate("Form", "Кабинет"))
        self.pushButton_2.setText(_translate("Form", "Создать"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "      инвентарник"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "      кабинет"))







'''

Создать QR и добавить в базу

'''
class Ui_Form_scr_1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1118, 701)
        Form.setStyleSheet("background-color: rgb(49, 49, 50);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 111, 61))
        self.pushButton.setStyleSheet('''QPushButton {
                                        border: 2px solid rgb(255, 255, 255);
                                        }
                                        QPushButton:hover {
                                           border: 4px solid #A52A2A;
                                        }
                                        QPushButton:pressed {
                                            border: 4px solid #A52A2A;
                                        }''')
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("methods/Group 3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(160, 160))
        self.pushButton.setShortcut("")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(570, 230, 171, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 460, 359, 64))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet('''QPushButton {
                                        color: rgb(255, 255, 255);
                                        border: 2px solid rgb(255, 255, 255);
                                        border-radius: 15px;
                                        margin-top:10px;
                                        height: 50px;
                                        background-color: #778899;
                                        }
                                        QPushButton:hover {
                                            background-color: #2F4F4F;
                                        }
                                        QPushButton:pressed {
                                            background-color: #2F4F4F;
                                        }''')
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(360, 230, 171, 211))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.return_scr)
        self.pushButton_2.clicked.connect(self.create_qr)

    def return_scr(self):
        MainWindow.show()
        Form_1.close()
        #Form_2.close()
        #print('hi')

    def create_qr(self):
        try:
            s_1 = self.lineEdit.text() #инвентарник
            s_2 = self.lineEdit_2.text() #название
            s_3 = self.lineEdit_3.text()  # кабинет
            s_4 = self.lineEdit_4.text()  # кол-во


            CreateQR.itog(s_2, s_1, s_3) #Номер Кабинета_Инвентарник, например 314_M001

            DF_method.append(s_1,s_2,int(s_3),int(s_4))

            dlg = QtWidgets.QMessageBox()
            dlg.setText('Данный добавлены и Qr создан')
            correct_button = QtWidgets.QPushButton('Ок')
            dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
            dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            button = dlg.exec()

        except Exception as e:
            print('Ошибка в добавлении и создании ', e)

            dlg = QtWidgets.QMessageBox()
            dlg.setText('Ошибка в данных, проверьте правильность написания')
            correct_button = QtWidgets.QPushButton('Ок')
            dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
            dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            button = dlg.exec()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "      номер"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "      название"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "      кабинет"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "      кол-во"))
        self.pushButton_2.setText(_translate("Form", "Создать"))
        self.label.setText(_translate("Form", "Инвентарник"))
        self.label_3.setText(_translate("Form", "Название"))
        self.label_4.setText(_translate("Form", "Кабинет"))
        self.label_2.setText(_translate("Form", "Количество"))


class Ui_MainWindow(object):

    flag = False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 700)
        MainWindow.setStyleSheet("background-color: rgb(49, 49, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(330, 40, 526, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet('''QPushButton {
                                        color: rgb(255, 255, 255);
                                        border: 2px solid rgb(255, 255, 255);
                                        border-radius: 15px;
                                        margin-top:10px;
                                        height: 50px;
                                        background-color: #778899;
                                        }
                                        QPushButton:hover {
                                            background-color: #2F4F4F;
                                        }
                                        QPushButton:pressed {
                                            background-color: #2F4F4F;
                                        }''')
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet('''QPushButton {
                                        color: rgb(255, 255, 255);
                                        border: 2px solid rgb(255, 255, 255);
                                        border-radius: 15px;
                                        margin-top:10px;
                                        height: 50px;
                                        background-color: #778899;
                                        }
                                        QPushButton:hover {
                                            background-color: #2F4F4F;
                                        }
                                        QPushButton:pressed {
                                            background-color: #2F4F4F;
                                        }''')
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet('''QPushButton {
                                        color: rgb(255, 255, 255);
                                        border: 2px solid rgb(255, 255, 255);
                                        border-radius: 15px;
                                        margin-top:10px;
                                        height: 50px;
                                        background-color: #778899;
                                        }
                                        QPushButton:hover {
                                            background-color: #2F4F4F;
                                        }
                                        QPushButton:pressed {
                                            background-color: #2F4F4F;
                                        }''')
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(
                                        '''QPushButton {
                                        color: rgb(255, 255, 255);
                                        border: 2px solid rgb(255, 255, 255);
                                        border-radius: 15px;
                                        margin-top:10px;
                                        height: 50px;
                                        background-color: #778899;
                                        }
                                        QPushButton:hover {
                                            background-color: #2F4F4F;
                                        }
                                        QPushButton:pressed {
                                            background-color: #2F4F4F;
                                        }''')
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(
                                        '''QPushButton {
                                        color: rgb(255, 255, 255);
                                        border: 2px solid rgb(255, 255, 255);
                                        border-radius: 15px;
                                        margin-top:10px;
                                        height: 50px;
                                        background-color: #778899;
                                        }
                                        QPushButton:hover {
                                            background-color: #2F4F4F;
                                        }
                                        QPushButton:pressed {
                                            background-color: #2F4F4F;
                                        }''')
        self.pushButton_6.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(1004, 10, 111, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(
                                        '''QPushButton {
                                        color: rgb(255, 255, 255);
                                        border: 2px solid rgb(255, 255, 255);
                                        border-radius: 15px;
                                        margin-top:10px;
                                        height: 50px;
                                        background-color: #778899;
                                        }
                                        QPushButton:hover {
                                            background-color: #2F4F4F;
                                        }
                                        QPushButton:pressed {
                                            background-color: #2F4F4F;
                                        }''')
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(330, 450, 531, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setStyleSheet('''QTextEdit{
                                        color: white;
                                        font-size: 18px;
                                                }''')
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)

        self.pushButton_2.clicked.connect(self.second_scr)
        self.pushButton.clicked.connect(self.third_scr)
        self.pushButton_5.clicked.connect(self.fourth_scr)
        self.pushButton_4.clicked.connect(self.start_check)
        self.pushButton_6.clicked.connect(self.del_value)
        self.pushButton_3.clicked.connect(self.faq)


    def second_scr(self):
        Form_1.show()
        MainWindow.close()

    def third_scr(self):
        Form_2.show()
        MainWindow.close()

    def fourth_scr(self):
        #print(self.textEdit.toPlainText())
        if self.flag == True:
            Form_3.show()
            MainWindow.close()
        else:
            self.textEdit.setText('Для начала необходимо подвести итоги и исправить все ошибки!')

    def start_check(self):
        self.textEdit.setText(' Дождитесь выполнения операции !!!!')

        errors = 1
        last_duplicate = ''
        log_txt = open('Логи\\log.txt', 'w')
        comp_data = DF_method.data.sort_values(by='invent').reset_index(drop=True)
        phone_data = DF_method.join_table('БД телефона')

        #print(phone_data.empty)

        if phone_data.empty:
            dlg = QtWidgets.QMessageBox()
            dlg.setText('Бд телефона пустая!')
            correct_button = QtWidgets.QPushButton('Ок')

            dlg.addButton(correct_button, QtWidgets.QMessageBox.YesRole)
            dlg.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            button = dlg.exec()

        else:
            cher = to_sum_up(DF_method.data, log_txt, last_duplicate, errors, comp_data, phone_data)
            cher.sum_up()

            self.textEdit.setText('')
            log_txt.close()

            log_txt = open('Логи\\log.txt', 'r')
            txt_line = ''
            for i in log_txt.readlines():
                txt_line += str(i)

            log_txt.close()

            result = time.gmtime(time.time())
            name_file = str(result.tm_year) + '_' + str(result.tm_mon) + '_' + str(result.tm_mday)

            full_db = open(f'Вывод БД с компьютера\\{name_file}.txt', 'w')

            newTable = PrettyTable(["Inventory", "Name", "Num_cab", "Count"])
            data_values = DF_method.data.values

            for row in data_values:
                newTable.add_row(row)

            full_db.write(newTable.get_string())
            full_db.close()

            if txt_line == '':
                self.textEdit.setText('Вывод окончательной БД сохранён в папке "Вывод БД с компьютера"')
            else:
                self.textEdit.setText(txt_line)

    def del_value(self):
        Form_4.show()
        MainWindow.close()

    def faq(self):
        os.startfile('methods\\FAQ.pdf')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Инвентаризация"))
        self.pushButton.setText(_translate("MainWindow", "Создать QR"))
        self.pushButton_2.setText(_translate("MainWindow", "Создать QR и добавить в базу"))
        self.pushButton_4.setText(_translate("MainWindow", "Подвести итоги"))
        self.pushButton_5.setText(_translate("MainWindow", "Сформировать ведомость"))
        self.pushButton_6.setText(_translate("MainWindow", "Удалить предмет из бд"))
        self.pushButton_3.setText(_translate("MainWindow", "FAQ"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #MainWindow.close()

    ''' Создать QR и добавить в базу '''
    Form_1 = QtWidgets.QWidget()
    ui_2 = Ui_Form_scr_1()
    ui_2.setupUi(Form_1)

    ''' Создать QR '''
    Form_2 = QtWidgets.QWidget()
    ui_3 = Ui_Form_scr_2()
    ui_3.setupUi(Form_2)

    ''' Создать ведомость '''
    Form_3 = QtWidgets.QWidget()
    ui_4 = Ui_Form_scr_3()
    ui_4.setupUi(Form_3)

    '''  Удалить предмет  '''
    Form_4 = QtWidgets.QWidget()
    ui_5 = Ui_Form_scr_4()
    ui_5.setupUi(Form_4)


    sys.exit(app.exec_())






