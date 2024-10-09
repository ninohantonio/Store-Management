# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_list_dialogARAsCx.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHeaderView, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_liste_client(object):
    def setupUi(self, liste_client):
        if not liste_client.objectName():
            liste_client.setObjectName(u"liste_client")
        liste_client.resize(405, 525)
        liste_client.setStyleSheet(u"#search_client{\n"
"	border: 2px solid rgb(0, 85, 255);\n"
"	border-radius: 15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"#pushButton{\n"
"	background-color: rgb(183, 214, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton_2{\n"
"	background-color: rgb(250, 255, 226);\n"
"	border-radius: 10px;\n"
"}")
        self.buttonBox = QDialogButtonBox(liste_client)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(310, 20, 81, 51))
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.tableWidget = QTableWidget(liste_client)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 80, 381, 381))
        self.search_client = QLineEdit(liste_client)
        self.search_client.setObjectName(u"search_client")
        self.search_client.setGeometry(QRect(10, 20, 261, 41))
        self.pushButton = QPushButton(liste_client)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 480, 151, 31))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2 = QPushButton(liste_client)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 480, 151, 31))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.retranslateUi(liste_client)
        self.buttonBox.accepted.connect(liste_client.accept)
        self.buttonBox.rejected.connect(liste_client.reject)

        QMetaObject.connectSlotsByName(liste_client)
    # setupUi

    def retranslateUi(self, liste_client):
        liste_client.setWindowTitle(QCoreApplication.translate("liste_client", u"Dialog", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("liste_client", u"Nom et prenom", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("liste_client", u"Contact", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("liste_client", u"numero", None));
        self.search_client.setPlaceholderText(QCoreApplication.translate("liste_client", u"rechercher un client ...", None))
        self.pushButton.setText(QCoreApplication.translate("liste_client", u"Nouveau Client", None))
        self.pushButton_2.setText(QCoreApplication.translate("liste_client", u"Client temporaire >>", None))
    # retranslateUi

