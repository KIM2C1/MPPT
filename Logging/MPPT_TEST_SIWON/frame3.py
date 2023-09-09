# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frameJUEiwF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def progress(self):
        self.count += 1
        if self.count > 100:
            self.count = 0
        self.PV_POWER.rpb_setValue(self.count)
        self.PV_INPUT.rpb_setValue(self.count)
    
    def text(self):
        self.count1 += 1
        if  self.count1 > 1050:
            self.count1 = 0
        self.ACvoltage_Value_2.setPlainText(str(self.count1))
        self.ACvoltagefrequency_Value_2.setPlainText(str(self.count1))
        self.PVinputpower_Value_2.setPlainText(str(self.count1))
        self.PVinputvoltage_Value_2.setPlainText(str(self.count1))
        self.PVinputcurrent_Value_2.setPlainText(str(self.count1))
        self.PVinputVal_2.setPlainText(str(self.count1))
        self.Batteryvoltage_Value_2.setPlainText(str(self.count1))
        self.BatterycapacityValue_2.setPlainText(str(self.count1))
        self.Chargingcurrent_Value_2.setPlainText(str(self.count1))
        self.Dischargingcurrent_Value_2.setPlainText(str(self.count1))
        self.LoadpercentVal_2.setPlainText(str(self.count1))
        self.Outputvoltage_Value_2.setPlainText(str(self.count1))
        self.Outputfrequency_Value_2.setPlainText(str(self.count1))
        self.Outputapparentpower_Value_2.setPlainText(str(self.count1))
        self.Outputactivepower_Value_2.setPlainText(str(self.count1))

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.count1 = 0
        MainWindow.resize(1577, 973)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 1391, 831))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.Battery_Capacity_home = QProgressBar(self.tab)
        self.Battery_Capacity_home.setObjectName(u"Battery_Capacity_home")
        self.Battery_Capacity_home.setGeometry(QRect(380, 490, 681, 31))
        self.Battery_Capacity_home.setLayoutDirection(Qt.LeftToRight)
        self.Battery_Capacity_home.setValue(24)
        ##############################################################
        self.PV_POWER = roundProgressBar(self.tab)  # QWidget (or a subclass) instance is expected as parent
        self.PV_POWER.setObjectName(u"PV_POWER")
        self.PV_POWER.setGeometry(QRect(400, 130, 271, 241))
        self.PV_POWER.rpb_setBarStyle('Hybrid1')
        self.PV_POWER.rpb_setLineWidth(3)
        self.PV_POWER.rpb_setPathWidth(15)
        self.PV_POWER.rpb_setPathColor((125, 255, 255))
        self.count = 0
        self.PV_POWER.rpb_setValue(self.count)
        self.timer = QtCore.QTimer()  # Corrected class name.
        self.timer.timeout.connect(self.progress)  # Ensure 'progress' method exists.
        self.timer.start(60)
        ##############################################################
        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(340, 30, 721, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"D2Coding")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)
###################################################################
        self.PV_INPUT = roundProgressBar(self.tab)  # QWidget (or a subclass) instance is expected as parent
        self.PV_INPUT.setObjectName(u"PV_INPUT")
        self.PV_INPUT.setGeometry(QRect(770, 130, 271, 241))
        self.PV_INPUT.rpb_setBarStyle('Hybrid2')
        self.PV_INPUT.rpb_setLineWidth(3)
        self.PV_INPUT.rpb_setPathWidth(15)
        self.PV_INPUT.rpb_setPathColor((125, 255, 255))
        self.count = 0
        self.PV_INPUT.rpb_setValue(self.count)
        self.timer = QtCore.QTimer()  # Corrected class name.
        self.timer.timeout.connect(self.progress)  # Ensure 'progress' method exists.
        self.timer.start(60)
