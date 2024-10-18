# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_admin_windowxKMCQz.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import views.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1312, 710)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame, QWidget{\n"
"	\n"
"}\n"
"\n"
"#search_frame{\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"#search_field{\n"
"	border: none;\n"
"	background: transparent;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: rgb(233, 233, 233);\n"
"}\n"
"\n"
"QRadioButton{\n"
"	border: 1px solid  rgb(89, 108, 112);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit{\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(89, 108, 112);\n"
"	background: #fefeff;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"#search_ajout{\n"
"	padding-left: 35px;\n"
"	background: #fefeff;\n"
"}\n"
"#affichage1{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 85, 255), stop:1 rgb(0, 170, 255));\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#affichage1 QLineEdit{\n"
"	border: none;\n"
"	border-radius: none;\n"
"	background-color: transparent;\n"
"	border-bottom: 2px solid #c4e4db;\n"
"	color: rgb(255, 171, 25);\n"
"	font-size: 1"
                        "5px;\n"
"	font-family: Arial;\n"
"}\n"
"\n"
"#affichage1 QLabel{\n"
"	color: #fefeff;\n"
"}\n"
"\n"
"#formulaire1{\n"
"	background: #fefeff;\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"#submitBtn{\n"
"	color: rgb(17, 166, 54);\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(17, 166, 54);\n"
"}\n"
"\n"
"#resetBtn{\n"
"	color: rgb(255, 58, 23);\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(255, 58, 23);\n"
"}\n"
"\n"
"#article_name{\n"
"	color: #fff;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"}\n"
"\n"
"#appro_detail{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QWidget(self.widget)
        self.left_menu.setObjectName(u"left_menu")
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(47, 109, 255);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#formulaireBtn{\n"
"	background-color: #fefeff;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formulaireBtn = QPushButton(self.frame_2)
        self.formulaireBtn.setObjectName(u"formulaireBtn")
        self.formulaireBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/caddie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.formulaireBtn.setIcon(icon)
        self.formulaireBtn.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.formulaireBtn)

        self.dashboardBtn = QPushButton(self.frame_2)
        self.dashboardBtn.setObjectName(u"dashboardBtn")
        self.dashboardBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/stock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboardBtn.setIcon(icon1)
        self.dashboardBtn.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.dashboardBtn)

        self.clientBtn = QPushButton(self.frame_2)
        self.clientBtn.setObjectName(u"clientBtn")
        self.clientBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/avatar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clientBtn.setIcon(icon2)
        self.clientBtn.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.clientBtn)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addWidget(self.left_menu, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_2)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.appHeader_2 = QLabel(self.widget_12)
        self.appHeader_2.setObjectName(u"appHeader_2")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.appHeader_2.setFont(font)

        self.horizontalLayout_16.addWidget(self.appHeader_2)


        self.horizontalLayout_17.addWidget(self.widget_12, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_10 = QWidget(self.widget_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(300, 0))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.search_frame = QFrame(self.widget_10)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(160, 0))
        self.search_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.search_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u":/icons/icons/search.png"))

        self.horizontalLayout_14.addWidget(self.label_12)

        self.search_field = QLineEdit(self.search_frame)
        self.search_field.setObjectName(u"search_field")
        self.search_field.setMaximumSize(QSize(16777215, 300))

        self.horizontalLayout_14.addWidget(self.search_field)


        self.horizontalLayout_13.addWidget(self.search_frame, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_17.addWidget(self.widget_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.accountBtn_2 = QPushButton(self.widget_11)
        self.accountBtn_2.setObjectName(u"accountBtn_2")
        self.accountBtn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.accountBtn_2.setIcon(icon2)
        self.accountBtn_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_15.addWidget(self.accountBtn_2, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_17.addWidget(self.widget_11)


        self.verticalLayout_4.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainNavigationScreen = QCustomQStackedWidget(self.widget_3)
        self.mainNavigationScreen.setObjectName(u"mainNavigationScreen")
        self.ajout_page = QWidget()
        self.ajout_page.setObjectName(u"ajout_page")
        self.horizontalLayout_5 = QHBoxLayout(self.ajout_page)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_4 = QWidget(self.ajout_page)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formulaire1 = QWidget(self.widget_4)
        self.formulaire1.setObjectName(u"formulaire1")
        self.frame_4 = QFrame(self.formulaire1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 20, 541, 361))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 16, 91, 20))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_3.setFont(font1)
        self.libelle_form = QLineEdit(self.frame_10)
        self.libelle_form.setObjectName(u"libelle_form")
        self.libelle_form.setGeometry(QRect(0, 40, 211, 31))
        self.lineEdit_6 = QLineEdit(self.frame_10)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(590, 40, 211, 31))

        self.verticalLayout_6.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 10, 81, 16))
        self.label_4.setFont(font1)
        self.radioButton = QRadioButton(self.frame_9)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(0, 40, 91, 31))
        self.radioButton_2 = QRadioButton(self.frame_9)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(120, 40, 91, 31))

        self.verticalLayout_6.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 20, 191, 18))
        self.label_2.setFont(font1)
        self.pieceParConteneur = QLineEdit(self.frame_8)
        self.pieceParConteneur.setObjectName(u"pieceParConteneur")
        self.pieceParConteneur.setGeometry(QRect(0, 40, 211, 31))

        self.verticalLayout_6.addWidget(self.frame_8)


        self.horizontalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 16, 91, 20))
        self.label_5.setFont(font1)
        self.prix_form = QLineEdit(self.frame_11)
        self.prix_form.setObjectName(u"prix_form")
        self.prix_form.setGeometry(QRect(10, 40, 201, 31))

        self.verticalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 16, 151, 20))
        self.label_6.setFont(font1)
        self.nbConteneur_form = QLineEdit(self.frame_12)
        self.nbConteneur_form.setObjectName(u"nbConteneur_form")
        self.nbConteneur_form.setGeometry(QRect(10, 40, 201, 31))

        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame_13)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 20, 231, 18))
        self.label_7.setFont(font1)
        self.pieceSupplement_form = QLineEdit(self.frame_13)
        self.pieceSupplement_form.setObjectName(u"pieceSupplement_form")
        self.pieceSupplement_form.setGeometry(QRect(10, 40, 201, 31))

        self.verticalLayout_7.addWidget(self.frame_13)


        self.horizontalLayout_6.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.formulaire1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 390, 501, 101))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_8)

        self.description_form = QLineEdit(self.frame_7)
        self.description_form.setObjectName(u"description_form")

        self.verticalLayout_8.addWidget(self.description_form)

        self.submitBtn = QPushButton(self.formulaire1)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(30, 530, 241, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.submitBtn.setFont(font2)
        self.resetBtn = QPushButton(self.formulaire1)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setGeometry(QRect(290, 530, 221, 41))
        self.resetBtn.setFont(font2)

        self.horizontalLayout_7.addWidget(self.formulaire1)

        self.affichage1 = QWidget(self.widget_4)
        self.affichage1.setObjectName(u"affichage1")
        self.widget_6 = QWidget(self.affichage1)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(10, 10, 521, 591))
        self.frame_14 = QFrame(self.widget_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(10, -40, 521, 631))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(10, 140, 261, 101))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.label_10 = QLabel(self.frame_15)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 20, 71, 16))
        self.prixUnitaire_detail = QLineEdit(self.frame_15)
        self.prixUnitaire_detail.setObjectName(u"prixUnitaire_detail")
        self.prixUnitaire_detail.setEnabled(False)
        self.prixUnitaire_detail.setGeometry(QRect(10, 40, 201, 31))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setBold(True)
        self.prixUnitaire_detail.setFont(font3)
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(280, 140, 231, 101))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.label_11 = QLabel(self.frame_16)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 20, 201, 16))
        self.pieceParConteneur_detail = QLineEdit(self.frame_16)
        self.pieceParConteneur_detail.setObjectName(u"pieceParConteneur_detail")
        self.pieceParConteneur_detail.setEnabled(False)
        self.pieceParConteneur_detail.setGeometry(QRect(10, 40, 201, 31))
        self.pieceParConteneur_detail.setFont(font3)
        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(10, 250, 261, 101))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 20, 71, 16))
        self.conteneur_detail = QLineEdit(self.frame_17)
        self.conteneur_detail.setObjectName(u"conteneur_detail")
        self.conteneur_detail.setEnabled(False)
        self.conteneur_detail.setGeometry(QRect(10, 40, 201, 31))
        self.conteneur_detail.setFont(font3)
        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(10, 360, 261, 101))
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.label_14 = QLabel(self.frame_18)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 20, 101, 16))
        self.piece_detail = QLineEdit(self.frame_18)
        self.piece_detail.setObjectName(u"piece_detail")
        self.piece_detail.setEnabled(False)
        self.piece_detail.setGeometry(QRect(10, 40, 201, 31))
        self.piece_detail.setFont(font3)
        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(280, 250, 231, 101))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.label_15 = QLabel(self.frame_19)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 20, 131, 16))
        self.nbConteneur_detail = QLineEdit(self.frame_19)
        self.nbConteneur_detail.setObjectName(u"nbConteneur_detail")
        self.nbConteneur_detail.setEnabled(False)
        self.nbConteneur_detail.setGeometry(QRect(10, 40, 201, 31))
        self.nbConteneur_detail.setFont(font3)
        self.frame_20 = QFrame(self.frame_14)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(280, 360, 261, 101))
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.label_16 = QLabel(self.frame_20)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 20, 131, 16))
        self.dateEntrer_detail = QLineEdit(self.frame_20)
        self.dateEntrer_detail.setObjectName(u"dateEntrer_detail")
        self.dateEntrer_detail.setEnabled(False)
        self.dateEntrer_detail.setGeometry(QRect(10, 40, 201, 31))
        self.dateEntrer_detail.setFont(font3)
        self.frame_21 = QFrame(self.frame_14)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(10, 50, 491, 80))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.article_name = QLabel(self.frame_21)
        self.article_name.setObjectName(u"article_name")
        self.article_name.setGeometry(QRect(180, 30, 181, 20))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.article_name.setFont(font4)
        self.frame_22 = QFrame(self.frame_14)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(10, 489, 511, 111))
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.description_detail = QTextEdit(self.frame_22)
        self.description_detail.setObjectName(u"description_detail")
        self.description_detail.setEnabled(False)
        self.description_detail.setGeometry(QRect(10, 30, 471, 61))
        self.description_detail.setFont(font1)
        self.label_18 = QLabel(self.frame_22)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 10, 121, 16))
        self.appro_detail = QPushButton(self.frame_14)
        self.appro_detail.setObjectName(u"appro_detail")
        self.appro_detail.setGeometry(QRect(150, 600, 231, 31))
        self.appro_detail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.affichage1)


        self.horizontalLayout_5.addWidget(self.widget_4)

        self.mainNavigationScreen.addWidget(self.ajout_page)
        self.dashboardPage = QWidget()
        self.dashboardPage.setObjectName(u"dashboardPage")
        self.label = QLabel(self.dashboardPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 341, 31))
        font5 = QFont()
        font5.setPointSize(15)
        self.label.setFont(font5)
        self.mainNavigationScreen.addWidget(self.dashboardPage)
        self.clientPage = QWidget()
        self.clientPage.setObjectName(u"clientPage")
        self.label_9 = QLabel(self.clientPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 40, 281, 31))
        self.label_9.setFont(font5)
        self.mainNavigationScreen.addWidget(self.clientPage)

        self.horizontalLayout_2.addWidget(self.mainNavigationScreen)


        self.verticalLayout_4.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.widget_5)


        self.horizontalLayout_3.addWidget(self.widget)

        self.profile_container = QCustomSlideMenu(self.centralwidget)
        self.profile_container.setObjectName(u"profile_container")
        self.verticalLayout_9 = QVBoxLayout(self.profile_container)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.widget_14 = QWidget(self.profile_container)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_5 = QVBoxLayout(self.widget_14)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget_14)
        self.label_19.setObjectName(u"label_19")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_19.setFont(font6)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_19)

        self.label_17 = QLabel(self.widget_14)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_17)

        self.label_20 = QLabel(self.widget_14)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setPixmap(QPixmap(u":/icons/icons/avatar.png"))
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_20)

        self.pushButton_5 = QPushButton(self.widget_14)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_5.addWidget(self.pushButton_5)

        self.logoutBtn = QPushButton(self.widget_14)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutBtn.setIcon(icon3)
        self.logoutBtn.setIconSize(QSize(18, 18))

        self.verticalLayout_5.addWidget(self.logoutBtn)


        self.verticalLayout_9.addWidget(self.widget_14, 0, Qt.AlignmentFlag.AlignTop)

        self.search_view = QTableWidget(self.profile_container)
        if (self.search_view.columnCount() < 2):
            self.search_view.setColumnCount(2)
        font7 = QFont()
        font7.setPointSize(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font7);
        self.search_view.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.search_view.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.search_view.setObjectName(u"search_view")
        self.search_view.setEnabled(True)
        self.search_view.setMaximumSize(QSize(120, 16777215))
        self.search_view.setBaseSize(QSize(100, 0))
        self.search_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_9.addWidget(self.search_view, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.profile_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainNavigationScreen.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.formulaireBtn.setText("")
        self.dashboardBtn.setText("")
        self.clientBtn.setText("")
        self.pushButton.setText("")
        self.appHeader_2.setText(QCoreApplication.translate("MainWindow", u"Administration", None))
        self.label_12.setText("")
        self.search_field.setText("")
        self.search_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher ici . . .", None))
        self.accountBtn_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Libelle *", None))
        self.libelle_form.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom de l'article", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom de l'article", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Conteneur *", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Paquet", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Boite", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre dans un conteneur *", None))
        self.pieceParConteneur.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre de piece par conteneur", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Prix unitaire *", None))
        self.prix_form.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prix unitaire en Ariary", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nombre de conteneur *", None))
        self.nbConteneur_form.setText("")
        self.nbConteneur_form.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Conteneur a ajouter", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nombre de piece supplementaire *", None))
        self.pieceSupplement_form.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Piece supplementaire a ajouter", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Description *", None))
        self.description_form.setText("")
        self.description_form.setPlaceholderText(QCoreApplication.translate("MainWindow", u"description de l'article", None))
        self.submitBtn.setText(QCoreApplication.translate("MainWindow", u"Enregistrer modification", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"Vider les champs", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Prix Unitaire", None))
        self.prixUnitaire_detail.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Nombre de piece dans un conteneur", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Conteneur", None))
        self.conteneur_detail.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Total des pieces", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Conteneur en stock", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Date d'entrer en stock", None))
        self.article_name.setText(QCoreApplication.translate("MainWindow", u"Nom de l'article", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.appro_detail.setText(QCoreApplication.translate("MainWindow", u"Details d'approvisionnement", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tableau de bord", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_20.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Mon Profile", None))
        self.logoutBtn.setText(QCoreApplication.translate("MainWindow", u"Se deconnecter", None))
        ___qtablewidgetitem = self.search_view.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Articles recherher", None));
        ___qtablewidgetitem1 = self.search_view.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"numero", None));
    # retranslateUi

