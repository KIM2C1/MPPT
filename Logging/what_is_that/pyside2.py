#test.py

import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide6.QtWidgets import QApplication, QLabel    # 사용할 class import

app = QApplication(sys.argv)                          # QApplication class에 대한 instance 생성
label = QLabel("Hello World!")                        # text 출력을 위한 label 생성
label.show()                                         
app.exec()   