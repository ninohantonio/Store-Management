import sys

from Custom_Widgets import *
from Custom_Widgets import QMainWindow
from Custom_Widgets.QCustomQDialog import QCustomQDialog

from controllers.article_controller import get_date_to_string
from models.model_class import Article
from services.article_service import verify_article_by_id, get_article_by_id, insert_new_article, get_article_by_name
from views.auth.ui_main_login import Ui_MainWindow

from PySide6.QtWidgets import QApplication

from views.states.stock_state import refresh_search_view_value


class AdminWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AdminWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles=["views/auth/style.json"])
        self.ui.resetBtn.clicked.connect(self.reset_form)
        if self.ui.mainNavigationScreen.currentIndex() == 0:
            self.ui.search_field.returnPressed.connect(self.manage_search_value_input)
            self.ui.search_field.textChanged.connect(self.manage_search_value_input)
            self.ui.search_field.setFocus()
            pass

        self.ui.radioButton.clicked.connect(self.manage_radio_checked)
        self.ui.radioButton_2.clicked.connect(self.manage_radio_checked)

        self.numero_to_insert = ""
        self.alert_label = QLabel()

    def manage_search_value_input(self):
        search_value = self.ui.search_field.text()
        if len(search_value) == 13 and search_value.isnumeric():
            self.print_search_value()
        else:
            self.refresh_search_view()

    def print_search_value(self):
        search_value = self.ui.search_field.text()

        # Vérifier si le champ n'est pas vide avant de continuer
        if search_value.strip() == "":
            return  # Ne rien faire si le champ est vide

        # Effacer le texte pour préparer le prochain scan
        self.ui.search_field.clear()
        self.numero_to_insert = search_value
        print(f"Article existe = {verify_article_by_id(search_value)}")
        if verify_article_by_id(search_value):
            self.show_detail_article(search_value)
            self.ui.submitBtn.clicked.disconnect()
            self.ui.submitBtn.clicked.connect(self.update_article)
        else:
            self.show_message_to_add()
            self.ui.submitBtn.clicked.disconnect()
            self.ui.submitBtn.clicked.connect(self.insert_new_article)


    def manage_radio_checked(self):
        if self.ui.radioButton.isChecked():
            self.ui.label_6.setText("Nombre de packets")
            self.ui.label_2.setText("Pieces dans un packet")
        else:
            self.ui.label_6.setText("Nombre de boites")
            self.ui.label_2.setText("Pieces dans une boite")

    def show_detail_article(self, numeroArticle):
        article = get_article_by_id(numeroArticle)

        ##   ET ALL DATA FOR DETAIL
        self.ui.article_name.setText(article.libelle)
        self.ui.prixUnitaire_detail.setText(str(article.prixUnitaire))
        self.ui.pieceParConteneur_detail.setText(str(article.pieceParPaquet)) if article.typeConteneur == "Paquet" else self.ui.pieceParConteneur_detail.setText(str(article.pieceParBoite))
        self.ui.conteneur_detail.setText(article.typeConteneur)
        self.ui.nbConteneur_detail.setText(str(article.packetEnStock)) if article.typeConteneur == "Paquet" else self.ui.nbConteneur_detail.setText(str(article.boiteEnStock))
        self.ui.piece_detail.setText(str(article.pieceEnStock))
        self.ui.dateEntrer_detail.setText(str(article.dateEntrer))
        self.ui.description_detail.setText(article.description)


    def show_message_to_add(self):
        self.ui.article_name.setText("Article Non Trouver")


    def insert_new_article(self):
        print("submit")


        # print(f"numero = {article.numeroArticle}")
        # print(f"type = {article.typeConteneur}")
        # print(f"par packet = {article.pieceParPaquet}")
        # print(article.pieceParBoite)
        # print(article.pieceEnStock)
        # print(article.dateEntrer)
        stock_error_dialog = QCustomQDialog(
            title="Validation de l'ajout de l'article !",
            description="Voulez vous ajouter cette nouvelle article ?",
            padding=20,
            margin=60,
            yesButtonText="Ajouter",
            cancelButtonText="Annuler",
            animationDuration=500,
            showYesButton=True,
            showCancelButton=True,
            setModal=True,
            frameless=True,
            windowMovable=True,
            parent=self,
            # addWidget=self.labele_stock_error  # append another widget or widget container to the dialog
        )

        stock_error_dialog.show()
        stock_error_dialog.accepted.connect(lambda : self.submit_insert_article())  # yes button clicked
        stock_error_dialog.rejected.connect(
            lambda: stock_error_dialog.close())  # cancel button clicked
        pass

    def submit_insert_article(self):
        nbPacket = 0
        pieceParPaquet = 0
        nbBoite = 0
        pieceParBoite = 0
        pieceEnStock = 0
        if self.ui.radioButton.isChecked():
            nbPacket = int(self.ui.nbConteneur_form.text())
            pieceParPaquet = int(self.ui.pieceParConteneur.text())
            pieceEnStock = int(self.ui.pieceSupplement_form.text()) + (
                        int(self.ui.nbConteneur_form.text()) * pieceParPaquet)

        else:
            nbBoite = int(self.ui.nbConteneur_form.text())
            pieceParBoite = int(self.ui.pieceParConteneur.text())
            pieceEnStock = int(self.ui.pieceSupplement_form.text()) + (
                    int(self.ui.nbConteneur_form.text()) * pieceParBoite)

        article = Article(
            libelle=self.ui.libelle_form.text(),
            prixUnitaire=self.ui.prix_form.text(),
            typeConteneur=self.ui.radioButton.text() if self.ui.radioButton.isChecked() else self.ui.radioButton_2.text(),
            pieceParPaquet=pieceParPaquet,
            pieceParBoite=pieceParBoite,
            pieceEnStock=pieceEnStock,
            packetEnStock=nbPacket,
            boiteEnStock=nbBoite,
            description=self.ui.description_form.text(),
            dateEntrer=get_date_to_string(),
            numeroArticle=self.numero_to_insert,
        )

        insert_new_article(article)
        print("submit success")
        self.reset_form()
        self.show_dialog_success()



    def update_article(self):
        print("update")
        pass

    def reset_form(self):
        self.ui.nbConteneur_form.clear()
        self.ui.description_form.clear()
        self.ui.prix_form.clear()
        self.ui.libelle_form.clear()
        self.ui.pieceSupplement_form.clear()
        self.ui.pieceParConteneur.clear()
        print("reset")

    def show_dialog_success(self):

        self.alert_label.setText("L'article a ete bien inserer :)")
        self.alert_label.setStyleSheet("color:#02c141; font-size: 18px;")
        stock_error_dialog = QCustomQDialog(
            # title="Validation de l'ajout de l'article !",
            # description="Voulez vous ajouter cette nouvelle article ?",
            padding=20,
            margin=60,
            yesButtonText="Ajouter",
            cancelButtonText="OK",
            animationDuration=500,
            showYesButton=False,
            showCancelButton=True,
            setModal=True,
            frameless=True,
            windowMovable=True,
            parent=self,
            addWidget=self.alert_label  # append another widget or widget container to the dialog
        )

        stock_error_dialog.show()
        stock_error_dialog.accepted.connect(lambda : stock_error_dialog.close())  # yes button clicked

    def refresh_search_view(self):
        libelle = self.ui.search_field.text()
        articles = get_article_by_name(libelle)
        refresh_search_view_value(self.ui.search_view, articles)
