from PySide6.QtWidgets import QWidget

from views.auth.ui_confirmation import Ui_Form


class ConfirmationWindow(QWidget):
    def __init__(self):
        super(ConfirmationWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)