# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windoweJbURV.ui'
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
    QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import views.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 613)
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
"#leftMenu,QCustomSlideMenu{\n"
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
"#menuFrame #accueilBtn{\n"
"	background-color: #fefeff;\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"\n"
"#profileContainer{\n"
"	background-color: #fefeff;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
""
                        "#logoutBtn{\n"
"	padding: 4px 7px;\n"
"	border: 1px solid #000;\n"
"	border-radius: 7px\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
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
        self.frame_9.setMinimumSize(QSize(200, 0))
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
        self.accueilBtn = QPushButton(self.menuFrame)
        self.accueilBtn.setObjectName(u"accueilBtn")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.accueilBtn.setFont(font1)
        self.accueilBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.accueilBtn.setIcon(icon)
        self.accueilBtn.setIconSize(QSize(22, 22))

        self.verticalLayout_9.addWidget(self.accueilBtn)

        self.stockBtn = QPushButton(self.menuFrame)
        self.stockBtn.setObjectName(u"stockBtn")
        font2 = QFont()
        font2.setPointSize(12)
        self.stockBtn.setFont(font2)
        self.stockBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/stock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stockBtn.setIcon(icon1)
        self.stockBtn.setIconSize(QSize(22, 22))

        self.verticalLayout_9.addWidget(self.stockBtn)

        self.clientBtn = QPushButton(self.menuFrame)
        self.clientBtn.setObjectName(u"clientBtn")
        self.clientBtn.setFont(font2)
        self.clientBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/people.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clientBtn.setIcon(icon2)
        self.clientBtn.setIconSize(QSize(22, 22))

        self.verticalLayout_9.addWidget(self.clientBtn)

        self.factureBtn = QPushButton(self.menuFrame)
        self.factureBtn.setObjectName(u"factureBtn")
        self.factureBtn.setFont(font2)
        self.factureBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/facture.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.factureBtn.setIcon(icon3)
        self.factureBtn.setIconSize(QSize(19, 19))

        self.verticalLayout_9.addWidget(self.factureBtn)

        self.journalBtn = QPushButton(self.menuFrame)
        self.journalBtn.setObjectName(u"journalBtn")
        self.journalBtn.setFont(font2)
        self.journalBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.journalBtn.setIcon(icon3)
        self.journalBtn.setIconSize(QSize(19, 19))

        self.verticalLayout_9.addWidget(self.journalBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.frame_6 = QFrame(self.menuFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingBtn = QPushButton(self.frame_6)
        self.settingBtn.setObjectName(u"settingBtn")
        self.settingBtn.setFont(font2)
        self.settingBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingBtn.setIcon(icon4)
        self.settingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.settingBtn)

        self.helpBtn = QPushButton(self.frame_6)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font2)
        self.helpBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/about.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon5)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.helpBtn)

        self.aboutBtn = QPushButton(self.frame_6)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setFont(font2)
        self.aboutBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.aboutBtn.setIcon(icon6)
        self.aboutBtn.setIconSize(QSize(22, 22))

        self.verticalLayout_2.addWidget(self.aboutBtn)


        self.verticalLayout_9.addWidget(self.frame_6)


        self.verticalLayout_10.addWidget(self.menuFrame)


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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy1)
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
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/burger-menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon7)
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
        self.widget_2.setMinimumSize(QSize(300, 0))
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
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/avatar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.accountBtn.setIcon(icon8)
        self.accountBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.accountBtn)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.mainNavigationScreen = QCustomQStackedWidget(self.mainContainer)
        self.mainNavigationScreen.setObjectName(u"mainNavigationScreen")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.frame = QFrame(self.homePage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 20, 401, 80))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 141, 31))
        font4 = QFont()
        font4.setPointSize(15)
        self.label.setFont(font4)
        self.mainNavigationScreen.addWidget(self.homePage)
        self.stockPage = QWidget()
        self.stockPage.setObjectName(u"stockPage")
        self.frame_2 = QFrame(self.stockPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 30, 401, 80))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 20, 141, 31))
        self.label_3.setFont(font4)
        self.mainNavigationScreen.addWidget(self.stockPage)
        self.clientPage = QWidget()
        self.clientPage.setObjectName(u"clientPage")
        self.frame_3 = QFrame(self.clientPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(40, 30, 401, 80))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 20, 141, 31))
        self.label_4.setFont(font4)
        self.mainNavigationScreen.addWidget(self.clientPage)
        self.facturePage = QWidget()
        self.facturePage.setObjectName(u"facturePage")
        self.frame_4 = QFrame(self.facturePage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(40, 30, 401, 80))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 20, 141, 31))
        self.label_5.setFont(font4)
        self.mainNavigationScreen.addWidget(self.facturePage)
        self.journalPage = QWidget()
        self.journalPage.setObjectName(u"journalPage")
        self.frame_5 = QFrame(self.journalPage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(30, 30, 401, 80))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 20, 141, 31))
        self.label_6.setFont(font4)
        self.mainNavigationScreen.addWidget(self.journalPage)

        self.verticalLayout.addWidget(self.mainNavigationScreen)


        self.horizontalLayout.addWidget(self.mainContainer)

        self.profileContainer = QWidget(self.centralwidget)
        self.profileContainer.setObjectName(u"profileContainer")
        self.verticalLayout_11 = QVBoxLayout(self.profileContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.profileMenu = QCustomSlideMenu(self.profileContainer)
        self.profileMenu.setObjectName(u"profileMenu")
        self.profileMenu.setMinimumSize(QSize(100, 150))
        self.verticalLayout_12 = QVBoxLayout(self.profileMenu)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_18 = QLabel(self.profileMenu)
        self.label_18.setObjectName(u"label_18")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_18.setFont(font5)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_18, 0, Qt.AlignmentFlag.AlignTop)

        self.label_17 = QLabel(self.profileMenu)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_17, 0, Qt.AlignmentFlag.AlignTop)

        self.label_16 = QLabel(self.profileMenu)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setPixmap(QPixmap(u":/icons/icons/avatar.png"))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.pushButton = QPushButton(self.profileMenu)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_12.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignTop)

        self.logoutBtn = QPushButton(self.profileMenu)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutBtn.setIcon(icon9)
        self.logoutBtn.setIconSize(QSize(18, 18))

        self.verticalLayout_12.addWidget(self.logoutBtn, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_11.addWidget(self.profileMenu)


        self.horizontalLayout.addWidget(self.profileContainer, 0, Qt.AlignmentFlag.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainNavigationScreen.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Irina Service", None))
        self.irinaServiceLabel.setText(QCoreApplication.translate("MainWindow", u"IrinaService", None))
        self.accueilBtn.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.stockBtn.setText(QCoreApplication.translate("MainWindow", u"Etat de Stock", None))
        self.clientBtn.setText(QCoreApplication.translate("MainWindow", u"Liste des clients", None))
        self.factureBtn.setText(QCoreApplication.translate("MainWindow", u"Consulter facture", None))
        self.journalBtn.setText(QCoreApplication.translate("MainWindow", u"Journal", None))
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuBtn.setText("")
        self.appHeader.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_2.setText("")
        self.searchField.setText("")
        self.searchField.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher ici . . .", None))
        self.accountBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Etat de stock", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Liste des clients", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Facture", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Journal", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_16.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Mon Profile", None))
        self.logoutBtn.setText(QCoreApplication.translate("MainWindow", u"Se deconnecter", None))
    # retranslateUi

