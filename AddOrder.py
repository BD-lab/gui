from PyQt5 import QtCore, QtGui, QtWidgets
from ExamTypes import ExamTypes
import requests

idT = ''
first = ''
last = ''


class Ui_AddOrder(object):
    def __init__(self, id, fn, ln):
        global idT, first, last
        idT = id
        first = fn
        last = ln

    def __init__(self, id, fn, ln):
        global idT, first, last
        idT = id
        first = fn
        last = ln

    def click(self):
        global idT
        idOrder = self.idOrderInput.text()
        exam1 = self.comboBox.currentText()
        exam2 = self.comboBox_2.currentText()
        exam3 = self.comboBox_3.currentText()
        exam4 = self.comboBox_4.currentText()
        exam5 = self.comboBox_5.currentText()
        exam6 = self.comboBox_6.currentText()
        exam7 = self.comboBox_7.currentText()
        exam8 = self.comboBox_8.currentText()
        exam9 = self.comboBox_9.currentText()
        exam10 = self.comboBox_10.currentText()
        exam11 = self.comboBox_11.currentText()
        exam12 = self.comboBox_12.currentText()
        if (exam2 == "brak"):
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                ]
            })
        elif (exam3 == "brak"):
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                    {
                        "type": ExamTypes(exam2).name
                    },
                ]
            })
        elif (exam4 == "brak"):
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                    {
                        "type": ExamTypes(exam2).name
                    },
                    {
                        "type": ExamTypes(exam3).name
                    },
                ]
            })
        elif (exam5 == "brak"):
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                    {
                        "type": ExamTypes(exam2).name
                    },
                    {
                        "type": ExamTypes(exam3).name
                    },
                    {
                        "type": ExamTypes(exam4).name
                    },
                ]
            })
        elif (exam6 == "brak"):
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                    {
                        "type": ExamTypes(exam2).name
                    },
                    {
                        "type": ExamTypes(exam3).name
                    },
                    {
                        "type": ExamTypes(exam4).name
                    },
                    {
                        "type": ExamTypes(exam5).name
                    },
                ]
            })
        elif (exam7 == "brak"):
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                    {
                        "type": ExamTypes(exam2).name
                    },
                    {
                        "type": ExamTypes(exam3).name
                    },
                    {
                        "type": ExamTypes(exam4).name
                    },
                    {
                        "type": ExamTypes(exam5).name
                    },
                    {
                        "type": ExamTypes(exam6).name
                    },
                ]
            })
        elif (exam8 == "brak"):
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                    {
                        "type": ExamTypes(exam2).name
                    },
                    {
                        "type": ExamTypes(exam3).name
                    },
                    {
                        "type": ExamTypes(exam4).name
                    },
                    {
                        "type": ExamTypes(exam5).name
                    },
                    {
                        "type": ExamTypes(exam6).name
                    },
                    {
                        "type": ExamTypes(exam7).name
                    },
                ]
            })
        elif (exam9 == "brak"):
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                    {
                        "type": ExamTypes(exam2).name
                    },
                    {
                        "type": ExamTypes(exam3).name
                    },
                    {
                        "type": ExamTypes(exam4).name
                    },
                    {
                        "type": ExamTypes(exam5).name
                    },
                    {
                        "type": ExamTypes(exam6).name
                    },
                    {
                        "type": ExamTypes(exam7).name
                    },
                    {
                        "type": ExamTypes(exam8).name
                    },
                ]
            })
        elif (exam10 == "brak"):
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                    {
                        "type": ExamTypes(exam2).name
                    },
                    {
                        "type": ExamTypes(exam3).name
                    },
                    {
                        "type": ExamTypes(exam4).name
                    },
                    {
                        "type": ExamTypes(exam5).name
                    },
                    {
                        "type": ExamTypes(exam6).name
                    },
                    {
                        "type": ExamTypes(exam7).name
                    },
                    {
                        "type": ExamTypes(exam8).name
                    },
                    {
                        "type": ExamTypes(exam9).name
                    },
                ]
            })
        elif (exam11 == "brak"):
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                    {
                        "type": ExamTypes(exam2).name
                    },
                    {
                        "type": ExamTypes(exam3).name
                    },
                    {
                        "type": ExamTypes(exam4).name
                    },
                    {
                        "type": ExamTypes(exam5).name
                    },
                    {
                        "type": ExamTypes(exam6).name
                    },
                    {
                        "type": ExamTypes(exam7).name
                    },
                    {
                        "type": ExamTypes(exam8).name
                    },
                    {
                        "type": ExamTypes(exam9).name
                    },
                    {
                        "type": ExamTypes(exam10).name
                    },
                ]
            })
        elif (exam12 == "brak"):
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                    {
                        "type": ExamTypes(exam2).name
                    },
                    {
                        "type": ExamTypes(exam3).name
                    },
                    {
                        "type": ExamTypes(exam4).name
                    },
                    {
                        "type": ExamTypes(exam5).name
                    },
                    {
                        "type": ExamTypes(exam6).name
                    },
                    {
                        "type": ExamTypes(exam7).name
                    },
                    {
                        "type": ExamTypes(exam8).name
                    },
                    {
                        "type": ExamTypes(exam9).name
                    },
                    {
                        "type": ExamTypes(exam10).name
                    },
                    {
                        "type": ExamTypes(exam11).name
                    },
                ]
            })
        else:
            response = requests.post("http://localhost:8080/orders", json={
                "orderNumber": idOrder,
                "patientId": idT,
                "examinations": [
                    {
                        "type": ExamTypes(exam1).name
                    },
                    {
                        "type": ExamTypes(exam2).name
                    },
                    {
                        "type": ExamTypes(exam3).name
                    },
                    {
                        "type": ExamTypes(exam4).name
                    },
                    {
                        "type": ExamTypes(exam5).name
                    },
                    {
                        "type": ExamTypes(exam6).name
                    },
                    {
                        "type": ExamTypes(exam7).name
                    },
                    {
                        "type": ExamTypes(exam8).name
                    },
                    {
                        "type": ExamTypes(exam9).name
                    },
                    {
                        "type": ExamTypes(exam10).name
                    },
                    {
                        "type": ExamTypes(exam11).name
                    },
                    {
                        "type": ExamTypes(exam12).name
                    },
                ]
            })
        if response.status_code == 201:
            self.info.setText("Poprawnie zlecono badania")

        elif response.status_code == 409:
            self.info.setText("Zamówienie o podanym numerze już istnieje")
        elif response.status_code == 423:
            self.info.setText("Nie można się połączyć z wszystkimi laboratoriami wymaganymi dla podanego zamówienia. Operacja została cofnięta.")
        else:
            print(response.status_code)
            self.info.setText("Wystąpił bład")

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
        self.saveButton.clicked.connect(self.click)
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.saveButton)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        for i in ExamTypes:
            self.comboBox.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        for i in ExamTypes:
            self.comboBox_2.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        for i in ExamTypes:
            self.comboBox_3.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        for i in ExamTypes:
            self.comboBox_4.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.info = QtWidgets.QLabel(self.formLayoutWidget)
        self.info.setText("")
        self.info.setObjectName("info")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.info)
        self.comboBox_5 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        for i in ExamTypes:
            self.comboBox_5.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox_5)
        self.comboBox_6 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_6.setObjectName("comboBox_6")
        for i in ExamTypes:
            self.comboBox_6.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.comboBox_6)
        self.comboBox_7 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_7.setObjectName("comboBox_7")
        for i in ExamTypes:
            self.comboBox_7.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboBox_7)
        self.comboBox_8 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_8.setObjectName("comboBox_8")
        for i in ExamTypes:
            self.comboBox_8.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.comboBox_8)
        self.comboBox_9 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_9.setObjectName("comboBox_9")
        for i in ExamTypes:
            self.comboBox_9.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.comboBox_9)
        self.comboBox_10 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_10.setObjectName("comboBox_10")
        for i in ExamTypes:
            self.comboBox_10.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.comboBox_10)
        self.comboBox_11 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_11.setObjectName("comboBox_11")
        for i in ExamTypes:
            self.comboBox_11.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.comboBox_11)
        self.comboBox_12 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_12.setObjectName("comboBox_12")
        for i in ExamTypes:
            self.comboBox_12.addItem(ExamTypes(i).value, ExamTypes(i).name)
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.comboBox_12)
        AddOrder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddOrder)
        self.statusbar.setObjectName("statusbar")
        AddOrder.setStatusBar(self.statusbar)

        self.retranslateUi(AddOrder)
        QtCore.QMetaObject.connectSlotsByName(AddOrder)

    def retranslateUi(self, AddOrder):
        global idT, first, last
        text = first + " " + last
        _translate = QtCore.QCoreApplication.translate
        AddOrder.setWindowTitle(_translate("AddOrder", "Dodaj zamówienie"))
        self.infoText.setText(_translate("AddOrder", "Dodajesz zamówienie do pacjenta"))
        self.infoPatient.setText(_translate("AddOrder", text))
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