###################################################################
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(380, 390, 356, 78))
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(380, 560, 356, 78))
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setFrameShadow(QFrame.Plain)
        self.Load_Percent_home = QProgressBar(self.tab)
        self.Load_Percent_home.setObjectName(u"Load_Percent_home")
        self.Load_Percent_home.setGeometry(QRect(380, 660, 681, 31))
        self.Load_Percent_home.setLayoutDirection(Qt.LeftToRight)
        self.Load_Percent_home.setValue(24)
        self.textBrowser_2 = QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(530, 380, 31, 31))
        self.textBrowser_2.setStyleSheet(u"background: transparent;border: none;")
        self.textBrowser_3 = QTextBrowser(self.tab)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(900, 380, 31, 31))
        self.textBrowser_3.setStyleSheet(u"border: none;background: transparent;")
        self.PVinput_home = QTextBrowser(self.tab)
        self.PVinput_home.setObjectName(u"PVinput_home")
        self.PVinput_home.setGeometry(QRect(490, 380, 41, 31))
        self.PVinput_home.setStyleSheet(u"background: transparent;border: none;")
        self.PVinput_home.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PVpower_home = QTextBrowser(self.tab)
        self.PVpower_home.setObjectName(u"PVpower_home")
        self.PVpower_home.setGeometry(QRect(860, 380, 41, 31))
        self.PVpower_home.setStyleSheet(u"border: none;background: transparent;")
        self.PVpower_home.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_2 = QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(250, 10, 361, 251))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.verticalLayoutWidget_2)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.verticalLayoutWidget_3 = QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(620, 10, 371, 251))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.graphicsView_2 = QGraphicsView(self.verticalLayoutWidget_3)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_3.addWidget(self.graphicsView_2)

        self.verticalLayoutWidget_4 = QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(1000, 10, 361, 251))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.graphicsView_3 = QGraphicsView(self.verticalLayoutWidget_4)
        self.graphicsView_3.setObjectName(u"graphicsView_3")

        self.verticalLayout_4.addWidget(self.graphicsView_3)

        self.textBrowser_7 = QTextBrowser(self.tab_2)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(740, 270, 141, 31))
        font1 = QFont()
        font1.setFamily(u"Eras Bold ITC")
        font1.setStyleStrategy(QFont.NoAntialias)
        self.textBrowser_7.setFont(font1)
        self.textBrowser_7.setStyleSheet(u"background: transparent;")
        self.textBrowser_7.setFrameShape(QFrame.NoFrame)
        self.textBrowser_8 = QTextBrowser(self.tab_2)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(350, 270, 141, 31))
        font2 = QFont()
        font2.setFamily(u"\ud734\uba3c\uc5d1\uc2a4\ud3ec")
        self.textBrowser_8.setFont(font2)
        self.textBrowser_8.setStyleSheet(u"background: transparent;")
        self.textBrowser_8.setFrameShape(QFrame.NoFrame)
        self.textBrowser_9 = QTextBrowser(self.tab_2)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(1100, 270, 181, 51))
        font3 = QFont()
        font3.setFamily(u"Lucida Handwriting")
        self.textBrowser_9.setFont(font3)
        self.textBrowser_9.setStyleSheet(u"background: transparent;")
        self.textBrowser_9.setFrameShape(QFrame.NoFrame)
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(250, 340, 1111, 51))
        self.checkBox_3 = QCheckBox(self.tab_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(350, 360, 51, 16))
        self.checkBox_3.setFont(font)
        self.checkBox_4 = QCheckBox(self.tab_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(630, 360, 51, 16))
        self.checkBox_4.setFont(font)
        self.checkBox_5 = QCheckBox(self.tab_2)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(910, 360, 51, 16))
        self.checkBox_5.setFont(font)
        self.checkBox_6 = QCheckBox(self.tab_2)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(1190, 360, 51, 16))
        self.checkBox_6.setFont(font)
        self.horizontalLayoutWidget_5 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(250, 400, 1111, 391))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_14 = QTextBrowser(self.horizontalLayoutWidget_5)
        self.textBrowser_14.setObjectName(u"textBrowser_14")
        self.textBrowser_14.setStyleSheet(u"background-color: rgb(235, 233, 234);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.textBrowser_14.setFrameShape(QFrame.Panel)

        self.horizontalLayout_5.addWidget(self.textBrowser_14)

        self.textBrowser_13 = QTextBrowser(self.horizontalLayoutWidget_5)
        self.textBrowser_13.setObjectName(u"textBrowser_13")
        self.textBrowser_13.setStyleSheet(u"background-color: rgb(235, 233, 234);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.textBrowser_13.setFrameShape(QFrame.Panel)

        self.horizontalLayout_5.addWidget(self.textBrowser_13)

        self.textBrowser_12 = QTextBrowser(self.horizontalLayoutWidget_5)
        self.textBrowser_12.setObjectName(u"textBrowser_12")
        self.textBrowser_12.setStyleSheet(u"background-color: rgb(235, 233, 234);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.textBrowser_12.setFrameShape(QFrame.Panel)

        self.horizontalLayout_5.addWidget(self.textBrowser_12)

        self.textBrowser_11 = QTextBrowser(self.horizontalLayoutWidget_5)
        self.textBrowser_11.setObjectName(u"textBrowser_11")
        self.textBrowser_11.setStyleSheet(u"background-color: rgb(235, 233, 234);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.textBrowser_11.setFrameShape(QFrame.Panel)

        self.horizontalLayout_5.addWidget(self.textBrowser_11)

        self.gridLayoutWidget_25 = QWidget(self.tab_2)
        self.gridLayoutWidget_25.setObjectName(u"gridLayoutWidget_25")
        self.gridLayoutWidget_25.setGeometry(QRect(0, 0, 241, 277))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_25)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PVinput_widget_2 = QFrame(self.gridLayoutWidget_25)
        self.PVinput_widget_2.setObjectName(u"PVinput_widget_2")
        self.PVinput_widget_2.setStyleSheet(u"background-color: rgb(25, 46, 63);")
        self.PVinput_widget_2.setFrameShape(QFrame.StyledPanel)
        self.PVinput_widget_2.setFrameShadow(QFrame.Raised)
        self.PVname_en_2 = QTextBrowser(self.PVinput_widget_2)
        self.PVname_en_2.setObjectName(u"PVname_en_2")
        self.PVname_en_2.setGeometry(QRect(0, 50, 141, 31))
        palette = QPalette()
        brush = QBrush(QColor(25, 46, 63, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVname_en_2.setPalette(palette)
        self.PVname_en_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.PVname_en_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PVinputVal_2 = QTextBrowser(self.PVinput_widget_2)
        self.PVinputVal_2.setObjectName(u"PVinputVal_2")
        self.PVinputVal_2.setGeometry(QRect(0, 80, 45, 41))
        self.PVinputVal_2.setMinimumSize(QSize(90, 41))
        self.PVinputVal_2.setMaximumSize(QSize(90, 41))
        self.font = QFont("D2Coding", 18)
        self.PVinputVal_2.setFont(self.font)
        self.count1 = 0
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVinputVal_2.setPalette(palette1)
        self.PVinputVal_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 18pt \"D2Coding\";\n"
"font-weight : bold;")
        self.PVinputVal_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PVinputVal_2.setTabStopDistance(79.000000000000000)
        self.PVinputVal_2.setAcceptRichText(True)
        self.PVinputVal_2.setPlainText(str(self.count1))

        
        self.PVname_ko_2 = QTextBrowser(self.PVinput_widget_2)
        self.PVname_ko_2.setObjectName(u"PVname_ko_2")
        self.PVname_ko_2.setGeometry(QRect(70, 20, 111, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVname_ko_2.setPalette(palette2)
        self.PVname_ko_2.setStyleSheet(u"background-color: rgb(25, 46, 63);border: none;\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.gridLayoutWidget_20 = QWidget(self.PVinput_widget_2)
        self.gridLayoutWidget_20.setObjectName(u"gridLayoutWidget_20")
        self.gridLayoutWidget_20.setGeometry(QRect(0, 150, 234, 23))
        self.ACvoltage_layout_2 = QGridLayout(self.gridLayoutWidget_20)
        self.ACvoltage_layout_2.setObjectName(u"ACvoltage_layout_2")
        self.ACvoltage_layout_2.setContentsMargins(0, 0, 0, 0)
        self.ACvoltage_name_2 = QTextBrowser(self.gridLayoutWidget_20)
        self.ACvoltage_name_2.setObjectName(u"ACvoltage_name_2")
        self.ACvoltage_name_2.setMinimumSize(QSize(121, 21))
        self.ACvoltage_name_2.setMaximumSize(QSize(121, 21))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.ACvoltage_name_2.setPalette(palette3)
        self.ACvoltage_name_2.setStyleSheet(u"background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"border: none;\n"
"")
        self.ACvoltage_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ACvoltage_layout_2.addWidget(self.ACvoltage_name_2, 0, 1, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.ACvoltage_layout_2.addItem(self.horizontalSpacer_20, 0, 2, 1, 1)

        self.ACvoltage_unit_2 = QTextBrowser(self.gridLayoutWidget_20)
        self.ACvoltage_unit_2.setObjectName(u"ACvoltage_unit_2")
        self.ACvoltage_unit_2.setMinimumSize(QSize(30, 21))
        self.ACvoltage_unit_2.setMaximumSize(QSize(30, 21))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.ACvoltage_unit_2.setPalette(palette4)
        self.ACvoltage_unit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.ACvoltage_unit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ACvoltage_Value_2 = QTextBrowser(self.gridLayoutWidget_20)
        self.ACvoltage_Value_2.setObjectName(u"ACvoltage_Value_2")
        self.ACvoltage_Value_2.setMinimumSize(QSize(45, 21))
        self.ACvoltage_Value_2.setMaximumSize(QSize(45, 21))
        self.count1 = 0
        self.ACvoltage_Value_2.setPlainText(str(self.count1))
        self.timer1 = QtCore.QTimer()  # Corrected class name.
        self.timer1.timeout.connect(self.text) 
        self.timer1.start(60)
        self.ACvoltage_layout_2.addWidget(self.ACvoltage_unit_2, 0, 4, 1, 1)

        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.ACvoltage_Value_2.setPalette(palette5)
        self.ACvoltage_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.ACvoltage_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ACvoltage_layout_2.addWidget(self.ACvoltage_Value_2, 0, 3, 1, 1)

        self.gridLayoutWidget_21 = QWidget(self.PVinput_widget_2)
        self.gridLayoutWidget_21.setObjectName(u"gridLayoutWidget_21")
        self.gridLayoutWidget_21.setGeometry(QRect(0, 170, 234, 23))
        self.ACfrequency_layout_2 = QGridLayout(self.gridLayoutWidget_21)
        self.ACfrequency_layout_2.setObjectName(u"ACfrequency_layout_2")
        self.ACfrequency_layout_2.setContentsMargins(0, 0, 0, 0)
        self.ACvoltagefrequency_Value_2 = QTextBrowser(self.gridLayoutWidget_21)
        self.ACvoltagefrequency_Value_2.setObjectName(u"ACvoltagefrequency_Value_2")
        self.ACvoltagefrequency_Value_2.setMinimumSize(QSize(45, 21))
        self.ACvoltagefrequency_Value_2.setMaximumSize(QSize(45, 21))
        self.ACvoltagefrequency_Value_2.setPlainText(str(self.count1))

        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.ACvoltagefrequency_Value_2.setPalette(palette6)
        self.ACvoltagefrequency_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.ACvoltagefrequency_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ACfrequency_layout_2.addWidget(self.ACvoltagefrequency_Value_2, 0, 3, 1, 1)

        self.ACvoltagefrequency_unit_2 = QTextBrowser(self.gridLayoutWidget_21)
        self.ACvoltagefrequency_unit_2.setObjectName(u"ACvoltagefrequency_unit_2")
        self.ACvoltagefrequency_unit_2.setMinimumSize(QSize(30, 21))
        self.ACvoltagefrequency_unit_2.setMaximumSize(QSize(30, 21))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.ACvoltagefrequency_unit_2.setPalette(palette7)
        self.ACvoltagefrequency_unit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.ACvoltagefrequency_unit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ACfrequency_layout_2.addWidget(self.ACvoltagefrequency_unit_2, 0, 4, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.ACfrequency_layout_2.addItem(self.horizontalSpacer_21, 0, 2, 1, 1)

        self.ACfrequency_name_2 = QTextBrowser(self.gridLayoutWidget_21)
        self.ACfrequency_name_2.setObjectName(u"ACfrequency_name_2")
        self.ACfrequency_name_2.setMinimumSize(QSize(121, 21))
        self.ACfrequency_name_2.setMaximumSize(QSize(121, 21))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.ACfrequency_name_2.setPalette(palette8)
        self.ACfrequency_name_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.ACfrequency_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ACfrequency_layout_2.addWidget(self.ACfrequency_name_2, 0, 1, 1, 1)

        self.gridLayoutWidget_22 = QWidget(self.PVinput_widget_2)
        self.gridLayoutWidget_22.setObjectName(u"gridLayoutWidget_22")
        self.gridLayoutWidget_22.setGeometry(QRect(0, 190, 234, 23))
        self.PVinputvoltage_layout_2 = QGridLayout(self.gridLayoutWidget_22)
        self.PVinputvoltage_layout_2.setObjectName(u"PVinputvoltage_layout_2")
        self.PVinputvoltage_layout_2.setContentsMargins(0, 0, 0, 0)
        self.PVinputvoltage_Value_2 = QTextBrowser(self.gridLayoutWidget_22)
        self.PVinputvoltage_Value_2.setObjectName(u"PVinputvoltage_Value_2")
        self.PVinputvoltage_Value_2.setMinimumSize(QSize(45, 21))
        self.PVinputvoltage_Value_2.setMaximumSize(QSize(45, 21))
        self.PVinputvoltage_Value_2.setPlainText(str(self.count1))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Button, brush)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVinputvoltage_Value_2.setPalette(palette9)
        self.PVinputvoltage_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.PVinputvoltage_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.PVinputvoltage_layout_2.addWidget(self.PVinputvoltage_Value_2, 0, 3, 1, 1)

        self.PVinputvoltage_unit_2 = QTextBrowser(self.gridLayoutWidget_22)
        self.PVinputvoltage_unit_2.setObjectName(u"PVinputvoltage_unit_2")
        self.PVinputvoltage_unit_2.setMinimumSize(QSize(30, 21))
        self.PVinputvoltage_unit_2.setMaximumSize(QSize(30, 21))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVinputvoltage_unit_2.setPalette(palette10)
        self.PVinputvoltage_unit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.PVinputvoltage_unit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.PVinputvoltage_layout_2.addWidget(self.PVinputvoltage_unit_2, 0, 4, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.PVinputvoltage_layout_2.addItem(self.horizontalSpacer_22, 0, 2, 1, 1)

        self.PVinputvoltage_name_2 = QTextBrowser(self.gridLayoutWidget_22)
        self.PVinputvoltage_name_2.setObjectName(u"PVinputvoltage_name_2")
        self.PVinputvoltage_name_2.setMinimumSize(QSize(140, 21))
        self.PVinputvoltage_name_2.setMaximumSize(QSize(140, 21))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.Button, brush)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVinputvoltage_name_2.setPalette(palette11)
        self.PVinputvoltage_name_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.PVinputvoltage_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.PVinputvoltage_layout_2.addWidget(self.PVinputvoltage_name_2, 0, 1, 1, 1)

        self.gridLayoutWidget_23 = QWidget(self.PVinput_widget_2)
        self.gridLayoutWidget_23.setObjectName(u"gridLayoutWidget_23")
        self.gridLayoutWidget_23.setGeometry(QRect(0, 210, 234, 23))
        self.PVinputpower_layout_2 = QGridLayout(self.gridLayoutWidget_23)
        self.PVinputpower_layout_2.setObjectName(u"PVinputpower_layout_2")
        self.PVinputpower_layout_2.setContentsMargins(0, 0, 0, 0)
        self.PVinputpower_Value_2 = QTextBrowser(self.gridLayoutWidget_23)
        self.PVinputpower_Value_2.setObjectName(u"PVinputpower_Value_2")
        self.PVinputpower_Value_2.setMinimumSize(QSize(45, 21))
        self.PVinputpower_Value_2.setMaximumSize(QSize(45, 21))
        self.PVinputpower_Value_2.setPlainText(str(self.count1))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.Button, brush)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVinputpower_Value_2.setPalette(palette12)
        self.PVinputpower_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.PVinputpower_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.PVinputpower_layout_2.addWidget(self.PVinputpower_Value_2, 0, 3, 1, 1)

        self.PVinputpower_unit_3 = QTextBrowser(self.gridLayoutWidget_23)
        self.PVinputpower_unit_3.setObjectName(u"PVinputpower_unit_3")
        self.PVinputpower_unit_3.setMinimumSize(QSize(30, 21))
        self.PVinputpower_unit_3.setMaximumSize(QSize(30, 21))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.Button, brush)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVinputpower_unit_3.setPalette(palette13)
        self.PVinputpower_unit_3.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.PVinputpower_unit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.PVinputpower_layout_2.addWidget(self.PVinputpower_unit_3, 0, 4, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.PVinputpower_layout_2.addItem(self.horizontalSpacer_23, 0, 2, 1, 1)

        self.PVinputpower_name_2 = QTextBrowser(self.gridLayoutWidget_23)
        self.PVinputpower_name_2.setObjectName(u"PVinputpower_name_2")
        self.PVinputpower_name_2.setMinimumSize(QSize(140, 21))
        self.PVinputpower_name_2.setMaximumSize(QSize(140, 21))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.Button, brush)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVinputpower_name_2.setPalette(palette14)
        self.PVinputpower_name_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.PVinputpower_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.PVinputpower_layout_2.addWidget(self.PVinputpower_name_2, 0, 1, 1, 1)

        self.gridLayoutWidget_24 = QWidget(self.PVinput_widget_2)
        self.gridLayoutWidget_24.setObjectName(u"gridLayoutWidget_24")
        self.gridLayoutWidget_24.setGeometry(QRect(0, 230, 234, 23))
        self.PVinputcurrent_layout_2 = QGridLayout(self.gridLayoutWidget_24)
        self.PVinputcurrent_layout_2.setObjectName(u"PVinputcurrent_layout_2")
        self.PVinputcurrent_layout_2.setContentsMargins(0, 0, 0, 0)
        self.PVinputcurrent_Value_2 = QTextBrowser(self.gridLayoutWidget_24)
        self.PVinputcurrent_Value_2.setObjectName(u"PVinputcurrent_Value_2")
        self.PVinputcurrent_Value_2.setMinimumSize(QSize(45, 21))
        self.PVinputcurrent_Value_2.setMaximumSize(QSize(45, 21))
        self.PVinputcurrent_Value_2.setPlainText(str(self.count1))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.Button, brush)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVinputcurrent_Value_2.setPalette(palette15)
        self.PVinputcurrent_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.PVinputcurrent_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.PVinputcurrent_layout_2.addWidget(self.PVinputcurrent_Value_2, 0, 3, 1, 1)

        self.PVinputcurrent_unit_2 = QTextBrowser(self.gridLayoutWidget_24)
        self.PVinputcurrent_unit_2.setObjectName(u"PVinputcurrent_unit_2")
        self.PVinputcurrent_unit_2.setMinimumSize(QSize(30, 21))
        self.PVinputcurrent_unit_2.setMaximumSize(QSize(30, 21))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.Button, brush)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVinputcurrent_unit_2.setPalette(palette16)
        self.PVinputcurrent_unit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.PVinputcurrent_unit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.PVinputcurrent_layout_2.addWidget(self.PVinputcurrent_unit_2, 0, 4, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.PVinputcurrent_layout_2.addItem(self.horizontalSpacer_24, 0, 2, 1, 1)

        self.PVinputcurrent_name_2 = QTextBrowser(self.gridLayoutWidget_24)
        self.PVinputcurrent_name_2.setObjectName(u"PVinputcurrent_name_2")
        self.PVinputcurrent_name_2.setMinimumSize(QSize(140, 21))
        self.PVinputcurrent_name_2.setMaximumSize(QSize(140, 21))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.Button, brush)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVinputcurrent_name_2.setPalette(palette17)
        self.PVinputcurrent_name_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.PVinputcurrent_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.PVinputcurrent_layout_2.addWidget(self.PVinputcurrent_name_2, 0, 1, 1, 1)

        self.PVinputunit_2 = QTextBrowser(self.PVinput_widget_2)
        self.PVinputunit_2.setObjectName(u"PVinputunit_2")
        self.PVinputunit_2.setGeometry(QRect(80, 80, 45, 41))
        self.PVinputunit_2.setMinimumSize(QSize(45, 41))
        self.PVinputunit_2.setMaximumSize(QSize(45, 41))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.Button, brush)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.PVinputunit_2.setPalette(palette18)
        self.PVinputunit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.PVinputunit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PVinputunit_2.setTabStopDistance(79.000000000000000)
        self.PVinputunit_2.setAcceptRichText(True)

        self.gridLayout_2.addWidget(self.PVinput_widget_2, 1, 0, 1, 1)

        self.gridLayoutWidget_27 = QWidget(self.tab_2)
        self.gridLayoutWidget_27.setObjectName(u"gridLayoutWidget_27")
        self.gridLayoutWidget_27.setGeometry(QRect(0, 530, 241, 261))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_27)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Loadpercent_widget_2 = QFrame(self.gridLayoutWidget_27)
        self.Loadpercent_widget_2.setObjectName(u"Loadpercent_widget_2")
        self.Loadpercent_widget_2.setStyleSheet(u"background-color: rgb(25, 46, 63);")
        self.Loadpercent_widget_2.setFrameShape(QFrame.StyledPanel)
        self.Loadpercent_widget_2.setFrameShadow(QFrame.Raised)
        self.Loadpercentname_en_2 = QTextBrowser(self.Loadpercent_widget_2)
        self.Loadpercentname_en_2.setObjectName(u"Loadpercentname_en_2")
        self.Loadpercentname_en_2.setGeometry(QRect(0, 50, 141, 31))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.Button, brush)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Loadpercentname_en_2.setPalette(palette19)
        self.Loadpercentname_en_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Loadpercentname_en_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LoadpercentVal_2 = QTextBrowser(self.Loadpercent_widget_2)
        self.LoadpercentVal_2.setObjectName(u"LoadpercentVal_2")
        self.LoadpercentVal_2.setGeometry(QRect(0, 80, 60, 41))
        self.LoadpercentVal_2.setMinimumSize(QSize(80, 41))
        self.LoadpercentVal_2.setMaximumSize(QSize(80, 41))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.Button, brush)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.LoadpercentVal_2.setPalette(palette20)
        self.LoadpercentVal_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 18pt \"D2Coding\";\n"
