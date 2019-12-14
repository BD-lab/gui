# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PrintOrder.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrintOrder(object):
    def setupUi(self, PrintOrder):
        PrintOrder.setObjectName("PrintOrder")
        PrintOrder.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PrintOrder)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 471))
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
        self.listInfo = QtWidgets.QLabel(self.formLayoutWidget)
        self.listInfo.setObjectName("listInfo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.listInfo)
        self.list = QtWidgets.QListWidget(self.formLayoutWidget)
        self.list.setObjectName("list")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.list)
        PrintOrder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PrintOrder)
        self.statusbar.setObjectName("statusbar")
        PrintOrder.setStatusBar(self.statusbar)

        self.retranslateUi(PrintOrder)
        QtCore.QMetaObject.connectSlotsByName(PrintOrder)

    def retranslateUi(self, PrintOrder):
        _translate = QtCore.QCoreApplication.translate
        PrintOrder.setWindowTitle(_translate("PrintOrder", "MainWindow"))
        self.infoText.setText(_translate("PrintOrder", "Dodajesz zamówienie do pacjenta"))
        self.infoPatient.setText(_translate("PrintOrder", "TextLabel"))
        self.listInfo.setText(_translate("PrintOrder", "Lista badań pacjenta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrintOrder = QtWidgets.QMainWindow()
    ui = Ui_PrintOrder()
    ui.setupUi(PrintOrder)
    PrintOrder.show()
    sys.exit(app.exec_())
