# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddOrder.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddOrder(object):
    def setupUi(self, AddOrder):
        AddOrder.setObjectName("AddOrder")
        AddOrder.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AddOrder)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 801, 531))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.infoText = QtWidgets.QLabel(self.formLayoutWidget)
        self.infoText.setObjectName("infoText")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.infoText)
        self.infoPatient = QtWidgets.QLabel(self.formLayoutWidget)
        self.infoPatient.setObjectName("infoPatient")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.infoPatient)
        self.idOrder = QtWidgets.QLabel(self.formLayoutWidget)
        self.idOrder.setObjectName("idOrder")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.idOrder)
        self.idOrderInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.idOrderInput.setObjectName("idOrderInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.idOrderInput)
        self.listOrder = QtWidgets.QLabel(self.formLayoutWidget)
        self.listOrder.setObjectName("listOrder")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.listOrder)
        self.saveButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.saveButton)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        AddOrder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddOrder)
        self.statusbar.setObjectName("statusbar")
        AddOrder.setStatusBar(self.statusbar)

        self.retranslateUi(AddOrder)
        QtCore.QMetaObject.connectSlotsByName(AddOrder)

    def retranslateUi(self, AddOrder):
        _translate = QtCore.QCoreApplication.translate
        AddOrder.setWindowTitle(_translate("AddOrder", "Dodaj zamówienie"))
        self.infoText.setText(_translate("AddOrder", "Dodajesz zamówienie do pacjenta"))
        self.infoPatient.setText(_translate("AddOrder", "TextLabel"))
        self.idOrder.setText(_translate("AddOrder", "Numer zamówienia"))
        self.listOrder.setText(_translate("AddOrder", "Zlecone badania"))
        self.saveButton.setText(_translate("AddOrder", "Zapisz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddOrder = QtWidgets.QMainWindow()
    ui = Ui_AddOrder()
    ui.setupUi(AddOrder)
    AddOrder.show()
    sys.exit(app.exec_())