"")
        self.LoadpercentVal_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LoadpercentVal_2.setTabStopDistance(79.000000000000000)
        self.LoadpercentVal_2.setAcceptRichText(True)
        self.Loadpercentname_ko_2 = QTextBrowser(self.Loadpercent_widget_2)
        self.Loadpercentname_ko_2.setObjectName(u"Loadpercentname_ko_2")
        self.Loadpercentname_ko_2.setGeometry(QRect(70, 20, 111, 31))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.Button, brush)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Loadpercentname_ko_2.setPalette(palette21)
        self.Loadpercentname_ko_2.setStyleSheet(u"background-color: rgb(25, 46, 63);border: none;\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.gridLayoutWidget_16 = QWidget(self.Loadpercent_widget_2)
        self.gridLayoutWidget_16.setObjectName(u"gridLayoutWidget_16")
        self.gridLayoutWidget_16.setGeometry(QRect(0, 150, 234, 23))
        self.Outputvoltage_layout_2 = QGridLayout(self.gridLayoutWidget_16)
        self.Outputvoltage_layout_2.setObjectName(u"Outputvoltage_layout_2")
        self.Outputvoltage_layout_2.setContentsMargins(0, 0, 0, 0)
        self.Outputvoltage_name_2 = QTextBrowser(self.gridLayoutWidget_16)
        self.Outputvoltage_name_2.setObjectName(u"Outputvoltage_name_2")
        self.Outputvoltage_name_2.setMinimumSize(QSize(130, 21))
        self.Outputvoltage_name_2.setMaximumSize(QSize(130, 21))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.Button, brush)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputvoltage_name_2.setPalette(palette22)
        self.Outputvoltage_name_2.setStyleSheet(u"background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"border: none;\n"
"")
        self.Outputvoltage_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputvoltage_layout_2.addWidget(self.Outputvoltage_name_2, 0, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.Outputvoltage_layout_2.addItem(self.horizontalSpacer_16, 0, 2, 1, 1)

        self.Outputvoltage_unit_2 = QTextBrowser(self.gridLayoutWidget_16)
        self.Outputvoltage_unit_2.setObjectName(u"Outputvoltage_unit_2")
        self.Outputvoltage_unit_2.setMinimumSize(QSize(30, 21))
        self.Outputvoltage_unit_2.setMaximumSize(QSize(30, 21))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.Button, brush)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputvoltage_unit_2.setPalette(palette23)
        self.Outputvoltage_unit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Outputvoltage_unit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputvoltage_layout_2.addWidget(self.Outputvoltage_unit_2, 0, 4, 1, 1)

        self.Outputvoltage_Value_2 = QTextBrowser(self.gridLayoutWidget_16)
        self.Outputvoltage_Value_2.setObjectName(u"Outputvoltage_Value_2")
        self.Outputvoltage_Value_2.setMinimumSize(QSize(40, 21))
        self.Outputvoltage_Value_2.setMaximumSize(QSize(40, 21))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.Button, brush)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputvoltage_Value_2.setPalette(palette24)
        self.Outputvoltage_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 9pt \"D2Coding\";\n"
