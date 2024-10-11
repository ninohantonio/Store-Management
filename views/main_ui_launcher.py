from Custom_Widgets.QCustomQDialog import QCustomQDialog
from Custom_Widgets.Widgets import *
from Custom_Widgets.Widgets import QMainWindow
from PySide6.QtCore import QEvent
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMessageBox, QDialog

from controllers.commande_controller import get_date_time_to_string, get_date_to_string
from models.model_class import Facture, Client, Commande, Journal
from services.article_service import verify_article_by_id, get_article_by_id, get_all_article, get_article_by_name, \
    get_article_by_price, session
from services.client_service import insert_new_client, get_client_by_id
from services.commande_service import insert_new_commande
from services.facture_service import insert_new_facture, get_facture_by_id, get_all_facture, search_factures_by_date_range
from services.journal_service import insert_new_journal
from views.auth.login_launcher import LoginWindow
from views.client_ui_launcher import ClientList
from views.main_window import *
from views.states.commande_card import CardCommande
from views.states.facture_dialog_launcher import FactureDialog
from views.states.stock_state import refresh_stock_table_data, refresh_facture_table_data

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

        self.selected_client = Client()

        if self.ui.mainNavigationScreen.currentIndex() == 0:
            self.ui.searchField.returnPressed.connect(self.print_search_value)
            self.ui.searchField.setFocus()
            pass

        self.ui.mainNavigationScreen.currentChanged.connect(self.manage_navigation)

        self.ui.valider_commandeBtn.clicked.connect(self.handle_submit_commande_validation)
        self.ui.avance_field.setValidator(QIntValidator(0, 9999999))

        self.ui.tout_payer.setChecked(True)

        self.ui.avance_field.installEventFilter(self)

        # Connecter les signaux dateChanged
        self.ui.dateEdit.dateChanged.connect(self.on_date_changed)
        self.ui.dateEdit_2.dateChanged.connect(self.on_date_changed)

        self.ui.facture_table.cellDoubleClicked.connect(self.manage_double_click_facture_item)

        self.show()

    def eventFilter(self, obj, event):
        # Vérifier si l'événement est lié au focus entrant dans le QLineEdit
        if obj == self.ui.avance_field and event.type() == QEvent.FocusIn:
            # Lorsque le focus entre dans le QLineEdit, cocher un bouton radio
            self.ui.avancement.setChecked(True)
            return True
        return super().eventFilter(obj, event)

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
        elif index == 2:
            self.ui.searchField.returnPressed.disconnect()
            self.refresh_facture_data_table()
            self.ui.searchField.returnPressed.connect(lambda : self.fill_facture_data_to_table(self.ui.searchField.text()))
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
        if self.check_if_card_container_empty():
            self.show_alert_message("Le panier de commande est vide!!")
            return

        #demander confirmation
        response = self.show_confirmation_dialog()
        if response:
            #choisir un client, en creer un
            self.show_client_selection_dialog()
            client = self.selected_client
            if client is not None:
                insert_new_client(client)
                #formater les donnee de la carte numero:libelle:sous-total:desciption:effectif et modifier l'etat de stocck
                liste_article = self.extract_info_to_card()
                #boucle pour stocker les informations dans commande
                self.store_data_to_commande(liste_article, client.numeroClient)
                #stocker dans Facture
                facture = self.store_data_to_facture(liste_article, client.numeroClient)
                #stocker dans journal de vente
                self.store_data_to_journal(liste_article)
                #afficher dialog avec facture
                self.facture_dialog = FactureDialog(facture)
                self.facture_dialog.show()
                #nettoyer carte
                self.reset_card_container()
                return
            else:
                self.show_alert_message("Acun client selectionnee!! Veuillez reessayer!")
        return

    def extract_info_to_card(self):
        liste_article: list[str] = []
        for i in range(self.ui.cardContainer.count()):
            card_widget = self.ui.cardContainer.itemAt(i).widget()
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

    def show_alert_message(self, message: str):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Info")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)

        # Afficher le dialogue et récupérer la réponse de l'utilisateur
        msg_box.exec()

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

    def check_if_card_container_empty(self):
        return self.ui.cardContainer.count()< 1

    def show_client_selection_dialog(self):
        # Créer un QDialog pour la sélection du client
        self.dialog = ClientList()

        # Si l'utilisateur a sélectionné un client et cliqué sur OK
        if self.dialog.exec() == QDialog.Accepted:
            if self.dialog.temporary_client_selected:
                print(f"Client sélectionné : temporaire")
                self.selected_client = Client()
                self.selected_client.nom = "temp"
                self.selected_client.telephone = "temp"
                self.selected_client.adresse = "temp"
            else:
                # Récupérer les informations du client sélectionné dans la table
                client_info = self.dialog.get_selected_client()
                if client_info:
                    # Afficher les informations du client sélectionné ou temporaire
                    self.selected_client = client_info
                    print(f"Client sélectionné : {client_info.nom}, Telephone : {client_info.telephone}")
                else:
                    print("Aucun client sélectionné.")
                    self.selected_client = None
                    return

        else:
            print("Sélection annulée.")

    def store_data_to_commande(self, liste_article: list[str], numero_client):
        #numero: libelle:sous - total: desciption:effectif
        for commande_data in liste_article:
            commande_split = commande_data.split(':')
            commande = Commande(dateCommande=get_date_time_to_string(), dateLivraison=get_date_to_string(), quantiteCommande=commande_split[4], type=commande_split[3], numeroClient=numero_client, numeroArticle=commande_split[0])
            insert_new_commande(commande)

    def store_data_to_facture(self, liste_article: list[str], numero_client):
        statut_payement = self.ui.tout_payer.isChecked()
        try:
            avancement = int(self.ui.avance_field.text())
        except ValueError:
            avancement = 0  # Si la quantité est vide ou invalide
        facture = Facture(dateEnregistrement=get_date_time_to_string(), listeArticle=liste_article, avancement = avancement,statutPayement=statut_payement, numeroClient=numero_client)
        insert_new_facture(facture)
        return facture

    def store_data_to_journal(self, liste_article: list[str]):
        journal = Journal(dateEnregistrement=get_date_time_to_string(), listeArticle=liste_article, typeAction="vente d'article")
        insert_new_journal(journal)

    def reset_card_container(self):
        self.ui.total_payer.setText(f"0 Ar")
        for i in range(self.ui.cardContainer.count()):
            card_widget = self.ui.cardContainer.itemAt(i).widget()
            card_widget.deleteLater()


    def fill_facture_data_to_table(self, search_value: str):
        if search_value.strip() == "":
            self.refresh_facture_data_table()
        else:
            factures = get_facture_by_id(int(search_value))
            refresh_facture_table_data(self.ui.facture_table, [factures])
            return

        print(f"facture search = {search_value}")



    def refresh_facture_data_table(self):
        factures = get_all_facture()
        refresh_facture_table_data(self.ui.facture_table, factures)
        return

    def on_date_changed(self):
        # Obtenir les dates sélectionnées par l'utilisateur
        start_date = self.ui.dateEdit.date().toPython()
        end_date = self.ui.dateEdit_2.date().toPython()

        # Appeler la fonction de recherche
        factures = search_factures_by_date_range(session, start_date, end_date)

        refresh_facture_table_data(self.ui.facture_table, factures)

    def manage_double_click_facture_item(self, row, column):

        numero = self.ui.facture_table.item(row, 0).text()
        facture = get_facture_by_id(int(numero))

        self.facture_dialog = FactureDialog(facture)
        self.facture_dialog.show()
        return