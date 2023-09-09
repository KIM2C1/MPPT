import sys
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from PySide2 import QtCore, QtWidgets, QtGui

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QProgressBar


from PySide2extn.RoundProgressBar import roundProgressBar


class MyWidget(QtWidgets.QWidget):
    def setupUi(self, MainWindow):

        QtWidgets.QWidget.__init__(self)
        ui_file = QFile("frame.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        window = loader.load(ui_file)

        QtWidgets.QWidget.__init__(self)

        self.rpb = roundProgressBar() #CREATING A ROUND PROGRESS BAR OBJECT
        
        self.layout = QtWidgets.QFrame()
        self.layout.addWidget(self.rpb)
        self.setLayout(self.layout)
  



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())