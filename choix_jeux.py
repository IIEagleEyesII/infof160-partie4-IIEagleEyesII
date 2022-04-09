from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel


def comboBox(self):
    combo_joueur1 = QtWidgets.QComboBox(self)
    combo_joueur1.setGeometry(110, 60, 850, 30)
    combo_joueur1.addItems(["Minimax", "Joueur humain"])
    # combo.setFont()

    combo_joueur2 = QtWidgets.QComboBox(self)
    combo_joueur2.setGeometry(110, 100, 850, 30)
    combo_joueur2.addItems(["Minimax", "Joueur humain"])


def index_changed(self, i): # i is an int
    print(i)

def text_changed(self, s): # s is a str
    print(s)








