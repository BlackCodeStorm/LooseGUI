from PyQt5.QtWidgets import *
from threading import *
from time import sleep
# s="e2802b ed6927 101702"

class LSelect(QLabel):
    def __init__(self,
                 width = 200,
                 height = 200,
                 rcs ="5",
                 parend = None,
                 fs = "1",
                 fscr = "3",
                 fc="#afafaf",
                 cfs="3",
                 cfscr = "3",
                 cfc = "#0078D4"):
        super(LSelect,self).__init__()

        self._WidgetColor = "#333333"
        self._RoundedCornersSize = rcs
        self._WidgetState = False
        self._WidgetSize = (width, height)

        self._FrameSize = fs
        self._FraneStyle = "solid"
        self._FrameColor = fc
        self._FrameSizeChangeRange = fscr

        self._ChooseFrameSize = cfs
        self._ChooseFraneStyle = "solid"
        self._ChooseFrameColor = cfc
        self._ChooseFrameSizeChangeRange = cfscr

        self._common = """
        #LSelect{
          border-radius: %spx;
          border: %spx %s %s;
          background:%s;
        }
        """ % (self._RoundedCornersSize,
             self._FrameSize,
             self._FraneStyle,
             self._FrameColor,
             self._WidgetColor)

        self.setObjectName("LSelect")
        self.setStyleSheet(self._common)
        self.setParent(parend)
        self.resize(self._WidgetSize[0],self._WidgetSize[1])

    def enterEvent(self,e):
        Thread(target=self._change_border_enter).start()
    def leaveEvent(self,e):
        Thread(target=self._change_border_leave ).start()
    def mousePressEvent(self, event):
        if event.button() == 1:
            if self._WidgetState == True:
                self._WidgetState = False
            else:
                self._WidgetState = True
        else:
            pass
        if self._WidgetState:
            self._common = """
                    #LSelect{
                      border-radius: %spx;
                      border: %spx %s %s;
                      background:%s;
                    }
                    """ % (self._RoundedCornersSize,
                           str(int(self._ChooseFrameSize) + int(self._ChooseFrameSizeChangeRange)-1),
                           self._ChooseFraneStyle,
                           self._ChooseFrameColor,
                           self._WidgetColor)
            self.setStyleSheet(self._common)
        else:
            self._common = """
                    #LSelect{
                      border-radius: %spx;
                      border: %spx %s %s;
                      background:%s;
                    }
                    """ % (self._RoundedCornersSize,
                           str(int(self._FrameSize) + int(self._FrameSizeChangeRange)-1),
                           self._FraneStyle,
                           self._FrameColor,
                           self._WidgetColor)
            self.setStyleSheet(self._common)
    def _change_border_enter(self):
        if self._WidgetState:
            for i in range(int(self._ChooseFrameSizeChangeRange)):
                common = """
                        #LSelect{
                            border-radius: %spx;
                            border: %spx %s %s;
                            background:%s;
                        }
                        """ % (self._RoundedCornersSize,
                               str(int(self._ChooseFrameSize) + i),
                               self._ChooseFraneStyle,
                               self._ChooseFrameColor,
                               self._WidgetColor)
                self.setStyleSheet(common)
                sleep(0.02)
        else:
            for i in range(int(self._FrameSizeChangeRange)):
                common = """
                        #LSelect{
                            border-radius: %spx;
                            border: %spx %s %s;
                            background:%s;
                        }
                        """ % (self._RoundedCornersSize,
                               str(int(self._FrameSize) + i),
                               self._FraneStyle,
                               self._FrameColor,
                               self._WidgetColor)
                self.setStyleSheet(common)
                sleep(0.02)
    def _change_border_leave(self):
        if self._WidgetState:
            for i in range(int(self._FrameSizeChangeRange)):
                common = """
                        #LSelect{
                            border-radius: %spx;
                            border: %spx %s %s;
                            background:%s;
                        }
                        """ % (self._RoundedCornersSize,
                               str(int(self._ChooseFrameSize) + int(self._ChooseFrameSizeChangeRange) - i -1),
                               self._ChooseFraneStyle,
                               self._ChooseFrameColor,
                               self._WidgetColor)
                self.setStyleSheet(common)
                sleep(0.02)
        else:
            for i in range(int(self._FrameSizeChangeRange)):
                common = """
                        #LSelect{
                            border-radius: %spx;
                            border: %spx %s %s;
                            background:%s;
                        }
                        """ % (self._RoundedCornersSize,
                               str(int(self._FrameSize) + int(self._FrameSizeChangeRange) - i -1),
                               self._FraneStyle,
                               self._FrameColor,
                               self._WidgetColor)
                self.setStyleSheet(common)
                sleep(0.02)

class LLittleInputBox(QLineEdit):
    def __init__(self,
                 width = 400,
                 height = 60,
                 parend = None,
                 rcs ="5",
                 fs = "1",
                 fscr = "3",
                 fc = "#0078D4"):
        super(LLittleInputBox,self).__init__()

        self._WidgetSize = (width,height)
        self._RoundedCornersSize = rcs
        self._FrameSizeChangeRange = fscr
        self._WidgetColor = "#333333"
        self._FrameSize = fs
        self._FraneStyle = "solid"
        self._FrameColor = fc

        self._common = """
        #LInputBox{
            border-radius: %spx;
            border: %spx %s %s;
            background-color:%s;
            font-size:30px;
            color:#ffffff;
        }
        """%(self._RoundedCornersSize,
             self._FrameSize,
             self._FraneStyle,
             self._FrameColor,
             self._WidgetColor
             )

        self.setParent(parend)
        self.setObjectName("LInputBox")
        self.setStyleSheet(self._common)
        self.resize(self._WidgetSize[0],self._WidgetSize[1])
    def enterEvent(self, e):
        Thread(target=self._change_border_enter).start()
    def leaveEvent(self, e):
        Thread(target=self._change_border_leave).start()
    def _change_border_enter(self):
        for i in range(int(self._FrameSizeChangeRange)):
            common = """
            #LInputBox{
                border-radius: %spx;
                border: %spx %s %s;
                background-color:%s;
                font-size:30px;
                color:#ffffff;
            }
            """ % (self._RoundedCornersSize,
                       str(int(self._FrameSize) + i),
                       self._FraneStyle,
                       self._FrameColor,
                       self._WidgetColor
                       )
            self.setStyleSheet(common)
            sleep(0.02)
    def _change_border_leave(self):
        for i in range(int(self._FrameSizeChangeRange)):
            common = """
            #LInputBox{
                border-radius: %spx;
                border: %spx %s %s;
                background-color:%s;
                font-size:30px;
                color:#ffffff;
            }
            """ % (self._RoundedCornersSize,
                    str(int(self._FrameSize) + int(self._FrameSizeChangeRange) - i - 1),
                    self._FraneStyle,
                    self._FrameColor,
                    self._WidgetColor
                    )
            self.setStyleSheet(common)
            sleep(0.02)


