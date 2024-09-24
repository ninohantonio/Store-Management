from Custom_Widgets.QCustomQDialog import QCustomQDialog
from Custom_Widgets.Widgets import *

from services.article_service import verify_article_by_id, get_article_by_id, get_all_article, get_article_by_name, \
    get_article_by_price
from views.auth.admin_ui_launcher import AdminWindow
from views.main_window import *
from Custom_Widgets.Widgets import QMainWindow

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
        if self.ui.mainNavigationScreen.currentIndex() == 0:
            self.ui.searchField.returnPressed.connect(self.print_search_value)
            self.ui.searchField.setFocus()
            pass


        self.ui.mainNavigationScreen.currentChanged.connect(self.manage_navigation)
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
        self.add_new_card_commande(search_value) if verify_article_by_id(search_value) else self.show_article_not_found()

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

            self.ui.cardContainer.addWidget(carte, (element - 1) // 3, (element -1 ) % 3)

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
        self.admin_window = AdminWindow()
        self.admin_window.show()
        return

    def show_article_not_found(self):
        stock_error_dialog = QCustomQDialog(
            title="Article scannee non trouver !!",
            description="Voulez vous ajouter cette nouvelle article ?",
            padding=20,
            margin=60,
            # yesButtonIcon=my_yes_icon,
            # cancelButtonIcon=my_cancel_icon,
            yesButtonText="Voir stock",
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




