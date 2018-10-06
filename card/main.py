from model import *
import sys
import math
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5 import uic
from PyQt5.QtCore import Qt,QTime,QTimer
from connector import *

name_card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'quen', 'king', 'tuz']
mast_card = ['pick', 'chirv', 'crest', 'buba']
impage = [['p2.bmp','p3.bmp','p4.bmp','p5.bmp','p6.bmp','p7.bmp','p8.bmp','p9.bmp','p10.bmp','p11.bmp','p12.bmp','p13.bmp','p1.bmp'],
          ['ch2.bmp','ch3.bmp','ch4.bmp','ch5.bmp','ch6.bmp','ch7.bmp','ch8.bmp','ch9.bmp','ch10.bmp','ch11.bmp','ch12.bmp','ch13.bmp','ch1.bmp'],
          ['c2.bmp','c3.bmp','c4.bmp','c5.bmp','c6.bmp','c7.bmp','c8.bmp','c9.bmp','c10.bmp','c11.bmp','c12.bmp','c13.bmp','c1.bmp'],
          ['b2.bmp','b3.bmp','b4.bmp','b5.bmp','b6.bmp','b7.bmp','b8.bmp','b9.bmp','b10.bmp','b11.bmp','b12.bmp','b13.bmp','b1.bmp']]
rubas_card = 'rub.bmp'

class prvl(QWidget):
    def __init__(self,obj):
        super().__init__()
        self.ui = uic.loadUi('dop.ui')
        self.defalut = [0, 0, 0, 0]
        self.obj = obj
        self.defalut[2] = self.ui.time.time()
        self.defalut[3] = self.ui.time.time()
        self.obj.ui.lcds.display(str(self.defalut[2].minute())+":"+str(0))
        self.initUI()
        self.ui.show()


    
        
    def initUI(self):
        self.ui.buttonBox.accepted.connect(self.acc)
        self.ui.buttonBox.rejected.connect(self.rej)
        self.ui.ch1.stateChanged.connect(self.mast)
        self.ui.ch2.stateChanged.connect(self.time)
        self.ui.time.timeChanged.connect(self.num)
        
    def time(self,s):
        if s == 2:
            self.defalut[1] = 1
        else:
            self.defalut[1] = 0
    def mast(self,s):
        if s == 2:
            self.defalut[0] = 1
        else:
            self.defalut[0] = 0
    def acc(self):
        self.obj.defalut = self.defalut
        if self.defalut[1] == 0:
            self.obj.timer.stop()
        elif self.defalut[1] == 1:
            self.obj.timer.start(1000)
        self.ui.close()
    def rej(self):
        self.ui.close()
    def num(self,e):
        self.obj.ui.lcds.display(str(e.minute())+":"+str(e.second()))
        self.defalut[2] = self.ui.time.time()
        self.defalut[3] = self.ui.time.time()


