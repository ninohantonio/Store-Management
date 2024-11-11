from PySide6.QtWidgets import QDialog

from models.model_class import Facture
from services.article_service import get_article_by_id
from views.states.commande_card import CardCommande
from views.states.remboursement_card import RemboursementCard
from views.states.remboursement_ui import Ui_Dialog


class RemboursementDialog(QDialog):
    def __init__(self, facture: Facture):
        super(RemboursementDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.facture = facture
        self.total_a_payer = 0

        self.load_card_container()


    def load_card_container(self):
        liste_article = self.facture.listeArticle

        for item in liste_article:
            data = item.split(':')
            self.total_a_payer += int(data[2])
            article = get_article_by_id(data[0])

            element = len(liste_article)
            index_quantite = 0 if data[3] == "pieces" else 1
            carte = RemboursementCard(article, numero_article=article.numeroArticle, parent=self, quantite=data[4], type_index=index_quantite, sous_total=data[2])
            carte.sous_total_changed.connect(self.update_total_payer)
            carte.card_removed.connect(self.remove_card)

            self.ui.card_container.addWidget(carte, (element - 1) // 3, (element - 1) % 3)

        self.ui.total_payer.setText(f"{self.total_a_payer} Ar")

    def remove_card(self, numero_article, sous_total):
        if numero_article in self.commande_item:
            del self.commande_item[numero_article]
            self.update_total_payer(0, sous_total * -1)

    def update_total_payer(self, ancien: int, sous_total: int):
        self.total_a_payer = self.total_a_payer + sous_total - ancien
        self.ui.total_payer.setText(f"{self.total_a_payer} Ar")