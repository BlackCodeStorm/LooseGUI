from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from modules import titlebox


class LMainWindow(QMainWindow):
    def __init__(self,w = 1120,h = 700):
        super(LMainWindow,self).__init__()
        self.resize(w,h)
        self.setObjectName("rootwindow")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("#rootwindow{background-color:#303030;}")

        self.closebutton = titlebox.LCloseButton(self)
        self.closebutton.move(1070,0)
        self.closebutton.show()

        self.closebutton = titlebox.LRehabilitationButton(self)
        self.closebutton.move(1020, 0)
        self.closebutton.show()

        self.closebutton = titlebox.LMinimizeButton(self)
        self.closebutton.move(970, 0)
        self.closebutton.show()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == 1:
            self.m_drag=True
            self.m_DragPosition= QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False

app = QApplication([])
root = LMainWindow()
root.show()
app.exec()
