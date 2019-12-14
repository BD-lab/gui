# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
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

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName(_fromUtf8("Main"))
        Main.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ChoosePatient = QtGui.QPushButton(self.centralwidget)
        self.ChoosePatient.setGeometry(QtCore.QRect(314, 186, 131, 61))
        self.ChoosePatient.setObjectName(_fromUtf8("ChoosePatient"))
        self.AddPatient = QtGui.QPushButton(self.centralwidget)
        self.AddPatient.setGeometry(QtCore.QRect(314, 266, 131, 61))
        self.AddPatient.setObjectName(_fromUtf8("AddPatient"))
        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Main)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(_translate("Main", "MainWindow", None))
        self.ChoosePatient.setText(_translate("Main", "Wybierz Pacjenta", None))
        self.AddPatient.setText(_translate("Main", "Dodaj Pacjenta", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Main = QtGui.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

