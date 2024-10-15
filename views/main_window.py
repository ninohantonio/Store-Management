# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowtkGugm.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import views.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1367, 701)
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
"#leftMenu, QCustomSlideMenu{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 85, 255), stop:1 rgb(0, 170, 255));\n"
"}\n"
"\n"
"#leftMenu{\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background: transparent;\n"
"}\n"
"\n"
"#searchFrame{\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"#appHeader{\n"
"	color: rgb(0, 170, 255);\n"
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
"	background-"
                        "color: #fefeff;\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"\n"
"#profileContainer{\n"
"	background-color: #fefeff;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#logoutBtn{\n"
"	padding: 4px 7px;\n"
"	border: 1px solid #000;\n"
"	border-radius: 7px\n"
"}\n"
"\n"
"\n"
"#welcomeLabel, #stock_labele, #facture_title{\n"
"	text-align: center;\n"
"	color:  rgb(0, 170, 255);\n"
"	background-color: #e5e0ff;\n"
"	padding: 10px 15px;\n"
"}\n"
"\n"
"#total_payer{\n"
"	color: #f56614;\n"
"}\n"
"\n"
"#valider_commandeBtn{\n"
"	background: #d5d2ff;\n"
"	padding: 7px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"#stockTable{\n"
"	background-color: rgb(244, 244, 255);\n"
"}\n"
"\n"
"#filter_labele{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"#filterCombo, #dateEdit, #dateEdit_2{\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 220, 219);\n"
"}\n"
"\n"
"#avance_field{\n"
"	border: 1px solid rgb(0, 85, 255);\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"#selection_rapide_combo, #quantite_spinBox{\n"
"	padding-left: 5px;\n"
""
                        "	border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"#add_selection_rapideBtn{\n"
