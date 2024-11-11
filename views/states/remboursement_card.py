from Custom_Widgets.QCustomQDialog import QCustomQDialog
from PySide6.QtCore import QSize, QRect, Signal
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, \
    QSpinBox, QMessageBox

from models.model_class import Article


class RemboursementCard(QWidget):
    sous_total_changed = Signal(int, int)
    card_removed = Signal(str, int)

    def __init__(self, article: Article, numero_article: str, sous_total: int, quantite: int, type_index: int, parent=None):
        super().__init__(parent)
        self.setObjectName(article.numeroArticle)
        self.parent = parent
        self.article = article
        self.numero_article = numero_article
        self.sou_total = sous_total
        self.quantite = quantite  # Quantité par défaut
        self.type_quantite = "pieces"  # Type par défaut
        self.piece_maximum = 0
        self.paquet_maximum = 0
        self.boite_maximum = 0
        # Création du cadre (carte)

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 150))
        self.widget.setMaximumSize(QSize(250, 150))
        self.widget.setStyleSheet(u"""
                    #widget{
                        background-color: #fefeff;
                        border-radius: 10px;
                        border: 2px solid #f56614;
                    }
                """)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.leftFrame = QFrame(self.widget)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.leftFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.libelle_card = QLabel(f"{article.libelle}", self.leftFrame)
        self.libelle_card.setStyleSheet("color: #2596be; font-size: 18px;")
        self.libelle_card.setObjectName(u"libelle_card")

        self.verticalLayout.addWidget(self.libelle_card)

        self.price_card = QLabel(f"Prix unitaire: {article.prixUnitaire} Ar", self.leftFrame)
        self.price_card.setObjectName(u"price_card")

        self.verticalLayout.addWidget(self.price_card)

        self.total_card = QLabel(f"Sous-total = {self.sou_total} Ar", self.leftFrame)
        self.total_card.setStyleSheet("padding: 2px; border-radius: 2px; background-color: #ffe4bd; background-opacity: 0.4;")
        self.total_card.setObjectName(u"total_card")

        self.verticalLayout.addWidget(self.total_card)

        self.horizontalLayout_2.addWidget(self.leftFrame)

        self.rightFrame = QFrame(self.widget)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        # Bouton de suppression (croix) en haut à droite
        self.btn_remove = QPushButton("❌", self.rightFrame)
        self.btn_remove.setFixedSize(25, 25)
        self.btn_remove.setStyleSheet("padding: 3px; background-color: #ffe4bd; border-radius: 3px;")
        self.btn_remove.clicked.connect(self.remove_card)  # Connecter au slot pour supprimer la carte
        self.verticalLayout_2.addWidget(self.btn_remove)

        # Champ pour entrer la quantité, uniquement numérique
        self.line_edit_quantite = QSpinBox(self.rightFrame)
        self.line_edit_quantite.setMinimum(1)
        self.line_edit_quantite.setValue(self.quantite)

        # self.line_edit_quantite.setValidator(QIntValidator(0, article.pieceEnStock))  # Limite numérique (ex: entre 0 et 10000)
        # self.line_edit_quantite.setPlaceholderText("Entrez la quantité")
        self.line_edit_quantite.setStyleSheet("padding: 3px; border: 1px solid #000; border-radius: 3px;")
        self.verticalLayout_2.addWidget(self.line_edit_quantite)



        self.comboBox = QComboBox(self.rightFrame)
        self.comboBox.addItem("pieces")
        self.comboBox.addItem("pacquets") if article.typeConteneur == "Paquet" else self.comboBox.addItem("boites")
        self.comboBox.setObjectName(u"comboBox")
        if article.typeConteneur == "Paquet":
            if type_index == 0 :
                self.piece_maximum = article.pieceEnStock + quantite
                self.paquet_maximum = article.packetEnStock + (quantite // article.pieceParPaquet)
            else:
                self.piece_maximum = article.pieceEnStock + quantite * article.pieceParPaquet
                self.paquet_maximum = article.packetEnStock + quantite
        else:
            if type_index == 0 :
                self.piece_maximum = article.pieceEnStock + quantite
                self.boite_maximum = article.boiteEnStock + (quantite // article.pieceParBoite)
            else:
                self.piece_maximum = article.pieceEnStock + quantite * article.pieceParBoite
                self.paquet_maximum = article.boiteEnStock + quantite

        self.verticalLayout_2.addWidget(self.comboBox)

        self.horizontalLayout_2.addWidget(self.rightFrame)

        self.horizontalLayout.addWidget(self.widget)

        # Connexion des signaux aux slots pour surveiller les changements
        self.line_edit_quantite.textChanged.connect(self.update_sous_total)
        self.comboBox.currentIndexChanged.connect(self.update_sous_total)

        #Labelle error
        self.labele_stock_error = QLabel(f"Stock insuffisant pour cette quantite en {self.type_quantite}")
        self.labele_stock_error.setStyleSheet("color: #2596be; font-size: 18px;")

    def update_sous_total(self):
        try:
            quantite = int(self.line_edit_quantite.text())
        except ValueError:
            quantite = 0  # Si la quantité est vide ou invalide

        type_quantite = self.comboBox.currentText()
        if type_quantite == "pacquets":
            if quantite <= self.paquet_maximum:
                ancien_sous_total = self.sou_total
                self.sou_total = quantite * self.article.prixUnitaire * self.article.pieceParPaquet
                self.sous_total_changed.emit(ancien_sous_total, self.sou_total)
            else:
                self.labele_stock_error.setText("Stock insuffisant pour cette quantite en packet")
                self.show_stock_unavailable("packets")

        elif type_quantite == "boites":
            if quantite <= self.boite_maximum:
                ancien_sous_total = self.sou_total
                self.sou_total = quantite * self.article.prixUnitaire * self.article.pieceParBoite
                self.sous_total_changed.emit(ancien_sous_total, self.sou_total)
            else:
                self.labele_stock_error.setText("Stock insuffisant pour cette quantite en boites")
                self.show_stock_unavailable("boites")

        else:
            if quantite <= self.piece_maximum:
                ancien_sous_total = self.sou_total
                self.sou_total = quantite * self.article.prixUnitaire
                self.sous_total_changed.emit(ancien_sous_total, self.sou_total)
            else:
                self.labele_stock_error.setText("Stock insuffisant pour cette quantite en pieces")
                self.show_stock_unavailable("pieces")

        # Calcul du sous-total (exemple simple, à ajuster selon les règles métier)

        self.total_card.setText(f"Sous-total = {self.sou_total} Ar")


    def show_stock_unavailable(self, type: str):
        stock_error_dialog = QCustomQDialog(
            title="Stock Insuffisant !!",
            description="Voulez vous voir l'etat de stock ?",
            padding=20,
            margin=60,
            # yesButtonIcon=my_yes_icon,
            # cancelButtonIcon=my_cancel_icon,
            yesButtonText="Voir stock",
            cancelButtonText="Annuler",
            animationDuration=500,
            showYesButton=True,
            showCancelButton=True,
            setModal=True,
            frameless=True,
            windowMovable=True,
            # showForm=myFormWidget,
            # display a ui form inside the dialog box ie importing your form(from ui_form import myFormWidget)
            # to access the widgets inside your form (custom_dialog.shownForm.myWidgetName)
            parent=self.parent,
            addWidget=self.labele_stock_error  # append another widget or widget container to the dialog
        )

        stock_error_dialog.show()

        if type == "packets":
            stock_error_dialog.accepted.connect(
                lambda: self.line_edit_quantite.setValue(self.paquet_maximum))  # yes button clicked
            stock_error_dialog.rejected.connect(
                lambda: self.line_edit_quantite.setValue(self.paquet_maximum))  # cancel button clicked
        elif type == "boites":
            stock_error_dialog.accepted.connect(
                lambda: self.line_edit_quantite.setValue(self.boite_maximum))  # yes button clicked
            stock_error_dialog.rejected.connect(
                lambda: self.line_edit_quantite.setValue(self.boite_maximum))  # cancel button clicked
        else:
            stock_error_dialog.accepted.connect(
                lambda: self.line_edit_quantite.setValue(self.piece_maximum))  # yes button clicked
            stock_error_dialog.rejected.connect(
                lambda: self.line_edit_quantite.setValue(self.piece_maximum))  # cancel button clicked,

    def remove_card(self):
        response = QMessageBox.question(self.parent, "Supprimer la carte", f"Etes vous sur de supprimer '{self.article.libelle}' de la commande ? Cela est ireversible !")
        if response == QMessageBox.Yes:
            """Supprime la carte de l'affichage."""
            # Émet un signal pour notifier la suppression de la carte
            self.card_removed.emit(self.article.numeroArticle, self.sou_total)
            # Supprime le widget lui-même
            self.setParent(None)
            self.deleteLater()
        else:
            print(response)
            return
