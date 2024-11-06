from Custom_Widgets.QCustomQDialog import QCustomQDialog
from Custom_Widgets.Widgets import *
from Custom_Widgets.Widgets import QMainWindow
from PySide6.QtCore import QEvent
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMessageBox, QDialog

import services.reliure_service
from controllers.commande_controller import get_date_time_to_string, get_date_to_string
from models.model_class import Facture, Client, Commande, Journal, Notification, Articlerapide, Article, Typelivre, \
    Reliure
from services.approvisionnement_service import get_article_in_limite
from services.article_service import verify_article_by_id, get_article_by_id, get_all_article, get_article_by_name, \
    get_article_by_price, session, filter_article_by_date
from services.articlerapide_service import insert_new_article_rapide, get_all_articlerapide
from services.client_service import insert_new_client, get_client_by_id
from services.commande_service import insert_new_commande
from services.facture_service import insert_new_facture, get_facture_by_id, get_all_facture, \
    search_factures_by_date_range, get_facture_by_state
from services.journal_service import insert_new_journal, get_all_journal, get_journal_by_type_action, \
    search_journals_by_date
from services.reliure_service import get_all_reliure_commande, get_all_type_livre, insert_new_reliure_commande, \
    get_reliure_by_id, get_type_livre_by_id, get_reliure_by_date, get_reliure_by_state, session, \
    get_reliure_by_client_name
from views.article_rapide_launcher import ArticleRapideDialog
from views.auth.login_launcher import LoginWindow
from views.client_ui_launcher import ClientList
from views.main_window import *
from views.states.commande_card import CardCommande
from views.states.facture_dialog_launcher import FactureDialog
from views.states.notification_card import NotificationCard
from views.states.reliure_facture_dialog_launcher import FactureReliureDialog
from views.states.stock_state import refresh_stock_table_data, refresh_facture_table_data, refresh_journal_table_data, \
    refresh_reliure_table_data
from views.states.type_livre_dialog import TypeLivreDialog

