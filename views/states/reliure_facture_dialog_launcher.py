from PySide6.QtGui import QPageLayout, QPainter, QPdfWriter, QPageSize, QPixmap
from PySide6.QtPrintSupport import QPrinter, QPrinterInfo, QPrintDialog
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QFileDialog
from num2words import num2words

from models.model_class import Reliure
from services.client_service import get_client_by_id
from services.reliure_service import get_total_for_reliure, get_type_livre_by_id
from views.states.facture_reliure_dialog_ui import Ui_Dialog

import os


class FactureReliureDialog(QDialog):
    def __init__(self, reliure: Reliure):
        super(FactureReliureDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.tableWidget.setColumnWidth(0, 300)
        self.ui.tableWidget.setColumnWidth(1, 120)
        self.ui.tableWidget.setColumnWidth(2, 120)
        self.ui.tableWidget.setColumnWidth(3, 140)

        self.ui.tableWidget.setRowHeight(0, 30)
        self.ui.tableWidget.setRowHeight(1, 30)
        self.ui.tableWidget.setRowHeight(2, 30)
        self.ui.tableWidget.setRowHeight(5, 30)
        self.ui.tableWidget.setRowHeight(3, 30)
        self.ui.tableWidget.setRowHeight(4, 30)

        self.reliure = reliure
        self.total_a_payer = get_total_for_reliure(self.reliure.numeroReliure)

        self.load_header_data_facture()
        self.load_facture_detail_table()


    def load_header_data_facture(self):
        self.ui.numero_facture.setText(str(self.reliure.numeroReliure))
        self.ui.date_facture.setText(f"{self.reliure.dateCommande}")
        self.ui.statut_facture.setText("Livré") if self.reliure.statutLivrer else self.ui.statut_facture.setText("Non Livré")

        total_a_payer = self.total_a_payer
        self.ui.total.setText(f"{total_a_payer} Ar")

        client = get_client_by_id(self.reliure.numeroClient)
        self.ui.nom_client.setText(client.nom)
        self.ui.numero_client.setText(client.telephone)
        self.ui.adresse_client.setText(client.adresse)

        total_lettre = num2words(total_a_payer, lang="fr")
        self.ui.total_lettre.setText(total_lettre)

    def load_facture_detail_table(self):
        self.ui.tableWidget.setRowCount(0)

        type = get_type_livre_by_id(self.reliure.numeroType)
        page_noir = type.prixPageNoir * self.reliure.nombrePageNoir
        page_couleur = type.prixPageCouleur * self.reliure.nombrePageCouleur

        self.ui.tableWidget.insertRow(0)
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("Page en Noir et Blanc"))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(f"{self.reliure.nombrePageNoir}"))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(str(type.prixPageNoir)))
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem(f"{page_noir} Ar"))

        self.ui.tableWidget.insertRow(1)
        self.ui.tableWidget.setItem(1, 0, QTableWidgetItem("Page en Couleur"))
        self.ui.tableWidget.setItem(1, 1, QTableWidgetItem(str(self.reliure.nombrePageCouleur)))
        self.ui.tableWidget.setItem(1, 2, QTableWidgetItem(str(type.prixPageCouleur)))
        self.ui.tableWidget.setItem(1, 3, QTableWidgetItem(f"{page_couleur} Ar"))

        couverture = "Bristole" if self.reliure.typeCouverture else "Glacé"
        prixCouverture = type.prixBristole if self.reliure.typeCouverture else type.prixPapierGlace
        self.ui.tableWidget.insertRow(2)
        self.ui.tableWidget.setItem(2, 0, QTableWidgetItem(f"Couverture Papier {couverture}"))
        self.ui.tableWidget.setItem(2, 1, QTableWidgetItem(str(self.reliure.nombreCouverture)))
        self.ui.tableWidget.setItem(2, 2, QTableWidgetItem(str(prixCouverture)))
        self.ui.tableWidget.setItem(2, 3, QTableWidgetItem(f"{self.reliure.nombreCouverture * prixCouverture} Ar"))

        self.ui.tableWidget.insertRow(3)
        self.ui.tableWidget.setItem(3, 0, QTableWidgetItem(f"Impression {type.typeLivre}"))
        self.ui.tableWidget.setItem(3, 1, QTableWidgetItem(str("Neant")))
        self.ui.tableWidget.setItem(3, 2, QTableWidgetItem(str(type.prixReliure)))
        self.ui.tableWidget.setItem(3, 3, QTableWidgetItem(f"{type.prixReliure} Ar"))

        self.ui.tableWidget.insertRow(4)
        self.ui.tableWidget.setSpan(4, 0, 1, 3)
        self.ui.tableWidget.setItem(4, 0, QTableWidgetItem("Sous-Total"))
        self.ui.tableWidget.setItem(4, 3, QTableWidgetItem(f"{page_noir + page_couleur + type.prixReliure + prixCouverture * self.reliure.nombreCouverture} Ar"))


        self.ui.tableWidget.insertRow(5)
        self.ui.tableWidget.setSpan(5, 0, 1, 3)
        self.ui.tableWidget.setItem(5, 0, QTableWidgetItem("Nombre d'Exemplaire"))
        self.ui.tableWidget.setItem(5, 3, QTableWidgetItem(f"{self.reliure.nombreExemplaire} "))

        self.ui.tableWidget.insertRow(6)
        self.ui.tableWidget.setSpan(6, 0, 1, 3)
        self.ui.tableWidget.setItem(6, 0, QTableWidgetItem("TOTAL"))
        self.ui.tableWidget.setItem(6, 3, QTableWidgetItem(f"{self.total_a_payer} Ar"))


    def print_or_save_invoice_with_double_copy(self):
        # Configuration de l'imprimante en mode paysage
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPageOrientation(QPageLayout.Landscape)

        # Vérification de la disponibilité de l'imprimante par son nom
        printer_info = QPrinterInfo.defaultPrinter() if not self.default_printer else QPrinterInfo.printerInfo(
            self.default_printer)

        if printer_info.isNull():
            # Si aucune imprimante valide n'est trouvée, créer un PDF
            self.export_to_pdf()
            QMessageBox.information(self, "PDF créé", "La facture double a été enregistrée en PDF.")
        else:
            # Si une imprimante valide est trouvée, l'utiliser pour imprimer
            printer.setPrinterName(printer_info.printerName())
            self.print_double_invoice_to_printer(printer)

    def print_double_invoice_to_printer(self, printer):
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QPrintDialog.Accepted:
            painter = QPainter(printer)
            self.draw_double_invoice(painter)
            painter.end()

    def save_double_invoice_to_pdf(self):
        facture_path = os.path.join(os.path.expanduser("~"), "Documents", f"facture-{self.facture.numeroFacture}.pdf")
        pdf_writer = QPdfWriter(facture_path)
        pdf_writer.setPageSize(QPageSize(QPageSize.A4))
        pdf_writer.setResolution(300)  # Résolution de haute qualité
        pdf_writer.setPageOrientation(QPageLayout.Landscape)
        painter = QPainter(pdf_writer)
        self.draw_double_invoice(painter)
        painter.end()

    def export_to_pdf(self):
        save_path = QFileDialog.getExistingDirectory(
            self,
            "Enregistrer la facture en PDF sous",
        )
        if save_path:
            try:
                with open(f"{save_path}/reliure_facture_{str(self.reliure.numeroFacture)}.pdf", 'w') as f:
                    print(f.name)
                    pass
            except Exception as e:
                print(f"exception: {e}")
            facture_path = os.path.join(save_path, f"reliure_facture_{str(self.reliure.numeroFacture)}.pdf").replace("\\", '/')
            print(facture_path)
            pdf_writer = QPdfWriter(facture_path)
            pdf_writer.setPageSize(QPageSize(QPageSize.A4))
            pdf_writer.setResolution(300)  # Résolution de haute qualité
            pdf_writer.setPageOrientation(QPageLayout.Landscape)

            painter = QPainter(pdf_writer)
            print(painter.isActive())
            self.draw_invoice_for_pdf(painter)
            painter.end()
            QMessageBox.information(self, "Facture de reliure", f"Le facture a ete enregistrer dans : {facture_path}")
        else:
            print("Erreur de path")

    def draw_double_invoice(self, painter):
        # Capture du QTableWidget sous forme d'image pour insérer dans chaque moitié
        table_image = QPixmap(self.ui.tableWidget.size())
        header_image = QPixmap(self.ui.header_frame.size())
        footer_image = QPixmap(self.ui.footer_frame.size())
        self.ui.header_frame.render(header_image)
        header_image = header_image.scaled(painter.device().width() // 2 - 100, painter.device().height()//5)
        self.ui.tableWidget.render(table_image)
        table_image = table_image.scaled(painter.device().width() // 2 - 100, painter.device().height()//2)
        self.ui.footer_frame.render(footer_image)
        footer_image = footer_image.scaled(painter.device().width() // 2 - 100, painter.device().height()//5)

        # Dimensions de la page
        page_width = painter.device().width()
        page_height = painter.device().height()

        # Dessiner la première copie à gauche
        # painter.setFont(self.headerFont)
        painter.drawPixmap(50, 50, header_image)
        painter.drawPixmap(50, 1070, table_image)  # Positionner le tableau
        # painter.setFont(self.footerFont)
        painter.drawPixmap(50, 3600, footer_image)  # Ajustez la position pour le bas de la facture
        # painter.drawText(400, 600, "Prix total: 1000€")

        # Dessiner la seconde copie à droite
        offset_x = page_width // 2
        # painter.setFont(self.headerFont)
        painter.drawPixmap(50 + offset_x, 50, header_image)
        painter.drawPixmap(50 + offset_x, 1070, table_image)  # Tableau à droite
        # painter.setFont(self.footerFont)
        painter.drawPixmap(50 + offset_x, 3600, footer_image)
        # painter.drawText(400 + offset_x, 600, "Prix total: 1000€")

        # Libérer les ressources du `painter`
        painter.end()

    def draw_invoice_for_pdf(self, painter):
        # Capture du QTableWidget sous forme d'image pour insérer dans chaque moitié
        table_image = QPixmap(self.ui.tableWidget.size())
        header_image = QPixmap(self.ui.header_frame.size())
        footer_image = QPixmap(self.ui.footer_frame.size())
        self.ui.header_frame.render(header_image)
        header_image = header_image.scaled(painter.device().width() // 2 - 100, painter.device().height() // 5)
        self.ui.tableWidget.render(table_image)
        table_image = table_image.scaled(painter.device().width() // 2 - 100, painter.device().height() // 2)
        self.ui.footer_frame.render(footer_image)
        footer_image = footer_image.scaled(painter.device().width() // 2 - 100, painter.device().height() // 5)

        # Dimensions de la page
        page_width = painter.device().width()
        page_height = painter.device().height()

        # Dessiner la première copie à gauche
        # painter.setFont(self.headerFont)
        painter.drawPixmap(50, 50, header_image)
        painter.drawPixmap(50, 550, table_image)  # Positionner le tableau
        # painter.setFont(self.footerFont)
        painter.drawPixmap(50, 1800, footer_image)  # Ajustez la position pour le bas de la facture
        # painter.drawText(400, 600, "Prix total: 1000€")

        # Dessiner la seconde copie à droite
        offset_x = page_width // 2
        # painter.setFont(self.headerFont)
        painter.drawPixmap(50 + offset_x, 50, header_image)
        painter.drawPixmap(50 + offset_x, 550, table_image)  # Tableau à droite
        # painter.setFont(self.footerFont)
        painter.drawPixmap(50 + offset_x, 1800, footer_image)
        # painter.drawText(400 + offset_x, 600, "Prix total: 1000€")

        painter.end()
