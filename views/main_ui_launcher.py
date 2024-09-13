from PySide6.QtWidgets import QMainWindow

from views.main_window import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.seeMoreButton.clicked.connect(lambda : self.print_search_value())
        self.show()

    def print_search_value(self):
        search_value = self.ui.searchField.text()
        print(f"search_value = {search_value}")
        self.ui.searchField.setText("")