import requests
from PySide2 import QtCore, QtWidgets

from patient import Ui_MainWindow


class Ui_ChoosePatientWindow(object):
    def click(self):
        pesel = self.peselInput.text()
        payload = {'pesel': pesel}
        response = requests.get("http://localhost:8080/patients", params=payload)
        if response.status_code == 200:
            self.window = QtWidgets.QMainWindow()
            self.message = response.json()
            self.id = response.json()['id']
            self.firstName = response.json()['firstName']
            self.lastName = response.json()['lastName']
            self.ui = Ui_MainWindow(self.firstName, self.lastName, self.id)
            self.ui.setupUi(self.window)
            self.info.setText("Poprawnie wybrano pacjenta")
            # ChoosePatientWindow.hide()
            self.window.show()

        elif response.status_code == 404:
            self.info.setText("Pacjent o podanym nr PESEL nie istnieje")
        else:
            self.info.setText("Nie ma takiego pacjenta")

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
        self.info = QtWidgets.QLabel(self.formLayoutWidget)
        self.info.setText("")
        self.info.setObjectName("info")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.info)
        ChoosePatientWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChoosePatientWindow)
        QtCore.QMetaObject.connectSlotsByName(ChoosePatientWindow)

    def retranslateUi(self, ChoosePatientWindow):
        _translate = QtCore.QCoreApplication.translate
        ChoosePatientWindow.setWindowTitle(_translate("ChoosePatientWindow", "Wybierz pacjenta"))
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
