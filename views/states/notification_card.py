from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from models.model_class import Notification


class NotificationCard(QWidget):
    def __init__(self, notification: Notification):
        super(NotificationCard, self).__init__()

        self.horizontalLayout = QVBoxLayout(self)
        # self.horizontalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 150))
        self.widget.setMaximumSize(QSize(300, 150))
        self.widget.setStyleSheet(u"""
                            #widget{
                                background-color: #fefeff;
                                border-radius: 10px;
                                border: 2px solid #f56614;
                            }
                        """)

