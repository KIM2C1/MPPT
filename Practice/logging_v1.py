import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


form_class = uic.loadUiType("loggingui_v1.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 