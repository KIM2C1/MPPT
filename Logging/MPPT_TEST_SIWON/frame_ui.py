# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QSizePolicy, QTabWidget,
    QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1039, 738)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 40, 931, 681))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.Battery_Capacity = QProgressBar(self.tab)
        self.Battery_Capacity.setObjectName(u"Battery_Capacity")
        self.Battery_Capacity.setGeometry(QRect(100, 440, 681, 31))
        self.Battery_Capacity.setLayoutDirection(Qt.LeftToRight)
        self.Battery_Capacity.setValue(24)
        self.PV_POWER = QFrame(self.tab)
        self.PV_POWER.setObjectName(u"PV_POWER")
        self.PV_POWER.setGeometry(QRect(470, 130, 271, 241))
        self.PV_POWER.setFrameShape(QFrame.StyledPanel)
        self.PV_POWER.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(100, 30, 721, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"D2Coding"])
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.PV_POWER_2 = QFrame(self.tab)
        self.PV_POWER_2.setObjectName(u"PV_POWER_2")
        self.PV_POWER_2.setGeometry(QRect(100, 130, 271, 241))
        self.PV_POWER_2.setFrameShape(QFrame.StyledPanel)
        self.PV_POWER_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 380, 356, 78))
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 510, 356, 78))
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setFrameShadow(QFrame.Plain)
        self.Load_Percent = QProgressBar(self.tab)
        self.Load_Percent.setObjectName(u"Load_Percent")
        self.Load_Percent.setGeometry(QRect(100, 570, 681, 31))
        self.Load_Percent.setLayoutDirection(Qt.LeftToRight)
        self.Load_Percent.setValue(24)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(-30, -60, 1191, 801))
        self.textBrowser.setStyleSheet(u"background-color: rgb(235, 233, 234)")
        self.textBrowser.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"PV_INPUT", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"PV POWER", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Battery Capacity", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Load Percent", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Details", None))
    # retranslateUi