"")
        self.Outputvoltage_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputvoltage_layout_2.addWidget(self.Outputvoltage_Value_2, 0, 3, 1, 1)

        self.gridLayoutWidget_17 = QWidget(self.Loadpercent_widget_2)
        self.gridLayoutWidget_17.setObjectName(u"gridLayoutWidget_17")
        self.gridLayoutWidget_17.setGeometry(QRect(0, 170, 234, 23))
        self.Outputfrequency_layout_2 = QGridLayout(self.gridLayoutWidget_17)
        self.Outputfrequency_layout_2.setObjectName(u"Outputfrequency_layout_2")
        self.Outputfrequency_layout_2.setContentsMargins(0, 0, 0, 0)
        self.Outputfrequency_Value_2 = QTextBrowser(self.gridLayoutWidget_17)
        self.Outputfrequency_Value_2.setObjectName(u"Outputfrequency_Value_2")
        self.Outputfrequency_Value_2.setMinimumSize(QSize(60, 21))
        self.Outputfrequency_Value_2.setMaximumSize(QSize(60, 21))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.Button, brush)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputfrequency_Value_2.setPalette(palette25)
        self.Outputfrequency_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 9pt \"D2Coding\";\n"
"")
        self.Outputfrequency_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputfrequency_layout_2.addWidget(self.Outputfrequency_Value_2, 0, 3, 1, 1)

        self.Outputfrequency_unit_2 = QTextBrowser(self.gridLayoutWidget_17)
        self.Outputfrequency_unit_2.setObjectName(u"Outputfrequency_unit_2")
        self.Outputfrequency_unit_2.setMinimumSize(QSize(30, 21))
        self.Outputfrequency_unit_2.setMaximumSize(QSize(30, 21))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.Button, brush)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputfrequency_unit_2.setPalette(palette26)
        self.Outputfrequency_unit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Outputfrequency_unit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputfrequency_layout_2.addWidget(self.Outputfrequency_unit_2, 0, 4, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.Outputfrequency_layout_2.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)

        self.Outputfrequency_name_2 = QTextBrowser(self.gridLayoutWidget_17)
        self.Outputfrequency_name_2.setObjectName(u"Outputfrequency_name_2")
        self.Outputfrequency_name_2.setMinimumSize(QSize(121, 21))
        self.Outputfrequency_name_2.setMaximumSize(QSize(121, 21))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.Button, brush)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputfrequency_name_2.setPalette(palette27)
        self.Outputfrequency_name_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Outputfrequency_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputfrequency_layout_2.addWidget(self.Outputfrequency_name_2, 0, 1, 1, 1)

        self.gridLayoutWidget_18 = QWidget(self.Loadpercent_widget_2)
        self.gridLayoutWidget_18.setObjectName(u"gridLayoutWidget_18")
        self.gridLayoutWidget_18.setGeometry(QRect(0, 190, 231, 23))
        self.Outputapparentpower_layout_2 = QGridLayout(self.gridLayoutWidget_18)
        self.Outputapparentpower_layout_2.setObjectName(u"Outputapparentpower_layout_2")
        self.Outputapparentpower_layout_2.setContentsMargins(0, 0, 0, 0)
        self.Outputapparentpower_Value_2 = QTextBrowser(self.gridLayoutWidget_18)
        self.Outputapparentpower_Value_2.setObjectName(u"Outputapparentpower_Value_2")
        self.Outputapparentpower_Value_2.setMinimumSize(QSize(40, 21))
        self.Outputapparentpower_Value_2.setMaximumSize(QSize(40, 21))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.Button, brush)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputapparentpower_Value_2.setPalette(palette28)
        self.Outputapparentpower_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 9pt \"D2Coding\";\n"
