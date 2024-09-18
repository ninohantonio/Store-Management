import sys
import os

from PySide6.QtWidgets import QApplication

from services.article_service import get_article_by_name
from views.main_ui_launcher import MainWindow

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
