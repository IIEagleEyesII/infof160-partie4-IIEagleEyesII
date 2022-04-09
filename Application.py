import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget,QComboBox,QComboBox,QGroupBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QPainter, QPen, QBrush, QFont, QPalette
from PyQt5.QtCore import pyqtSlot , QObject
from players import MinimaxAiPlayer, HumanPlayer
from breakthrough import Breakthrough
import time as t
from PyQt5.QtCore import Qt

class App(QWidget):
    '''Class app  affiche l'interface graphic qui comporte:
     un combo box : — le choix d’un joueur humain ou IA (MCTS, Minimax...) pour chaque joueur ;
     un Qdial
     '''
    def __init__ ( self,matrice = [[1, 1, 1, 1, 1,1,1], [1, 1, 1, 1, 1,1,1], [0, 0, 0, 0, 0,0,0], [0, 0, 0, 0, 0,0,0], [0, 0, 0, 0, 0,0,0], [2,2,2, 2, 2, 2, 2], [2,2,2, 2, 2, 2, 2]] ):
        self.matrice = matrice
        super (). __init__ ()
        self . title = "INFO F-106 Breakthrough game"
        self . left = 540
        self . top = 100
        self . width = 1050
        self . height = 900
        self . initUI ()


    def initUI ( self ):
        self . setWindowTitle ( self . title )
        self . setGeometry ( self.left , self.top , self .width , self . height )

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray )
        self.setPalette(p)
        self.labels()

        #creation d'un petit rectangle
        self.createHorizontalLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.comboBox()
        self.create_widgets()
        self.bouttons()


        self.show()


    def click_charger(self):
        '''Charger la matrice '''


    def click_start(self):
        '''commencer la partie'''
        #Breakthrough().play()

    def bouttons(self):
        change_button = QPushButton('Charger', self)
        change_button.setGeometry(30, 200, 80, 30)
        change_button.clicked.connect(self.click_charger)

        start_button = QPushButton('Commencer', self)
        start_button.setGeometry(20, 800, 1000, 30)
        start_button.clicked.connect(self.click_start)


    def comboBox(self):
        combo_joueur1 = QComboBox(self)
        combo_joueur1.setGeometry(110, 60, 850, 30)
        combo_joueur1.addItems(["Minimax", "Joueur humain"])
        # combo.setFont()

        combo_joueur2 = QComboBox(self)
        combo_joueur2.setGeometry(110, 100, 850, 30)
        combo_joueur2.addItems(["Minimax", "Joueur humain"])

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black ))
        painter.drawRect(int((self.left * 3)/50) , int((self.top * 2)/5) , int((self.width * 47)/50) , int((self.height * 3)/14))

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

    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("Parameters")

    def foo(self, s):
        '''Une fonction qui prends une matrice en parametre et renvoie une autre matrice qui contiens des differents strings avec tel que :
        string[0]= position selon x ,string[1] = position selon y
        if len(string) == 2 : la case contient 0 donc aucun pion
        if len(string) == 4 : la case contient 1 donc aucun pion blanc
        if len(string) == 6 : la case contient 0 donc aucun pion noir
        '''
        le = len(s)
        l = []
        for i in range(le):
            l.append([])
        for i in range(len(s)):
            for j in range(len(s[i])):
                string = f"{i}{j}"
                if s[i][j] == 0:
                    l[i].append((string))
                elif s[i][j] == 1:
                    l[i].append((string) * 2)
                else:
                    l[i].append((string) * 3)
        l = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]) - 1, -1, -1)] #une rotation de 90deg de la matrice pour l'afficher correctement
        return l

    def check(self, c):
        '''Fonction pour placer les icones foncées et claires dans leurs places
        returns float (foncée) , int(claire) '''
        if len(c) == 2:
            if (int(c[0]) + int(c[1])) % 2 == 0:
                res = 0.0
            else:
                res = 0
        elif len(c) == 4:
            if (int(c[0]) + int(c[1])) % 2 == 0:
                res = 1.0
            else:
                res = 1
        else:
            if (int(c[0]) + int(c[1])) % 2 == 0:
                res = 2
            else:
                res = 2.0
        return res

    def create_widgets(self):
        s = self.foo(self.matrice)
        for l in s:
            for string in l:
                self.string = string
                if self.check(string) == 0:
                    if type(self.check(string)) is float:
                        self.string = QPushButton("", self)
                        self.string.setIcon(
                            QtGui.QIcon('/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/light.png'))
                    else:
                        self.string = QPushButton("", self)
                        self.string.setIcon(
                            QtGui.QIcon('/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/dark.png'))
                elif self.check(string) == 1:
                    if type(self.check(string)) is float:
                        self.string = QPushButton("", self)
                        self.string.setIcon(QtGui.QIcon(
                            '/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/black light.png'))
                    else:
                        self.string = QPushButton("", self)
                        self.string.setIcon(
                            QtGui.QIcon('/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/black dark.png'))
                else:
                    if type(self.check(string)) is float:
                        self.string = QPushButton("", self)
                        self.string.setIcon(
                            QtGui.QIcon('/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/white dark.png'))
                    else:
                        self.string = QPushButton("", self)
                        self.string.setIcon(QtGui.QIcon(
                            '/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/white light.png'))
                self.string.setGeometry(330 + (s.index(l) * 50), 290 + (l.index(string) * 50), 50, 50)
                self.string.setIconSize(QtCore.QSize(50, 50))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())













