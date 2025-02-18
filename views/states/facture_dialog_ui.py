# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'facture_dialogwSvNVZ.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
import views.resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(730, 922)
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
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 180, 721, 461))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(550, 350))
        self.tableWidget.setMaximumSize(QSize(720, 500))
        self.tableWidget.setBaseSize(QSize(720, 500))
        font1 = QFont()
        font1.setPointSize(11)
        self.tableWidget.setFont(font1)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)

        self.horizontalLayout.addWidget(self.tableWidget)

        self.change_state_btn = QPushButton(Dialog)
        self.change_state_btn.setObjectName(u"change_state_btn")
        self.change_state_btn.setGeometry(QRect(260, 140, 91, 31))
        self.change_state_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.print_btn = QPushButton(Dialog)
        self.print_btn.setObjectName(u"print_btn")
        self.print_btn.setGeometry(QRect(670, 10, 51, 41))
        self.print_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.print_btn.setStyleSheet(u"border: 2px solid rgb(0, 85, 255);\n"
"border-radius: 10px;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/printer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.print_btn.setIcon(icon)
        self.print_btn.setIconSize(QSize(30, 30))
        self.footer_frame = QFrame(Dialog)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setGeometry(QRect(10, 640, 720, 275))
        self.footer_frame.setMinimumSize(QSize(720, 275))
        self.footer_frame.setMaximumSize(QSize(720, 275))
        self.footer_frame.setBaseSize(QSize(720, 275))
        self.footer_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_8 = QLabel(self.footer_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(530, 120, 111, 16))
        self.label_8.setFont(font1)
        self.reste_payer = QLabel(self.footer_frame)
        self.reste_payer.setObjectName(u"reste_payer")
        self.reste_payer.setGeometry(QRect(600, 20, 131, 21))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.reste_payer.setFont(font2)
        self.label_5 = QLabel(self.footer_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(450, 20, 141, 21))
        self.label_5.setFont(font)
        self.label_11 = QLabel(self.footer_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 20, 61, 21))
        self.label_11.setFont(font)
        self.avance = QLabel(self.footer_frame)
        self.avance.setObjectName(u"avance")
        self.avance.setGeometry(QRect(310, 20, 131, 21))
        self.avance.setFont(font2)
        self.total = QLabel(self.footer_frame)
        self.total.setObjectName(u"total")
        self.total.setGeometry(QRect(80, 20, 131, 21))
        self.total.setFont(font2)
        self.label_10 = QLabel(self.footer_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(250, 20, 61, 21))
        self.label_10.setFont(font)
        self.label_17 = QLabel(self.footer_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 65, 311, 21))
        self.label_17.setFont(font1)
        self.total_lettre = QLabel(self.footer_frame)
        self.total_lettre.setObjectName(u"total_lettre")
        self.total_lettre.setGeometry(QRect(10, 90, 691, 31))
        font3 = QFont()
        font3.setPointSize(13)
        self.total_lettre.setFont(font3)
        self.total_lettre.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_18 = QLabel(self.footer_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(90, 130, 101, 16))
        font4 = QFont()
        font4.setPointSize(12)
        self.label_18.setFont(font4)
        self.header_frame = QFrame(Dialog)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setGeometry(QRect(10, -1, 720, 180))
        self.header_frame.setMinimumSize(QSize(720, 180))
        self.header_frame.setMaximumSize(QSize(720, 180))
        self.header_frame.setBaseSize(QSize(720, 180))
        self.header_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.statut_facture = QLabel(self.header_frame)
        self.statut_facture.setObjectName(u"statut_facture")
        self.statut_facture.setGeometry(QRect(490, 145, 121, 21))
        self.statut_facture.setFont(font1)
        self.label_16 = QLabel(self.header_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 150, 221, 31))
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_facture = QLabel(self.header_frame)
        self.date_facture.setObjectName(u"date_facture")
        self.date_facture.setGeometry(QRect(510, 120, 171, 21))
        self.date_facture.setFont(font1)
        self.label = QLabel(self.header_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 100, 121, 16))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setUnderline(True)
        self.label.setFont(font5)
        self.label_2 = QLabel(self.header_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, -30, 161, 151))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.label_2.setFont(font6)
        self.label_2.setPixmap(QPixmap(u":/icons/icons/LOGO IRINA SERVICE-02.jpg"))
        self.label_2.setScaledContents(True)
        self.label_14 = QLabel(self.header_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 120, 211, 20))
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.numero_facture = QLabel(self.header_frame)
        self.numero_facture.setObjectName(u"numero_facture")
        self.numero_facture.setGeometry(QRect(500, 100, 191, 21))
        self.numero_facture.setFont(font1)
        self.label_3 = QLabel(self.header_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 124, 151, 16))
        self.label_3.setFont(font5)
        self.label_4 = QLabel(self.header_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 150, 141, 16))
        self.label_4.setFont(font5)
        self.label_13 = QLabel(self.header_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 100, 211, 16))
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_12 = QLabel(self.header_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 80, 211, 16))
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15 = QLabel(self.header_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 140, 211, 16))
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.client_frame = QFrame(self.header_frame)
        self.client_frame.setObjectName(u"client_frame")
        self.client_frame.setGeometry(QRect(340, 0, 311, 91))
        self.client_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.client_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.client_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 101, 16))
        self.label_6.setFont(font)
        self.nom_client = QLabel(self.client_frame)
        self.nom_client.setObjectName(u"nom_client")
        self.nom_client.setGeometry(QRect(110, 10, 221, 16))
        self.nom_client.setFont(font)
        self.label_7 = QLabel(self.client_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 40, 81, 16))
        self.label_7.setFont(font)
        self.numero_client = QLabel(self.client_frame)
        self.numero_client.setObjectName(u"numero_client")
        self.numero_client.setGeometry(QRect(110, 40, 211, 16))
        self.numero_client.setFont(font)
        self.label_9 = QLabel(self.client_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 70, 71, 16))
        self.label_9.setFont(font)
        self.adresse_client = QLabel(self.client_frame)
        self.adresse_client.setObjectName(u"adresse_client")
        self.adresse_client.setGeometry(QRect(110, 70, 221, 16))
        self.adresse_client.setFont(font)
        self.label_2.raise_()
        self.statut_facture.raise_()
        self.label_16.raise_()
        self.date_facture.raise_()
        self.label.raise_()
        self.label_14.raise_()
        self.numero_facture.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_13.raise_()
        self.label_12.raise_()
        self.label_15.raise_()
        self.client_frame.raise_()
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(670, 60, 51, 41))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border: 2px solid rgb(0, 85, 255);\n"
"border-radius: 10px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/topdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(25, 25))
        self.modify_btn = QPushButton(Dialog)
        self.modify_btn.setObjectName(u"modify_btn")
        self.modify_btn.setGeometry(QRect(670, 110, 51, 41))
        self.modify_btn.setStyleSheet(u"border: 2px solid rgb(0, 85, 255);\n"
"border-radius: 10px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modify_btn.setIcon(icon2)
        self.modify_btn.setIconSize(QSize(30, 30))
        self.frame.raise_()
        self.footer_frame.raise_()
        self.header_frame.raise_()
        self.change_state_btn.raise_()
        self.print_btn.raise_()
        self.pushButton.raise_()
        self.modify_btn.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Facture", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Designation", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Quantite", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Conteneur", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Montant", None));
        self.change_state_btn.setText(QCoreApplication.translate("Dialog", u"changer", None))
        self.print_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Le Responsable", None))
        self.reste_payer.setText(QCoreApplication.translate("Dialog", u"0 Ar", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Reste a payer :", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Total :", None))
        self.avance.setText(QCoreApplication.translate("Dialog", u"0 Ar", None))
        self.total.setText(QCoreApplication.translate("Dialog", u"0 Ar", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Avance :", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"La presente facture est arretee a la somme de :", None))
        self.total_lettre.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Le Client", None))
        self.statut_facture.setText(QCoreApplication.translate("Dialog", u"payement_facture", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"thommyjohnson14@gmail.com", None))
        self.date_facture.setText(QCoreApplication.translate("Dialog", u"date", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Facture numero : ", None))
        self.label_2.setText("")
        self.label_14.setText(QCoreApplication.translate("Dialog", u"NIF : 4001940730", None))
        self.numero_facture.setText(QCoreApplication.translate("Dialog", u"numero_facture", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Date de Commande :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Etat de payement :", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"STAT : 82193 21 2015 0 00381", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Andrainjato Fianarantsoa 301", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Tel : 034 79 800 86", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Client : M(me). ", None))
        self.nom_client.setText(QCoreApplication.translate("Dialog", u"nom_client", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Telephone :", None))
        self.numero_client.setText(QCoreApplication.translate("Dialog", u"1234567890", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Adresse :", None))
        self.adresse_client.setText(QCoreApplication.translate("Dialog", u"adresse", None))
        self.pushButton.setText("")
        self.modify_btn.setText("")
    # retranslateUi

