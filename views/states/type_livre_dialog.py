from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QDialog, QMessageBox
from scripts.regsetup import description

from models.model_class import Typelivre
from services.reliure_service import insert_new_type_livre, get_all_type_livre, get_type_livre_by_id, session
from views.states.type_livre_ui import Ui_Dialog


class TypeLivreDialog(QDialog):
    def __init__(self, modification: bool = False):
        super(TypeLivreDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.type_selection: Typelivre = None

        self.ui.prix_noir.setValidator(QIntValidator(0, 99999))
        self.ui.prix_couleur.setValidator(QIntValidator(0, 99999))
        self.ui.prix_reliure.setValidator(QIntValidator(0, 99999))
        self.ui.prix_glace.setValidator(QIntValidator(0, 99999))


        if modification:
            self.ui.comboBox.setHidden(False)
            self.ui.reset_type.setText("Supprimer")
            self.ui.submit_type.setText("Enregistrer modifier")
            self.ui.submit_type.clicked.connect(self.modify_typelivre)
            self.ui.reset_type.clicked.connect(self.handle_delete_type)
            self.ui.comboBox.currentIndexChanged.connect(self.manage_type_selection_changed)
            self.ui.label_5.setText("Modifier ou Supprimer un Type de Livre")
            self.load_type_selection()
        else:
            self.ui.submit_type.clicked.connect(self.submit_new_type_livre)
            self.ui.reset_type.clicked.connect(lambda : self.close())
            self.ui.comboBox.setHidden(True)
            self.ui.submit_type.clicked.connect(self.submit_new_type_livre)
            self.ui.reset_type.clicked.connect(lambda: self.close())


    def submit_new_type_livre(self):
        description = self.ui.description.text()
        prix_noir = self.ui.prix_noir.text()
        prix_couleur = self.ui.prix_couleur.text()
        prix_reliure = self.ui.prix_reliure.text()
        prix_bristole = self.ui.prix_bristole.text()
        prix_glace = self.ui.prix_glace.text()

        if description != "" and prix_reliure != 0 and prix_couleur != 0 and prix_noir != "" and prix_glace != "" and prix_bristole != "":
            type = Typelivre()
            type.typeLivre = description
            type.prixPageNoir = int(prix_noir)
            type.prixPageCouleur = int(prix_couleur)
            type.prixReliure = int(prix_reliure)
            type.prixBristole = int(prix_bristole)
            type.prixPapierGlace = int(prix_glace)
            insert_new_type_livre(type)
            self.reset_form()
            self.show_alert_message("Le type a ete ajouter avec succes :)")
            return
        else:
            self.show_alert_message("Veuillez Remplir toutes les champs !!")
        return


    def show_alert_message(self, message: str):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Info")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)

        # Afficher le dialogue et récupérer la réponse de l'utilisateur
        msg_box.exec()

    def reset_form(self):
        self.ui.prix_reliure.clear()
        self.ui.prix_noir.clear()
        self.ui.prix_couleur.clear()
        self.ui.description.clear()
        self.ui.prix_glace.clear()
        self.ui.prix_bristole.clear()

    def load_type_selection(self):
        types = get_all_type_livre()
        self.ui.comboBox.clear()
        for type in types:
            self.ui.comboBox.addItem(type.typeLivre, type)
        return


    def manage_type_selection_changed(self, index):
        self.type_selection: Typelivre = self.ui.comboBox.itemData(index)
        self.ui.description.setText(self.type_selection.typeLivre)
        self.ui.prix_noir.setText(str(self.type_selection.prixPageNoir))
        self.ui.prix_reliure.setText(str(self.type_selection.prixReliure))
        self.ui.prix_couleur.setText(str(self.type_selection.prixPageCouleur))
        self.ui.prix_bristole.setText(str(self.type_selection.prixBristole))
        self.ui.prix_glace.setText(str(self.type_selection.prixPapierGlace))

    def modify_typelivre(self):
        type = get_type_livre_by_id(self.type_selection.numeroType)

        description = self.ui.description.text()
        prix_noir = self.ui.prix_noir.text()
        prix_couleur = self.ui.prix_couleur.text()
        prix_reliure = self.ui.prix_reliure.text()
        prix_bristole = self.ui.prix_bristole.text()
        prix_glace = self.ui.prix_glace.text()

        if description != "" and prix_reliure != 0 and prix_couleur != 0 and prix_noir != "":
            type.typeLivre = description
            type.prixPageNoir = int(prix_noir)
            type.prixPageCouleur = int(prix_couleur)
            type.prixReliure = int(prix_reliure)
            type.prixBristole = int(prix_bristole)
            type.prixPapierGlace = int(prix_glace)
            session.commit()
            self.show_alert_message("Le type a ete modifier avec succes :)")
            return
        else:
            self.show_alert_message("Veuillez Remplir toutes les champs !!")
        return

    def handle_delete_type(self):
        type = get_type_livre_by_id(self.type_selection.numeroType)
        session.delete(type)
        session.commit()
        self.show_alert_message("Le type a ete supprimer")
        self.ui.comboBox.setCurrentIndex(0)
