from Custom_Widgets.QCustomQDialog import QCustomQDialog
from Custom_Widgets.Widgets import *
from Custom_Widgets.Widgets import QMainWindow
from PySide6.QtWidgets import QMessageBox

from services.article_service import verify_article_by_id, get_article_by_id, get_all_article, get_article_by_name, \
    get_article_by_price, session
from views.auth.login_launcher import LoginWindow
from views.main_window import *
from views.states.commande_card import CardCommande
from views.states.stock_state import refresh_stock_table_data

settings = QSettings()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.total_a_payer = 0
        QMainWindow.__init__(self)
        self.commande_item = {}
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles=["views/style.json"])

        self.showMaximized()
        if self.ui.mainNavigationScreen.currentIndex() == 0:
            self.ui.searchField.returnPressed.connect(self.print_search_value)
            self.ui.searchField.setFocus()
            pass

        self.ui.mainNavigationScreen.currentChanged.connect(self.manage_navigation)

        self.ui.valider_commandeBtn.clicked.connect(self.handle_submit_commande_validation)
        # self.ui.searchField.setVisible(False)
        self.show()

    def print_search_value(self):
        search_value = self.ui.searchField.text()

        # Vérifier si le champ n'est pas vide avant de continuer
        if search_value.strip() == "":
            return  # Ne rien faire si le champ est vide

        # Effacer le texte pour préparer le prochain scan
        self.ui.searchField.clear()
        print(f"Article existe = {verify_article_by_id(search_value)}")
        self.add_new_card_commande(search_value) if verify_article_by_id(
            search_value) else self.show_article_not_found()

    def add_new_card_commande(self, numero):
        if numero in self.commande_item:
            print("deja scanner")
            carte = self.find_card_by_numero(numero)  # Trouver la carte associée à cet article

            if carte:
                current_quantity = int(carte.line_edit_quantite.text() or 0)
                new_quantity = current_quantity + 1  # Incrémenter la quantité de 1
                carte.line_edit_quantite.setText(str(new_quantity))  # Mettre à jour l'affichage
                carte.update_sous_total()

        else:
            self.commande_item[numero] = get_article_by_id(numero)
            article = self.commande_item[numero]
            element = len(self.commande_item)
            carte = CardCommande(article, numero_article=article.numeroArticle, parent=self)

            carte.sous_total_changed.connect(self.update_total_payer)

            # Connecter le signal card_removed pour gérer la suppression
            carte.card_removed.connect(self.remove_card)

            self.ui.cardContainer.addWidget(carte, (element - 1) // 3, (element - 1) % 3)

    def find_card_by_numero(self, numero: str):
        for i in range(self.ui.cardContainer.count()):
            card_widget = self.ui.cardContainer.itemAt(i).widget()
            if card_widget.numero_article == numero:
                return card_widget

        return None

    def update_total_payer(self, ancien: int, sous_total: int):
        self.total_a_payer = self.total_a_payer + sous_total - ancien
        self.ui.total_payer.setText(f"{self.total_a_payer} Ar")

    def remove_card(self, numero_article, sous_total):
        if numero_article in self.commande_item:
            del self.commande_item[numero_article]
            self.update_total_payer(0, sous_total * -1)

    def manage_navigation(self, index):
        if index == 1:
            self.refresh_stock_screen()
            self.ui.searchField.returnPressed.disconnect()
            self.ui.searchField.returnPressed.connect(self.refresh_data_search)
        elif index == 0:
            self.ui.searchField.returnPressed.disconnect()
            self.ui.searchField.returnPressed.connect(self.print_search_value)
            self.ui.searchField.setFocus()
        pass

    def refresh_stock_screen(self):
        articles = get_all_article()
        refresh_stock_table_data(self.ui.stockTable, articles)

    def refresh_data_search(self):
        current_filter_index = self.ui.filterCombo.currentIndex()
        articles = []
        if current_filter_index == 0:
            ## search by libelle
            if self.ui.searchField.text().strip() == "":
                articles = get_all_article()
            else:
                articles = get_article_by_name(self.ui.searchField.text())

        elif current_filter_index == 1:
            ## search by quantite en stock
            if self.ui.searchField.text().strip() == "":
                articles = get_all_article()
            else:
                pass
            pass

        elif current_filter_index == 2:
            ## search by prix unitaire
            if self.ui.searchField.text().strip() == "":
                articles = get_all_article()
            else:
                articles = get_article_by_price(self.ui.searchField.text())
            pass

        elif current_filter_index == 3:
            ## search by date d'entrer
            if self.ui.searchField.text().strip() == "":
                articles = get_all_article()
            else:
                articles = get_article_by_name(self.ui.searchField.text())
            pass
        print(f"articles = {articles}")
        refresh_stock_table_data(self.ui.stockTable, articles)
        pass

    def redirect_to_admin_window(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        return

    def show_article_not_found(self):
        stock_error_dialog = QCustomQDialog(
            title="Article scannee non trouver !!",
            description="Voulez vous ajouter cette nouvelle article ?",
            padding=20,
            margin=60,
            # yesButtonIcon=my_yes_icon,
            # cancelButtonIcon=my_cancel_icon,
            yesButtonText="Ajouter",
            cancelButtonText="Annuler",
            animationDuration=500,
            showYesButton=True,
            showCancelButton=True,
            setModal=True,
            frameless=True,
            windowMovable=True,
            # showForm=myFormWidget,
            # display a ui form inside the dialog box ie importing your form(from ui_form import myFormWidget)
            # to access the widgets inside your form (custom_dialog.shownForm.myWidgetName)
            parent=self,
            # addWidget=self.labele_stock_error  # append another widget or widget container to the dialog
        )

        stock_error_dialog.show()

        stock_error_dialog.accepted.connect(self.redirect_to_admin_window)  # yes button clicked
        stock_error_dialog.rejected.connect(
            lambda: stock_error_dialog.close())  # cancel button clicked

    def handle_submit_commande_validation(self):
        #demander confirmation
        response = self.show_confirmation_dialog()
        if response:
            #choisir un client, en creer un

            #formater les donnee de la carte numero:libelle:sous-total:desciption:effectif et modifier l'etat de stocck
            print(self.extract_info_to_card())
            #stocker dans Facture
            #stocker dans journal de vente
        return

    def extract_info_to_card(self):
        liste_article: list[str] = []
        for i in range(self.ui.cardContainer.count()):
            card_widget = self.ui.cardContainer.itemAt(i).widget()
            str_detail = f"{card_widget.numero_article}:{card_widget.article.libelle}:{card_widget.sou_total}:{card_widget.comboBox.currentText()}:{card_widget.line_edit_quantite.text()}"
            liste_article.append(str_detail)

            if card_widget.comboBox.currentText() == "pieces":
                self.modify_stock_for_type(card_widget.numero_article, int(card_widget.line_edit_quantite.text()), 1)
                pass
            elif card_widget.comboBox.currentText() == "pacquets":
                self.modify_stock_for_type(card_widget.numero_article, int(card_widget.line_edit_quantite.text()), 2)
                pass
            else:
                self.modify_stock_for_type(card_widget.numero_article, int(card_widget.line_edit_quantite.text()), 3)
                pass

        return liste_article

    def modify_stock_for_type(self, numero: str, quantite: int, type: int):
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
            session.commit()
            return

        elif type == 2:
            packet_actuel = article.packetEnStock
            nouveau_packet = packet_actuel - quantite
            nouveau_stock = article.pieceEnStock - (article.pieceParPaquet * quantite)
            article.pieceEnStock = nouveau_stock
            article.packetEnStock = nouveau_packet
            session.commit()
            return

        else:
            boite_actuel = article.boiteEnStock
            nouveau_boite = boite_actuel - quantite
            nouveau_stock = article.pieceEnStock - (article.pieceParBoite * quantite)
            article.pieceEnStock = nouveau_stock
            article.boiteEnStock = nouveau_boite
            session.commit()
            return

    def show_confirmation_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Êtes-vous sûr de vouloir continuer ?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)

        # Afficher le dialogue et récupérer la réponse de l'utilisateur
        response = msg_box.exec()

        # Vérifier la réponse et agir en conséquence
        if response == QMessageBox.Yes:
            return True  # Si Oui, on effectue l'action
        else:
            return False  # Si Non, on annule l'action

