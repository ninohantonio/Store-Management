# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmation_uiiGiFMJ.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 400)
        Form.setMinimumSize(QSize(400, 400))
        Form.setMaximumSize(QSize(400, 400))
        Form.setBaseSize(QSize(400, 400))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        Form.setFont(font)
        Form.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 10px;\n"
"	border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 85, 255), stop:1 rgb(0, 170, 255));\n"
"	padding: 5px 10px;\n"
"}\n"
"\n"
"#send_mail{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(0, 85, 255);\n"
"	color: white;\n"
"}\n"
"\n"
"#invalid_code{\n"
"	background-color: orange;\n"
"	padding: 5px 7px;\n"
"	border-radius: 5px;\n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 80, 121, 16))
        self.email = QLineEdit(Form)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(70, 100, 251, 31))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 200, 121, 16))
        self.code_field = QLineEdit(Form)
        self.code_field.setObjectName(u"code_field")
        self.code_field.setGeometry(QRect(70, 220, 251, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.code_field.setFont(font1)
        self.send_mail = QPushButton(Form)
        self.send_mail.setObjectName(u"send_mail")
        self.send_mail.setGeometry(QRect(70, 140, 251, 31))
        self.invalid_code = QLabel(Form)
        self.invalid_code.setObjectName(u"invalid_code")
        self.invalid_code.setGeometry(QRect(70, 280, 251, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Confirmation", None))
        self.label.setText(QCoreApplication.translate("Form", u"Email de confirmation", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Code de validation", None))
        self.code_field.setText("")
        self.send_mail.setText(QCoreApplication.translate("Form", u"Envoyer le code", None))
        self.invalid_code.setText(QCoreApplication.translate("Form", u"Code invalide", None))
    # retranslateUi

