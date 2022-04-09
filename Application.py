import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QComboBox,QGroupBox
from PyQt5.QtGui import QIcon, QPainter, QPen, QBrush, QFont, QPalette
from PyQt5.QtCore import pyqtSlot , Qt
from players import MinimaxAiPlayer, HumanPlayer
from breakthrough import Breakthrough
import buttons
import labels
import choix_jeux
import buttons
import labels
import choix_jeux

class App(QWidget):

    def __init__ ( self ):
        super (). __init__ ()
        self . title = "INFO F-106"
        self . left = 500
        self . top = 100
        self . width = 1000
        self . height = 700
        self . initUI ()

    def initUI ( self ):
        self . setWindowTitle ( self . title )
        self . setGeometry ( self.left , self.top , self .width , self . height )



        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)

        #creation d'un petit rectangle
        self.createHorizontalLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        comboBox = choix_jeux.comboBox(self)

        button = buttons.add_button(self)

        # slide = internet.slide(self)
        self.create_widgets()

        self.show()

    @pyqtSlot()
    def on_click1(self):
        buttons.on_click1(self)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black ))
        painter.drawRect( int((self.left * 3)/50) , int((self.top * 2)/5) , int((self.width * 47)/50) , int((self.height * 3)/14))

    @pyqtSlot()
    def on_click(self):
        buttons.on_click(self)

    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("Parameters")

    def foo(self, s):
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

    def check(self, c):
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
        s = self.foo([[1,2,1,2,0],[1,1,1,1,1],[0,0,0,0,0],[2,2,2,2,2],[1,2,1,2,0]])
        # print(s)
        for l in s:
            print(l)
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
                self.string.setGeometry(400 + (s.index(l) * 50), 300 + (l.index(string) * 50), 50, 50)
                self.string.setIconSize(QtCore.QSize(50, 50))


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
                self.string.setGeometry(100 + (s.index(l) * 50), 100 + (l.index(string) * 50), 50, 50)
                self.string.setIconSize(QtCore.QSize(50, 50))


"""app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
"""

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit ( app.exec_ ())

#l = [[1,2,1,2,0],[1,1,1,1,1],[0,0,0,0,0],[2,2,2,2,2],[1,2,1,2,0]]