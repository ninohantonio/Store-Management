from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from models.model_class import Notification


class NotificationCard(QWidget):
    def __init__(self, notification: Notification):
        super(NotificationCard, self).__init__()

        self.horizontalLayout = QVBoxLayout(self)
        # self.horizontalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(500, 90))
        self.widget.setMaximumSize(QSize(500, 90))
        self.widget.setStyleSheet(u"""
                            #widget{
                                background-color: #fefeff;
                                border-radius: 10px;
                                border: 2px solid #f56614;
                            }
                        """)

        # Créer les labels pour afficher les détails de la notification
        self.titre_label = QLabel(notification.titre, self)
        self.date_label = QLabel(str(notification.dateEmmission), self)  # Format de la date
        self.contenu_label = QLabel(notification.contenu, self)

        # Appliquer un style aux labels
        self.titre_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #333;")
        self.date_label.setStyleSheet("font-size: 12px; color: #999;")
        self.contenu_label.setStyleSheet("font-size: 14px; color: #555;")

        # Ajouter les labels au layout de la carte
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.titre_label)
        layout.addWidget(self.date_label)
        layout.addWidget(self.contenu_label)

        # Ajouter le widget de notification au layout principal
        self.horizontalLayout.addWidget(self.widget)
        self.setLayout(self.horizontalLayout)

