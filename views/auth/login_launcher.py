from PySide6.QtWidgets import QWidget

from views.auth.admin_ui_launcher import AdminWindow
from views.auth.auth_ui import Ui_Form


class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.login_btn.clicked.connect(self.handle_login)


    def handle_login(self):
        self.admin_window = AdminWindow()
        self.admin_window.show()
        return