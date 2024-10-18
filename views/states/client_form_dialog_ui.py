# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_form_dialogViBvCw.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(429, 454)
        Dialog.setStyleSheet(u"*{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-radius: 10px;	\n"
"	border: 2px solid rgb(0, 85, 255);\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#submit_client{\n"
"	border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"#reset_client{\n"
"	border: 2px solid orange;\n"
"}\n"
"\n"
"#label_4{\n"
"	background-color: rgb(0, 170, 255);\n"
"	color: white;\n"
"}")
        self.nom_client = QLineEdit(Dialog)
        self.nom_client.setObjectName(u"nom_client")
        self.nom_client.setGeometry(QRect(100, 110, 231, 31))
        self.telephone_client = QLineEdit(Dialog)
        self.telephone_client.setObjectName(u"telephone_client")
        self.telephone_client.setGeometry(QRect(100, 190, 231, 31))
        self.adresse_client = QLineEdit(Dialog)
        self.adresse_client.setObjectName(u"adresse_client")
        self.adresse_client.setGeometry(QRect(100, 270, 231, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 90, 91, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 170, 61, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 250, 81, 16))
        self.submit_client = QPushButton(Dialog)
        self.submit_client.setObjectName(u"submit_client")
        self.submit_client.setGeometry(QRect(100, 350, 111, 31))
        self.submit_client.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reset_client = QPushButton(Dialog)
        self.reset_client.setObjectName(u"reset_client")
        self.reset_client.setGeometry(QRect(230, 350, 101, 31))
        self.reset_client.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 391, 31))
        font = QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Ajout de client", None))
        self.nom_client.setPlaceholderText(QCoreApplication.translate("Dialog", u"ex : Rakoto kely", None))
        self.telephone_client.setPlaceholderText(QCoreApplication.translate("Dialog", u"ex : 0341234567", None))
        self.adresse_client.setPlaceholderText(QCoreApplication.translate("Dialog", u"ex : 123 VR Antanana", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nom et prenom", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Telephone", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Adresse", None))
        self.submit_client.setText(QCoreApplication.translate("Dialog", u"Ajouter", None))
        self.reset_client.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Ajouter votre nouveau client", None))
    # retranslateUi