"")
        self.Outputapparentpower_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputapparentpower_layout_2.addWidget(self.Outputapparentpower_Value_2, 0, 3, 1, 1)

        self.Outputapparentpower_unit_2 = QTextBrowser(self.gridLayoutWidget_18)
        self.Outputapparentpower_unit_2.setObjectName(u"Outputapparentpower_unit_2")
        self.Outputapparentpower_unit_2.setMinimumSize(QSize(29, 21))
        self.Outputapparentpower_unit_2.setMaximumSize(QSize(29, 21))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.Button, brush)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputapparentpower_unit_2.setPalette(palette29)
        self.Outputapparentpower_unit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Outputapparentpower_unit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputapparentpower_layout_2.addWidget(self.Outputapparentpower_unit_2, 0, 4, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.Outputapparentpower_layout_2.addItem(self.horizontalSpacer_18, 0, 2, 1, 1)

        self.Outputapparentpower_name_2 = QTextBrowser(self.gridLayoutWidget_18)
        self.Outputapparentpower_name_2.setObjectName(u"Outputapparentpower_name_2")
        self.Outputapparentpower_name_2.setMinimumSize(QSize(157, 21))
        self.Outputapparentpower_name_2.setMaximumSize(QSize(157, 21))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.Button, brush)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputapparentpower_name_2.setPalette(palette30)
        self.Outputapparentpower_name_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Outputapparentpower_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputapparentpower_layout_2.addWidget(self.Outputapparentpower_name_2, 0, 1, 1, 1)

        self.gridLayoutWidget_19 = QWidget(self.Loadpercent_widget_2)
        self.gridLayoutWidget_19.setObjectName(u"gridLayoutWidget_19")
        self.gridLayoutWidget_19.setGeometry(QRect(0, 210, 248, 23))
        self.Outputactivepower_layout_2 = QGridLayout(self.gridLayoutWidget_19)
        self.Outputactivepower_layout_2.setObjectName(u"Outputactivepower_layout_2")
        self.Outputactivepower_layout_2.setContentsMargins(0, 0, 0, 0)
        self.Outputactivepower_Value_2 = QTextBrowser(self.gridLayoutWidget_19)
        self.Outputactivepower_Value_2.setObjectName(u"Outputactivepower_Value_2")
        self.Outputactivepower_Value_2.setMinimumSize(QSize(40, 21))
        self.Outputactivepower_Value_2.setMaximumSize(QSize(40, 21))
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.Button, brush)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputactivepower_Value_2.setPalette(palette31)
        self.Outputactivepower_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 9pt \"D2Coding\";\n"
