# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowbDlIwr.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import views.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1092, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	background-color: #fefeff;\n"
"}\n"
"\n"
"*{\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	color: #000;\n"
"	border: none;\n"
"}\n"
"#leftMenu{\n"
"	background-color: #2596be;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background: transparent;\n"
"}\n"
"\n"
"#searchFrame{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #2596be;\n"
"}\n"
"\n"
"#appHeader{\n"
"	color: #2596be;\n"
"}\n"
"\n"
"#card1, #card2, #card3, #card4{\n"
"	background-color: #fefeff;\n"
"	border-radius:  15px;\n"
"}\n"
"\n"
"#seeMoreButton{\n"
"	background-color: #f6f2ff;\n"
"	color: #2596be;\n"
"	padding: 7px;\n"
"	border-radius: 10px;\n"
"	box-shadow: 0px 0px 10px 0px #000;\n"
"}\n"
"\n"
"#irinaServiceLabel{\n"
"	color: #fefeff;\n"
"}\n"
"\n"
"#menuFrame QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 15px;\n"
"}\n"
"\n"
"#menuFrame #btn1{\n"
"	background-color: #fefeff;\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"\n"
"#profileContainer{\n"
"	background-color: #fefeff;\n"
"	border-radius: 20px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout_7 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.leftMenu)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.irinaServiceLabel = QLabel(self.frame_8)
        self.irinaServiceLabel.setObjectName(u"irinaServiceLabel")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.irinaServiceLabel.setFont(font)

        self.horizontalLayout_14.addWidget(self.irinaServiceLabel, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_8, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 15, 0, 0)
        self.menuFrame = QFrame(self.frame_9)
        self.menuFrame.setObjectName(u"menuFrame")
        sizePolicy.setHeightForWidth(self.menuFrame.sizePolicy().hasHeightForWidth())
        self.menuFrame.setSizePolicy(sizePolicy)
        self.menuFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.menuFrame)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 0, 0, -1)
        self.btn1 = QPushButton(self.menuFrame)
        self.btn1.setObjectName(u"btn1")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.btn1.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn1.setIcon(icon)
        self.btn1.setIconSize(QSize(22, 22))

        self.verticalLayout_9.addWidget(self.btn1)

        self.pushButton_2 = QPushButton(self.menuFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton_2.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/stock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(22, 22))

        self.verticalLayout_9.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.menuFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/people.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(22, 22))

        self.verticalLayout_9.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.menuFrame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/facture.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(19, 19))

        self.verticalLayout_9.addWidget(self.pushButton_4)


        self.verticalLayout_10.addWidget(self.menuFrame, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_9)


        self.verticalLayout_7.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.verticalLayout = QVBoxLayout(self.mainContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QWidget(self.mainContainer)
        self.headerFrame.setObjectName(u"headerFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.widget = QWidget(self.headerFrame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/burger-menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon4)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn)

        self.appHeader = QLabel(self.widget)
        self.appHeader.setObjectName(u"appHeader")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.appHeader.setFont(font3)

        self.horizontalLayout_3.addWidget(self.appHeader)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.widget_2 = QWidget(self.headerFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.searchFrame = QFrame(self.widget_2)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(160, 0))
        self.searchFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.searchFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/icons/search.png"))

        self.horizontalLayout_5.addWidget(self.label_2)

        self.searchField = QLineEdit(self.searchFrame)
        self.searchField.setObjectName(u"searchField")
        self.searchField.setMaximumSize(QSize(16777215, 300))

        self.horizontalLayout_5.addWidget(self.searchField)


        self.horizontalLayout_4.addWidget(self.searchFrame, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_2.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.widget_3 = QWidget(self.headerFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.accountBtn = QPushButton(self.widget_3)
        self.accountBtn.setObjectName(u"accountBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/avatar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.accountBtn.setIcon(icon5)
        self.accountBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.accountBtn)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.cardFrame = QWidget(self.mainContainer)
        self.cardFrame.setObjectName(u"cardFrame")
        self.horizontalLayout_7 = QHBoxLayout(self.cardFrame)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.card1 = QFrame(self.cardFrame)
        self.card1.setObjectName(u"card1")
        self.card1.setFrameShape(QFrame.Shape.StyledPanel)
        self.card1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.card1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.card1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.label.setFont(font4)

        self.horizontalLayout_8.addWidget(self.label)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(40, 40))
        self.label_3.setMaximumSize(QSize(40, 40))
        font5 = QFont()
        font5.setPointSize(14)
        self.label_3.setFont(font5)
        self.label_3.setPixmap(QPixmap(u":/icons/icons/caddie.png"))

        self.horizontalLayout_8.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.label_4 = QLabel(self.card1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_7.addWidget(self.card1)

        self.card2 = QFrame(self.cardFrame)
        self.card2.setObjectName(u"card2")
        self.card2.setFrameShape(QFrame.Shape.StyledPanel)
        self.card2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.card2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.card2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(40, 40))
        self.label_7.setMaximumSize(QSize(40, 40))
        self.label_7.setFont(font5)
        self.label_7.setPixmap(QPixmap(u":/icons/icons/caddie.png"))

        self.horizontalLayout_9.addWidget(self.label_7)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignTop)

        self.label_5 = QLabel(self.card2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_7.addWidget(self.card2)

        self.card3 = QFrame(self.cardFrame)
        self.card3.setObjectName(u"card3")
        self.card3.setFrameShape(QFrame.Shape.StyledPanel)
        self.card3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.card3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.card3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(40, 40))
        self.label_10.setMaximumSize(QSize(40, 40))
        self.label_10.setFont(font5)
        self.label_10.setPixmap(QPixmap(u":/icons/icons/caddie.png"))

        self.horizontalLayout_10.addWidget(self.label_10)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignTop)

        self.label_8 = QLabel(self.card3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_7.addWidget(self.card3)

        self.card4 = QFrame(self.cardFrame)
        self.card4.setObjectName(u"card4")
        self.card4.setFrameShape(QFrame.Shape.StyledPanel)
        self.card4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.card4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.card4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.horizontalLayout_11.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(40, 40))
        self.label_13.setMaximumSize(QSize(40, 40))
        self.label_13.setFont(font5)
        self.label_13.setPixmap(QPixmap(u":/icons/icons/caddie.png"))

        self.horizontalLayout_11.addWidget(self.label_13)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignTop)

        self.label_11 = QLabel(self.card4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_7.addWidget(self.card4)


        self.verticalLayout.addWidget(self.cardFrame)

        self.mainFrame = QWidget(self.mainContainer)
        self.mainFrame.setObjectName(u"mainFrame")
        self.horizontalLayout_12 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.mainFrame)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.widget_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        font6 = QFont()
        font6.setPointSize(13)
        font6.setBold(True)
        self.label_14.setFont(font6)

        self.horizontalLayout_13.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignLeft)

        self.seeMoreButton = QPushButton(self.frame_5)
        self.seeMoreButton.setObjectName(u"seeMoreButton")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/arrow-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.seeMoreButton.setIcon(icon6)
        self.seeMoreButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.seeMoreButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_5, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_6 = QFrame(self.widget_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 40, 111, 16))

        self.verticalLayout_6.addWidget(self.frame_6)


        self.horizontalLayout_12.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.mainFrame)
        self.widget_5.setObjectName(u"widget_5")

        self.horizontalLayout_12.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.mainFrame)


        self.horizontalLayout.addWidget(self.mainContainer)

        self.profileContainer = QWidget(self.centralwidget)
        self.profileContainer.setObjectName(u"profileContainer")
        self.verticalLayout_11 = QVBoxLayout(self.profileContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.profileContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(100, 0))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_18 = QLabel(self.frame_10)
        self.label_18.setObjectName(u"label_18")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.label_18.setFont(font7)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_18, 0, Qt.AlignmentFlag.AlignTop)

        self.label_17 = QLabel(self.frame_10)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_17, 0, Qt.AlignmentFlag.AlignTop)

        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setPixmap(QPixmap(u":/icons/icons/avatar.png"))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_12.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignTop)

        self.pushButton_5 = QPushButton(self.frame_10)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setIconSize(QSize(18, 18))

        self.verticalLayout_12.addWidget(self.pushButton_5, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_11.addWidget(self.frame_10, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout.addWidget(self.profileContainer, 0, Qt.AlignmentFlag.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Irina Service", None))
        self.irinaServiceLabel.setText(QCoreApplication.translate("MainWindow", u"IrinaService", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Etat de Stock", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Liste des clients", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Consulter facture", None))
        self.menuBtn.setText("")
        self.appHeader.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_2.setText("")
        self.searchField.setText("")
        self.searchField.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher ici . . .", None))
        self.accountBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"2000,000", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ariary", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"2000,000", None))
        self.label_7.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ariary", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"2000,000", None))
        self.label_10.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ariary", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"2000,000", None))
        self.label_13.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Ariary", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Produits recents", None))
        self.seeMoreButton.setText(QCoreApplication.translate("MainWindow", u"Voir Plus", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Liste des produits", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_16.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Mon Profile", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Se deconnecter", None))
    # retranslateUi

