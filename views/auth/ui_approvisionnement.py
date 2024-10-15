# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'approvisionnementFQYngS.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(426, 324)
        Dialog.setStyleSheet(u"#Dialog{\n"
"	background-color: white;\n"
"}\n"
"\n"
"#submit{\n"
"	background-color: rgb(0, 85, 255);\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#cancel{\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	border: 2px solid orange;\n"
"	border-radius: 5px;\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 291, 16))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        self.label.setFont(font)
        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(50, 80, 89, 21))
        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(180, 80, 89, 21))
        self.radioButton_3 = QRadioButton(Dialog)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(300, 80, 89, 21))
        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(170, 140, 81, 21))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 140, 49, 16))
        self.submit = QPushButton(Dialog)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(90, 240, 111, 31))
        self.submit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(230, 240, 111, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Approvisionnement", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Choisissez les options d'approvisionnement", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Paquet", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Boite", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Piece", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Seuil :", None))
        self.submit.setText(QCoreApplication.translate("Dialog", u"Enregistrer", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
    # retranslateUi

