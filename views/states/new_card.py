# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_cardKpbrQg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_cardCommande(object):
    def setupUi(self, cardCommande):
        if not cardCommande.objectName():
            cardCommande.setObjectName(u"cardCommande")
        cardCommande.resize(308, 128)
        cardCommande.setStyleSheet(u"#cardCommande{\n"
"	background-color: #fefeff;\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(cardCommande)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(cardCommande)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(100, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftFrame = QFrame(self.widget)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.leftFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.libelle_card = QLabel(self.leftFrame)
        self.libelle_card.setObjectName(u"libelle_card")

        self.verticalLayout.addWidget(self.libelle_card)

        self.price_card = QLabel(self.leftFrame)
        self.price_card.setObjectName(u"price_card")

        self.verticalLayout.addWidget(self.price_card)

        self.total_card = QLabel(self.leftFrame)
        self.total_card.setObjectName(u"total_card")

        self.verticalLayout.addWidget(self.total_card)


        self.horizontalLayout_2.addWidget(self.leftFrame)

        self.rightFrame = QFrame(self.widget)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.rightFrame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.comboBox = QComboBox(self.rightFrame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)


        self.horizontalLayout_2.addWidget(self.rightFrame)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(cardCommande)

        QMetaObject.connectSlotsByName(cardCommande)
    # setupUi

    def retranslateUi(self, cardCommande):
        cardCommande.setWindowTitle(QCoreApplication.translate("cardCommande", u"Form", None))
        self.libelle_card.setText(QCoreApplication.translate("cardCommande", u"nomArticle", None))
        self.price_card.setText(QCoreApplication.translate("cardCommande", u"prix unitaire", None))
        self.total_card.setText(QCoreApplication.translate("cardCommande", u"sous Total: 100000Ar", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("cardCommande", u"quantite", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("cardCommande", u"paquets", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("cardCommande", u"pieces", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("cardCommande", u"boites", None))

    # retranslateUi