"")
        self.Outputactivepower_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputactivepower_layout_2.addWidget(self.Outputactivepower_Value_2, 0, 2, 1, 1)

        self.Outputactivepower_unit_2 = QTextBrowser(self.gridLayoutWidget_19)
        self.Outputactivepower_unit_2.setObjectName(u"Outputactivepower_unit_2")
        self.Outputactivepower_unit_2.setMinimumSize(QSize(38, 21))
        self.Outputactivepower_unit_2.setMaximumSize(QSize(38, 21))
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.Button, brush)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputactivepower_unit_2.setPalette(palette32)
        self.Outputactivepower_unit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Outputactivepower_unit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputactivepower_layout_2.addWidget(self.Outputactivepower_unit_2, 0, 3, 1, 1)

        self.Outputactivepower_name_2 = QTextBrowser(self.gridLayoutWidget_19)
        self.Outputactivepower_name_2.setObjectName(u"Outputactivepower_name_2")
        self.Outputactivepower_name_2.setMinimumSize(QSize(147, 21))
        self.Outputactivepower_name_2.setMaximumSize(QSize(147, 21))
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.Button, brush)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Outputactivepower_name_2.setPalette(palette33)
        self.Outputactivepower_name_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Outputactivepower_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Outputactivepower_layout_2.addWidget(self.Outputactivepower_name_2, 0, 1, 1, 1)

        self.Loadpercentunit_2 = QTextBrowser(self.Loadpercent_widget_2)
        self.Loadpercentunit_2.setObjectName(u"Loadpercentunit_2")
        self.Loadpercentunit_2.setGeometry(QRect(80, 80, 45, 41))
        self.Loadpercentunit_2.setMinimumSize(QSize(45, 41))
        self.Loadpercentunit_2.setMaximumSize(QSize(45, 41))
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.Button, brush)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Loadpercentunit_2.setPalette(palette34)
        self.Loadpercentunit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Loadpercentunit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Loadpercentunit_2.setTabStopDistance(79.000000000000000)
        self.Loadpercentunit_2.setAcceptRichText(True)

        self.gridLayout_4.addWidget(self.Loadpercent_widget_2, 0, 0, 1, 1)

        self.gridLayoutWidget_26 = QWidget(self.tab_2)
        self.gridLayoutWidget_26.setObjectName(u"gridLayoutWidget_26")
        self.gridLayoutWidget_26.setGeometry(QRect(0, 290, 241, 231))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_26)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Batterycapacity_widget_2 = QFrame(self.gridLayoutWidget_26)
        self.Batterycapacity_widget_2.setObjectName(u"Batterycapacity_widget_2")
        self.Batterycapacity_widget_2.setStyleSheet(u"background-color: rgb(25, 46, 63);")
        self.Batterycapacity_widget_2.setFrameShape(QFrame.StyledPanel)
        self.Batterycapacity_widget_2.setFrameShadow(QFrame.Raised)
        self.Batteryname_en_2 = QTextBrowser(self.Batterycapacity_widget_2)
        self.Batteryname_en_2.setObjectName(u"Batteryname_en_2")
        self.Batteryname_en_2.setGeometry(QRect(0, 50, 160, 31))
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.Button, brush)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Batteryname_en_2.setPalette(palette35)
        self.Batteryname_en_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Batteryname_en_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Batteryname_ko_2 = QTextBrowser(self.Batterycapacity_widget_2)
        self.Batteryname_ko_2.setObjectName(u"Batteryname_ko_2")
        self.Batteryname_ko_2.setGeometry(QRect(60, 20, 115, 31))
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.Button, brush)
        palette36.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Batteryname_ko_2.setPalette(palette36)
        self.Batteryname_ko_2.setStyleSheet(u"background-color: rgb(25, 46, 63);border: none;\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Batteryname_ko_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.gridLayoutWidget_13 = QWidget(self.Batterycapacity_widget_2)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(0, 150, 234, 23))
        self.Batteryvoltage_layout_2 = QGridLayout(self.gridLayoutWidget_13)
        self.Batteryvoltage_layout_2.setObjectName(u"Batteryvoltage_layout_2")
        self.Batteryvoltage_layout_2.setContentsMargins(0, 0, 0, 0)
        self.Batteryvoltage_name_2 = QTextBrowser(self.gridLayoutWidget_13)
        self.Batteryvoltage_name_2.setObjectName(u"Batteryvoltage_name_2")
        self.Batteryvoltage_name_2.setMinimumSize(QSize(140, 21))
        self.Batteryvoltage_name_2.setMaximumSize(QSize(140, 21))
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.Button, brush)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Batteryvoltage_name_2.setPalette(palette37)
        self.Batteryvoltage_name_2.setStyleSheet(u"background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"border: none;\n"
"")
        self.Batteryvoltage_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Batteryvoltage_layout_2.addWidget(self.Batteryvoltage_name_2, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.Batteryvoltage_layout_2.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)

        self.Batteryvoltage_unit_2 = QTextBrowser(self.gridLayoutWidget_13)
        self.Batteryvoltage_unit_2.setObjectName(u"Batteryvoltage_unit_2")
        self.Batteryvoltage_unit_2.setMinimumSize(QSize(30, 21))
        self.Batteryvoltage_unit_2.setMaximumSize(QSize(30, 21))
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.Button, brush)
        palette38.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Batteryvoltage_unit_2.setPalette(palette38)
        self.Batteryvoltage_unit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Batteryvoltage_unit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Batteryvoltage_layout_2.addWidget(self.Batteryvoltage_unit_2, 0, 4, 1, 1)

        self.Batteryvoltage_Value_2 = QTextBrowser(self.gridLayoutWidget_13)
        self.Batteryvoltage_Value_2.setObjectName(u"Batteryvoltage_Value_2")
        self.Batteryvoltage_Value_2.setMinimumSize(QSize(48, 21))
        self.Batteryvoltage_Value_2.setMaximumSize(QSize(48, 21))
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.Button, brush)
        palette39.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Batteryvoltage_Value_2.setPalette(palette39)
        self.Batteryvoltage_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 9pt \"D2Coding\";\n"
