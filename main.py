##############################
# main.py

import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from config import getFont
from random import choice


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 250))

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        option_layout = QGridLayout()
        self.password_generated = QLineEdit()
        button_layout = QHBoxLayout()

        main_layout.addLayout(option_layout)
        main_layout.addWidget(self.password_generated)
        main_layout.addLayout(button_layout)

        btn_quit = QPushButton("Quitter", self)
        btn_copy = QPushButton("Copier", self)
        btn_generate = QPushButton("Générer", self)
        button_layout.addWidget(btn_quit)
        button_layout.addWidget(btn_copy)
        button_layout.addWidget(btn_generate)

        self.txt_size = QLabel("Taille : 10")
        option_layout.addWidget(self.txt_size, 0, 0)

        self.option_size = QSlider(Qt.Horizontal)
        self.option_size.setMinimum(8)
        self.option_size.setMaximum(30)
        self.option_size.setValue(10)
        option_layout.addWidget(self.option_size, 1, 0)

        self.option_lowercase = QCheckBox("Minuscules")
        option_layout.addWidget(self.option_lowercase, 0, 1)
        self.option_uppercase = QCheckBox("Majuscules")
        option_layout.addWidget(self.option_uppercase, 1, 1)
        self.option_numbers = QCheckBox("Chiffres")
        option_layout.addWidget(self.option_numbers, 0, 2)
        self.option_symbols = QCheckBox("Symboles")
        option_layout.addWidget(self.option_symbols, 1, 2)

        self.option_lowercase.setChecked(True)
        self.option_numbers.setChecked(True)

        btn_quit.clicked.connect(self.quit)
        btn_copy.clicked.connect(self.copy)

        self.option_size.valueChanged.connect(self.change_size)

        btn_generate.clicked.connect(self.generate)

        self.generate()

        self.setStatusBar(QStatusBar(self))
        self.status = self.statusBar()

    def quit(self):
        QApplication.quit()

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_generated.text())
        self.status.showMessage("Mot de passe copié", 1000)

    def change_size(self):
        # récupérer la valeur => actualiser le texte
        value = self.option_size.value()
        self.txt_size.setText("Taille : " + str(value))

    def generate(self):
        size = self.option_size.value()
        has_lower = self.option_lowercase.isChecked()
        has_upper = self.option_uppercase.isChecked()
        has_numbers = self.option_numbers.isChecked()
        has_symbols = self.option_symbols.isChecked()

        letters = ""
        if has_lower:
            letters += "abcdefghijklmnopqrstuvwxyz"
        if has_upper:
            letters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if has_numbers:
            letters += "0123456789"
        if has_symbols:
            letters += "$*&%@+=?"

        password = ""
        for i in range(size):
            password += choice(letters)  # from random import choice

        self.password_generated.setText(password)


app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("Password Generator")
window.show()
app.exec()
