import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic
import time
from PyQt5.QtCore import QTimer

form_class = uic.loadUiType("textbrowserTest.ui")[0]

def randomreturn() :
    return random.randint(0, 10)

class WindowClass(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 할당하는 코드
        self.btn_Print.clicked.connect(self.printTextFunction)
        self.btn_setText.clicked.connect(self.changeTextFunction)
        self.btn_appendText.clicked.connect(self.appendTextFunction)
        self.btn_Clear.clicked.connect(self.clearTextFunction)

    def printTextFunction(self) :
        #self.Textbrowser이름.toPlainText()
        #Textbrowser에 있는 글자를 가져오는 메서드
        print(self.textbrow_Test.toPlainText())

    def changeTextFunction(self) :
        #self.Textbrowser이름.setPlainText()
        #Textbrowser에 있는 글자를 가져오는 메서드
        self.textbrow_Test.setPlainText(str(randomreturn()))

    def appendTextFunction(self) :
        #self.Textbrowser이름.append()
        #Textbrowser에 있는 글자를 가져오는 메서드
        self.textbrow_Test.append("Append Text")

    def clearTextFunction(self) :
        #self.Textbrowser.clear()
        #Textbrowser에 있는 글자를 지우는 메서드
        self.textbrow_Test.clear()

    


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    
    timer = QTimer()
    timer.timeout.connect(myWindow.changeTextFunction)
    timer.start(1000)  # 1초마다 changeTextFunction() 호출

    app.exec_()