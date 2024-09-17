from Custom_Widgets.Widgets import *

from services.article_service import verify_article_by_id
from views.main_window import *
from Custom_Widgets.Widgets import QMainWindow

settings = QSettings()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
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
        print(f"search scan = {verify_article_by_id(search_value)}")
