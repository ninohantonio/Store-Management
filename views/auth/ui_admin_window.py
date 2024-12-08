# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_admin_windowCPRJbq.ui'
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
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import views.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1365, 697)
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

        self.reliureBtn = QPushButton(self.frame_2)
        self.reliureBtn.setObjectName(u"reliureBtn")
        self.reliureBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reliureBtn.setIcon(icon2)
        self.reliureBtn.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.reliureBtn)

        self.clientBtn = QPushButton(self.frame_2)
        self.clientBtn.setObjectName(u"clientBtn")
        self.clientBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/avatar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clientBtn.setIcon(icon3)
        self.clientBtn.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.clientBtn)

        self.barcodeBtn = QPushButton(self.frame_2)
        self.barcodeBtn.setObjectName(u"barcodeBtn")
        self.barcodeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/barcode.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.barcodeBtn.setIcon(icon4)
        self.barcodeBtn.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.barcodeBtn)

        self.changePasswordBtn = QPushButton(self.frame_2)
        self.changePasswordBtn.setObjectName(u"changePasswordBtn")
        self.changePasswordBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.changePasswordBtn.setIcon(icon5)
        self.changePasswordBtn.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.changePasswordBtn)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

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
        self.accountBtn_2.setIcon(icon3)
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
        self.article_name.setGeometry(QRect(110, 30, 301, 20))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.article_name.setFont(font4)
        self.article_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label.setGeometry(QRect(10, 20, 521, 41))
        font5 = QFont()
        font5.setPointSize(15)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: white;\n"
"padding-left: 10px;")
        self.widget_7 = QWidget(self.dashboardPage)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 80, 1131, 551))
        self.widget_7.setStyleSheet(u"background-color: white;\n"
"")
        self.frame_23 = QFrame(self.widget_7)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(10, 10, 161, 101))
        self.frame_23.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-radius: 20px;")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_23)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_21 = QLabel(self.frame_23)
        self.label_21.setObjectName(u"label_21")
        font6 = QFont()
        font6.setBold(True)
        self.label_21.setFont(font6)
        self.label_21.setStyleSheet(u"background-color: transparent;\n"
"color: #dfdfdf;")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_21)

        self.vente_jour = QLabel(self.frame_23)
        self.vente_jour.setObjectName(u"vente_jour")
        font7 = QFont()
        font7.setFamilies([u"Nirmala UI Semilight"])
        font7.setPointSize(11)
        font7.setBold(True)
        self.vente_jour.setFont(font7)
        self.vente_jour.setStyleSheet(u"color: #fefeff;\n"
"background: transparent;")
        self.vente_jour.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.vente_jour)

        self.label_23 = QLabel(self.frame_23)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"background: transparent;")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_23)

        self.frame_26 = QFrame(self.widget_7)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(260, 10, 161, 101))
        self.frame_26.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-radius: 20px;")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_26)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_30 = QLabel(self.frame_26)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font6)
        self.label_30.setStyleSheet(u"background-color: transparent;\n"
"color: #dedede;")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_30)

        self.vente_mois = QLabel(self.frame_26)
        self.vente_mois.setObjectName(u"vente_mois")
        self.vente_mois.setFont(font7)
        self.vente_mois.setStyleSheet(u"color: #fefeff;\n"
"background: transparent;")
        self.vente_mois.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.vente_mois)

        self.label_32 = QLabel(self.frame_26)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"background: transparent;")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_32)

        self.frame_27 = QFrame(self.widget_7)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(10, 180, 421, 361))
        self.frame_27.setStyleSheet(u"QFrame{\n"
"	background: rgb(234, 234, 234);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.label_33 = QLabel(self.frame_27)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 10, 171, 21))
        font8 = QFont()
        font8.setPointSize(10)
        self.label_33.setFont(font8)
        self.pushButton_2 = QPushButton(self.frame_27)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 10, 81, 24))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border-radius: 10px;\n"
