import random
from sing import *
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QMimeData,QPoint
from connector import *

# class for card replacement
class space(QLabel):
    def __init__(self,rubash):
        self.rubash = rubash
        self.test = 23
        self.initial = 0
        self.clid = None

    def init(self,parent):
        super().__init__(parent)
        self.setPixmap(QPixmap(None))
        self.initial = 1
        self.st = self.pos()
    def up(self):
        return self.rubash
    def __str__(self):
        return self.rubash
    def nam(self):
        pass
# class of creating maps
class card(update):
    def __init__(self,name,mast,num,rubash,img):
        self.num = int(num)
        self.mast = mast
        self.name = name
        self.rubash = rubash
        self.img = img
        self.test = 0
        self.cli = 0
        self.clid = 0

    def __str__(self):
        if self.test == 0:
            return str(self.name)+' '+str(self.mast)
        else:
            return self.rubash

    def nam(self):
        return self.num

class colod:
    def __init__(self,name,mast,rubash,img):
        self.__rubash = rubash
        self.__name = name
        self.__mast = mast
        self.__img = img
# starting deck
        self.cold_cards = []
# the end deck
        self.list_colod = []

        self.create_cards()
        self.gen_cold()
# shuffle cards
    def gen_cold(self):
        random.shuffle(self.cold_cards)
# create maps
    def create_cards(self):
        for i in range(4):
            for j in range(13):
                self.cold_cards.append(card(self.__name[j], self.__mast[i], game.num[j],'res/'+self.__rubash,'res/'+self.__img[i][j]))

# debugging function for creating a pyramid
    def check(self,num):
        for i in range(num):
            self.cold_cards.pop(0)

class game:
    num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
    def __init__(self,rub,colod):
        self.reck = [] # Dustbin
        self.pir = [] # Pyramid
        self.cold = colod # creating a deck
        self.void_sp = space(rub) #fold space
        self.creat_pir(self.cold)# creating a pyramid

# card splitting
    def creat_pir(self,clas):
        self.pir = [clas.cold_cards[0:1], clas.cold_cards[1:3], clas.cold_cards[3:6], clas.cold_cards[6:10],
                    clas.cold_cards[10:15], clas.cold_cards[15:21], clas.cold_cards[21:28]]
        clas.check(28)
# removing the king
    def king(self,obj):
        y,x = obj
        pir_card = self.pir
        cold_card = self.cold.list_colod
        if (y != 8 and pir_card[y][x].nam() == 13) and (pir_card[y][x].up() != pir_card[y][x].rubash and pir_card[y][x] != self.void_sp):
            self.reck.append([ [pir_card[y][x],y,x] ])
            pir_card[y][x] = self.void_sp
            
            return 0
            
        elif (len(cold_card) - 1) >= 0 and cold_card[len(cold_card) - 1].nam() == 13 and y == 8:
            self.reck.append([ [cold_card[len(cold_card)-1],8] ])
            cold_card.pop()
            
            return 0
        else:
            return 1
# card removal
    def void(self,obj,obj1):
        y1,x1 = obj
        y2,x2 = obj1
        et = 0
        pir_card = self.pir
        cold_card = self.cold.list_colod

        sum = 0
        if y1 == 8 and (pir_card[y2][x2].up() != pir_card[y2][x2].rubash and pir_card[y2][x2] != self.void_sp):
            sum = cold_card[len(cold_card) - 1].nam() + pir_card[y2][x2].nam()

        elif (pir_card[y1][x1].up() != pir_card[y1][x1].rubash and pir_card[y1][x1] != self.void_sp) and (pir_card[y2][x2].up() != pir_card[y2][x2].rubash and pir_card[y2][x2] != self.void_sp):
            sum = pir_card[y1][x1].nam() + pir_card[y2][x2].nam()
        if sum == 13 and y1 == 8:
            self.reck.append([ [cold_card[len(cold_card) - 1],8], [pir_card[y2][x2],y2,x2] ])
            cold_card.pop()
            pir_card[y2][x2] = self.void_sp
            et = 1
        elif sum == 13:
            self.reck.append([ [pir_card[y1][x1], y1, x1] , [pir_card[y2][x2], y2, x2] ])
            pir_card[y1][x1] = self.void_sp
            pir_card[y2][x2] = self.void_sp
            et = 1
        return et

# inverting the deck and cleaning
    def peremsh(self):
        cold_card = self.cold.cold_cards
        two = self.cold.list_colod
        nast = self.void_sp.rubash
        if len(cold_card) <= 0:
            self.cold.cold_cards = self.cold.list_colod
            self.cold.list_colod = []
            return 1

        elif len(self.cold.cold_cards) != 0:
            self.cold.list_colod.append(cold_card[0])
            self.cold.cold_cards.pop(0)

        for i in range(len(two)):
            if two[i].rubash == nast:
                two.pop[i]
        
#definition is open or closed card in the pyramid
    def block(self):
        for i in range(len(self.pir)):
            for j in range(i+1):
                if i < 6:
                    if self.pir[i+1][j] != self.void_sp or self.pir[i+1][j+1] != self.void_sp:
                        self.pir[i][j].test = 1
                        self.pir[i][j].up()
                    elif self.pir[i+1][j] == self.void_sp and self.pir[i+1][j+1] == self.void_sp:
                        self.pir[i][j].test = 0
                        self.pir[i][j].up()
# move back without regard to order in the deck
    def back(self):
        hod = self.reck[len(self.reck)-1]
        if len(hod) > 1 and hod[0][1] == 8:
            self.cold.list_colod.append(hod[0][0])
            self.pir[hod[1][1]][hod[1][2]] = hod[1][0]
            del self.reck[len(self.reck)-1]
        elif len(hod) > 1:
            self.pir[hod[0][1]][hod[0][2]] = hod[0][0]
            self.pir[hod[1][1]][hod[1][2]] = hod[1][0]
            del self.reck[len(self.reck)-1]

        elif len(hod) == 1 and hod[0][1] == 8:
            self.cold.list_colod.append(hod[0][0])
            del self.reck[len(self.reck)-1]

        elif len(hod) == 1 and hod[0][1] != 8:
            self.pir[hod[0][1]][hod[0][2]] = hod[0][0]
            del self.reck[len(self.reck)-1]
# debugging function
    def history(self):
        return self.reck
# determination of victory
    def win(self):
        if self.pir[0][0] == self.void_sp:
            return 1