"	border: 2px solid rgb(0, 170, 255);\n"
"	border-radius: 7px;\n"
"	padding: 2px;\n"
"	cursor: pointer;\n"
"}\n"
"\n"
"#submit_section_rapideBtn{\n"
"	border: 2px solid rgb(0, 255, 127);\n"
"	border-radius: 7px;\n"
"	padding: 2px;\n"
"	cursor: pointer;\n"
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

        self.factureBtn = QPushButton(self.menuFrame)
        self.factureBtn.setObjectName(u"factureBtn")
        self.factureBtn.setFont(font2)
        self.factureBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/caddie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.factureBtn.setIcon(icon2)
        self.factureBtn.setIconSize(QSize(27, 27))

        self.verticalLayout_9.addWidget(self.factureBtn)

        self.journalBtn = QPushButton(self.menuFrame)
        self.journalBtn.setObjectName(u"journalBtn")
        self.journalBtn.setFont(font2)
        self.journalBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/facture.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.journalBtn.setIcon(icon3)
        self.journalBtn.setIconSize(QSize(19, 19))

        self.verticalLayout_9.addWidget(self.journalBtn)

        self.clientBtn = QPushButton(self.menuFrame)
        self.clientBtn.setObjectName(u"clientBtn")
        self.clientBtn.setFont(font2)
        self.clientBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/people.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clientBtn.setIcon(icon4)
        self.clientBtn.setIconSize(QSize(22, 22))

        self.verticalLayout_9.addWidget(self.clientBtn)

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
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingBtn.setIcon(icon5)
        self.settingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.settingBtn)

        self.helpBtn = QPushButton(self.frame_6)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font2)
        self.helpBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/about.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.helpBtn)

        self.aboutBtn = QPushButton(self.frame_6)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setFont(font2)
        self.aboutBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.aboutBtn.setIcon(icon7)
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
        self.menuBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/burger-menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon8)
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
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/avatar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.accountBtn.setIcon(icon9)
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
        self.frame.setGeometry(QRect(0, 20, 661, 71))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.welcomeLabel = QLabel(self.frame)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        font4 = QFont()
        font4.setPointSize(15)
        self.welcomeLabel.setFont(font4)

        self.verticalLayout_3.addWidget(self.welcomeLabel)

        self.frame_10 = QFrame(self.homePage)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 90, 161, 34))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setPointSize(13)
        font5.setBold(True)
        self.label.setFont(font5)

        self.horizontalLayout_7.addWidget(self.label)

        self.widget_5 = QWidget(self.homePage)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 580, 441, 51))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.total_payer = QLabel(self.widget_5)
        self.total_payer.setObjectName(u"total_payer")
        font6 = QFont()
        font6.setFamilies([u"Lucida Fax"])
        font6.setPointSize(15)
        self.total_payer.setFont(font6)

        self.horizontalLayout_8.addWidget(self.total_payer)

        self.gridLayoutWidget = QWidget(self.homePage)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 140, 761, 431))
        self.cardContainer = QGridLayout(self.gridLayoutWidget)
        self.cardContainer.setObjectName(u"cardContainer")
        self.cardContainer.setContentsMargins(0, 0, 0, 0)
        self.valider_commandeBtn = QPushButton(self.homePage)
        self.valider_commandeBtn.setObjectName(u"valider_commandeBtn")
        self.valider_commandeBtn.setGeometry(QRect(540, 580, 241, 51))
        font7 = QFont()
        font7.setPointSize(13)
        font7.setBold(False)
        self.valider_commandeBtn.setFont(font7)
        self.valider_commandeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.valider_commandeBtn.setIcon(icon2)
        self.valider_commandeBtn.setIconSize(QSize(30, 30))
        self.tout_payer = QRadioButton(self.homePage)
        self.tout_payer.setObjectName(u"tout_payer")
        self.tout_payer.setGeometry(QRect(250, 100, 89, 20))
        self.non_payer = QRadioButton(self.homePage)
        self.non_payer.setObjectName(u"non_payer")
        self.non_payer.setGeometry(QRect(390, 100, 89, 20))
        self.avancement = QRadioButton(self.homePage)
        self.avancement.setObjectName(u"avancement")
        self.avancement.setGeometry(QRect(520, 100, 89, 20))
        self.avance_field = QLineEdit(self.homePage)
        self.avance_field.setObjectName(u"avance_field")
        self.avance_field.setGeometry(QRect(540, 100, 113, 22))
        self.label_9 = QLabel(self.homePage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(680, 50, 111, 16))
        font8 = QFont()
        font8.setPointSize(10)
        self.label_9.setFont(font8)
        self.selection_rapide_combo = QComboBox(self.homePage)
        self.selection_rapide_combo.addItem("")
        self.selection_rapide_combo.setObjectName(u"selection_rapide_combo")
        self.selection_rapide_combo.setGeometry(QRect(790, 50, 141, 22))
        self.quantite_spinBox = QSpinBox(self.homePage)
        self.quantite_spinBox.setObjectName(u"quantite_spinBox")
        self.quantite_spinBox.setGeometry(QRect(940, 50, 61, 22))
        self.add_selection_rapideBtn = QPushButton(self.homePage)
        self.add_selection_rapideBtn.setObjectName(u"add_selection_rapideBtn")
        self.add_selection_rapideBtn.setGeometry(QRect(800, 90, 81, 31))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_selection_rapideBtn.setIcon(icon10)
        self.add_selection_rapideBtn.setIconSize(QSize(26, 26))
        self.submit_section_rapideBtn = QPushButton(self.homePage)
        self.submit_section_rapideBtn.setObjectName(u"submit_section_rapideBtn")
        self.submit_section_rapideBtn.setGeometry(QRect(924, 90, 81, 31))
        self.submit_section_rapideBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/valide.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.submit_section_rapideBtn.setIcon(icon11)
        self.submit_section_rapideBtn.setIconSize(QSize(26, 26))
        self.mainNavigationScreen.addWidget(self.homePage)
        self.stockPage = QWidget()
        self.stockPage.setObjectName(u"stockPage")
        self.verticalLayout_4 = QVBoxLayout(self.stockPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.stockPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.stock_labele = QLabel(self.frame_2)
        self.stock_labele.setObjectName(u"stock_labele")
        self.stock_labele.setGeometry(QRect(20, 20, 601, 51))
        self.stock_labele.setFont(font4)
        self.stockTable = QTableWidget(self.frame_2)
        if (self.stockTable.columnCount() < 9):
            self.stockTable.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.stockTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.stockTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.stockTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.stockTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.stockTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.stockTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.stockTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.stockTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.stockTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.stockTable.setObjectName(u"stockTable")
        self.stockTable.setGeometry(QRect(20, 130, 951, 431))
        self.filter_labele = QLabel(self.frame_2)
        self.filter_labele.setObjectName(u"filter_labele")
        self.filter_labele.setGeometry(QRect(70, 80, 151, 31))
        font9 = QFont()
        font9.setPointSize(13)
        self.filter_labele.setFont(font9)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 80, 31, 31))
        self.label_3.setPixmap(QPixmap(u":/icons/icons/filter.png"))
        self.label_3.setScaledContents(True)
        self.filterCombo = QComboBox(self.frame_2)
        self.filterCombo.addItem("")
        self.filterCombo.addItem("")
        self.filterCombo.addItem("")
        self.filterCombo.addItem("")
        self.filterCombo.setObjectName(u"filterCombo")
        self.filterCombo.setGeometry(QRect(220, 81, 161, 31))

        self.verticalLayout_4.addWidget(self.frame_2)

        self.mainNavigationScreen.addWidget(self.stockPage)
        self.facturePage = QWidget()
        self.facturePage.setObjectName(u"facturePage")
        self.verticalLayout_5 = QVBoxLayout(self.facturePage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.facturePage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.facture_title = QLabel(self.frame_3)
        self.facture_title.setObjectName(u"facture_title")
        self.facture_title.setGeometry(QRect(10, 20, 631, 51))
        self.facture_title.setFont(font4)
        self.facture_table = QTableWidget(self.frame_3)
        if (self.facture_table.columnCount() < 5):
            self.facture_table.setColumnCount(5)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.facture_table.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.facture_table.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.facture_table.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.facture_table.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.facture_table.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        self.facture_table.setObjectName(u"facture_table")
        self.facture_table.setGeometry(QRect(10, 130, 881, 471))
        self.facture_table.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.dateEdit = QDateEdit(self.frame_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(220, 90, 121, 31))
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 90, 101, 31))
        font10 = QFont()
        font10.setPointSize(11)
        self.label_4.setFont(font10)
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(360, 95, 61, 21))
        self.label_8.setFont(font8)
        self.dateEdit_2 = QDateEdit(self.frame_3)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(430, 90, 121, 31))

        self.verticalLayout_5.addWidget(self.frame_3)

        self.mainNavigationScreen.addWidget(self.facturePage)
        self.journalPage = QWidget()
        self.journalPage.setObjectName(u"journalPage")
        self.frame_4 = QFrame(self.journalPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(40, 30, 401, 80))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 20, 141, 31))
        self.label_5.setFont(font4)
        self.mainNavigationScreen.addWidget(self.journalPage)
        self.clientPage = QWidget()
        self.clientPage.setObjectName(u"clientPage")
        self.frame_5 = QFrame(self.clientPage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(30, 30, 401, 80))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 20, 141, 31))
        self.label_6.setFont(font4)
        self.mainNavigationScreen.addWidget(self.clientPage)

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
        font11 = QFont()
        font11.setPointSize(12)
        font11.setBold(True)
        self.label_18.setFont(font11)
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
        self.logoutBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutBtn.setIcon(icon12)
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
        self.factureBtn.setText(QCoreApplication.translate("MainWindow", u"Consulter facture", None))
        self.journalBtn.setText(QCoreApplication.translate("MainWindow", u"Journal", None))
        self.clientBtn.setText(QCoreApplication.translate("MainWindow", u"Liste des clients", None))
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuBtn.setText("")
        self.appHeader.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_2.setText("")
        self.searchField.setText("")
        self.searchField.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher ici . . .", None))
        self.accountBtn.setText("")
        self.welcomeLabel.setText(QCoreApplication.translate("MainWindow", u"BIENVENUE DANS NOTRE SERVICE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Vos commandes :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Total a payer :", None))
        self.total_payer.setText(QCoreApplication.translate("MainWindow", u"0 Ar", None))
        self.valider_commandeBtn.setText(QCoreApplication.translate("MainWindow", u"Valider la commande", None))
        self.tout_payer.setText(QCoreApplication.translate("MainWindow", u"Tout payer", None))
        self.non_payer.setText(QCoreApplication.translate("MainWindow", u"Non Payer", None))
        self.avancement.setText("")
        self.avance_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Avancement", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Selection rapide :", None))
        self.selection_rapide_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"papier velin", None))

        self.add_selection_rapideBtn.setText(QCoreApplication.translate("MainWindow", u"ajouter", None))
        self.submit_section_rapideBtn.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.stock_labele.setText(QCoreApplication.translate("MainWindow", u"Etat de stock", None))
        ___qtablewidgetitem = self.stockTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Libelle", None));
        ___qtablewidgetitem1 = self.stockTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Prix unitaire", None));
        ___qtablewidgetitem2 = self.stockTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Pieces en stock", None));
        ___qtablewidgetitem3 = self.stockTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem4 = self.stockTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Pieces par pacquet", None));
        ___qtablewidgetitem5 = self.stockTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Pieces par boite", None));
        ___qtablewidgetitem6 = self.stockTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Paquets en stock", None));
        ___qtablewidgetitem7 = self.stockTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Boites en stock", None));
        ___qtablewidgetitem8 = self.stockTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Date d'entrer en stock", None));
        self.filter_labele.setText(QCoreApplication.translate("MainWindow", u"Rechecrcher par :", None))
        self.label_3.setText("")
        self.filterCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Libelle", None))
        self.filterCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Quantite en stock", None))
        self.filterCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Prix Unitaire", None))
        self.filterCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"Date d'entrer en stock", None))

        self.facture_title.setText(QCoreApplication.translate("MainWindow", u"Liste des factures", None))
        ___qtablewidgetitem9 = self.facture_table.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Numero de facture", None));
        ___qtablewidgetitem10 = self.facture_table.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Date enregistrement", None));
        ___qtablewidgetitem11 = self.facture_table.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Statut de payement", None));
        ___qtablewidgetitem12 = self.facture_table.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Aavancement", None));
        ___qtablewidgetitem13 = self.facture_table.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Identifiant client", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Filtre de date :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"jusqu'au", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Journal", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Liste des clients", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Vendeur", None))
        self.label_16.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Mon Profile", None))
        self.logoutBtn.setText(QCoreApplication.translate("MainWindow", u"Se deconnecter", None))
    # retranslateUi

