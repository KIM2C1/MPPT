import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer

form_class = uic.loadUiType("testui.ui")[0]

class WindowClass(QWidget):
    def __init__(self):
        super().__init__()
        self.label_4 = QLabel(self)
        self.label_4.setText("0")
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)

    def update_label(self):
        val = int(self.label_4.text())
        if val == 9:
            self.timer.stop()
        self.label_4.setText(str(val+1))
        
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 