"")
        self.Batteryvoltage_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Batteryvoltage_layout_2.addWidget(self.Batteryvoltage_Value_2, 0, 3, 1, 1)

        self.gridLayoutWidget_14 = QWidget(self.Batterycapacity_widget_2)
        self.gridLayoutWidget_14.setObjectName(u"gridLayoutWidget_14")
        self.gridLayoutWidget_14.setGeometry(QRect(0, 170, 255, 23))
        self.Chargingcurrent_layout_2 = QGridLayout(self.gridLayoutWidget_14)
        self.Chargingcurrent_layout_2.setObjectName(u"Chargingcurrent_layout_2")
        self.Chargingcurrent_layout_2.setContentsMargins(0, 0, 0, 0)
        self.Chargingcurrent_Value_2 = QTextBrowser(self.gridLayoutWidget_14)
        self.Chargingcurrent_Value_2.setObjectName(u"Chargingcurrent_Value_2")
        self.Chargingcurrent_Value_2.setMinimumSize(QSize(40, 21))
        self.Chargingcurrent_Value_2.setMaximumSize(QSize(40, 21))
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.Button, brush)
        palette40.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Chargingcurrent_Value_2.setPalette(palette40)
        self.Chargingcurrent_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 9pt \"D2Coding\";\n"
"")
        self.Chargingcurrent_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Chargingcurrent_layout_2.addWidget(self.Chargingcurrent_Value_2, 0, 3, 1, 1)

        self.Chargingcurrent_unit_2 = QTextBrowser(self.gridLayoutWidget_14)
        self.Chargingcurrent_unit_2.setObjectName(u"Chargingcurrent_unit_2")
        self.Chargingcurrent_unit_2.setMinimumSize(QSize(30, 21))
        self.Chargingcurrent_unit_2.setMaximumSize(QSize(30, 21))
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.Button, brush)
        palette41.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette41.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette41.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Chargingcurrent_unit_2.setPalette(palette41)
        self.Chargingcurrent_unit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Chargingcurrent_unit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Chargingcurrent_layout_2.addWidget(self.Chargingcurrent_unit_2, 0, 4, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.Chargingcurrent_layout_2.addItem(self.horizontalSpacer_14, 0, 2, 1, 1)

        self.Chargingcurrent_name_2 = QTextBrowser(self.gridLayoutWidget_14)
        self.Chargingcurrent_name_2.setObjectName(u"Chargingcurrent_name_2")
        self.Chargingcurrent_name_2.setMinimumSize(QSize(170, 21))
        self.Chargingcurrent_name_2.setMaximumSize(QSize(170, 21))
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.Button, brush)
        palette42.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette42.setBrush(QPalette.Active, QPalette.Base, brush)
        palette42.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette42.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette42.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette42.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette42.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Chargingcurrent_name_2.setPalette(palette42)
        self.Chargingcurrent_name_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Chargingcurrent_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Chargingcurrent_layout_2.addWidget(self.Chargingcurrent_name_2, 0, 1, 1, 1)

        self.gridLayoutWidget_15 = QWidget(self.Batterycapacity_widget_2)
        self.gridLayoutWidget_15.setObjectName(u"gridLayoutWidget_15")
        self.gridLayoutWidget_15.setGeometry(QRect(0, 190, 250, 23))
        self.Dischargingcurrent_layout_2 = QGridLayout(self.gridLayoutWidget_15)
        self.Dischargingcurrent_layout_2.setObjectName(u"Dischargingcurrent_layout_2")
        self.Dischargingcurrent_layout_2.setContentsMargins(0, 0, 0, 0)
        self.Dischargingcurrent_Value_2 = QTextBrowser(self.gridLayoutWidget_15)
        self.Dischargingcurrent_Value_2.setObjectName(u"Dischargingcurrent_Value_2")
        self.Dischargingcurrent_Value_2.setMinimumSize(QSize(40, 21))
        self.Dischargingcurrent_Value_2.setMaximumSize(QSize(40, 21))
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.Button, brush)
        palette43.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette43.setBrush(QPalette.Active, QPalette.Base, brush)
        palette43.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette43.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette43.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette43.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette43.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Dischargingcurrent_Value_2.setPalette(palette43)
        self.Dischargingcurrent_Value_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 9pt \"D2Coding\";\n"
"")
        self.Dischargingcurrent_Value_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Dischargingcurrent_layout_2.addWidget(self.Dischargingcurrent_Value_2, 0, 3, 1, 1)

        self.Dischargingcurrent_unit_2 = QTextBrowser(self.gridLayoutWidget_15)
        self.Dischargingcurrent_unit_2.setObjectName(u"Dischargingcurrent_unit_2")
        self.Dischargingcurrent_unit_2.setMinimumSize(QSize(29, 21))
        self.Dischargingcurrent_unit_2.setMaximumSize(QSize(29, 21))
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.Button, brush)
        palette44.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette44.setBrush(QPalette.Active, QPalette.Base, brush)
        palette44.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette44.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette44.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette44.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette44.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Dischargingcurrent_unit_2.setPalette(palette44)
        self.Dischargingcurrent_unit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Dischargingcurrent_unit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Dischargingcurrent_layout_2.addWidget(self.Dischargingcurrent_unit_2, 0, 4, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(10, 10, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.Dischargingcurrent_layout_2.addItem(self.horizontalSpacer_15, 0, 2, 1, 1)

        self.Dischargingcurrent_name_2 = QTextBrowser(self.gridLayoutWidget_15)
        self.Dischargingcurrent_name_2.setObjectName(u"Dischargingcurrent_name_2")
        self.Dischargingcurrent_name_2.setMinimumSize(QSize(170, 21))
        self.Dischargingcurrent_name_2.setMaximumSize(QSize(170, 21))
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.Button, brush)
        palette45.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Dischargingcurrent_name_2.setPalette(palette45)
        self.Dischargingcurrent_name_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Dischargingcurrent_name_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.Dischargingcurrent_layout_2.addWidget(self.Dischargingcurrent_name_2, 0, 1, 1, 1)

        self.BatterycapacityValue_2 = QTextBrowser(self.Batterycapacity_widget_2)
        self.BatterycapacityValue_2.setObjectName(u"BatterycapacityValue_2")
        self.BatterycapacityValue_2.setGeometry(QRect(0, 80, 45, 41))
        self.BatterycapacityValue_2.setMinimumSize(QSize(80, 41))
        self.BatterycapacityValue_2.setMaximumSize(QSize(80, 41))
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.Button, brush)
        palette46.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.BatterycapacityValue_2.setPalette(palette46)
        self.BatterycapacityValue_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 18pt \"D2Coding\";\n"
