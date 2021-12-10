import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.createCircleButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.createCircle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def createCircle(self, qp):
        size = random.randint(0, 200)
        x, y = random.randint(0, 400), random.randint(0, 400)

        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, size, size)


def main():
    app = QApplication(sys.argv)
    process = YellowCircles()
    process.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
