
from Custom_Widgets.Widgets import *
from views.main_window import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()

    def print_search_value(self):
        search_value = self.ui.searchField.text()
        print(f"search_value = {search_value}")
        self.ui.searchField.setText("")