"background: rgb(249, 249, 249);")
        self.facture_tableWidget = QTableWidget(self.frame_27)
        if (self.facture_tableWidget.columnCount() < 4):
            self.facture_tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.facture_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.facture_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.facture_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.facture_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.facture_tableWidget.setObjectName(u"facture_tableWidget")
        self.facture_tableWidget.setGeometry(QRect(0, 40, 421, 311))
        self.facture_tableWidget.setStyleSheet(u"background-color: white;")
        self.facture_tableWidget.setAlternatingRowColors(True)
        self.verticalLayoutWidget = QWidget(self.widget_7)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(440, 50, 681, 481))
        self.chartContainer = QVBoxLayout(self.verticalLayoutWidget)
        self.chartContainer.setObjectName(u"chartContainer")
        self.chartContainer.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.widget_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(440, 10, 681, 41))
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"border: 1px solid rgb(0, 85, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_facture = QDateEdit(self.widget_7)
        self.date_facture.setObjectName(u"date_facture")
        self.date_facture.setGeometry(QRect(20, 130, 121, 31))
        self.date_facture.setStyleSheet(u"border: 2px solid rgb(0, 85, 255);\n"
"border-radius: 10px;")
        self.filter_facture_combo = QComboBox(self.widget_7)
        self.filter_facture_combo.addItem("")
        self.filter_facture_combo.addItem("")
        self.filter_facture_combo.addItem("")
        self.filter_facture_combo.setObjectName(u"filter_facture_combo")
        self.filter_facture_combo.setGeometry(QRect(240, 131, 181, 31))
        self.filter_facture_combo.setStyleSheet(u"border: 2px solid rgb(0, 85, 255);\n"
"border-radius: 10px;")
        self.mainNavigationScreen.addWidget(self.dashboardPage)
        self.clientPage = QWidget()
        self.clientPage.setObjectName(u"clientPage")
        self.label_22 = QLabel(self.clientPage)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 20, 521, 41))
        self.label_22.setFont(font5)
        self.label_22.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: white;\n"
"padding-left: 10px;")
        self.frame_24 = QFrame(self.clientPage)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(10, 80, 201, 101))
        self.frame_24.setStyleSheet(u"#frame_24{\n"
"	border: 2px solid rgb(0, 85, 255);\n"
"	border-radius: 12px;\n"
"}")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_24)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.frame_24)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: rgb(255, 85, 0);")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_9)

        self.reliure_jour = QLabel(self.frame_24)
        self.reliure_jour.setObjectName(u"reliure_jour")
        font9 = QFont()
        font9.setFamilies([u"Yu Gothic Medium"])
        font9.setPointSize(15)
        self.reliure_jour.setFont(font9)
        self.reliure_jour.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.reliure_jour.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.reliure_jour)

        self.livre_jour = QLabel(self.frame_24)
        self.livre_jour.setObjectName(u"livre_jour")
        self.livre_jour.setFont(font1)
        self.livre_jour.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.livre_jour)

        self.frame_25 = QFrame(self.clientPage)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(320, 80, 211, 101))
        self.frame_25.setStyleSheet(u"#frame_25{\n"
"	border: 2px solid rgb(0, 85, 255);\n"
"	border-radius: 12px;\n"
"}")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_25)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_26 = QLabel(self.frame_25)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)
        self.label_26.setStyleSheet(u"color: rgb(255, 85, 0);")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_26)

        self.reliure_mois = QLabel(self.frame_25)
        self.reliure_mois.setObjectName(u"reliure_mois")
        self.reliure_mois.setFont(font9)
        self.reliure_mois.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.reliure_mois.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.reliure_mois)

        self.livre_mois = QLabel(self.frame_25)
        self.livre_mois.setObjectName(u"livre_mois")
        self.livre_mois.setFont(font1)
        self.livre_mois.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.livre_mois)

        self.reliureTableWidget = QTableWidget(self.clientPage)
        if (self.reliureTableWidget.columnCount() < 8):
            self.reliureTableWidget.setColumnCount(8)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.reliureTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.reliureTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.reliureTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.reliureTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.reliureTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.reliureTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.reliureTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.reliureTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        self.reliureTableWidget.setObjectName(u"reliureTableWidget")
        self.reliureTableWidget.setGeometry(QRect(10, 280, 521, 351))
        self.verticalLayoutWidget_2 = QWidget(self.clientPage)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(550, 139, 591, 491))
        self.reliureCourbe = QVBoxLayout(self.verticalLayoutWidget_2)
        self.reliureCourbe.setObjectName(u"reliureCourbe")
        self.reliureCourbe.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.clientPage)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(550, 100, 591, 41))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"border: 1px solid rgb(0, 85, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.reliureDate = QDateEdit(self.clientPage)
        self.reliureDate.setObjectName(u"reliureDate")
        self.reliureDate.setGeometry(QRect(20, 210, 151, 31))
        self.reliureDate.setStyleSheet(u"\n"
"border: 2px solid rgb(0, 85, 255);\n"
"border-radius: 10px;")
        self.reliure_filterCombo = QComboBox(self.clientPage)
        self.reliure_filterCombo.addItem("")
        self.reliure_filterCombo.addItem("")
        self.reliure_filterCombo.addItem("")
        self.reliure_filterCombo.setObjectName(u"reliure_filterCombo")
        self.reliure_filterCombo.setGeometry(QRect(240, 211, 181, 31))
        self.reliure_filterCombo.setStyleSheet(u"background: white;\n"
"border: 2px solid rgb(0, 85, 255);\n"
"border-radius: 10px;")
        self.refreshReliure = QPushButton(self.clientPage)
        self.refreshReliure.setObjectName(u"refreshReliure")
        self.refreshReliure.setGeometry(QRect(440, 250, 75, 24))
        self.refreshReliure.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.refreshReliure.setStyleSheet(u"border-radius: 10px;\n"
"background: white;")
        self.mainNavigationScreen.addWidget(self.clientPage)
        self.client_listPage = QWidget()
        self.client_listPage.setObjectName(u"client_listPage")
        self.label_36 = QLabel(self.client_listPage)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, 10, 521, 41))
        self.label_36.setFont(font5)
        self.label_36.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: white;\n"
