# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests

id = 0
class Ui_MainWindow(object):
    def getOrdersFun(self):
        response = requests.get("http://localhost:8081/examinations/orderNumbers")
        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                self.orders.addItem(i)


    def getExamsFun(self):
        global id
        order_number = self.orders.currentText()
        url="http://localhost:8081/examinations/order/?orderNumber={}".format(order_number)
        response = requests.get(url)

        if response.status_code == 200:
            json = response.json()
            print(json)
            for i in json:
                id = i['id']
                examination_type = i['examinationType']
                self.exams.addItem(examination_type) # TO DO chyba tak jak teraz tyko dla większej ilosci



    def saveFun(self):
        global id
        examination_result_id = id
        patient_value=self.putResult.text()
        response = requests.put("http://localhost:8081/examinations/examination_result_id{}".format(examination_result_id))
        print(response.status_code)
        if response.status_code == 200:
            json = response.json()
            self.info.setText("Poprawnie zapisano wynik")
        else:
            self.info.setText("Wystąpił błąd")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 801, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.getOrders = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.getOrders.setObjectName("getOrders")
        self.getOrders.clicked.connect(self.getOrdersFun)
        self.verticalLayout.addWidget(self.getOrders)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.orders = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.orders.setObjectName("orders")
        self.verticalLayout.addWidget(self.orders)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.getExams = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.getExams.setObjectName("getExams")
        self.getExams.clicked.connect(self.getExamsFun)
        self.verticalLayout.addWidget(self.getExams)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.exams = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.exams.setObjectName("exams")
        self.verticalLayout.addWidget(self.exams)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.putResult = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.putResult.setObjectName("putResult")
        self.verticalLayout.addWidget(self.putResult)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saveFun)
        self.verticalLayout.addWidget(self.save)
        self.info = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.info.setText("")
        self.info.setObjectName("info")
        self.verticalLayout.addWidget(self.info)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Laboratorium"))
        self.getOrders.setText(_translate("MainWindow", "Pobierz zamówienia"))
        self.getExams.setText(_translate("MainWindow", "Pobierz badania dla wybranego zamówienia"))
        self.putResult.setText(_translate("MainWindow", "Wpisz wartość badania"))
        self.save.setText(_translate("MainWindow", "Zapisz wynik"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())