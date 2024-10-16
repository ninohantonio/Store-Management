from PySide6.QtWidgets import QDialog, QWidget, QVBoxLayout

from services.article_service import get_all_article
from views.states.article_rapide_card import ArticleRapideCard
from views.ui_article_rapide_dialog import Ui_Dialog


class ArticleRapideDialog(QDialog):
    def __init__(self):
        super(ArticleRapideDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.container = QWidget()
        self.layout = QVBoxLayout(self.container)

        self.load_article_list()

    def load_article_list(self):
        articles = get_all_article()

        for article in articles:
            card = ArticleRapideCard(article)
            self.layout.addWidget(card)

        self.ui.scrollArea.setWidget(self.container)