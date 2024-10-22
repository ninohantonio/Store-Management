# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'type_livrePQIMCk.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(474, 457)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid black;\n"
"	border-radius: 15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"#submit_type{\n"
"	border: 2px solid rgb(0, 85, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#reset_type{\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"border-radius: 10px;\n"
"}")
        self.description = QLineEdit(Dialog)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(60, 80, 171, 31))
        self.prix_noir = QLineEdit(Dialog)
        self.prix_noir.setObjectName(u"prix_noir")
        self.prix_noir.setGeometry(QRect(60, 180, 171, 31))
        self.prix_couleur = QLineEdit(Dialog)
        self.prix_couleur.setObjectName(u"prix_couleur")
        self.prix_couleur.setGeometry(QRect(270, 180, 131, 31))
        self.prix_reliure = QLineEdit(Dialog)
        self.prix_reliure.setObjectName(u"prix_reliure")
        self.prix_reliure.setGeometry(QRect(270, 80, 131, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 60, 121, 20))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 160, 181, 20))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 160, 171, 21))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 60, 211, 20))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 10, 371, 20))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.submit_type = QPushButton(Dialog)
        self.submit_type.setObjectName(u"submit_type")
        self.submit_type.setGeometry(QRect(60, 360, 141, 31))
        self.submit_type.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reset_type = QPushButton(Dialog)
        self.reset_type.setObjectName(u"reset_type")
        self.reset_type.setGeometry(QRect(260, 360, 141, 31))
        self.reset_type.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(70, 260, 331, 41))
        self.comboBox.setStyleSheet(u"background: white;\n"
"border: 2px solid rgb(0, 85, 255);\n"
"bo")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Type de livre", None))
        self.description.setPlaceholderText(QCoreApplication.translate("Dialog", u"ex : Livre d'Or", None))
        self.prix_noir.setPlaceholderText(QCoreApplication.translate("Dialog", u"ex : 100", None))
        self.prix_couleur.setPlaceholderText(QCoreApplication.translate("Dialog", u"ex : 200", None))
        self.prix_reliure.setPlaceholderText(QCoreApplication.translate("Dialog", u"ex : 15000", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Description :", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Prix d'une Page Noir et Blanc :", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Prix d'une Page en Couleur :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Prix du Reliure", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Ajouter un nouveau type de livre ", None))
        self.submit_type.setText(QCoreApplication.translate("Dialog", u"Ajouter le type", None))
        self.reset_type.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
    # retranslateUi

