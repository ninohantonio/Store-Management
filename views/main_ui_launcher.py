from Custom_Widgets.Widgets import *

from services.article_service import verify_article_by_id, get_article_by_id
from views.main_window import *
from Custom_Widgets.Widgets import QMainWindow

from views.states.commande_card import CardCommande

settings = QSettings()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.total_a_payer = 0
        QMainWindow.__init__(self)
        self.commande_item = {}
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles=["views/style.json"])
        self.ui.searchField.returnPressed.connect(self.print_search_value)
        self.ui.searchField.setFocus()
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
        self.add_new_card_commande(search_value) if verify_article_by_id(search_value) else print("Veuillez ajoutez l'article")

    def add_new_card_commande(self, numero):
        if numero in self.commande_item:
            print("deja scanner")
        else:
            self.commande_item[numero] = get_article_by_id(numero)
            article = self.commande_item[numero]
            element = len(self.commande_item)
            carte = CardCommande(article, parent=self)

            carte.sous_total_changed.connect(self.update_total_payer)

            self.ui.cardContainer.addWidget(carte, (element - 1) // 3, (element -1 ) % 3)

    def update_total_payer(self, sous_total: int):
        total = self.total_a_payer + sous_total
        self.ui.total_payer.setText(f"{total} Ar")