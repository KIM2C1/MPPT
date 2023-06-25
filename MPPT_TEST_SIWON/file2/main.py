import os
import sys
#import qdarkstyle
from frame import *

class MainWindow(QMainWindow) :
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())