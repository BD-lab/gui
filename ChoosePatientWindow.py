# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChoosePatientWindow.ui'
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

class Ui_ChoosePatientWindow(object):
    def setupUi(self, ChoosePatientWindow):
        ChoosePatientWindow.setObjectName(_fromUtf8("ChoosePatientWindow"))
        ChoosePatientWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(ChoosePatientWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(200, 150, 431, 221))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pesel = QtGui.QLabel(self.formLayoutWidget)
        self.pesel.setObjectName(_fromUtf8("pesel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pesel)
        self.peselInput = QtGui.QLineEdit(self.formLayoutWidget)
        self.peselInput.setObjectName(_fromUtf8("peselInput"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.peselInput)
        self.chooseButton = QtGui.QPushButton(self.formLayoutWidget)
        self.chooseButton.setObjectName(_fromUtf8("chooseButton"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.chooseButton)
        ChoosePatientWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(ChoosePatientWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ChoosePatientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChoosePatientWindow)
        QtCore.QMetaObject.connectSlotsByName(ChoosePatientWindow)

    def retranslateUi(self, ChoosePatientWindow):
        ChoosePatientWindow.setWindowTitle(_translate("ChoosePatientWindow", "MainWindow", None))
        self.pesel.setText(_translate("ChoosePatientWindow", "Pesel", None))
        self.chooseButton.setText(_translate("ChoosePatientWindow", "Wybierz", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ChoosePatientWindow = QtGui.QMainWindow()
    ui = Ui_ChoosePatientWindow()
    ui.setupUi(ChoosePatientWindow)
    ChoosePatientWindow.show()
    sys.exit(app.exec_())

