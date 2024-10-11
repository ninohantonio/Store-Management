# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'facture_dialogEBZfSz.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(737, 705)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: white;\n"
"}\n"
"\n"
"#client_frame{\n"
"	border: 2px solid rgb(0, 85, 255);\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"#title_list{\n"
"	background-color:  rgb(85, 170, 255);\n"
"	color: white;\n"
"	padding-left: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#reste_payer{\n"
"	color:  rgb(255, 85, 0);\n"
"}\n"
"\n"
"#avance{\n"
"	color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"#change_state_btn{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 10px;\n"
"	cursor: pointer;\n"
"	color: white;\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 121, 16))
        font = QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 161, 16))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.numero_facture = QLabel(Dialog)
        self.numero_facture.setObjectName(u"numero_facture")
        self.numero_facture.setGeometry(QRect(180, 40, 171, 16))
        font2 = QFont()
        font2.setPointSize(10)
        self.numero_facture.setFont(font2)
        self.date_facture = QLabel(Dialog)
        self.date_facture.setObjectName(u"date_facture")
        self.date_facture.setGeometry(QRect(180, 70, 171, 16))
        self.date_facture.setFont(font2)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 151, 16))
        self.label_3.setFont(font)
        self.statut_facture = QLabel(Dialog)
        self.statut_facture.setObjectName(u"statut_facture")
        self.statut_facture.setGeometry(QRect(160, 100, 111, 16))
        self.statut_facture.setFont(font2)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 141, 16))
        self.label_4.setFont(font)
        self.title_list = QLabel(Dialog)
        self.title_list.setObjectName(u"title_list")
        self.title_list.setGeometry(QRect(10, 140, 721, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.title_list.setFont(font3)
        self.client_frame = QFrame(Dialog)
        self.client_frame.setObjectName(u"client_frame")
        self.client_frame.setGeometry(QRect(390, 20, 341, 111))
        self.client_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.client_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.client_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 20, 101, 16))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        self.label_6.setFont(font4)
        self.nom_client = QLabel(self.client_frame)
        self.nom_client.setObjectName(u"nom_client")
        self.nom_client.setGeometry(QRect(110, 20, 221, 16))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(10)
        self.nom_client.setFont(font5)
        self.label_7 = QLabel(self.client_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 50, 81, 16))
        self.label_7.setFont(font4)
        self.numero_client = QLabel(self.client_frame)
        self.numero_client.setObjectName(u"numero_client")
        self.numero_client.setGeometry(QRect(110, 50, 211, 16))
        self.numero_client.setFont(font5)
        self.label_9 = QLabel(self.client_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 80, 71, 16))
        self.label_9.setFont(font4)
        self.adresse_client = QLabel(self.client_frame)
        self.adresse_client.setObjectName(u"adresse_client")
        self.adresse_client.setGeometry(QRect(110, 80, 221, 16))
        self.adresse_client.setFont(font5)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 180, 721, 451))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(701, 16777215))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)

        self.horizontalLayout.addWidget(self.tableWidget)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(490, 660, 101, 21))
        self.label_5.setFont(font4)
        self.reste_payer = QLabel(Dialog)
        self.reste_payer.setObjectName(u"reste_payer")
        self.reste_payer.setGeometry(QRect(600, 660, 131, 21))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(15)
        font6.setBold(True)
        self.reste_payer.setFont(font6)
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(280, 660, 61, 21))
        self.label_10.setFont(font4)
        self.avance = QLabel(Dialog)
        self.avance.setObjectName(u"avance")
        self.avance.setGeometry(QRect(340, 660, 131, 21))
        self.avance.setFont(font6)
        self.total = QLabel(Dialog)
        self.total.setObjectName(u"total")
        self.total.setGeometry(QRect(80, 660, 131, 21))
        self.total.setFont(font6)
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 660, 61, 21))
        self.label_11.setFont(font4)
        self.change_state_btn = QPushButton(Dialog)
        self.change_state_btn.setObjectName(u"change_state_btn")
        self.change_state_btn.setGeometry(QRect(280, 90, 91, 31))
        self.change_state_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Facture", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Facture numero : ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"IrinaService", None))
        self.numero_facture.setText(QCoreApplication.translate("Dialog", u"numero_facture", None))
        self.date_facture.setText(QCoreApplication.translate("Dialog", u"date", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Date de Commande :", None))
        self.statut_facture.setText(QCoreApplication.translate("Dialog", u"payement_facture", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Etat de payement :", None))
        self.title_list.setText(QCoreApplication.translate("Dialog", u"Liste des commandes", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Client : M(me). ", None))
        self.nom_client.setText(QCoreApplication.translate("Dialog", u"nom_client", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Telephone :", None))
        self.numero_client.setText(QCoreApplication.translate("Dialog", u"1234567890", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Adresse :", None))
        self.adresse_client.setText(QCoreApplication.translate("Dialog", u"adresse", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Libelle", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Quantite", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Conteneur", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Sous-total", None));
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Reste a payer :", None))
        self.reste_payer.setText(QCoreApplication.translate("Dialog", u"0 Ar", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Avance :", None))
        self.avance.setText(QCoreApplication.translate("Dialog", u"0 Ar", None))
        self.total.setText(QCoreApplication.translate("Dialog", u"0 Ar", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Total :", None))
        self.change_state_btn.setText(QCoreApplication.translate("Dialog", u"changer", None))
    # retranslateUi

