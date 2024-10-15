from PySide6.QtWidgets import QDialog

from models.model_class import Approvisionnement
from services.approvisionnement_service import insert_new_approvisionnement, update_appro
from views.auth.ui_approvisionnement import Ui_Dialog


class ApprovisionnementDialog(QDialog):
    def __init__(self, article: str = "", appro: Approvisionnement = None, modification: bool = False):
        super(ApprovisionnementDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.modification = modification
        self.appro = appro

        self.ui.submit.clicked.connect(lambda: self.submit_approvisionnement(article))
        self.ui.cancel.clicked.connect(lambda: self.close())

        self.load_appro_info(appro)

    def submit_approvisionnement(self, article):
        type = ""
        if self.ui.radioButton.isChecked():
            type = "Paquet"
        elif self.ui.radioButton_2.isChecked():
            type = "Boite"
        else:
            type = "Piece"
        appro = Approvisionnement()
        appro.numeroArticle = article
        appro.typeQuantite = type
        appro.quantiteLimite = int(self.ui.spinBox.text())
        insert_new_approvisionnement(appro) if not self.modification else update_appro(self.appro.numeroApprovisionnement, appro)

        self.close()

    def load_appro_info(self, appro: Approvisionnement):
        if appro:
            if appro.typeQuantite == "Paquet":
                self.ui.radioButton.setChecked(True)
            elif appro.typeQuantite == "Boite":
                self.ui.radioButton_2.setChecked(True)
            else:
                self.ui.radioButton_3.setChecked(True)
            self.ui.spinBox.setValue(appro.quantiteLimite)
        else:
            return