settings = QSettings()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.total_a_payer = 0
        QMainWindow.__init__(self)
        self.commande_item = {}
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.article_rapide_selection: Article = None
        self.typeLivre_selection: Typelivre = None
        self.total_reliure = 0
        self.reliure_numero = None
        loadJsonStyle(self, self.ui, jsonFiles=["views/style.json"])

        self.showMaximized()

        self.selected_client: Client = None

        if self.ui.mainNavigationScreen.currentIndex() == 0:
            self.ui.searchField.returnPressed.connect(self.print_search_value)
            self.ui.searchField.setFocus()
            pass

        self.ui.mainNavigationScreen.currentChanged.connect(self.manage_navigation)

        self.ui.valider_commandeBtn.clicked.connect(self.handle_submit_commande_validation)
        self.ui.avance_field.setValidator(QIntValidator(0, 999999))

        self.ui.tout_payer.setChecked(True)

        self.ui.avance_field.installEventFilter(self)

        # Connecter les signaux dateChanged
        self.ui.dateEdit.dateChanged.connect(self.on_date_changed)
        self.ui.dateEdit_2.dateChanged.connect(self.on_date_changed)

        self.ui.add_selection_rapideBtn.clicked.connect(self.show_article_rapide_dialog)

        self.ui.facture_table.setColumnWidth(0, 150)
        self.ui.facture_table.setColumnWidth(1, 150)
        self.ui.facture_table.setColumnWidth(2, 150)
        self.ui.facture_table.setColumnWidth(3, 150)
        self.ui.facture_table.setColumnWidth(4, 150)

        self.ui.journal_tableWidget.setColumnWidth(0, 150)
        self.ui.journal_tableWidget.setColumnWidth(1, 150)
        self.ui.journal_tableWidget.setColumnWidth(2, 150)

        self.ui.facture_table.cellDoubleClicked.connect(self.manage_double_click_facture_item)
        self.ui.filter_facture_combo.currentIndexChanged.connect(self.manage_filter_facture_change)

        self.ui.selection_rapide_combo.currentIndexChanged.connect(self.manage_article_rapide_selection_change)
        self.ui.quantite_spinBox.setMinimum(0)
        self.ui.submit_section_rapideBtn.clicked.connect(self.manage_submit_article_rapide_selection)

        self.ui.logoutBtn.clicked.connect(self.manage_logout)

        self.ui.journal_dateEdit.dateChanged.connect(self.manage_journal_date_change)

        self.ui.reliure_table.hideColumn(0)
        self.ui.reliure_table.hideColumn(3)
        self.ui.reliure_table.hideColumn(4)
        self.ui.comboBox.currentIndexChanged.connect(self.manage_type_livre_change)
        self.ui.add_type.clicked.connect(self.show_type_livre_dialog_add)
        self.ui.delete_type.clicked.connect(self.show_type_livre_dialog_modify)
        self.ui.exemplaire_spinBox.setMinimum(0)

        self.ui.page_noir_spinBox.textChanged.connect(self.manage_page_spinbox_change)
        self.ui.page_couleur_spinBox.textChanged.connect(self.manage_page_spinbox_change)
        self.ui.exemplaire_spinBox.textChanged.connect(self.manage_page_spinbox_change)
        self.ui.couverture_spin_box.textChanged.connect(self.manage_page_spinbox_change)
        self.ui.reset_reliure.clicked.connect(self.reset_reliure_form)
        self.ui.submit_reliure.clicked.connect(self.handle_submit_reliure)
        self.ui.modify_reliure.clicked.connect(self.handle_modify_reliure)
        self.ui.facture_reliure.clicked.connect(self.show_reliure_facture_dialog)

        self.ui.reliure_table.cellDoubleClicked.connect(self.manage_reliure_table_cell_click)
        self.ui.date_reliure.dateChanged.connect(self.handle_date_reliure_changed)
        self.ui.filter_reliure.currentIndexChanged.connect(self.manage_filter_reliure_change)

        self.manage_page_spinbox_change()
        self.load_type_livre_data()

        self.load_notification_for_user()

        self.load_article_rapide_combo_list()

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
                carte.line_edit_quantite.setValue(new_quantity)  # Mettre à jour l'affichage
                carte.update_sous_total()

        else:
            self.commande_item[numero] = get_article_by_id(numero)
            article = self.commande_item[numero]
            element = len(self.commande_item)
            carte = CardCommande(article, numero_article=article.numeroArticle, parent=self)

            carte.sous_total_changed.connect(self.update_total_payer)
            self.total_a_payer += article.prixUnitaire
            self.ui.total_payer.setText(f"{self.total_a_payer} Ar")
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
        if index == 2:
            self.refresh_stock_screen()
            self.ui.date_article.setHidden(True)
            self.ui.searchField.returnPressed.disconnect()
            self.ui.filterCombo.currentIndexChanged.connect(self.refresh_data_search)
            self.ui.searchField.returnPressed.connect(self.refresh_data_search)
        elif index == 0:
            self.ui.searchField.returnPressed.disconnect()
            self.ui.searchField.returnPressed.connect(self.print_search_value)
            self.ui.searchField.setFocus()
        elif index == 1:
            self.ui.searchField.returnPressed.disconnect()
        elif index == 3:
            self.ui.searchField.returnPressed.disconnect()
            self.refresh_facture_data_table()
            self.ui.searchField.returnPressed.connect(lambda : self.fill_facture_data_to_table(self.ui.searchField.text()))
        elif index == 4:
            self.ui.searchField.returnPressed.disconnect()
            self.refresh_journal_table_data()
            self.ui.searchField.returnPressed.connect(lambda : self.get_journal_by_typeaction(self.ui.searchField.text()))
        elif index == 6:
            self.ui.searchField.returnPressed.disconnect()
            self.refresh_reliure_data_table()
            self.ui.searchField.returnPressed.connect(lambda : self.search_reliure_by_clientname(self.ui.searchField.text()))
        pass

    def refresh_stock_screen(self):
        articles = get_all_article()
        refresh_stock_table_data(self.ui.stockTable, articles)

    def refresh_data_search(self):
        current_filter_index = self.ui.filterCombo.currentIndex()
        articles = []
        self.ui.date_article.setHidden(True)
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
            self.ui.date_article.dateChanged.connect(self.search_article_by_date)
            self.ui.date_article.setHidden(False)
            date = self.ui.date_article.date().toPython()
            if self.ui.searchField.text().strip() == "":
                articles = get_all_article()
            else:
                articles = filter_article_by_date(date)
            pass
        print(f"articles = {articles}")
        refresh_stock_table_data(self.ui.stockTable, articles)
        pass

    def search_article_by_date(self):
        date = self.ui.date_article.date().toPython()
        articles = filter_article_by_date(date)
        refresh_stock_table_data(self.ui.stockTable, articles)

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
        response = self.show_confirmation_dialog("Êtes-vous sûr de vouloir continuer ?")
        if response:
            #choisir un client, en creer un
            self.show_client_selection_dialog()
            client = self.selected_client
            if client is not None:
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
                self.load_notification_for_user()
                return
            else:
                self.show_alert_message("Aucun client selectionnee!! Veuillez reessayer!")
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

    def show_confirmation_dialog(self, message: str):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText(message)
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
                newclient_tmp = Client()
                newclient_tmp.nom = "tmp"
                newclient_tmp.telephone = "tmp"
                newclient_tmp.adresse = "tmp"
                insert_new_client(newclient_tmp)
                self.selected_client = newclient_tmp
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
            commande = Commande(dateCommande=get_date_time_to_string(), quantiteCommande=commande_split[4], type=commande_split[3], numeroClient=numero_client, numeroArticle=commande_split[0])
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
        self.commande_item = {}


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
        factures = search_factures_by_date_range(start_date, end_date)

        refresh_facture_table_data(self.ui.facture_table, factures)

    def manage_double_click_facture_item(self, row, column):

        numero = self.ui.facture_table.item(row, 0).text()
        facture = get_facture_by_id(int(numero))

        self.facture_dialog = FactureDialog(facture, can_change_state=True)
        self.facture_dialog.finished.connect(self.refresh_facture_data_table)
        self.facture_dialog.exec()
        return

    def manage_filter_facture_change(self, index):
        if index == 0:
            self.refresh_facture_data_table()
        elif index == 1:
            factures = get_facture_by_state(False)
            refresh_facture_table_data(self.ui.facture_table, factures)
        else:
            factures = get_facture_by_state(True)
            refresh_facture_table_data(self.ui.facture_table, factures)


    def load_notification_for_user(self):
        articles = get_article_in_limite()
        self.ui.notificationBtn.setText(f"Notifications ({len(articles)})")
        # articles = ["3210330054346", "8991389783085", "8991389783085", "3210330054346", "3210330054346", "3210330054346"]
        self.container = QWidget()
        self.layout = QVBoxLayout(self.container)

        for article in articles:
            notification = Notification()
            notification.numeroArticle = article
            notification.titre = "Marge d'approvisionnement atteint"
            notification.contenu = f"Veuillez approvisionner le stock portant le numero Bar : {article}"
            notification.dateEmmission = get_date_time_to_string()

            card = NotificationCard(notification)
            self.layout.addWidget(card)

        self.ui.scrollArea.setWidget(self.container)


    def show_article_rapide_dialog(self):
        self.articleDialog = ArticleRapideDialog()
        container = self.articleDialog.layout
        if self.articleDialog.exec() == QDialog.Accepted:
            article_rapides = []
            for i in range(container.count()):
                card_widget = container.itemAt(i).widget()
                if card_widget.is_checked:
                    article_rapides.append(card_widget.numeroArticle)
                    article_rapide = Articlerapide()
                    article_rapide.numeroArticle = card_widget.numeroArticle
                    insert_new_article_rapide(article_rapide)
            self.load_article_rapide_combo_list()
            print(article_rapides)
        else:
            return

    def load_article_rapide_combo_list(self):
        article_rapides = get_all_articlerapide()
        self.ui.selection_rapide_combo.clear()

        for i in article_rapides:
            article = get_article_by_id(i.numeroArticle)
            self.ui.selection_rapide_combo.addItem(article.libelle, article)

    def manage_article_rapide_selection_change(self, index):
        article: Article = self.ui.selection_rapide_combo.itemData(index)
        self.article_rapide_selection = article
        self.ui.quantite_spinBox.setMaximum(article.pieceEnStock)

    def manage_submit_article_rapide_selection(self):
        quantite = int(self.ui.quantite_spinBox.text())
        if quantite > 0:
            detail_article = f"{self.article_rapide_selection.numeroArticle}:{self.article_rapide_selection.libelle}:{self.article_rapide_selection.prixUnitaire * quantite}:Piece:{quantite}"
            # modifier stock
            self.modify_stock_for_type(self.article_rapide_selection.numeroArticle, quantite, 1)
            # ajouter au facture
            facture = self.store_data_to_facture([detail_article], 1)
            # ajouter au journal
            self.store_data_to_journal([detail_article])
            # refresh notifications
            print(f"facture rapide : {facture}")
            self.ui.quantite_spinBox.clear()
            return


    def refresh_journal_table_data(self):
        journals = get_all_journal()
        refresh_journal_table_data(self.ui.journal_tableWidget, journals)
        return

    def get_journal_by_typeaction(self, action: str):
        if action.strip() == "":
            self.refresh_journal_table_data()
            return
        journals = get_journal_by_type_action(action)
        refresh_journal_table_data(self.ui.journal_tableWidget, journals)
        return

    def manage_journal_date_change(self):
        search_date = self.ui.journal_dateEdit.date().toPython()

        journals = search_journals_by_date(search_date)
        refresh_journal_table_data(self.ui.journal_tableWidget, journals)


    def refresh_reliure_data_table(self):
        reliures = get_all_reliure_commande()
        refresh_reliure_table_data(self.ui.reliure_table, reliures)
        return

    def show_type_livre_dialog_add(self):
        type_livre_dialog = TypeLivreDialog()
        type_livre_dialog.finished.connect(self.load_type_livre_data)

        type_livre_dialog.exec()
        return

    def show_type_livre_dialog_modify(self):
        type_livre_dialog = TypeLivreDialog(True)
        type_livre_dialog.finished.connect(self.load_type_livre_data)

        type_livre_dialog.exec()
        return

    def load_type_livre_data(self):
        types = get_all_type_livre()
        self.ui.comboBox.clear()
        for type in types:
            self.ui.comboBox.addItem(type.typeLivre, type)
        return

    def manage_type_livre_change(self, index):
        self.typeLivre_selection = self.ui.comboBox.itemData(index)
        self.manage_page_spinbox_change()


    def manage_page_spinbox_change(self):
        if self.typeLivre_selection:
            page_noir = int(self.ui.page_noir_spinBox.text())
            page_couleur = int(self.ui.page_couleur_spinBox.text())
            exemplaire = int(self.ui.exemplaire_spinBox.text())
            type_couverture = self.ui.radioBristole.isChecked()
            couverture = int(self.ui.couverture_spin_box.text())
            prix_couverture = couverture * self.typeLivre_selection.prixBristole if type_couverture else couverture * self.typeLivre_selection.prixPapierGlace
            total = (
                                page_noir * self.typeLivre_selection.prixPageNoir + page_couleur * self.typeLivre_selection.prixPageCouleur + self.typeLivre_selection.prixReliure + prix_couverture) * exemplaire
            self.ui.total_reliure.setText(f"{total} Ar")
            self.total_reliure = total

        else:
            self.ui.total_reliure.setText(f"{0} Ar")

    def reset_reliure_form(self):
        self.ui.page_noir_spinBox.setValue(0)
        self.ui.page_couleur_spinBox.setValue(0)
        self.ui.exemplaire_spinBox.setValue(0)
        self.ui.total_reliure.setText(f"{0} Ar")
        self.ui.couverture_spin_box.setValue(0)
        self.total_reliure = 0
        self.reliure_numero = None

    def handle_submit_reliure(self):
        if self.reliure_numero is None:
            response = self.show_confirmation_dialog("Etes vous sur pour cette commande de reliure")
            if response:
                if self.total_reliure == 0:
                    self.show_alert_message("Votre Commande est de 0 Ar, veuillez verifier!")
                else:
                    self.show_client_selection_dialog()
                    if self.selected_client:
                        reliure = Reliure()
                        reliure.nombreExemplaire = int(self.ui.exemplaire_spinBox.text())
                        reliure.nombrePageNoir = int(self.ui.page_noir_spinBox.text())
                        reliure.nombrePageCouleur = int(self.ui.page_couleur_spinBox.text())
                        reliure.numeroType = self.typeLivre_selection.numeroType
                        reliure.numeroClient = self.selected_client.numeroClient
                        reliure.statutLivrer = self.ui.reliure_state.isChecked()
                        reliure.nombreCouverture = int(self.ui.couverture_spin_box.text())
                        reliure.typeCouverture = self.ui.radioBristole.isChecked()
                        reliure.dateCommande = get_date_to_string()

                        insert_new_reliure_commande(reliure)
                        self.refresh_reliure_data_table()
                        self.reset_reliure_form()
                    else:
                        return
            else:
                return
        else:
            self.show_alert_message("Cette commande est deja ajouter")


    def manage_reliure_table_cell_click(self, row, column):
        numero = self.ui.reliure_table.item(row, 0).text()
        reliure = get_reliure_by_id(int(numero))
        type = get_type_livre_by_id(reliure.numeroType)

        for i in range(self.ui.comboBox.count()):
            if self.ui.comboBox.itemData(i) == type:
                self.ui.comboBox.setCurrentIndex(i)
        print(self.typeLivre_selection.numeroType)
        self.ui.page_noir_spinBox.setValue(reliure.nombrePageNoir)
        self.ui.page_couleur_spinBox.setValue(reliure.nombrePageCouleur)
        self.ui.reliure_state.setChecked(reliure.statutLivrer)
        self.ui.exemplaire_spinBox.setValue(reliure.nombreExemplaire)
        self.ui.couverture_spin_box.setValue(reliure.nombreCouverture)
        self.ui.radioBristole.setChecked(reliure.typeCouverture)
        self.ui.radioGlace.setChecked(not reliure.typeCouverture)
        self.reliure_numero = numero
        return

    def handle_modify_reliure(self):
        if self.reliure_numero:
            reliure = get_reliure_by_id(self.reliure_numero)
            reliure.nombreExemplaire = int(self.ui.exemplaire_spinBox.text())
            reliure.nombrePageNoir = int(self.ui.page_noir_spinBox.text())
            reliure.nombrePageCouleur = int(self.ui.page_couleur_spinBox.text())
            reliure.numeroType = self.typeLivre_selection.numeroType
            reliure.statutLivrer = self.ui.reliure_state.isChecked()
            reliure.typeCouverture = self.ui.radioBristole.isChecked()
            reliure.nombreCouverture = int(self.ui.couverture_spin_box.text())
            services.reliure_service.session.commit()

            self.reset_reliure_form()
            self.refresh_reliure_data_table()

        else:
            self.show_alert_message("La commande n'existe pas encore")
            return

    def handle_delete_reliure(self):
        if self.reliure_numero:
            if self.show_confirmation_dialog("Etes vous sur de supprimer cette commande?"):
                reliure = get_reliure_by_id(self.reliure_numero)
                session.delete(reliure)
                session.commit()

                self.reset_reliure_form()
                self.refresh_reliure_data_table()


        else:
            self.show_alert_message("La commande n'existe pas encore")
            return

    def handle_date_reliure_changed(self):
        search_date = self.ui.date_reliure.date().toPython()

        reliures = get_reliure_by_date(search_date)
        refresh_reliure_table_data(self.ui.reliure_table, reliures)
        print(len(reliures))
        pass

    def manage_filter_reliure_change(self, index):
        if index == 0:
            self.refresh_reliure_data_table()
        elif index == 1:
            reliures = get_reliure_by_state(False)
            refresh_reliure_table_data(self.ui.reliure_table, reliures)
        else:
            reliures = get_reliure_by_state(True)
            refresh_reliure_table_data(self.ui.reliure_table, reliures)

    def search_reliure_by_clientname(self, client: str):
        if client.strip() == "":
            self.refresh_reliure_data_table()
        else:
            reliures = get_reliure_by_client_name(client)
            refresh_reliure_table_data(self.ui.reliure_table, reliures)


    def show_reliure_facture_dialog(self):
        reliure = get_reliure_by_id(int(self.reliure_numero))
        self.reliure_facture = FactureReliureDialog(reliure)
        self.reliure_facture.exec()

    def manage_logout(self):
        response = self.show_confirmation_dialog("Êtes-vous sûr de vouloir basculer de compte")
        if response:
            self.login_window = LoginWindow()
            self.login_window.show()
        return




