from Custom_Widgets.Widgets import *

from services.article_service import verify_article_by_id
from views.main_window import *
from Custom_Widgets.Widgets import QMainWindow

from views.states.commande_card import CardCommande

settings = QSettings()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.commande_item = []
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
        self.add_new_card_commande(search_value)

    def add_new_card_commande(self, numero):
        self.commande_item.append(numero)
        element = len(self.commande_item)
        carte = CardCommande(numero)
        # self.ui.cardContainer.addWidget(carte, (element // 3) - 1, element % 4)
        self.ui.cardContainer.addWidget(carte, (element - 1) // 3, (element -1 ) % 3)
