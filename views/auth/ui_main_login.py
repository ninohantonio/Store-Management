# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_loginJyUqXD.ui'
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
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1312, 669)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame, QWidget{\n"
"	\n"
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
"\n"
"#formulaire1{\n"
"	background: rgb(146, 200, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#submitBtn{\n"
"	color: rgb(16, 120, 23);\n"
"	border-radius: 10px;\n"
"	background-color: rgba(206, 203, 220, 0.7);\n"
"	border: 1px solid rgb(16, 120, 23);\n"
"}\n"
"\n"
"#resetBtn{\n"
"	color: rgb(255, 58, 23);\n"
"	border-radius: 10px;\n"
"	background-color: rgba(206, 203, 220, 0.7);\n"
"	border: 1px solid rgb(255, 58, 23);\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_menu = QWidget(self.widget)
        self.left_menu.setObjectName(u"left_menu")
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon = QIcon()
        icon.addFile(u":/icons/icons/caddie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.pushButton_4)


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
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formulaire1 = QWidget(self.widget_5)
        self.formulaire1.setObjectName(u"formulaire1")
        self.frame_4 = QFrame(self.formulaire1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 90, 541, 361))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
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
        self.label_3.setGeometry(QRect(20, 16, 91, 20))
        self.lineEdit_2 = QLineEdit(self.frame_10)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(0, 40, 211, 31))

        self.verticalLayout_6.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 81, 16))
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
        self.label_2.setGeometry(QRect(10, 20, 151, 18))
        self.lineEdit = QLineEdit(self.frame_8)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 40, 211, 31))

        self.verticalLayout_6.addWidget(self.frame_8)


        self.horizontalLayout_5.addWidget(self.frame_5)

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
        self.label_5.setGeometry(QRect(20, 16, 91, 20))
        self.lineEdit_3 = QLineEdit(self.frame_11)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 40, 201, 31))

        self.verticalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 16, 151, 20))
        self.lineEdit_5 = QLineEdit(self.frame_12)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(20, 40, 201, 31))

        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame_13)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 20, 191, 18))
        self.lineEdit_4 = QLineEdit(self.frame_13)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 40, 201, 31))

        self.verticalLayout_7.addWidget(self.frame_13)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.formulaire1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(30, 460, 511, 81))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.descriptionEdit = QTextEdit(self.frame_7)
        self.descriptionEdit.setObjectName(u"descriptionEdit")

        self.verticalLayout_4.addWidget(self.descriptionEdit)

        self.search_ajout = QLineEdit(self.formulaire1)
        self.search_ajout.setObjectName(u"search_ajout")
        self.search_ajout.setGeometry(QRect(170, 20, 221, 31))
        self.label_8 = QLabel(self.formulaire1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(170, 20, 31, 31))
        self.label_8.setPixmap(QPixmap(u":/icons/icons/search.png"))
        self.label_8.setScaledContents(True)
        self.submitBtn = QPushButton(self.formulaire1)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(40, 560, 241, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.submitBtn.setFont(font)
        self.resetBtn = QPushButton(self.formulaire1)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setGeometry(QRect(320, 560, 211, 41))
        self.resetBtn.setFont(font)

        self.horizontalLayout_2.addWidget(self.formulaire1)

        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")

        self.horizontalLayout_2.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget_5)


        self.horizontalLayout_3.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Libelle", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom de l'article", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Conteneur", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Packet", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Boite", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre dans un conteneur", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre de piece par conteneur", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Prix unitaire", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prix unitaire en Ariary", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nombre de conteneur", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Conteneur a ajouter", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nombre de piece supplementaire", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Piece supplementaire a ajouter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.descriptionEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description de l'article", None))
        self.search_ajout.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Scanner un article", None))
        self.label_8.setText("")
        self.submitBtn.setText(QCoreApplication.translate("MainWindow", u"Enregistrer modification", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"Vider les champs", None))
    # retranslateUi

