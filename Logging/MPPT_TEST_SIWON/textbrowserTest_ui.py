# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'textbrowserTest.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(410, 228)
        self.textbrow_Test = QTextBrowser(Dialog)
        self.textbrow_Test.setObjectName(u"textbrow_Test")
        self.textbrow_Test.setGeometry(QRect(10, 20, 256, 192))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(280, 50, 116, 134))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_Print = QPushButton(self.widget)
        self.btn_Print.setObjectName(u"btn_Print")

        self.verticalLayout.addWidget(self.btn_Print)

        self.btn_setText = QPushButton(self.widget)
        self.btn_setText.setObjectName(u"btn_setText")

        self.verticalLayout.addWidget(self.btn_setText)

        self.btn_appendText = QPushButton(self.widget)
        self.btn_appendText.setObjectName(u"btn_appendText")

        self.verticalLayout.addWidget(self.btn_appendText)

        self.btn_Clear = QPushButton(self.widget)
        self.btn_Clear.setObjectName(u"btn_Clear")

        self.verticalLayout.addWidget(self.btn_Clear)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_Print.setText(QCoreApplication.translate("Dialog", u"Print", None))
        self.btn_setText.setText(QCoreApplication.translate("Dialog", u"SetText", None))
        self.btn_appendText.setText(QCoreApplication.translate("Dialog", u"AppendText", None))
        self.btn_Clear.setText(QCoreApplication.translate("Dialog", u"Clear", None))
    # retranslateUi