class d(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('1.ui')
        self.cod = []
        self.defalut = [0,0,0,0]
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.numd)
        self.mti = QTimer(self)
        self.mti.timeout.connect(self.who)
        self.mti.start(5000)
        self.initUI()
        self.tr()
        self.ui.show()
    def initUI(self):
        self.pl = QMediaPlayer(self)
        self.pl.setMedia(QMediaContent(QUrl('res/music.mp3')))
        self.revrsi = -1
        
        self.btn = QPushButton('0',self.ui)
        self.btn.move(100,500)
        self.btn.resize(62,91)
        
        self.setGeometry(100,100,800,800)
        self.ui.setStyleSheet("QMainWindow { background-color: green; }")
        
        self.btn.clicked.connect(self.colod)
        seag.dr.connect(self.pirf)
        seag.col.connect(self.colod)
        self.ui.newgs.triggered.connect(self.tr)
        self.ui.nst.triggered.connect(self.cread)
        self.ui.check.triggered.connect(self.check)
        self.ui.exs.triggered.connect(self.ui.close)
        self.ui.on_of.clicked.connect(self.media)
        
        self.btn.show()
    def who(self):
        if self.revrsi == 1 and self.pl.state() == 0:
            self.pl.play()
    def media(self):
        self.revrsi = -self.revrsi
        if self.revrsi == -1:
            self.pl.pause()
            self.ui.on_of.setIcon(QIcon('res/off.png'))
        else:
            self.pl.play()
            self.ui.on_of.setIcon(QIcon('res/on.png'))
        
    def check(self):
        if len(self.b.reck) > 0:
            self.b.back()
            for i in self.b.pir:
                for j in i:
                    j.raise_()
                    if j.clid == 1 and j.test == 3:
                        j.clid = 0
                        j.test = 0
                        j.move(j.st)
            for j in self.b.cold.list_colod:
                if j.clid == 1 and j.test == 3:
                        j.clid = 0
                        j.test = 0
                        j.raise_()
                        j.move(j.st)
        self.b.block()
    def numd(self):
        self.defalut[2] = self.defalut[2].addSecs(-1)
        self.ui.lcds.display(str(self.defalut[2].minute())+":"+str(self.defalut[2].second()))
        if QTime(0,0,0) == self.defalut[2]:
            self.fun_win('You lose')
            self.timer.stop()
    
    def cread(self):
        self.nst = prvl(self)

    def game(self):
        self.a = colod(name_card,mast_card,rubas_card,impage)
        self.b = game('()()()',self.a)
        self.b.void_sp.init(self)
    def deli(self):
        del self.a
        del self.b
        for i in range(len(self.sd)):
            del self.sd[0]
    def tr(self):
        sender = self.sender()
        if sender:
            if sender.text() == 'нов':
                self.deli()
        self.sd = self.ui.findChildren(card)
        if self.defalut[1] == 1:
            self.timer.start(1000)
            self.defalut[2] = self.defalut[3]
        if self.sd:
            for i in self.sd:
                i.hide()
        self.game()
        self.cra()
        self.b.block()
        if sender:
            if sender.text() == 'You Win' or sender.text() == 'You lose':
                sender.hide()
                sender.disconnect()

    def colod(self,a):
        if self.b.peremsh() == 1:
            for i in range(len(self.b.cold.cold_cards) - 1, -1, -1):
                self.b.cold.cold_cards[i].raise_()
                self.b.cold.cold_cards[i].move(100, 500)
                self.b.cold.cold_cards[i].cli = 1
    def convert(self):
        self.cod = []
        for i in self.b.pir:
            for j in i:
                self.cod.append(j)
                if j.test == 23 and j.initial == 0:
                    j.init(self.ui)

    def pirf(self,ob):
        self.convert()
        obj = ob[0]
        if self.b.king(obj.cord) == 0:
            self.b.block()
            obj.clid = 1
            obj.test = 3
            obj.move(self.ui.rec.pos())
            

        for i in self.cod:
            if i != obj:
                eq1 = (i.x() - obj.x())**2
                eq2 = (i.y() - obj.y())**2
                line = math.sqrt(eq1+eq2)
                if line <= 40 and i.test == 0:
                    if self.defalut[0] == 0:
                        if self.b.void(obj.cord,i.cord) == 1:
                            obj.clid = 1
                            obj.test = 3
                            i.clid = 1
                            i.test = 3
                            self.b.block()
                            obj.move(self.ui.rec.pos())
                            i.move(self.ui.rec.pos())
                    elif self.defalut[0] == 1 and obj.mast == i.mast:
                        if self.b.void(obj.cord,i.cord) == 1:
                            obj.clid = 1
                            obj.test = 3
                            i.clid = 1
                            i.test = 3
                            self.b.block()
                            obj.move(self.ui.rec.pos())
                            i.move(self.ui.rec.pos())
                            
        if self.b.win() == 1:
            self.fun_win('You Win')
        obj = []



    def fun_win(self,you):
        win = QPushButton(you,self.ui)
        win.clicked.connect(self.tr)
        win.move(300,200)
        win.show()
        
    def cra(self):
        self.s = self.ui.findChildren(QLabel)
        self.pir = [self.s[0:1], self.s[1:3], self.s[3:6], self.s[6:10],
                    self.s[10:15], self.s[15:21], self.s[21:28]]
        for i in range(len(self.pir)):
            for j in range(len(self.pir[i])):
                self.b.pir[i][j].cord = [i,j]
                self.b.pir[i][j].init(self.ui)
                self.b.pir[i][j].move(self.pir[i][j].pos())
                self.b.pir[i][j].position()
                self.b.pir[i][j].show()
        for i in range(len(self.b.cold.cold_cards)-1,-1,-1):
            self.b.cold.cold_cards[i].cord = [8,1]
            self.b.cold.cold_cards[i].init(self.ui)
            self.b.cold.cold_cards[i].move(100,500)
            self.b.cold.cold_cards[i].cli = 1
            self.b.cold.cold_cards[i].show()
            self.b.cold.cold_cards[i].raise_()

app = QApplication(sys.argv)
v = d()
sys.exit(app.exec_())
