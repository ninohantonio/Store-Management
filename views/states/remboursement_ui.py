# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remboursement_dialogjzYUBZ.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(792, 676)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(243, 243, 243);\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 411, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: white;\n"
"padding-left: 10px;")
        self.numero_facture = QLabel(Dialog)
        self.numero_facture.setObjectName(u"numero_facture")
        self.numero_facture.setGeometry(QRect(470, 15, 291, 31))
        font1 = QFont()
        font1.setPointSize(15)
        self.numero_facture.setFont(font1)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 241, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_2.setFont(font2)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 130, 751, 441))
        self.card_container = QGridLayout(self.gridLayoutWidget)
        self.card_container.setObjectName(u"card_container")
        self.card_container.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 615, 121, 31))
        self.label_3.setFont(font2)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 610, 161, 41))
        font3 = QFont()
        font3.setPointSize(17)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 85, 0)")
        self.submit = QPushButton(Dialog)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(550, 610, 211, 41))
        font4 = QFont()
        font4.setPointSize(11)
        self.submit.setFont(font4)
        self.submit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.submit.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border: none;\n"
"border-radius: 10px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Remboursement", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Effectuer un Remboursement sur la Facture :", None))
        self.numero_facture.setText(QCoreApplication.translate("Dialog", u"000000001", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Liste des commandes :", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Total \u00e0 payer :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"0 Ar", None))
        self.submit.setText(QCoreApplication.translate("Dialog", u"Enregistrer les modifications", None))
    # retranslateUi

