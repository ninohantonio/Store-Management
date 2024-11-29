from PySide6.QtWidgets import QDialog, QMessageBox

import services.article_service
import services.journal_service
from controllers.commande_controller import get_date_time_to_string
from models.model_class import Facture, Journal
from services.article_service import get_article_by_id
from services.facture_service import session
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

        self.ui.numero_facture.setText(self.facture.numeroFacture)
        self.ui.submit.clicked.connect(self.handle_submit_modification)

        self.load_card_container()


    def load_card_container(self):
        liste_article = self.facture.listeArticle

        for item in liste_article:
            data = item.split(':')
            self.total_a_payer += int(data[2])
            article = get_article_by_id(data[0])

            element = liste_article.index(item) + 1
            index_quantite = 0 if data[3] == "pieces" else 1
            carte = RemboursementCard(article, numero_article=article.numeroArticle, parent=self, quantite=int(data[4]), type_index=index_quantite, sous_total=int(data[2]))
            carte.sous_total_changed.connect(self.update_total_payer)
            carte.card_removed.connect(self.remove_card)

            self.ui.card_container.addWidget(carte, (element - 1) // 3, (element - 1) % 3)

        self.ui.total_payer.setText(f"{self.total_a_payer} Ar")

    def remove_card(self, numero_article, sous_total):
        self.update_total_payer(0, sous_total * -1)

    def update_total_payer(self, ancien: int, sous_total: int):
        self.total_a_payer = self.total_a_payer + sous_total - ancien
        self.ui.total_payer.setText(f"{self.total_a_payer} Ar")

    def handle_submit_modification(self):
        if self.ui.card_container.count() < 1:
            self.reset_all_facture_items()
            journal = Journal()
            journal.listeArticle = []
            journal.description = f"Modification et remboursement sur la facture {self.facture.numeroFacture}"
            journal.dateEnregistrement = get_date_time_to_string()
            journal.typeAction = "Modification de commande"
            services.journal_service.session.add(journal)
            services.journal_service.session.commit()
            self.close()
        else:
            self.reset_all_facture_items()
            facture_detail = self.update_facture_liste_article()
            self.facture.listeArticle = facture_detail
            session.commit()
            journal = Journal()
            journal.listeArticle = []
            journal.description = f"Modification et remboursement sur la facture {self.facture.numeroFacture}"
            journal.dateEnregistrement = get_date_time_to_string()
            journal.typeAction = "Modification de commande"
            services.journal_service.session.add(journal)
            services.journal_service.session.commit()
            self.close()

    def reset_all_facture_items(self):
        for item in self.facture.listeArticle:
            row = item.split(':')
            article = get_article_by_id(row[0])

            if article.typeConteneur == "Paquet":
                if row[3] == "pieces":
                    article.pieceEnStock = article.pieceEnStock + int(row[4])
                    article.packetEnStock = article.packetEnStock + (int(row[4]) // article.pieceParPaquet)
                    services.article_service.session.commit()
                else:
                    article.pieceEnStock = article.pieceEnStock + (int(row[4]) * article.pieceParPaquet)
                    article.packetEnStock = article.packetEnStock + int(row[4])
                    services.article_service.session.commit()
            else:
                if row[3] == "pieces":
                    article.pieceEnStock = article.pieceEnStock + int(row[4])
                    article.boiteEnStock = article.boiteEnStock + (int(row[4]) // article.pieceParBoite)
                    services.article_service.session.commit()
                else:
                    article.pieceEnStock = article.pieceEnStock + (int(row[4]) * article.pieceParBoite)
                    article.boiteEnStock = article.boiteEnStock + int(row[4])
                    services.article_service.session.commit()

        self.facture.listeArticle = []
        session.commit()


    def update_facture_liste_article(self):
        liste_article: list[str] = []
        for i in range(self.ui.card_container.count()):
            card_widget = self.ui.card_container.itemAt(i).widget()
            str_detail = f"{card_widget.numero_article}:{card_widget.article.libelle}:{card_widget.sou_total}:{card_widget.comboBox.currentText()}:{card_widget.line_edit_quantite.text()}"
            liste_article.append(str_detail)

            if card_widget.comboBox.currentText() == "pieces":
                self.modify_stock_for_type(card_widget.numero_article, card_widget.line_edit_quantite.text(), 1)
                pass
            elif card_widget.comboBox.currentText() == "pacquets":
                self.modify_stock_for_type(card_widget.numero_article, card_widget.line_edit_quantite.text(), 2)
                pass
            else:
                self.modify_stock_for_type(card_widget.numero_article, card_widget.line_edit_quantite.text(), 3)
                pass

        return liste_article

    def modify_stock_for_type(self, numero: str, quantite, type: int):
        quantite = int(quantite)
        article = get_article_by_id(numero)
        type_quantite = article.typeConteneur
        if type == 1:
            stock_actuel = article.pieceEnStock
            nouveau_stock = stock_actuel - quantite
            nouveau_conteneur = nouveau_stock // article.pieceParPaquet if type_quantite == "Paquet" else nouveau_stock // article.pieceParBoite
            if type_quantite == "Paquet":
                article.pieceEnStock = nouveau_stock
                article.packetEnStock = nouveau_conteneur
            else:
                article.pieceEnStock = nouveau_stock
                article.boiteEnStock = nouveau_conteneur
            services.article_service.session.commit()
            return

        elif type == 2:
            packet_actuel = article.packetEnStock
            nouveau_packet = packet_actuel - quantite
            nouveau_stock = article.pieceEnStock - (article.pieceParPaquet * quantite)
            article.pieceEnStock = nouveau_stock
            article.packetEnStock = nouveau_packet
            services.article_service.session.commit()
            return

        else:
            boite_actuel = article.boiteEnStock
            nouveau_boite = boite_actuel - quantite
            nouveau_stock = article.pieceEnStock - (article.pieceParBoite * quantite)
            article.pieceEnStock = nouveau_stock
            article.boiteEnStock = nouveau_boite
            services.article_service.session.commit()
            return

