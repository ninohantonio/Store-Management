from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QDialog, QMessageBox

from models.model_class import Client
from services.client_service import insert_new_client
from views.states.client_form_dialog_ui import Ui_Dialog


class ClientFormDialog(QDialog):
    def __init__(self):
        super(ClientFormDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.telephone_client.setValidator(QIntValidator(0, 9999999999))


    def handle_submit_client(self):
        if self.ui.nom_client.text() != "" and self.ui.telephone_client.text() != "" and self.ui.adresse_client.text() != "":
            if self.is_valide_numero(numero=self.ui.telephone_client.text()) :
                client = Client()
                client.nom = self.ui.nom_client.text()
                client.telephone = self.ui.telephone_client.text()
                client.adresse = self.ui.adresse_client.text()
                try:
                    insert_new_client(client)
                    self.show_success_message("Votre client a ete bien inserer")
                    self.close()
                    return
                except:
                    self.show_alert_message("Une erreur s'est produit, veuillez recommencer!")
            else:
                self.show_alert_message("Le numero telephone est invalide")
        else:
            self.show_alert_message("Veuillez remplir toutes les champs!!")

    def show_alert_message(self, message: str):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Info")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)

    def show_success_message(self, message: str):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Succes")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)

    def reset_form(self):
        self.ui.nom_client.clear()
        self.ui.adresse_client.clear()
        self.ui.telephone_client.clear()

    def is_valide_numero(self, numero: str):
        valide_start = ("032", "033", "034", "037", "038")
        return numero.startswith(valide_start)
