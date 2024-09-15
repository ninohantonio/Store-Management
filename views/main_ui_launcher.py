from Custom_Widgets.Qss.colorsystem import Theme
from Custom_Widgets.Widgets import *
from views.main_window import *
from Custom_Widgets.Widgets import QMainWindow

settings = QSettings()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles=["views/style.json"])
        self.show()

    # def styleVariablesFromTheme(self, active_style):
    #     # Implémentez la logique qui extrait les variables de style du thème
    #     # Par exemple, si `active_style` contient des informations sur les couleurs
    #     return {
    #         'background': active_style.get('bg_color', 'default_bg'),
    #         'text': active_style.get('txt_color', 'default_text'),
    #         'accent': active_style.get('accent_color', 'default_accent'),
    #     }

    def print_search_value(self):
        search_value = self.ui.searchField.text()
        print(f"search_value = {search_value}")
        self.ui.searchField.setText("")
