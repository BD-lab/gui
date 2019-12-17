from PyQt5 import QtCore, QtGui, QtWidgets
from ExamTypes import ExamTypes
import requests

idT = ''
first=''
last=''

class Ui_AddOrder(object):
    def __init__(self, id,fn,ln):
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
                    }
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

        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.saveButton)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("brak", ExamTypes.NONE)
        self.comboBox.addItem("Hemoglobina", ExamTypes.HAEMOGLOBIN)
        self.comboBox.addItem("Leukocyty", ExamTypes.LEUKOCYTES)
        self.comboBox.addItem("Płytki krwi", ExamTypes.PLATELETS)
        self.comboBox.addItem("Hematokryt", ExamTypes.HAEMATOCRIT)
        self.comboBox.addItem("INR", ExamTypes.INR)
        self.comboBox.addItem("Sód", ExamTypes.SODIUM)
        self.comboBox.addItem("Potas", ExamTypes.POTASSIUM)
        self.comboBox.addItem("Chlorek", ExamTypes.CHLORIDE)
        self.comboBox.addItem("Azot mocznikowy", ExamTypes.UREA_NITROGEN)
        self.comboBox.addItem("Osmolalność surowicy", ExamTypes.OSMOLALITY_SERUM)
        self.comboBox.addItem("Glukoza", ExamTypes.GLUCOSE)
        self.comboBox.addItem("HbA1c", ExamTypes.HbA1c)
        self.comboBox.addItem("Urobilinogen", ExamTypes.URIBILINOGEN)
        self.comboBox.addItem("Bilirubina", ExamTypes.BILIRUBIN)
        self.comboBox.addItem("Ketony", ExamTypes.KETONE)
        self.comboBox.addItem("Krew", ExamTypes.BLOOD)
        self.comboBox.addItem("Białko", ExamTypes.PROTEIN)
        self.comboBox.addItem("pH", ExamTypes.PH)
        self.comboBox.addItem("Trawa", ExamTypes.GRASS)
        self.comboBox.addItem("Brzoza", ExamTypes.BIRCH_TREE)
        self.comboBox.addItem("Bylica", ExamTypes.WORMWOOD)
        self.comboBox.addItem("Kot", ExamTypes.CAT)
        self.comboBox.addItem("Pies", ExamTypes.DOG)
        self.comboBox.addItem("Cladosporium herbarum", ExamTypes.CLADOSPORIUM)
        self.comboBox.addItem("Alternaria alternata", ExamTypes.ALTERNARIA)
        self.comboBox.addItem("Białko jaja", ExamTypes.EGG_WHITE)
        self.comboBox.addItem("Żółtko jaja", ExamTypes.EGG_YOLK)
        self.comboBox.addItem("Mleko", ExamTypes.MILK)
        self.comboBox.addItem("Dorsz", ExamTypes.COD)
        self.comboBox.addItem("Kazeina", ExamTypes.CASEIN)
        self.comboBox.addItem("Mąka pszenna", ExamTypes.WHEAT_FLOUR)
        self.comboBox.addItem("Ryż", ExamTypes.RICE)
        self.comboBox.addItem("Soja", ExamTypes.SOY)
        self.comboBox.addItem("Orzech ziemny", ExamTypes.PEANUT)
        self.comboBox.addItem("Orzech laskowy", ExamTypes.HAZELNUT)
        self.comboBox.addItem("Marchewka", ExamTypes.CARROT)
        self.comboBox.addItem("Ziemniak", ExamTypes.POTATO)
        self.comboBox.addItem("Jabłko", ExamTypes.APPLE)

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("brak", ExamTypes.NONE)
        self.comboBox_2.addItem("Hemoglobina", ExamTypes.HAEMOGLOBIN)
        self.comboBox_2.addItem("Leukocyty", ExamTypes.LEUKOCYTES)
        self.comboBox_2.addItem("Płytki krwi", ExamTypes.PLATELETS)
        self.comboBox_2.addItem("Hematokryt", ExamTypes.HAEMATOCRIT)
        self.comboBox_2.addItem("INR", ExamTypes.INR)
        self.comboBox_2.addItem("Sód", ExamTypes.SODIUM)
        self.comboBox_2.addItem("Potas", ExamTypes.POTASSIUM)
        self.comboBox_2.addItem("Chlorek", ExamTypes.CHLORIDE)
        self.comboBox_2.addItem("Azot mocznikowy", ExamTypes.UREA_NITROGEN)
        self.comboBox_2.addItem("Osmolalność surowicy", ExamTypes.OSMOLALITY_SERUM)
        self.comboBox_2.addItem("Glukoza", ExamTypes.GLUCOSE)
        self.comboBox_2.addItem("HbA1c", ExamTypes.HbA1c)
        self.comboBox_2.addItem("Urobilinogen", ExamTypes.URIBILINOGEN)
        self.comboBox_2.addItem("Bilirubina", ExamTypes.BILIRUBIN)
        self.comboBox_2.addItem("Ketony", ExamTypes.KETONE)
        self.comboBox_2.addItem("Krew", ExamTypes.BLOOD)
        self.comboBox_2.addItem("Białko", ExamTypes.PROTEIN)
        self.comboBox_2.addItem("pH", ExamTypes.PH)
        self.comboBox_2.addItem("Trawa", ExamTypes.GRASS)
        self.comboBox_2.addItem("Brzoza", ExamTypes.BIRCH_TREE)
        self.comboBox_2.addItem("Bylica", ExamTypes.WORMWOOD)
        self.comboBox_2.addItem("Kot", ExamTypes.CAT)
        self.comboBox_2.addItem("Pies", ExamTypes.DOG)
        self.comboBox_2.addItem("Cladosporium herbarum", ExamTypes.CLADOSPORIUM)
        self.comboBox_2.addItem("Alternaria alternata", ExamTypes.ALTERNARIA)
        self.comboBox_2.addItem("Białko jaja", ExamTypes.EGG_WHITE)
        self.comboBox_2.addItem("Żółtko jaja", ExamTypes.EGG_YOLK)
        self.comboBox_2.addItem("Mleko", ExamTypes.MILK)
        self.comboBox_2.addItem("Dorsz", ExamTypes.COD)
        self.comboBox_2.addItem("Kazeina", ExamTypes.CASEIN)
        self.comboBox_2.addItem("Mąka pszenna", ExamTypes.WHEAT_FLOUR)
        self.comboBox_2.addItem("Ryż", ExamTypes.RICE)
        self.comboBox_2.addItem("Soja", ExamTypes.SOY)
        self.comboBox_2.addItem("Orzech ziemny", ExamTypes.PEANUT)
        self.comboBox_2.addItem("Orzech laskowy", ExamTypes.HAZELNUT)
        self.comboBox_2.addItem("Marchewka", ExamTypes.CARROT)
        self.comboBox_2.addItem("Ziemniak", ExamTypes.POTATO)
        self.comboBox_2.addItem("Jabłko", ExamTypes.APPLE)

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("brak", ExamTypes.NONE)
        self.comboBox_3.addItem("Hemoglobina", ExamTypes.HAEMOGLOBIN)
        self.comboBox_3.addItem("Leukocyty", ExamTypes.LEUKOCYTES)
        self.comboBox_3.addItem("Płytki krwi", ExamTypes.PLATELETS)
        self.comboBox_3.addItem("Hematokryt", ExamTypes.HAEMATOCRIT)
        self.comboBox_3.addItem("INR", ExamTypes.INR)
        self.comboBox_3.addItem("Sód", ExamTypes.SODIUM)
        self.comboBox_3.addItem("Potas", ExamTypes.POTASSIUM)
        self.comboBox_3.addItem("Chlorek", ExamTypes.CHLORIDE)
        self.comboBox_3.addItem("Azot mocznikowy", ExamTypes.UREA_NITROGEN)
        self.comboBox_3.addItem("Osmolalność surowicy", ExamTypes.OSMOLALITY_SERUM)
        self.comboBox_3.addItem("Glukoza", ExamTypes.GLUCOSE)
        self.comboBox_3.addItem("HbA1c", ExamTypes.HbA1c)
        self.comboBox_3.addItem("Urobilinogen", ExamTypes.URIBILINOGEN)
        self.comboBox_3.addItem("Bilirubina", ExamTypes.BILIRUBIN)
        self.comboBox_3.addItem("Ketony", ExamTypes.KETONE)
        self.comboBox_3.addItem("Krew", ExamTypes.BLOOD)
        self.comboBox_3.addItem("Białko", ExamTypes.PROTEIN)
        self.comboBox_3.addItem("pH", ExamTypes.PH)
        self.comboBox_3.addItem("Trawa", ExamTypes.GRASS)
        self.comboBox_3.addItem("Brzoza", ExamTypes.BIRCH_TREE)
        self.comboBox_3.addItem("Bylica", ExamTypes.WORMWOOD)
        self.comboBox_3.addItem("Kot", ExamTypes.CAT)
        self.comboBox_3.addItem("Pies", ExamTypes.DOG)
        self.comboBox_3.addItem("Cladosporium herbarum", ExamTypes.CLADOSPORIUM)
        self.comboBox_3.addItem("Alternaria alternata", ExamTypes.ALTERNARIA)
        self.comboBox_3.addItem("Białko jaja", ExamTypes.EGG_WHITE)
        self.comboBox_3.addItem("Żółtko jaja", ExamTypes.EGG_YOLK)
        self.comboBox_3.addItem("Mleko", ExamTypes.MILK)
        self.comboBox_3.addItem("Dorsz", ExamTypes.COD)
        self.comboBox_3.addItem("Kazeina", ExamTypes.CASEIN)
        self.comboBox_3.addItem("Mąka pszenna", ExamTypes.WHEAT_FLOUR)
        self.comboBox_3.addItem("Ryż", ExamTypes.RICE)
        self.comboBox_3.addItem("Soja", ExamTypes.SOY)
        self.comboBox_3.addItem("Orzech ziemny", ExamTypes.PEANUT)
        self.comboBox_3.addItem("Orzech laskowy", ExamTypes.HAZELNUT)
        self.comboBox_3.addItem("Marchewka", ExamTypes.CARROT)
        self.comboBox_3.addItem("Ziemniak", ExamTypes.POTATO)
        self.comboBox_3.addItem("Jabłko", ExamTypes.APPLE)

        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("brak", ExamTypes.NONE)
        self.comboBox_4.addItem("Hemoglobina", ExamTypes.HAEMOGLOBIN)
        self.comboBox_4.addItem("Leukocyty", ExamTypes.LEUKOCYTES)
        self.comboBox_4.addItem("Płytki krwi", ExamTypes.PLATELETS)
        self.comboBox_4.addItem("Hematokryt", ExamTypes.HAEMATOCRIT)
        self.comboBox_4.addItem("INR", ExamTypes.INR)
        self.comboBox_4.addItem("Sód", ExamTypes.SODIUM)
        self.comboBox_4.addItem("Potas", ExamTypes.POTASSIUM)
        self.comboBox_4.addItem("Chlorek", ExamTypes.CHLORIDE)
        self.comboBox_4.addItem("Azot mocznikowy", ExamTypes.UREA_NITROGEN)
        self.comboBox_4.addItem("Osmolalność surowicy", ExamTypes.OSMOLALITY_SERUM)
        self.comboBox_4.addItem("Glukoza", ExamTypes.GLUCOSE)
        self.comboBox_4.addItem("HbA1c", ExamTypes.HbA1c)
        self.comboBox_4.addItem("Urobilinogen", ExamTypes.URIBILINOGEN)
        self.comboBox_4.addItem("Bilirubina", ExamTypes.BILIRUBIN)
        self.comboBox_4.addItem("Ketony", ExamTypes.KETONE)
        self.comboBox_4.addItem("Krew", ExamTypes.BLOOD)
        self.comboBox_4.addItem("Białko", ExamTypes.PROTEIN)
        self.comboBox_4.addItem("pH", ExamTypes.PH)
        self.comboBox_4.addItem("Trawa", ExamTypes.GRASS)
        self.comboBox_4.addItem("Brzoza", ExamTypes.BIRCH_TREE)
        self.comboBox_4.addItem("Bylica", ExamTypes.WORMWOOD)
        self.comboBox_4.addItem("Kot", ExamTypes.CAT)
        self.comboBox_4.addItem("Pies", ExamTypes.DOG)
        self.comboBox_4.addItem("Cladosporium herbarum", ExamTypes.CLADOSPORIUM)
        self.comboBox_4.addItem("Alternaria alternata", ExamTypes.ALTERNARIA)
        self.comboBox_4.addItem("Białko jaja", ExamTypes.EGG_WHITE)
        self.comboBox_4.addItem("Żółtko jaja", ExamTypes.EGG_YOLK)
        self.comboBox_4.addItem("Mleko", ExamTypes.MILK)
        self.comboBox_4.addItem("Dorsz", ExamTypes.COD)
        self.comboBox_4.addItem("Kazeina", ExamTypes.CASEIN)
        self.comboBox_4.addItem("Mąka pszenna", ExamTypes.WHEAT_FLOUR)
        self.comboBox_4.addItem("Ryż", ExamTypes.RICE)
        self.comboBox_4.addItem("Soja", ExamTypes.SOY)
        self.comboBox_4.addItem("Orzech ziemny", ExamTypes.PEANUT)
        self.comboBox_4.addItem("Orzech laskowy", ExamTypes.HAZELNUT)
        self.comboBox_4.addItem("Marchewka", ExamTypes.CARROT)
        self.comboBox_4.addItem("Ziemniak", ExamTypes.POTATO)
        self.comboBox_4.addItem("Jabłko", ExamTypes.APPLE)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.info = QtWidgets.QLabel(self.formLayoutWidget)
        self.info.setText("")
        self.info.setObjectName("info")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.info)
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
