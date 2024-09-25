import sys

from Custom_Widgets import *
from Custom_Widgets import QMainWindow

from views.auth.ui_main_login import Ui_MainWindow

from PySide6.QtWidgets import QApplication

class AdminWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AdminWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles=["views/auth/style.json"])


#         self.show()
#
# def main():
#
#     window = AdminWindow()
