# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from EditPatientWindow import Ui_EditPatientWindow
from AddOrder import Ui_AddOrder
from PrintOrder import Ui_PrintOrder



class Ui_MainWindow(object):
    def edit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EditPatientWindow()
        self.ui.setupUi(self.window)
        #MainWindow.hide()
        self.window.show()
    def add(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddOrder()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()
    def print(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PrintOrder()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 70, 571, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.printButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.printButton.setObjectName("printButton")
        self.printButton.clicked.connect(self.print)
        self.gridLayout.addWidget(self.printButton, 8, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.addOrderButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addOrderButton.setObjectName("addOrderButton")
        self.addOrderButton.clicked.connect(self.add)
        self.gridLayout.addWidget(self.addOrderButton, 5, 0, 1, 3)
        self.lastN = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lastN.setObjectName("lastN")
        self.gridLayout.addWidget(self.lastN, 0, 2, 1, 1)
        self.firstN = QtWidgets.QLabel(self.gridLayoutWidget)
        self.firstN.setObjectName("firstN")
        self.gridLayout.addWidget(self.firstN, 0, 1, 1, 1)
        self.editPatientButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.editPatientButton.setObjectName("editPatientButton")
        self.editPatientButton.clicked.connect(self.edit)
        self.gridLayout.addWidget(self.editPatientButton, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pacjent"))
        self.printButton.setText(_translate("MainWindow", "Drukuj wyniki"))
        self.label_3.setText(_translate("MainWindow", "Karta Pacjenta"))
        self.addOrderButton.setText(_translate("MainWindow", "Dodaj zamówienie"))
        self.lastN.setText(_translate("MainWindow", "Nazwisko"))
        self.firstN.setText(_translate("MainWindow", "Imię"))
        self.editPatientButton.setText(_translate("MainWindow", "Edytuj Pacjenta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
