# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth_uiOtnbCM.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import views.resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(987, 596)
        Form.setStyleSheet(u"#pushButton{\n"
"	background-color: #fff;\n"
"	border: none;\n"
"}\n"
"\n"
"#right{\n"
"	\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 85, 255), stop:1 rgb(0, 170, 255))\n"
"}\n"
"\n"
"#label{\n"
"	color: #fefeff;\n"
"}\n"
"\n"
"#password, #email{\n"
"	border-radius: 6px;\n"
"	padding: 5px 10px;\n"
"}\n"
"\n"
"#login_btn{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(0, 85, 255);\n"
"	color: #fefeff;\n"
"}\n"
"\n"
"#signin_label{\n"
"	font-weight: bold;\n"
"	padding-left: 23px;\n"
"}\n"
"\n"
"#irina_label{\n"
"	color: rgb(0, 85, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left = QFrame(Form)
        self.left.setObjectName(u"left")
        self.left.setFrameShape(QFrame.Shape.StyledPanel)
        self.left.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.left)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.left)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.irina_label = QLabel(self.frame_3)
        self.irina_label.setObjectName(u"irina_label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(True)
        self.irina_label.setFont(font)
        self.irina_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.irina_label)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_4 = QFrame(self.left)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.signin_label = QLabel(self.frame_5)
        self.signin_label.setObjectName(u"signin_label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(17)
        font1.setBold(True)
        self.signin_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.signin_label)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.email_label = QLabel(self.frame_6)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setGeometry(QRect(40, 80, 49, 16))
        font2 = QFont()
        font2.setPointSize(10)
        self.email_label.setFont(font2)
        self.email = QLineEdit(self.frame_6)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(40, 100, 291, 41))
        self.email.setFont(font2)
        self.password = QLineEdit(self.frame_6)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(40, 180, 291, 41))
        self.password.setFont(font2)
        self.password_label = QLabel(self.frame_6)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(40, 160, 121, 16))
        self.password_label.setFont(font2)
        self.forgot = QLabel(self.frame_6)
        self.forgot.setObjectName(u"forgot")
        self.forgot.setGeometry(QRect(40, 240, 191, 16))
        self.forgot.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_btn = QPushButton(self.frame_6)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(40, 280, 291, 41))
        self.login_btn.setFont(font2)

        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.left)

        self.right = QFrame(Form)
        self.right.setObjectName(u"right")
        self.right.setFrameShape(QFrame.Shape.StyledPanel)
        self.right.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.right)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 70, 331, 281))
        icon = QIcon()
        icon.addFile(u":/images/LOGO IRINA SERVICE.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(300, 300))
        self.label = QLabel(self.right)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 390, 191, 16))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        self.label.setFont(font3)

        self.horizontalLayout.addWidget(self.right)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.irina_label.setText(QCoreApplication.translate("Form", u"Irina Service", None))
        self.signin_label.setText(QCoreApplication.translate("Form", u"Se Connecter", None))
        self.email_label.setText(QCoreApplication.translate("Form", u"Email", None))
        self.email.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"Mot de passe", None))
        self.password_label.setText(QCoreApplication.translate("Form", u"Mot de passe", None))
        self.forgot.setText(QCoreApplication.translate("Form", u"Mot de passe oublie ?", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"Se connecter", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<< La qualite avant tous >>", None))
    # retranslateUi

