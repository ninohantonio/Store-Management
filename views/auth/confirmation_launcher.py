from time import sleep

from PySide6.QtWidgets import QWidget, QMessageBox

from services.auth_service import check_if_mail_is_admin, send_email_confirmation_to_admin
from views.auth.ui_confirmation import Ui_Form


class ConfirmationWindow(QWidget):
    def __init__(self):
        super(ConfirmationWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.send_mail.clicked.connect(self.handle_send_code)


    def handle_send_code(self):
        if check_if_mail_is_admin(self.ui.email.text()):
            if send_email_confirmation_to_admin(self.ui.email.text(), "Code de validation Irina service", "Voici la code de validation"):
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
        msg_box.setText("Le code de validation a bien ete envoyer")
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
        pass