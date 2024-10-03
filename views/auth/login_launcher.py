from PySide6.QtWidgets import QWidget, QLineEdit

from services.auth_service import verify_password
from views.auth.admin_ui_launcher import AdminWindow
from views.auth.auth_ui import Ui_Form


class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.show_password.clicked.connect(self.show_password)
        self.ui.hide_password.clicked.connect(self.hide_password)

        self.ui.password.setEchoMode(QLineEdit.Password)
        self.ui.login_btn.clicked.connect(self.handle_login)

    def show_password(self):
        self.ui.password.setEchoMode(QLineEdit.Normal)
        self.ui.hide_password.setHidden(False)
        self.ui.show_password.setHidden(True)
        pass


    def hide_password(self):
        self.ui.password.setEchoMode(QLineEdit.Password)
        self.ui.hide_password.setHidden(True)
        self.ui.show_password.setHidden(False)
        pass

    def redirect_to_admin_window(self):
        self.admin_window = AdminWindow()
        self.admin_window.show()
        return

    def handle_login(self):
        password = self.ui.password.text()
        email = self.ui.email.text()
        if verify_password(email, password) :
            self.redirect_to_admin_window()
            return
        else:
            return
