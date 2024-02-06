from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import *
from time import sleep
class LCloseButton(QLabel):
    def __init__(self,parent = None,):
        super(LCloseButton,self).__init__()

        self.parent = parent
        self._common = """
        #closebutton{
            border: 0px solid #ff3020;
            background-color:#303030;
        }
        """

        self.setParent(parent)
        self.setObjectName("closebutton")
        self.setStyleSheet(self._common)

        self.img = QLabel(self)
        self.img.resize(20,20)
        self.img.move(15,5)
        self.img.setPixmap(QPixmap("image/close.png"))
        self.img.setScaledContents(True)
        self.resize(50,30)

    def mouseReleaseEvent(self, QMouseEvent):
        pass
    def enterEvent(self, e):
        Thread(target=self._change_border_enter).start()
    def leaveEvent(self, e):
        Thread(target=self._change_border_leave).start()
    def _change_border_enter(self):
        for i in range(3):
            common = """
            #closebutton{
                border: %spx solid #ff3020;
                background-color:#303030;
            }
            """
            self.setStyleSheet(common%i)
            sleep(0.03)
    def _change_border_leave(self):
        for i in range(3):
            common = """
            #closebutton{
                border: %spx solid #ff3020;
                background-color:#303030;
            }
            """
            self.setStyleSheet(common%(2-i))
            sleep(0.03)

class LRehabilitationButton(QLabel):
    def __init__(self,parent = None,):
        super(LRehabilitationButton,self).__init__()

        self.parent = parent
        self._common = """
        #rehabilitationbutton{
            border: 0px solid #0078D4;
            background-color:#303030;
        }
        """

        self.setParent(parent)
        self.setObjectName("rehabilitationbutton")
        self.setStyleSheet(self._common)
        self.resize(50,30)

        self.img = QLabel(self)
        self.img.resize(20, 20)
        self.img.move(15, 5)
        self.img.setPixmap(QPixmap("image/close.png"))
        self.img.setScaledContents(True)
        self.resize(50, 30)

    def mouseReleaseEvent(self, QMouseEvent):
        pass
    def enterEvent(self, e):
        Thread(target=self._change_border_enter).start()
    def leaveEvent(self, e):
        Thread(target=self._change_border_leave).start()
    def _change_border_enter(self):
        for i in range(3):
            common = """
            #rehabilitationbutton{
                border: %spx solid #0078D4;
                background-color:#303030;
            }
            """
            self.setStyleSheet(common%i)
            sleep(0.03)
    def _change_border_leave(self):
        for i in range(3):
            common = """
            #rehabilitationbutton{
                border: %spx solid #0078D4;
                background-color:#303030;
            }
            """
            self.setStyleSheet(common%(2-i))
            sleep(0.03)

class LMinimizeButton(QLabel):
    def __init__(self,parent = None,):
        super(LMinimizeButton,self).__init__()

        self.parent = parent
        self._common = """
        #minimizebutton{
            border: 0px solid #0078D4;
            background-color:#303030;
        }
        """

        self.setParent(parent)
        self.setObjectName("minimizebutton")
        self.setStyleSheet(self._common)
        self.resize(50,25)

        self.img = QLabel(self)
        self.img.resize(20, 20)
        self.img.move(15, 5)
        self.img.setPixmap(QPixmap("image/close.png"))
        self.img.setScaledContents(True)
        self.resize(50, 30)

    def mouseReleaseEvent(self, QMouseEvent):
        pass
    def enterEvent(self, e):
        Thread(target=self._change_border_enter).start()
    def leaveEvent(self, e):
        Thread(target=self._change_border_leave).start()
    def _change_border_enter(self):
        for i in range(3):
            common = """
            #minimizebutton{
                border: %spx solid #0078D4;
                background-color:#303030;
            }
            """
            self.setStyleSheet(common%i)
            sleep(0.03)
    def _change_border_leave(self):
        for i in range(3):
            common = """
            #minimizebutton{
                border: %spx solid #0078D4;
                background-color:#303030;
            }
            """
            self.setStyleSheet(common%(2-i))
            sleep(0.03)