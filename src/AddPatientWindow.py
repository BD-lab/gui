# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddPatientWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from tokenize import String

from PyQt5 import QtCore, QtGui, QtWidgets
import requests


class Patient:
    id: int
    firstName: String
    lastName: String
    pesel: String
    streetName: String
    buildingNumber: String
    zipCode: String
    city: String

class Ui_AddPatientWindow(object):
    def click(self):
        firstName = self.firstNameInput.text()
        lastName = self.lastNameInput.text()
        pesel = self.peselInput.text()
        streetName = self.streetNameInput.text()
        buildingNumber = self.buildingNumberInput.text()
        zipCode = self.zipCodeInput.text()
        city = self.cityInput.text()

        response = requests.post("http://localhost:8080/patients", json={
            "firstName": firstName,
            "lastName": lastName,
            "pesel": pesel,
            "streetName": streetName,
            "buildingNumber": buildingNumber,
            "zipCode": zipCode,
            "city": city
        })
        if response.status_code == 200 :
            self.info.setText("Poprawnie dodano pacjenta")

        elif response.status_code == 201:
            self.info.setText("Poprawnie dodano pacjenta")

        elif response.status_code == 400:
            self.info.setText("Nieprawidłowy numer PESEL")

        elif response.status_code == 409:
            self.info.setText("Pacjent o podanym nr PESEL już istnieje")
        else:
            print(response.status_code)
            self.info.setText("Wystąpił błąd")
    def setupUi(self, AddPatientWindow):
        AddPatientWindow.setObjectName("AddPatientWindow")
        AddPatientWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AddPatientWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 611))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.firstName = QtWidgets.QLabel(self.formLayoutWidget)
        self.firstName.setObjectName("firstName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstName)
        self.firstNameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.firstNameInput.setObjectName("firstNameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameInput)
        self.lastName = QtWidgets.QLabel(self.formLayoutWidget)
        self.lastName.setObjectName("lastName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastName)
        self.lastNameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lastNameInput.setObjectName("lastNameInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastNameInput)
        self.pesel = QtWidgets.QLabel(self.formLayoutWidget)
        self.pesel.setObjectName("pesel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pesel)
        self.peselInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.peselInput.setObjectName("peselInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.peselInput)
        self.streetName = QtWidgets.QLabel(self.formLayoutWidget)
        self.streetName.setObjectName("streetName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.streetName)
        self.streetNameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.streetNameInput.setObjectName("streetNameInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.streetNameInput)
        self.buildingNumber = QtWidgets.QLabel(self.formLayoutWidget)
        self.buildingNumber.setObjectName("buildingNumber")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.buildingNumber)
        self.buildingNumberInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.buildingNumberInput.setObjectName("buildingNumberInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.buildingNumberInput)
        self.zipCode = QtWidgets.QLabel(self.formLayoutWidget)
        self.zipCode.setObjectName("zipCode")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.zipCode)
        self.zipCodeInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.zipCodeInput.setObjectName("zipCodeInput")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.zipCodeInput)
        self.city = QtWidgets.QLabel(self.formLayoutWidget)
        self.city.setObjectName("city")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.city)
        self.cityInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cityInput.setObjectName("cityInput")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cityInput)
        self.saveButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.saveButton)
        self.saveButton.clicked.connect(self.click)
        self.info = QtWidgets.QLabel(self.formLayoutWidget)
        self.info.setText("")
        self.info.setObjectName("info")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.info)
        AddPatientWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddPatientWindow)
        self.statusbar.setObjectName("statusbar")
        AddPatientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddPatientWindow)
        QtCore.QMetaObject.connectSlotsByName(AddPatientWindow)

    def retranslateUi(self, AddPatientWindow):
        _translate = QtCore.QCoreApplication.translate
        AddPatientWindow.setWindowTitle(_translate("AddPatientWindow", "Dodaj Pacjenta"))
        self.firstName.setText(_translate("AddPatientWindow", "Imię"))
        self.lastName.setText(_translate("AddPatientWindow", "Nazwisko"))
        self.pesel.setText(_translate("AddPatientWindow", "Pesel"))
        self.streetName.setText(_translate("AddPatientWindow", "Ulica"))
        self.buildingNumber.setText(_translate("AddPatientWindow", "Numer Domu"))
        self.zipCode.setText(_translate("AddPatientWindow", "Kod Pocztowy"))
        self.city.setText(_translate("AddPatientWindow", "Miasto"))
        self.saveButton.setText(_translate("AddPatientWindow", "Zapisz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddPatientWindow = QtWidgets.QMainWindow()
    ui = Ui_AddPatientWindow()
    ui.setupUi(AddPatientWindow)
    AddPatientWindow.show()
    sys.exit(app.exec_())


