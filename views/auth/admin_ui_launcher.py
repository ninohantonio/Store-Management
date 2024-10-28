import sys
from datetime import datetime, date

from Custom_Widgets import *
from Custom_Widgets import QMainWindow
from Custom_Widgets.QCustomQDialog import QCustomQDialog
from PySide6.QtGui import QIntValidator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


from matplotlib.figure import Figure

from controllers.article_controller import get_date_to_string
from models.model_class import Article, Approvisionnement
from services.approvisionnement_service import get_appro_by_article_id
from services.article_service import verify_article_by_id, get_article_by_id, insert_new_article, get_article_by_name, \
    update_article
from services.facture_service import get_total_facture_group_by_date, search_factures_by_date, get_total_for_facture, \
    get_facture_by_id
from services.reliure_service import get_total_reliure_group_by_date, get_reliure_by_date
from views.auth.approvisionnement_launcher import ApprovisionnementDialog
from views.auth.ui_admin_window import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMessageBox

from views.states.facture_dialog_launcher import FactureDialog
from views.states.stock_state import refresh_search_view_value, refresh_facture_table_data, refresh_reliure_table_data


class AdminWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AdminWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles=["views/auth/style.json"])

        self.showMaximized()
        self.ui.resetBtn.clicked.connect(self.reset_form)
        if self.ui.mainNavigationScreen.currentIndex() == 0:
            self.ui.search_field.returnPressed.connect(self.manage_search_value_input)
            self.ui.search_field.textChanged.connect(self.manage_search_value_input)
            self.ui.search_field.setFocus()
            pass

        self.numero_is_valid = False

        self.ui.mainNavigationScreen.currentChanged.connect(self.manage_navigation)

        self.ui.radioButton.clicked.connect(self.manage_radio_checked)
        self.ui.radioButton_2.clicked.connect(self.manage_radio_checked)

        self.ui.search_view.cellDoubleClicked.connect(self.print_search_view_item_clicked)
        self.ui.search_view.setColumnHidden(1, True)

        self.numero_to_insert = None
        self.numero_article_to_modify = None
        self.alert_label = QLabel()

        self.ui.prix_form.setValidator(QIntValidator(0, 9999999))
        self.ui.nbConteneur_form.setValidator(QIntValidator(0, 999))
        self.ui.pieceParConteneur.setValidator(QIntValidator(0, 9999))
        self.ui.pieceSupplement_form.setValidator(QIntValidator(0, 9999))

        self.ui.appro_detail.setVisible(False)
        self.ui.appro_detail.clicked.connect(lambda : self.show_appro_dialog(self.numero_article_to_modify))

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.reliure_figure = Figure()
        self.reliure_canvas = FigureCanvas(self.reliure_figure)

        self.ui.facture_tableWidget.cellDoubleClicked.connect(self.manage_double_click_facture_item)

        self.ui.chartContainer.addWidget(self.canvas)
        self.ui.reliureCourbe.addWidget(self.reliure_canvas)
        self.load_reliure_line_chart()
        self.load_line_chart_graphics()
        self.load_facture_table_list()
        self.load_reliure_table_list()

    def manage_navigation(self, index):
        if index == 1:
            self.ui.search_field.returnPressed.disconnect()
        elif index == 0:
            self.ui.search_field.returnPressed.connect(self.manage_search_value_input)
            self.ui.search_field.textChanged.connect(self.manage_search_value_input)
            self.ui.search_field.setFocus()
        elif index == 2:
            self.ui.search_field.returnPressed.disconnect()


    def manage_search_value_input(self):
        search_value = self.ui.search_field.text()
        if len(search_value) == 13 and search_value.isdigit():
            self.print_search_value()
            return True
        else:
            self.refresh_search_view()
            return False

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
            self.ui.appro_detail.setVisible(True)
            self.ui.submitBtn.clicked.disconnect()
            self.ui.submitBtn.clicked.connect(self.update_article)
        else:
            self.show_message_to_add()
            self.ui.appro_detail.setVisible(False)
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
        self.numero_article_to_modify = numeroArticle

        ##   ET ALL DATA FOR DETAIL
        self.ui.article_name.setText(article.libelle)
        self.ui.prixUnitaire_detail.setText(str(article.prixUnitaire))
        self.ui.pieceParConteneur_detail.setText(str(article.pieceParPaquet)) if article.typeConteneur == "Paquet" else self.ui.pieceParConteneur_detail.setText(str(article.pieceParBoite))
        self.ui.conteneur_detail.setText(article.typeConteneur)
        self.ui.nbConteneur_detail.setText(str(article.packetEnStock)) if article.typeConteneur == "Paquet" else self.ui.nbConteneur_detail.setText(str(article.boiteEnStock))
        self.ui.piece_detail.setText(str(article.pieceEnStock))
        self.ui.dateEntrer_detail.setText(str(article.dateEntrer))
        self.ui.description_detail.setText(article.description)

        ##  SET ALL DATA FOR FORM
        self.ui.libelle_form.setText(article.libelle)
        self.ui.prix_form.setText(str(article.prixUnitaire))
        self.ui.pieceParConteneur.setText(
            str(article.pieceParPaquet)) if article.typeConteneur == "Paquet" else self.ui.pieceParConteneur_detail.setText(
            str(article.pieceParBoite))
        self.ui.radioButton.setChecked(True) if article.typeConteneur == "Paquet" else self.ui.radioButton_2.setChecked(True)
        self.ui.nbConteneur_form.setText(
            str(article.packetEnStock)) if article.typeConteneur == "Paquet" else self.ui.nbConteneur_detail.setText(
            str(article.boiteEnStock))
        self.manage_radio_checked()
        self.ui.description_form.setText(article.description)
        self.ui.pieceSupplement_form.setText(str(article.pieceEnStock - int(self.ui.nbConteneur_form.text()) * int(self.ui.pieceParConteneur.text())))

        self.ui.submitBtn.clicked.disconnect()
        self.ui.submitBtn.clicked.connect(self.update_article)
        pass

    def show_message_to_add(self):
        self.ui.article_name.setText("Article Non Trouver")

    def controll_provided_data(self) -> bool:
        if self.ui.prix_form.text().strip() != "" and self.ui.description_form.text().strip() != "" and self.ui.nbConteneur_form.text().strip() != "" and self.ui.pieceSupplement_form.text().strip() != "" and self.ui.pieceParConteneur.text().strip() != "":
            return True
        return False

    def insert_new_article(self):
        print("submit")

        if not self.numero_to_insert.isdigit() and not len(self.numero_to_insert) == 13:
            self.show_info_message("Veuillez scanner ou renseigner un numero de serie d'article valide pour inserer")
            return
        elif not self.controll_provided_data():
            self.show_info_message("Veuillez remplir toutes les champs!!")
            return


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
        self.appro_dialog = ApprovisionnementDialog(article)
        self.appro_dialog.show()
        self.reset_form()
        self.show_dialog_success()



    def update_article(self):
        print("update")

        if self.numero_article_to_modify is None:
            self.show_info_message("Veuillez selectionner ou scanner un article!!")
            return

        elif not self.controll_provided_data():
            self.show_info_message("Veuillez remplir toutes les champs !!")
            return


        stock_error_dialog = QCustomQDialog(
            title="Validation de la modification de l'article !",
            description="Voulez vous enregistrer ce(s) modification(s) ?",
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
        stock_error_dialog.accepted.connect(lambda: self.submit_update_article())  # yes button clicked
        stock_error_dialog.rejected.connect(
            lambda: stock_error_dialog.close())  # cancel button clicked

        pass

    def submit_update_article(self):
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
        )

        update_article(self.numero_article_to_modify, article)
        print("submit success")
        self.reset_form()
        self.show_dialog_success()

    def reset_form(self):
        self.ui.nbConteneur_form.clear()
        self.ui.description_form.clear()
        self.ui.prix_form.clear()
        self.ui.libelle_form.clear()
        self.ui.pieceSupplement_form.clear()
        self.ui.pieceParConteneur.clear()

        self.ui.article_name.setText("Nom de l'article")
        self.ui.prixUnitaire_detail.clear()
        self.ui.pieceParConteneur_detail.clear()
        self.ui.conteneur_detail.clear()
        self.ui.nbConteneur_detail.clear()
        self.ui.piece_detail.clear()
        self.ui.dateEntrer_detail.clear()
        self.ui.description_detail.clear()
        self.numero_article_to_modify = None
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

    def print_search_view_item_clicked(self, row, column):

        numero = self.ui.search_view.item(row, 1).text()
        self.show_detail_article(numero)
        print(f"numero = {numero}")
        return


    def show_info_message(self, message: str):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Info")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)

        # Afficher le dialogue et récupérer la réponse de l'utilisateur
        msg_box.exec()


    def show_appro_dialog(self, article_id):
        appro = get_appro_by_article_id(article_id)
        if appro:
            self.appro_dialog = ApprovisionnementDialog(article=article_id, appro=appro, modification=True)
            self.appro_dialog.show()

    def load_line_chart_graphics(self):
        ventes_par_jour = get_total_facture_group_by_date()

        # Trier les dates pour un affichage correct
        dates = sorted(ventes_par_jour.keys())
        montants = [ventes_par_jour[date] for date in dates]

        # Tracer le graphique
        ax = self.figure.add_subplot(111)
        ax.clear()  # Nettoyer l'axe avant de dessiner

        ax.plot(dates, montants, marker='o', linestyle='-', color='b', label='Ventes')
        ax.set_xlabel('Date')
        ax.set_ylabel('Montant Total (Ar)')
        # ax.set_title('Progression des Ventes Journalières')
        ax.legend()

        total = 0
        # Ajouter les annotations des montants
        for date, montant in zip(dates, montants):
            ax.annotate(f"{montant}Ar",  # Texte à afficher
                        (date, montant),  # Coordonnées du point
                        textcoords="offset points",  # Décalage par rapport au point
                        xytext=(0, 5),  # Décalage vertical
                        ha='center',  # Alignement horizontal
                        fontsize=10,  # Taille de la police
                        color='#af0000')

            total += montant

        self.ui.vente_mois.setText(f"{total} Ar")
        # Rotation des labels de date pour une meilleure lisibilité
        self.figure.autofmt_xdate()

        self.ui.chartContainer.update()
        # Mettre à jour le canvas
        self.canvas.draw()

    def load_facture_table_list(self):
        date_now = datetime.now()

        factures = search_factures_by_date(date_now)
        refresh_facture_table_data(self.ui.facture_tableWidget, factures)

        total = 0
        for facture in factures:
            total += get_total_for_facture(facture.numeroFacture)

        self.ui.vente_jour.setText(f"{total} Ar")
        return

    def manage_double_click_facture_item(self, row, column):
        numero = self.ui.facture_tableWidget.item(row, 0).text()
        facture = get_facture_by_id(int(numero))

        self.facture_dialog = FactureDialog(facture, can_change_state=True)
        self.facture_dialog.show()
        return


    def load_reliure_line_chart(self):
        reliures_par_jours = get_total_reliure_group_by_date()

        dates = sorted(reliures_par_jours.keys())
        montants = [reliures_par_jours[date] for date in dates]

        # Tracer le graphique
        ax = self.figure.add_subplot(111)
        ax.clear()  # Nettoyer l'axe avant de dessiner

        ax.plot(dates, montants, marker='o', linestyle='-', color='b', label='Commandes')
        ax.set_xlabel('Date')
        ax.set_ylabel('Montant Total (Ar)')
        # ax.set_title('Progression des Ventes Journalières')
        ax.legend()

        total = 0
        # Ajouter les annotations des montants
        for date, montant in zip(dates, montants):
            ax.annotate(f"{montant}Ar",  # Texte à afficher
                        (date, montant),  # Coordonnées du point
                        textcoords="offset points",  # Décalage par rapport au point
                        xytext=(0, 5),  # Décalage vertical
                        ha='center',  # Alignement horizontal
                        fontsize=10,  # Taille de la police
                        color='#af0000')

            total += montant

            # Rotation des labels de date pour une meilleure lisibilité
            self.reliure_figure.autofmt_xdate()

            self.ui.reliureCourbe.update()

            self.reliure_canvas.draw()
        return

    def load_reliure_table_list(self):
        reliures = get_reliure_by_date(datetime.now())
        refresh_reliure_table_data(self.ui.reliureTableWidget, reliures)
        return



