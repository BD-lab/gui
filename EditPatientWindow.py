from PyQt5 import QtCore, QtGui, QtWidgets
import requests

lastName='x'
firstName=''
pesel=''
streetName=''
buildingNumber=''
zipCode=''
city=''
idG=""

class Ui_EditPatientWindow(object):
    def __init__(self, id):
        global idG
        idG = id
        print(id)
        url = "http://localhost:8080/patients/{}".format(id)
        response = requests.get(url)
        print(response.json())
        global lastName
        lastName = response.json()['lastName']
        global firstName
        firstName = response.json()['firstName']
        global pesel
        pesel = response.json()['pesel']
        global streetName
        streetName = response.json()['streetName']
        global buildingNumber
        buildingNumber = response.json()['buildingNumber']
        global zipCode
        zipCode = response.json()['zipCode']
        global city
        city = response.json()['city']

    def click(self):
        global idG
        firstName = self.firstNameInput.text()
        lastName = self.lastNameInput.text()
        streetName = self.streetNameInput.text()
        buildingNumber = self.buildingNumberInput.text()
        zipCode = self.zipCodeInput.text()
        city = self.cityInput.text()
        url="http://localhost:8080/patients/{}".format(idG)
        response = requests.put(url, json={
            "id": idG,
            "firstName": firstName,
            "lastName": lastName,
            "streetName": streetName,
            "buildingNumber": buildingNumber,
            "zipCode": zipCode,
            "city": city
        })
        if response.status_code == 200:
            print(response.status_code)
            self.label.setText("Poprawnie edytowano dane")
        else:
            print(response.status_code)
            self.label.setText("Wystąpił bład")

    def setupUi(self, EditPatientWindow):
        global lastName
        global firstName
        global pesel
        global streetName
        global buildingNumber
        global zipCode
        global city
        EditPatientWindow.setObjectName("EditPatientWindow")
        EditPatientWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(EditPatientWindow)
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
        self.firstNameInput.setText(firstName)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameInput)
        self.lastName = QtWidgets.QLabel(self.formLayoutWidget)
        self.lastName.setObjectName("lastName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastName)
        self.lastNameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lastNameInput.setObjectName("lastNameInput")
        self.lastNameInput.setText(lastName)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastNameInput)
        self.streetName = QtWidgets.QLabel(self.formLayoutWidget)
        self.streetName.setObjectName("streetName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.streetName)
        self.streetNameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.streetNameInput.setObjectName("streetNameInput")
        self.streetNameInput.setText(streetName)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.streetNameInput)
        self.buildingNumber = QtWidgets.QLabel(self.formLayoutWidget)
        self.buildingNumber.setObjectName("buildingNumber")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.buildingNumber)
        self.buildingNumberInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.buildingNumberInput.setObjectName("buildingNumberInput")
        self.buildingNumberInput.setText(buildingNumber)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.buildingNumberInput)
        self.zipCode = QtWidgets.QLabel(self.formLayoutWidget)
        self.zipCode.setObjectName("zipCode")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.zipCode)
        self.zipCodeInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.zipCodeInput.setObjectName("zipCodeInput")
        self.zipCodeInput.setText(zipCode)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.zipCodeInput)
        self.city = QtWidgets.QLabel(self.formLayoutWidget)
        self.city.setObjectName("city")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.city)
        self.cityInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cityInput.setObjectName("cityInput")
        self.cityInput.setText(city)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cityInput)
        self.saveButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.click)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.saveButton)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label)
        EditPatientWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EditPatientWindow)
        self.statusbar.setObjectName("statusbar")
        EditPatientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EditPatientWindow)
        QtCore.QMetaObject.connectSlotsByName(EditPatientWindow)

    def retranslateUi(self, EditPatientWindow):
        _translate = QtCore.QCoreApplication.translate
        EditPatientWindow.setWindowTitle(_translate("EditPatientWindow", "Edytuj pacjenta"))
        self.firstName.setText(_translate("EditPatientWindow", "Imię"))
        self.lastName.setText(_translate("EditPatientWindow", "Nazwisko"))
        self.streetName.setText(_translate("EditPatientWindow", "Ulica"))
        self.buildingNumber.setText(_translate("EditPatientWindow", "Numer Domu"))
        self.zipCode.setText(_translate("EditPatientWindow", "Kod Pocztowy"))
        self.city.setText(_translate("EditPatientWindow", "Miasto"))
        self.saveButton.setText(_translate("EditPatientWindow", "Zapisz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditPatientWindow = QtWidgets.QMainWindow()
    ui = Ui_EditPatientWindow()
    ui.setupUi(EditPatientWindow)
    EditPatientWindow.show()
    sys.exit(app.exec_())