"padding-left: 10px;")
        self.client_liste_tableWidget = QTableWidget(self.client_listPage)
        if (self.client_liste_tableWidget.columnCount() < 3):
            self.client_liste_tableWidget.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.client_liste_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.client_liste_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.client_liste_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        self.client_liste_tableWidget.setObjectName(u"client_liste_tableWidget")
        self.client_liste_tableWidget.setGeometry(QRect(10, 70, 521, 411))
        self.mainNavigationScreen.addWidget(self.client_listPage)
        self.barcodePage = QWidget()
        self.barcodePage.setObjectName(u"barcodePage")
        self.generer_code_barre = QPushButton(self.barcodePage)
        self.generer_code_barre.setObjectName(u"generer_code_barre")
        self.generer_code_barre.setGeometry(QRect(440, 80, 271, 41))
        self.generer_code_barre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.generer_code_barre.setStyleSheet(u"border: 2px solid rgb(0, 85, 255);\n"
"border-radius: 10px;")
        self.mainNavigationScreen.addWidget(self.barcodePage)
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.confirmation_form = QFrame(self.settingPage)
        self.confirmation_form.setObjectName(u"confirmation_form")
        self.confirmation_form.setGeometry(QRect(10, 100, 271, 221))
        self.confirmation_form.setFrameShape(QFrame.Shape.StyledPanel)
        self.confirmation_form.setFrameShadow(QFrame.Shadow.Raised)
        self.email_confirmation = QLineEdit(self.confirmation_form)
        self.email_confirmation.setObjectName(u"email_confirmation")
        self.email_confirmation.setGeometry(QRect(10, 30, 241, 31))
        self.code_confirmation = QLineEdit(self.confirmation_form)
        self.code_confirmation.setObjectName(u"code_confirmation")
        self.code_confirmation.setGeometry(QRect(10, 110, 241, 31))
        self.label_25 = QLabel(self.confirmation_form)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 6, 101, 20))
        self.label_25.setFont(font8)
        self.label_28 = QLabel(self.confirmation_form)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 86, 141, 20))
        self.label_28.setFont(font8)
        self.send_code_confirmation = QPushButton(self.confirmation_form)
        self.send_code_confirmation.setObjectName(u"send_code_confirmation")
        self.send_code_confirmation.setGeometry(QRect(10, 170, 241, 31))
        self.send_code_confirmation.setStyleSheet(u"border: 2px solid rgb(0, 85, 255);\n"
"border-radius: 10px;")
        self.change_password_frame = QFrame(self.settingPage)
        self.change_password_frame.setObjectName(u"change_password_frame")
        self.change_password_frame.setGeometry(QRect(10, 100, 271, 221))
        self.change_password_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.change_password_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.new_password = QLineEdit(self.change_password_frame)
        self.new_password.setObjectName(u"new_password")
        self.new_password.setGeometry(QRect(10, 30, 241, 41))
        self.new_password_confirm = QLineEdit(self.change_password_frame)
        self.new_password_confirm.setObjectName(u"new_password_confirm")
        self.new_password_confirm.setGeometry(QRect(10, 110, 241, 41))
        self.submit_new_password = QPushButton(self.change_password_frame)
        self.submit_new_password.setObjectName(u"submit_new_password")
        self.submit_new_password.setGeometry(QRect(10, 170, 241, 31))
        self.submit_new_password.setStyleSheet(u"border: 2px solid rgb(0, 85, 255);\n"
"border-radius: 10px;")
        self.label_29 = QLabel(self.change_password_frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 10, 171, 21))
        self.label_29.setFont(font8)
        self.label_34 = QLabel(self.change_password_frame)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(20, 85, 221, 21))
        self.label_34.setFont(font8)
        self.show_password = QPushButton(self.change_password_frame)
        self.show_password.setObjectName(u"show_password")
        self.show_password.setGeometry(QRect(220, 40, 21, 21))
        self.show_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_password.setStyleSheet(u"border: none;\n"
"background: white;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/visible.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_password.setIcon(icon6)
        self.show_password_confirm = QPushButton(self.change_password_frame)
        self.show_password_confirm.setObjectName(u"show_password_confirm")
        self.show_password_confirm.setGeometry(QRect(220, 120, 21, 21))
        self.show_password_confirm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_password_confirm.setStyleSheet(u"border: none;\n"
"background: white;")
        self.show_password_confirm.setIcon(icon6)
        self.hide_password = QPushButton(self.change_password_frame)
        self.hide_password.setObjectName(u"hide_password")
        self.hide_password.setGeometry(QRect(220, 40, 21, 21))
        self.hide_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hide_password.setStyleSheet(u"border: none;\n"
"background: white;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/invisible.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hide_password.setIcon(icon7)
        self.hide_password_confirm = QPushButton(self.change_password_frame)
        self.hide_password_confirm.setObjectName(u"hide_password_confirm")
        self.hide_password_confirm.setGeometry(QRect(220, 120, 21, 21))
        self.hide_password_confirm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hide_password_confirm.setStyleSheet(u"border: none;\n"
"background: white;")
        self.hide_password_confirm.setIcon(icon7)
        self.hide_password_confirm.raise_()
        self.hide_password.raise_()
        self.new_password.raise_()
        self.new_password_confirm.raise_()
        self.submit_new_password.raise_()
        self.label_29.raise_()
        self.label_34.raise_()
        self.show_password.raise_()
        self.show_password_confirm.raise_()
        self.label_35 = QLabel(self.settingPage)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 30, 481, 41))
        self.label_35.setFont(font5)
        self.label_35.setStyleSheet(u"background: rgb(0, 170, 255);\n"
"padding-left: 10px;\n"
"color: white;")
        self.mainNavigationScreen.addWidget(self.settingPage)

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
        self.widget_14.setStyleSheet(u"#widget_14{\n"
"	background: rgb(0, 85, 255);\n"
"padding-bottom: 10px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_14)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget_14)
        self.label_19.setObjectName(u"label_19")
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(True)
        self.label_19.setFont(font10)
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

        self.logoutBtn = QPushButton(self.widget_14)
        self.logoutBtn.setObjectName(u"logoutBtn")
        self.logoutBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logoutBtn.setStyleSheet(u"border: 2px solid orange;\n"
"border-radius: 10px;\n"
"height: 30px;\n"
"margin-bottom: 5px;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutBtn.setIcon(icon8)
        self.logoutBtn.setIconSize(QSize(18, 18))

        self.verticalLayout_5.addWidget(self.logoutBtn)


        self.verticalLayout_9.addWidget(self.widget_14, 0, Qt.AlignmentFlag.AlignTop)

        self.search_view = QTableWidget(self.profile_container)
        if (self.search_view.columnCount() < 2):
            self.search_view.setColumnCount(2)
        font11 = QFont()
        font11.setPointSize(9)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font11);
        self.search_view.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.search_view.setHorizontalHeaderItem(1, __qtablewidgetitem16)
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
#if QT_CONFIG(whatsthis)
        self.formulaireBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.formulaireBtn.setText("")
#if QT_CONFIG(whatsthis)
        self.dashboardBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.dashboardBtn.setText("")
#if QT_CONFIG(whatsthis)
        self.reliureBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.reliureBtn.setText("")
#if QT_CONFIG(whatsthis)
        self.clientBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.clientBtn.setText("")
#if QT_CONFIG(whatsthis)
        self.barcodeBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.barcodeBtn.setText("")
        self.changePasswordBtn.setText("")
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Evolution des Ventes", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Ventes du jour", None))
        self.vente_jour.setText(QCoreApplication.translate("MainWindow", u"30000 Ar", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"21 Oct 2024", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Ventes du mois", None))
        self.vente_mois.setText(QCoreApplication.translate("MainWindow", u"700000 Ar", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"21 Oct 2024", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Liste des Factures du Jours", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Rafraichir", None))
        ___qtablewidgetitem = self.facture_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Numero Facture", None));
        ___qtablewidgetitem1 = self.facture_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Etat de Payement", None));
        ___qtablewidgetitem2 = self.facture_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date Enregistrement", None));
        ___qtablewidgetitem3 = self.facture_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Identifiant du Client", None));
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Evolution des ventes du mois", None))
        self.filter_facture_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Toutes les Factures", None))
        self.filter_facture_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Factures Payer", None))
        self.filter_facture_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Facture Non Payer", None))

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Commande de Livre", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Commande livrer du Jour", None))
        self.reliure_jour.setText(QCoreApplication.translate("MainWindow", u"100000 Ar", None))
        self.livre_jour.setText(QCoreApplication.translate("MainWindow", u"50 livre", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Commande livrer du mois", None))
        self.reliure_mois.setText(QCoreApplication.translate("MainWindow", u"100000 Ar", None))
        self.livre_mois.setText(QCoreApplication.translate("MainWindow", u"50 livre", None))
        ___qtablewidgetitem4 = self.reliureTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"numero", None));
        ___qtablewidgetitem5 = self.reliureTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Nom du client", None));
        ___qtablewidgetitem6 = self.reliureTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem7 = self.reliureTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Page Noir", None));
        ___qtablewidgetitem8 = self.reliureTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Page Couleur", None));
        ___qtablewidgetitem9 = self.reliureTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Exemplaire", None));
        ___qtablewidgetitem10 = self.reliureTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Total a payer", None));
        ___qtablewidgetitem11 = self.reliureTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Etat Livrer", None));
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Evolutions des Commandes Livrees", None))
        self.reliure_filterCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Toutes les Commandes", None))
        self.reliure_filterCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Commandes Livrees", None))
        self.reliure_filterCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Commandes Non Livrees", None))

        self.refreshReliure.setText(QCoreApplication.translate("MainWindow", u"Rafraichir", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Liste des Clients", None))
        ___qtablewidgetitem12 = self.client_liste_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Nom et Prenom", None));
        ___qtablewidgetitem13 = self.client_liste_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Telephone", None));
        ___qtablewidgetitem14 = self.client_liste_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        self.generer_code_barre.setText(QCoreApplication.translate("MainWindow", u"Generer un Code Barre", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"email admin", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Code de confirmation", None))
        self.send_code_confirmation.setText(QCoreApplication.translate("MainWindow", u"Envoyer le code", None))
        self.submit_new_password.setText(QCoreApplication.translate("MainWindow", u"Valider le nouveau mot de passe", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Nouveau Mot de passe", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Confirmer le nouveau mot de passe", None))
        self.show_password.setText("")
        self.show_password_confirm.setText("")
        self.hide_password.setText("")
        self.hide_password_confirm.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Changer Votre mot de Passe", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_20.setText("")
        self.logoutBtn.setText(QCoreApplication.translate("MainWindow", u"Se deconnecter", None))
        ___qtablewidgetitem15 = self.search_view.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Articles recherher", None));
        ___qtablewidgetitem16 = self.search_view.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"numero", None));
    # retranslateUi

