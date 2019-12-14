# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChoosePatientWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from patient import Ui_MainWindow


class Ui_ChoosePatientWindow(object):
    def click(self):
        pesel=self.peselInput.text()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        #ChoosePatientWindow.hide
        self.window.show()
        print(pesel)

    def setupUi(self, ChoosePatientWindow):
        ChoosePatientWindow.setObjectName("ChoosePatientWindow")
        ChoosePatientWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ChoosePatientWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(200, 150, 431, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.pesel = QtWidgets.QLabel(self.formLayoutWidget)
        self.pesel.setObjectName("pesel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pesel)
        self.peselInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.peselInput.setObjectName("peselInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.peselInput)
        self.chooseButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.chooseButton.setObjectName("chooseButton")
        self.chooseButton.clicked.connect(self.click)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chooseButton)
        ChoosePatientWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ChoosePatientWindow)
        self.statusbar.setObjectName("statusbar")
        ChoosePatientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChoosePatientWindow)
        QtCore.QMetaObject.connectSlotsByName(ChoosePatientWindow)

    def retranslateUi(self, ChoosePatientWindow):
        _translate = QtCore.QCoreApplication.translate
        ChoosePatientWindow.setWindowTitle(_translate("ChoosePatientWindow", "Wybierz Pacjenta"))
        self.pesel.setText(_translate("ChoosePatientWindow", "Pesel"))
        self.chooseButton.setText(_translate("ChoosePatientWindow", "Wybierz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChoosePatientWindow = QtWidgets.QMainWindow()
    ui = Ui_ChoosePatientWindow()
    ui.setupUi(ChoosePatientWindow)
    ChoosePatientWindow.show()
    sys.exit(app.exec_())
