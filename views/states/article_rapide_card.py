from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QHBoxLayout

from models.model_class import Article


class ArticleRapideCard(QWidget):
    def __init__(self, article: Article):
        super(ArticleRapideCard, self).__init__()

        self.numeroArticle = article.numeroArticle
        self.is_checked = False

        self.horizontalLayout = QVBoxLayout(self)
        # self.horizontalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(500, 60))
        self.widget.setMaximumSize(QSize(500, 60))
        self.widget.setStyleSheet(u"""
                                    #widget{
                                        background-color: #fefeff;
                                        border-radius: 10px;
                                        border: 2px solid #0055ff;
                                    }
                                """)
        # Créer les labels pour afficher les détails de la notification
        self.titre_label = QLabel(article.libelle, self)
        self.description_label = QLabel(str(article.description), self)  # Format de la date
        self.check_box = QCheckBox(self)


        # Appliquer un style aux labels
        self.titre_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #333;")
        self.description_label.setStyleSheet("font-size: 12px; color: #999;")

        # Ajouter les labels au layout de la carte
        layout = QHBoxLayout(self.widget)
        layout.addWidget(self.titre_label)
        layout.addWidget(self.description_label)
        layout.addWidget(self.check_box)

        # Ajouter le widget de notification au layout principal
        self.horizontalLayout.addWidget(self.widget)
        self.setLayout(self.horizontalLayout)

        self.check_box.clicked.connect(self.manage_check_box)

    def manage_check_box(self):
        self.is_checked = not self.is_checked


