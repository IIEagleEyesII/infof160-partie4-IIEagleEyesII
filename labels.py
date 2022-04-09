from PyQt5.QtWidgets import QLabel

info_label = ""
def labels(self):
    player1_label = QLabel("Joueur 1:", self)
    player1_label.move(50, 60)

    player2_label = QLabel("Joueur 2:", self)
    player2_label.move(50, 100)
    # label2.setFont(QFont("Helvetica",  18)) permets d'augmenter la taille du font

    player3_label = QLabel("Délai de l'IA: ", self)
    player3_label.move(50, 140)

    info_label = QLabel("Bonjour: ", self)
    info_label.move(100, 250)