''' def creat_grid(self, board):
    for i in range(board.getlines):
        line = QWidget()
        line.setLayout(QHBoxLayout())
        line.layout().setSpacing(0)
        line.layout().setContentsMargins(0, 0, 0, 0)
        for j in range(board.getcols):
            new_square = QPushButton()
            new_square.clicked.connect(partial(self.grid_button_click(i, j)))
            new_square.setFixedSize(self.grid_width // board.getcols, self.grid_height // board.getlines)
            new_square.setStyleSheet("background-color: lightgreen" if (i + j) % 2 else "background-color: green")
        square_data = board.get.getSquaredata(((i, j)))
        if square_data == 1:
            new_square.setIcon("graphic pion blanc.png")
        if square_data == 2:
            new_square.setIcon("graphic pion noir.png")
        new_square.setIconSize(50, 50, 50, 50)
        board.setButton((i, j), new_square)
        line.Layout().addWidget(new_square)
    self.Layout.addWidget(line)'''

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Info F-106 Breakthrough game")
        # self.setStyleSheet('background-color:lightgreen')
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.player = 1
        self.opponent = None
        self.opponentID = 2
        self.matrix = [[1,2,1,2,0],[1,1,1,1,1],[0,0,0,0,0],[2,2,2,2,2],[1,2,1,2,0]]
        #self.matrix = Breakthrough.make_default_board(self)
        self.initUI()

    def initUI(self):
        # self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar.')
        self.create_widgets()
        self.show()

  


    def create_widget(self):

        self.IA = QPushButton("", self)
        self.IA.setIcon(QtGui.QIcon('IBM_PC_5150.jpg'))
        self.IA.setIconSize(QtCore.QSize(150, 150))
        self.IA.setGeometry(50, 100, 100, 100)
        self.AI_Label = QLabel("opponent is IA", self)
        self.AI_Label.setGeometry(50, 200, 200, 50)
        self.AI_Label.setStyleSheet('color: purple')
        self.IA.clicked.connect(self.jouer_contre_IA)

        self.Player2 = QPushButton("", self)
        self.Player2.setIcon(QtGui.QIcon('FInal-game-position2.jpg'))
        self.Player2.setGeometry(230, 100, 100, 100)
        self.Player2.setIconSize(QtCore.QSize(150, 150))
        self.Player2.clicked.connect(self.jouer_contre_humain)
        self.Player2_Label = QLabel("opponent is homosapiens", self)
        self.Player2_Label.setGeometry(230, 200, 200, 50)
        self.Player2_Label.setStyleSheet('color: purple')


        self.black_peg = QPushButton("", self)
        self.black_peg.setGeometry(50, 250, 100, 100)
        self.black_peg.setIconSize(QtCore.QSize(100, 100))
        self.black_peg.setIcon(QtGui.QIcon('Capture d’écran 2022-04-07 à 16.05.43.png'))
        self.black_peg_Label = QLabel("use black pegs", self)
        self.black_peg_Label.setGeometry(50, 350, 200, 50)
        self.black_peg_Label.setStyleSheet('color: purple')
        self.black_peg.clicked.connect(self.use_black_peg)

        self.white_peg = QPushButton("", self)
        self.white_peg.setIcon(QtGui.QIcon('Capture d’écran 2022-04-07 à 16.05.56.png'))
        self.white_peg.setGeometry(230, 250, 100, 100)
        self.white_peg.setIconSize(QtCore.QSize(100, 100))
        self.white_peg_Label = QLabel("use white pegs", self)
        self.white_peg_Label.setGeometry(230, 350, 200, 50)
        self.white_peg_Label.setStyleSheet('color: purple')
        self.white_peg.clicked.connect(self.use_white_peg)

    def jouer_contre_IA(self):
        self.opponent = MinimaxAiPlayer(self.opponentID,Board)
    def jouer_contre_humain(self):
        self.opponent = HumanPlayer(self.player,Board)
    def use_black_peg(self):
        self.player = 1
        self.opponentID = 2
    def use_white_peg(self):
        self.player = 2
        self.opponentID = 1

    def foo(self,s):
        print(s)
        le = len(s)
        l = []
        for i in range(le):
            l.append([])
        for i in range(len(s)):
            for j in range(len(s[i])):
                string = f"{i}{j}"
                if s[i][j] == 0:
                    l[i].append((string))
                elif s[i][j] == 1:
                    l[i].append((string) * 2)
                else:
                    l[i].append((string) * 3)
        l = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]) - 1, -1, -1)]
        return l

    def check(self,c):
        if len(c) == 2:
            if (int(c[0]) + int(c[1])) % 2 == 0:
                res = 0.0
            else:
                res = 0
        elif len(c) == 4:
            if (int(c[0])+int(c[1]))%2 == 0:
             res = 1.0
            else:
                res = 1
        else:
            if (int(c[0]) + int(c[1])) % 2 == 0:
                res = 2
            else :
                res = 2.0
        return res

    def create_widgets(self):
        s = self.foo(self.matrix)
        #print(s)
        for l in s :
            print(l)
            for string in l :
                self.string = string
                if self.check(string) == 0 :
                    if type(self.check(string)) is float :
                        self.string = QPushButton("", self)
                        self.string.setIcon(QtGui.QIcon('/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/light.png'))
                    else :
                        self.string = QPushButton("", self)
                        self.string.setIcon(QtGui.QIcon('/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/dark.png'))
                elif self.check(string) == 1:
                    if type(self.check(string)) is float:
                        self.string = QPushButton("",self)
                        self.string.setIcon(QtGui.QIcon('/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/black light.png'))
                    else:
                        self.string = QPushButton("", self)
                        self.string.setIcon(QtGui.QIcon('/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/black dark.png'))
                else :
                    if type(self.check(string)) is float:
                        self.string = QPushButton("", self)
                        self.string.setIcon(QtGui.QIcon('/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/white dark.png'))
                    else :
                        self.string = QPushButton("", self)
                        self.string.setIcon(QtGui.QIcon('/Users/souadbouterfass/Desktop/infof160-partie4-IIEagleEyesII/white light.png'))
                self.string.setGeometry(50 + (s.index(l) * 50), 100 + (l.index(string) * 50), 50, 50)
                self.string.setIconSize(QtCore.QSize(50, 50))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
'''



#l = [[1,2,1,2,0],[1,1,1,1,1],[0,0,0,0,0],[2,2,2,2,2],[1,2,1,2,0]]