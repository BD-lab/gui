import sys

from PySide2.QtCore import (Qt, Slot)
from PySide2.QtWidgets import (QApplication, QPushButton,
                               QVBoxLayout, QWidget, QMenuBar, QAction, QMainWindow, QDialog, QLabel)

from AddPatientWindow import Ui_AddPatientWindow
from ChoosePatientWindow import Ui_ChoosePatientWindow


class HelpDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setFixedSize(300, 400)
        self.label = QLabel("""
        Test
        Test
        """)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setFixedSize(200, 200)
        self.setWindowTitle("O programie")

        self.label = QLabel("Autorzy:\n"
                            "\n"
                            "Adrian Glapiński\n"
                            "Marta Tarka\n"
                            "Jakub Pogodziński\n"
                            "Miłosz Szkudlarek\n")

        self.label.setAlignment(Qt.AlignCenter)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(400, 200)
        self.setWindowTitle("Clinic")

        # Widgets
        self.menu = QMenuBar()
        self.file_menu = self.menu.addMenu("Plik")
        self.help_menu = self.menu.addMenu("Pomoc")
        self.button1 = QPushButton("Wybierz pacjenta")
        self.button1.setMinimumHeight(50)
        self.button2 = QPushButton("Dodaj pacjenta")
        self.button2.setMinimumHeight(50)

        # Menu
        self.exit_action = QAction("Wyjdź")
        self.help_action = QAction("Pomoc")
        self.about_action = QAction("O programie")
        self.file_menu.addAction(self.exit_action)
        self.help_menu.addAction(self.help_action)
        self.help_menu.addAction(self.about_action)

        # Layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.setMenuBar(self.menu)
        self.setLayout(self.layout)

        # Actions
        self.button1.clicked.connect(self.show_choose_patient)
        self.button2.clicked.connect(self.show_add_patient)
        self.exit_action.triggered.connect(self.close)
        self.help_action.triggered.connect(self.show_help_dialog)
        self.about_action.triggered.connect(self.show_about_dialog)

    @Slot()
    def show_choose_patient(self):
        self.window = QMainWindow()
        self.ui = Ui_ChoosePatientWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    @Slot()
    def show_add_patient(self):
        self.window = QMainWindow()
        self.ui = Ui_AddPatientWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    @Slot()
    def show_help_dialog(self):
        window = HelpDialog(parent=self)
        window.show()

    @Slot()
    def show_about_dialog(self):
        window = AboutDialog(parent=self)
        window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec_())
