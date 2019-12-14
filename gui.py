# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from AddPatientWindow import Ui_AddPatientWindow
from ChoosePatientWindow import Ui_ChoosePatientWindow


class Ui_Main(object):
    def AddPatientFun(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_AddPatientWindow()
        self.ui.setupUi(self.window)
        Main.hide()
        self.window.show()

    def ChoosePatientFun(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ChoosePatientWindow()
        self.ui.setupUi(self.window)
        Main.hide()
        self.window.show()

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.ChoosePatient = QtWidgets.QPushButton(self.centralwidget)
        self.ChoosePatient.setGeometry(QtCore.QRect(314, 186, 131, 61))
        self.ChoosePatient.setObjectName("ChoosePatient")

        self.ChoosePatient.clicked.connect(self.ChoosePatientFun)

        self.AddPatient = QtWidgets.QPushButton(self.centralwidget)
        self.AddPatient.setGeometry(QtCore.QRect(314, 266, 131, 61))
        self.AddPatient.setObjectName("AddPatient")

        self.AddPatient.clicked.connect(self.AddPatientFun)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.ChoosePatient.setText(_translate("Main", "Wybierz Pacjenta"))
        self.AddPatient.setText(_translate("Main", "Dodaj Pacjenta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
