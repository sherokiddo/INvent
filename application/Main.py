
from PyQt5 import QtCore, QtGui, QtWidgets
#from methods.Invetory_list import report
import methods.Invetory_list as Invetory_list
import methods.SQL_method as SQL_method
import CreateQR

'''

FAQ - информация

'''





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
        self.pushButton.setStyleSheet("border: 2px solid rgb(255, 255, 255);\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI_file/Group 3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"margin-top:10px;\n"
"height: 50px;")
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
            inventory.InputData(self.lineEdit.text())
        except Exception as e:
            print('Это не номер кабинета', e)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "      Номер кабинета"))
        self.pushButton_2.setText(_translate("Form", "Создать ведомость"))




'''

Создать QR 

'''
class Ui_Form_scr_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Scr_2")
        Form.resize(1118, 701)
        Form.setStyleSheet("background-color: rgb(49, 49, 50);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 111, 61))
        self.pushButton.setStyleSheet("border: 2px solid rgb(255, 255, 255);\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI_file/Group 3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(160, 160))
        self.pushButton.setShortcut("")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(380, 230, 361, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"margin-top:10px;\n"
"height: 50px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)

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
            s = self.lineEdit.text()
            CreateQR.createQrCode(s)

        except Exception as e:
            print('Ошибка в создании ', e)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "      инвентарник"))
        self.pushButton_2.setText(_translate("Form", "Создать"))







'''

Создать QR и добавить в базу

'''
class Ui_Form_scr_1(object):
    def setupUi(self, Form):
        Form.setObjectName("Scr_1")
        Form.resize(1118, 701)
        Form.setStyleSheet("background-color: rgb(49, 49, 50);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 111, 61))
        self.pushButton.setStyleSheet("border: 2px solid rgb(255, 255, 255);\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI_file/Group 3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(160, 160))
        self.pushButton.setShortcut("")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(380, 230, 361, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"margin-top:10px;\n"
"height: 50px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)

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
            s = self.lineEdit.text()
            s = s.split(', ')
            CreateQR.createQrCode(s[0])

            SQL_method.Append(s[0],s[1],int(s[2]), int(s[3]))

        except Exception as e:
            print('Ошибка в добавлении и создании ', e)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "      номер, название, кабинет, кол-во"))
        self.pushButton_2.setText(_translate("Form", "Создать"))







class Ui_MainWindow(object):
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
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"margin-top:10px;\n"
"height: 50px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"margin-top:10px;\n"
"height: 50px;")
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"margin-top:10px;\n"
"height: 50px;")
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"margin-top:10px;\n"
"height: 50px;")
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
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
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"margin-top:10px;\n"
"height: 50px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(330, 450, 531, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setStyleSheet("color: white;\n"
"")
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

    def second_scr(self):
        Form_1.show()
        MainWindow.close()

    def third_scr(self):
        Form_2.show()
        MainWindow.close()

    def fourth_scr(self):
        Form_3.show()
        MainWindow.close()




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Инвентаризация"))
        self.pushButton.setText(_translate("MainWindow", "Создать QR"))
        self.pushButton_2.setText(_translate("MainWindow", "Создать QR и добавить в базу"))
        self.pushButton_4.setText(_translate("MainWindow", "Подвести итоги"))
        self.pushButton_5.setText(_translate("MainWindow", "Сформировать ведомость"))
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


    sys.exit(app.exec_())


