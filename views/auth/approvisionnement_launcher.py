from PySide6.QtWidgets import QDialog

from models.model_class import Approvisionnement
from services.approvisionnement_service import insert_new_approvisionnement
from views.auth.ui_approvisionnement import Ui_Dialog


class ApprovisionnementDialog(QDialog):
    def __init__(self, article: str):
        super(ApprovisionnementDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.submit.clicked.connect(lambda: self.submit_approvisionnement(article))
        self.ui.cancel.clicked.connect(lambda: self.close())

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
        insert_new_approvisionnement(appro)