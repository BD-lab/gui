# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditPatientWindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EditPatientWindow(object):
    def setupUi(self, EditPatientWindow):
        EditPatientWindow.setObjectName(_fromUtf8("EditPatientWindow"))
        EditPatientWindow.resize(768, 600)
        self.centralwidget = QtGui.QWidget(EditPatientWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 611))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.firstName = QtGui.QLabel(self.formLayoutWidget)
        self.firstName.setObjectName(_fromUtf8("firstName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.firstName)
        self.lastName = QtGui.QLabel(self.formLayoutWidget)
        self.lastName.setObjectName(_fromUtf8("lastName"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lastName)
        self.lastNameInput = QtGui.QLineEdit(self.formLayoutWidget)
        self.lastNameInput.setObjectName(_fromUtf8("lastNameInput"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lastNameInput)
        self.pesel = QtGui.QLabel(self.formLayoutWidget)
        self.pesel.setObjectName(_fromUtf8("pesel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.pesel)
        self.streetName = QtGui.QLabel(self.formLayoutWidget)
        self.streetName.setObjectName(_fromUtf8("streetName"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.streetName)
        self.buildingNumber = QtGui.QLabel(self.formLayoutWidget)
        self.buildingNumber.setObjectName(_fromUtf8("buildingNumber"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.buildingNumber)
        self.zipCode = QtGui.QLabel(self.formLayoutWidget)
        self.zipCode.setObjectName(_fromUtf8("zipCode"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.zipCode)
        self.city = QtGui.QLabel(self.formLayoutWidget)
        self.city.setObjectName(_fromUtf8("city"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.city)
        self.cityInput = QtGui.QLineEdit(self.formLayoutWidget)
        self.cityInput.setObjectName(_fromUtf8("cityInput"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.cityInput)
        self.zipCodeInput = QtGui.QLineEdit(self.formLayoutWidget)
        self.zipCodeInput.setObjectName(_fromUtf8("zipCodeInput"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.zipCodeInput)
        self.firstNameInput = QtGui.QLineEdit(self.formLayoutWidget)
        self.firstNameInput.setObjectName(_fromUtf8("firstNameInput"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.firstNameInput)
        self.peselInput = QtGui.QLineEdit(self.formLayoutWidget)
        self.peselInput.setObjectName(_fromUtf8("peselInput"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.peselInput)
        self.buildingNumberInput = QtGui.QLineEdit(self.formLayoutWidget)
        self.buildingNumberInput.setObjectName(_fromUtf8("buildingNumberInput"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.buildingNumberInput)
        self.streetNameInput = QtGui.QLineEdit(self.formLayoutWidget)
        self.streetNameInput.setObjectName(_fromUtf8("streetNameInput"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.streetNameInput)
        self.saveButton = QtGui.QPushButton(self.formLayoutWidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.saveButton)
        EditPatientWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(EditPatientWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EditPatientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EditPatientWindow)
        QtCore.QMetaObject.connectSlotsByName(EditPatientWindow)

    def retranslateUi(self, EditPatientWindow):
        EditPatientWindow.setWindowTitle(_translate("EditPatientWindow", "MainWindow", None))
        self.firstName.setText(_translate("EditPatientWindow", "Imię", None))
        self.lastName.setText(_translate("EditPatientWindow", "Nazwisko", None))
        self.pesel.setText(_translate("EditPatientWindow", "Pesel", None))
        self.streetName.setText(_translate("EditPatientWindow", "Ulica", None))
        self.buildingNumber.setText(_translate("EditPatientWindow", "Numer Domu", None))
        self.zipCode.setText(_translate("EditPatientWindow", "Kod Pocztowy", None))
        self.city.setText(_translate("EditPatientWindow", "Miasto", None))
        self.saveButton.setText(_translate("EditPatientWindow", "Zapisz", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EditPatientWindow = QtGui.QMainWindow()
    ui = Ui_EditPatientWindow()
    ui.setupUi(EditPatientWindow)
    EditPatientWindow.show()
    sys.exit(app.exec_())

