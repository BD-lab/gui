import requests
from PySide2 import QtCore, QtWidgets


class Ui_PrintOrder(object):
    def printClick(self):
        idOrder = self.orderInput.text()

        response = requests.get('http://localhost:8080/orders/result/{}/print'.format(idOrder))
        if response.status_code == 200:
            self.response.setText("Poprawnie wydrukowano")
        elif response.status_code == 201:
            self.response.setText("Poprawnie wydrukowano")
        elif response.status_code == 404:
            self.response.setText("Zamówienie o podanym numerze nie istnieje")
        elif response.status_code == 409:
            self.response.setText("Zamówienie jeszcze nie zostało skompletowane")

        else:
            print(response.status_code)
            self.response.setText("Wystąpił bład")

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
        self.listInfo = QtWidgets.QLabel(self.formLayoutWidget)
        self.listInfo.setObjectName("listInfo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.listInfo)
        self.printButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.printButton.setObjectName("printButton")
        self.printButton.clicked.connect(self.printClick)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.printButton)
        self.orderInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.orderInput.setObjectName("orderInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.orderInput)
        self.response = QtWidgets.QLabel(self.formLayoutWidget)
        self.response.setText("")
        self.response.setObjectName("response")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.response)
        PrintOrder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PrintOrder)
        self.statusbar.setObjectName("statusbar")
        PrintOrder.setStatusBar(self.statusbar)

        self.retranslateUi(PrintOrder)
        QtCore.QMetaObject.connectSlotsByName(PrintOrder)

    def retranslateUi(self, PrintOrder):
        _translate = QtCore.QCoreApplication.translate
        PrintOrder.setWindowTitle(_translate("PrintOrder", "Drukuj wyniki"))
        self.infoText.setText(_translate("PrintOrder", "Drukujesz zamówienie"))
        self.listInfo.setText(_translate("PrintOrder", "Wpisz numer zamówienia"))
        self.printButton.setText(_translate("PrintOrder", "Drukuj"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PrintOrder = QtWidgets.QMainWindow()
    ui = Ui_PrintOrder()
    ui.setupUi(PrintOrder)
    PrintOrder.show()
    sys.exit(app.exec_())
