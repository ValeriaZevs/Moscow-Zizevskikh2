import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap, QColor
from PyQt5.QtCore import Qt
import random


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('circles.ui', self)
        self.setWindowTitle('Circles all around')
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)
        painter = QPainter(self.label.pixmap())
        for i in range(7):
            t, t1, t2 = random.randrange(256), random.randrange(256), random.randrange(256)
            painter.setPen(QPen(QColor(t, t1, t2), 5, Qt.SolidLine))
            painter.setBrush(QBrush(QColor(t, t1, t2), Qt.SolidPattern))
            c = random.randrange(200)
            painter.drawEllipse(random.randrange(500), random.randrange(500), c, c)



if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())