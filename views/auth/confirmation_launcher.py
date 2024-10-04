

from PySide6.QtWidgets import QWidget, QMessageBox
from numpy.random import random_integers

from services.auth_service import check_if_mail_is_admin, send_email_confirmation_to_admin
from views.auth.admin_ui_launcher import AdminWindow
from views.auth.ui_confirmation import Ui_Form


class ConfirmationWindow(QWidget):
    def __init__(self, parent: QWidget = None):
        super(ConfirmationWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.parent = parent

        self.ui.code_field.textChanged.connect(self.handle_code_validation_change)

        self.confirmation_code = None

        self.ui.send_mail.clicked.connect(self.handle_send_code)


    def generate_confirmation_code(self):
        code = random_integers(low=100000, high=999999)
        return code

    def handle_send_code(self):
        if check_if_mail_is_admin(self.ui.email.text()):
            self.confirmation_code = self.generate_confirmation_code()
            if send_email_confirmation_to_admin(self.ui.email.text(), "Code de validation Irina service", f"Voici la code de validation {self.confirmation_code}"):
                self.show_info_box_dialog()
            else:
                self.show_critical_box_dialog()
        else:
            self.show_warning_box_dialog()
        return

    def show_warning_box_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Erreur d'email")
        msg_box.setText("L'email que vous avez entré n'existe pas ou est incorrect.")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def show_info_box_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Email evoyer")
        msg_box.setText("Le code de validation a bien ete envoyer, verifiez votre boite mail")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def show_critical_box_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Email non envoyer")
        msg_box.setText("L'email ne peut pas etre envoyer, veillez reesayer")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def handle_code_validation_change(self):
        self.ui.invalid_code.setHidden(True)
        if self.ui.code_field.text() != "" and len(self.ui.code_field.text()) == 6:
            if str(self.confirmation_code) == self.ui.code_field.text():
                print("Code de validation correct")
                self.admin_window = AdminWindow()
                self.admin_window.show()
                self.parent.close()
                self.close()
                return
            else:
                self.ui.invalid_code.setHidden(False)
        pass