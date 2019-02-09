import sys
import os
from time import time
from random import random
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QDesktopWidget)
from PyQt5.QtGui import (QPainter, QColor, QFont, QPen, QBrush, QPainterPath, QPolygonF,
                                QPixmap, QPalette, QImage)
from PyQt5.QtCore import QCoreApplication, Qt, QPoint, QPointF, QRect, QTimer
from math import sqrt, sin, cos, pi, radians

SCREEN_WIDTH  = 100
SCREEN_HEIGHT = 500

SQUARE_LENGTH = 400
DEPTH         = 8

BASE_ANGLE    = 45

ANIMATE       = False

FILE_NAME     = 'ArrOfStations.txt'



class Example(QWidget):
    overlay: QImage #Overlay(Накладываем) Picture on Window
    timer: QTimer #Timet init
    painter: QPainter
    
    arr_points: list
    DeltaX: int
    DeltaY: int

    def __init__(self):
        super().__init__()
        self.initUI()


    def mousePressEvent(self, event):
        WindowW = self.frameGeometry().width()#    WindowSize
        WindowH = self.frameGeometry().height()#  WindowSize
        imgH = self.overlay.height()# Picture Size
        imgW = self.overlay.width()#  Picture Size

        mousePoint = event.pos()
        img = self.overlay.scaledToHeight(WindowH, Qt.FastTransformation)

        AdjX = (WindowW-img.width())/2
        ResultX = imgW * (mousePoint.x() - AdjX) / img.width()

        ResultY = imgH * mousePoint.y() / WindowH

        radius = 10
        self.painter.drawEllipse(QPoint(ResultX, ResultY), radius, radius)
        self.arr_points.append((ResultX, ResultY))
        #print([(round(x[0]), round(x[1])) for x in self.arr_points])
        self.update()#Redraw


    def FileSaving(fileName: str):
        with open(fileName, 'w') as f:
            for item in self.arr_points:
                f.write(';'.join(str(x) for x in item) + '\n')
            f.close()


    def mouseReleaseEvent(self, event):
        self.point = None


    def closeEvent(self, event):
        FileSaving(FILE_NAME)
        sys.exit() #Programm Closing
      
            
    def initUI(self):
        self.arr_points = []
        self.timer = QTimer() #Timer init
        self.timer.timeout.connect(self.update)# Timer init
        self.setWindowTitle('Moscow Metro Map Poppularity')# Title
        self.point = None

        self.overlay = QImage()
        self.overlay.load('Moscow Metro Map Stations Popularity\\MainMap.bmp')

        pen = QPen(QColor(Qt.red))
        pen.setWidth(5)
        self.painter = QPainter(self.overlay)
        self.painter.setPen(pen)  
        self.showMaximized()
        self.timer.start(1000/15) #15 кадров в секунду


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        #windowsWidth = self.frameGeometry().width()
        windowsHeight = self.frameGeometry().height()
        
        img = self.overlay.scaledToHeight(windowsHeight, 0)
        painter.drawImage(DeltaX, DeltaY, img)
        painter.end()
        del painter
       



if __name__ == '__main__':
   #Window Settings:
   app = QApplication(sys.argv)#Init application
   ex = Example()#Init programm
   sys.exit(app.exec_())#Make Programm End when Window is closed