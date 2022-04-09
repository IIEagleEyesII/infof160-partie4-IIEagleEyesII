from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton
#import partie3
import choix_jeux


def add_button(objet):
    change_button = QPushButton('Charger', objet)
    change_button.setGeometry(30, 200, 80, 30)
    change_button.clicked.connect(objet.on_click)


    start_button = QPushButton('Commencer', objet)
    start_button.setGeometry(20, 650, 960, 30)
    start_button.clicked.connect(objet.on_click1)


@pyqtSlot()
def on_click(self):

    print("OUI")

@pyqtSlot()
def on_click1(self):
    print(6)