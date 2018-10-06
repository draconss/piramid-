from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject,pyqtSignal,QPoint
class sig(QObject):
    dr = pyqtSignal(list,name='cls')
    col = pyqtSignal(list,name='colod')
seag = sig()



class update(QLabel):
    def position(self):
        self.st = self.pos()

    def init(self,parent):
        super().__init__(parent)
        self.setPixmap(QPixmap(self.up()))
        self.resize(64,90)
    def mousePressEvent(self, QMouseEvent):
        #print(self.name,self.num)
        
        if self.cli == 1 and self.test == 0:
            seag.col.emit([self])
            self.raise_()
            self.move(200,500)
            self.cli = 0
            self.position()
    def mouseReleaseEvent(self, QMouseEvent):
        
        if self.cli == 0 and self.test == 0:
            seag.dr.emit([self])
            if self.clid != 1: 
                self.move(self.st)

    def mouseMoveEvent(self, QMouseEvent):
        if self.cli == 0 and self.test == 0:
            self.raise_()
            self.move(self.mapToParent(QMouseEvent.pos()-QPoint(30,45)))

    def up(self):

        if self.test == 0:
            self.setPixmap(QPixmap(self.img))
            return self.img
        else:
            self.setPixmap(QPixmap(self.rubash))
            return self.rubash