"font-weight : bold;")
        self.BatterycapacityValue_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.BatterycapacityValue_2.setTabStopDistance(79.000000000000000)
        self.BatterycapacityValue_2.setAcceptRichText(True)
        self.Batteryunit_2 = QTextBrowser(self.Batterycapacity_widget_2)
        self.Batteryunit_2.setObjectName(u"Batteryunit_2")
        self.Batteryunit_2.setGeometry(QRect(75, 80, 45, 41))
        self.Batteryunit_2.setMinimumSize(QSize(45, 41))
        self.Batteryunit_2.setMaximumSize(QSize(45, 41))
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.Button, brush)
        palette47.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette47.setBrush(QPalette.Active, QPalette.Base, brush)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette47.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette47.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette47.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Batteryunit_2.setPalette(palette47)
        self.Batteryunit_2.setStyleSheet(u"border: none;background-color: rgb(25, 46, 63);\n"
"font: 75 10pt \"D2Coding\";\n"
"")
        self.Batteryunit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Batteryunit_2.setTabStopDistance(79.000000000000000)
        self.Batteryunit_2.setAcceptRichText(True)

        self.gridLayout_3.addWidget(self.Batterycapacity_widget_2, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_5.addWidget(self.tabWidget)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1577, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PV_INPUT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PV POWER", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Battery Capacity", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Load Percent", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">V</span></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">W</span></p></body></html>", None))
        self.PVinput_home.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">55</span></p></body></html>", None))
        self.PVpower_home.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">55</span></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"home", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Eras Bold ITC'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim';\">\ubca0\ud130\ub9ac \uc0c1\ud0dc</span></p></body></html>", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ud734\uba3c\uc5d1\uc2a4\ud3ec'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim';\">\uc785\ub825 \uc804\uc6d0</span></p></body></html>", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lucida Handwriting'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim';\">\ubd80\ud558 \ucd9c\ub825</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim';\"><br /></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"ON", None))
#if QT_CONFIG(whatsthis)
        self.textBrowser_14.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Gulim'; color:#ffffff;\">\uc785\ub825 \uc804\uc6d00</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.textBrowser_14.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc7a5\uce58 1</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-weight:400; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        ">\uc18c\ube44 \uc804\ub825</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-size:18pt; font-weight:600; color:#000000;\">0.021 KWH</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:18pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-weight:400; color:#000000;\">\uc804\uc555	0 V</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-fam"
                        "ily:'Gulim'; font-weight:400; color:#000000;\">	</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc804\ub958	0 A</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc8fc\ud30c\uc218	0 Hz</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:"
                        "'Gulim'; color:#000000;\">\uc804\ub825	0 W</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:9pt; color:#000000;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:9pt; color:#000000;\"><br /></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.textBrowser_13.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Gulim'; color:#ffffff;\">\uc785\ub825 \uc804\uc6d00</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.textBrowser_13.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc7a5\uce58 2</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-weight:400; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        ">\uc18c\ube44 \uc804\ub825</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-size:18pt; font-weight:600; color:#000000;\">0.021 KWH</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:18pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-weight:400; color:#000000;\">\uc804\uc555	0 V</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-fam"
                        "ily:'Gulim'; font-weight:400; color:#000000;\">	</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc804\ub958	0 A</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc8fc\ud30c\uc218	0 Hz</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:"
                        "'Gulim'; color:#000000;\">\uc804\ub825	0 W</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:9pt; color:#000000;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:9pt; color:#000000;\"><br /></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.textBrowser_12.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Gulim'; color:#ffffff;\">\uc785\ub825 \uc804\uc6d00</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.textBrowser_12.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc7a5\uce58 3</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-weight:400; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        ">\uc18c\ube44 \uc804\ub825</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-size:18pt; font-weight:600; color:#000000;\">0.021 KWH</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:18pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc804\uc555	0 V</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; colo"
                        "r:#000000;\">	</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc804\ub958	0 A</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc8fc\ud30c\uc218	0 Hz</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc804\ub825"
                        "	0 W</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:9pt; color:#000000;\"><br /></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.textBrowser_11.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Gulim'; color:#ffffff;\">\uc785\ub825 \uc804\uc6d00</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.textBrowser_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc7a5\uce58 4</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-weight:400; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        ">\uc18c\ube44 \uc804\ub825</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-size:18pt; font-weight:600; color:#000000;\">0.021 KWH</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:18pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc804\uc555	0 V</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; colo"
                        "r:#000000;\">	</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc804\ub958	0 A</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc8fc\ud30c\uc218	0 Hz</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; color:#000000;\">\uc804\ub825"
                        "	0 W</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:9pt; color:#000000;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:9pt; color:#000000;\"><br /></p></body></html>", None))
        self.PVname_en_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">PV Input voltage</span></p></body></html>", None))
        self.PVinputVal_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">75</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p></body></html>", None))
        self.PVname_ko_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc785\ub825 \uc804\uc6d0</p></body></html>", None))
        self.ACvoltage_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">AC voltage</span></p></body></html>", None))
        self.ACvoltage_unit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">V</span></p></body></html>", None))
        self.ACvoltage_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.ACvoltagefrequency_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.ACvoltagefrequency_unit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Hz</span></p></body></html>", None))
        self.ACfrequency_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-size:9pt;\">AC frequency</span></p></body></html>", None))
        self.PVinputvoltage_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.PVinputvoltage_unit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">V</span></p></body></html>", None))
        self.PVinputvoltage_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-size:9pt;\">PV input voltage</span></p></body></html>", None))
        self.PVinputpower_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.PVinputpower_unit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">W</span></p></body></html>", None))
        self.PVinputpower_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-size:9pt;\">PV input power</span></p></body></html>", None))
        self.PVinputcurrent_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.PVinputcurrent_unit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">A</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.PVinputcurrent_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">PV input current</span></p></body></html>", None))
        self.PVinputunit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">V</span></p></body></html>", None))
        self.Loadpercentname_en_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Load percent</p></body></html>", None))
        self.LoadpercentVal_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">75</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p></body></html>", None))
        self.Loadpercentname_ko_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\ubd80\ud558 \ucd9c\ub825</p></body></html>", None))
        self.Outputvoltage_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Output voltage</span></p></body></html>", None))
        self.Outputvoltage_unit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">V</span></p></body></html>", None))
        self.Outputvoltage_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.Outputfrequency_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.Outputfrequency_unit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Hz</span></p></body></html>", None))
        self.Outputfrequency_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-size:9pt;\">Output frequency</span></p></body></html>", None))
        self.Outputapparentpower_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.Outputapparentpower_unit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">VA</span></p></body></html>", None))
        self.Outputapparentpower_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-size:9pt;\">Output apparent power</span></p></body></html>", None))
        self.Outputactivepower_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.Outputactivepower_unit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">W</span></p></body></html>", None))
        self.Outputactivepower_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-size:9pt;\">Output active power</span></p></body></html>", None))
        self.Loadpercentunit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">%</span></p></body></html>", None))
        self.Batteryname_en_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Battery capacity</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>", None))
        self.Batteryname_ko_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\ubc30\ud130\ub9ac \uc0c1\ud0dc</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Batteryvoltage_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Battery voltage</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.Batteryvoltage_unit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">V</span></p></body></html>", None))
        self.Batteryvoltage_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.Chargingcurrent_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.Chargingcurrent_unit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">A</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.Chargingcurrent_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim'; font-size:9pt;\">Charging current</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim'; font-size:9pt;\"><br /></p></body></html>", None))
        self.Dischargingcurrent_Value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">95</p></body></html>", None))
        self.Dischargingcurrent_unit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">A</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.Dischargingcurrent_name_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Discharging current</span></p></body></html>", None))
        self.BatterycapacityValue_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">75</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p></body></html>", None))
        self.Batteryunit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'D2Coding'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">%</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Details", None))
    # retranslateUi

