from PySide6.QtCore import Qt
from PySide6.QtGui import QPdfWriter, QPageLayout, QPageSize, QPainter, QPixmap
from PySide6.QtPrintSupport import QPrinter, QPrintDialog, QPrinterInfo
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QFileDialog
from num2words import num2words

from models.model_class import Facture, Client
from services.article_service import get_article_by_id
from services.client_service import get_client_by_id
from services.facture_service import session
from views.states.facture_dialog_ui import Ui_Dialog

import os


class FactureDialog(QDialog):
    def __init__(self, facture: Facture=None, can_change_state=False):
        super(FactureDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.facture = facture

        self.total_a_payer = 0

        self.statut_payement = True

        self.default_printer = None

        self.ui.tableWidget.setColumnWidth(0, 300)
        self.ui.tableWidget.setColumnWidth(1, 120)
        self.ui.tableWidget.setColumnWidth(2, 120)
        self.ui.tableWidget.setColumnWidth(3, 140)

        if can_change_state :
            self.ui.change_state_btn.setHidden(False)
            self.ui.change_state_btn.clicked.connect(self.change_facture_state)
        else:
            self.ui.change_state_btn.setHidden(True)

        client = get_client_by_id(facture.numeroClient)

        self.display_header_information(facture, client)
        self.display_facture_detail(facture)
        self.ui.print_btn.clicked.connect(self.print_or_save_invoice_with_double_copy)
        self.ui.pushButton.clicked.connect(self.export_to_pdf)

    def display_header_information(self, facture: Facture, client: Client):
        self.ui.numero_facture.setText(facture.numeroFacture)
        self.ui.date_facture.setText(f"{facture.dateEnregistrement}")

        statut = "Tout payer" if facture.statutPayement else "Non payer"
        self.statut_payement = facture.statutPayement
        self.ui.statut_facture.setText(statut)


        self.ui.nom_client.setText(client.nom)
        self.ui.numero_client.setText(str(client.telephone))
        self.ui.adresse_client.setText(client.adresse)



    def display_facture_detail(self, facture: Facture):
        self.ui.tableWidget.setRowCount(0)
        self.total_a_payer = 0

        liste_article = facture.listeArticle
        for i, row in enumerate(liste_article):
            self.ui.tableWidget.insertRow(i)
            row_data = row.split(':')
            self.total_a_payer += int(row_data[2])
            article = get_article_by_id(row_data[0])

            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(f"{row_data[1]}, {article.description}"))
            self.ui.tableWidget.setItem(i, 1,  QTableWidgetItem(row_data[4]))
            self.ui.tableWidget.setItem(i, 2,  QTableWidgetItem(row_data[3]))
            self.ui.tableWidget.setItem(i, 3,  QTableWidgetItem(row_data[2]))

        reste_payer = "0 Ar" if facture.statutPayement else f"{self.total_a_payer - facture.avancement} Ar"
        self.ui.reste_payer.setText(reste_payer)
        self.ui.avance.setText(f"{facture.avancement} Ar")
        self.ui.total.setText(f"{self.total_a_payer} Ar")
        total_lettre = num2words(self.total_a_payer, lang='fr')
        self.ui.total_lettre.setText(total_lettre)

    def change_facture_state(self):
        if self.statut_payement:
            self.facture.statutPayement = False
            self.statut_payement = False
            self.ui.statut_facture.setText("Non payer")
        else:
            self.facture.statutPayement = True
            self.statut_payement = True
            self.ui.statut_facture.setText("Tout payer")
        session.commit()
        self.display_facture_detail(self.facture)
        return

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
                with open(f"{save_path}/facture_{str(self.facture.numeroFacture)}.pdf", 'w') as f:
                    print(f.name)
                    pass
            except Exception as e:
                print(f"exsception: {e}")
            facture_path = os.path.join(save_path, f"facture_{str(self.facture.numeroFacture)}.pdf").replace("\\", '/')
            print(facture_path)
            pdf_writer = QPdfWriter(facture_path)
            pdf_writer.setPageSize(QPageSize(QPageSize.A4))
            pdf_writer.setResolution(300)  # Résolution de haute qualité
            pdf_writer.setPageOrientation(QPageLayout.Landscape)

            painter = QPainter(pdf_writer)
            print(painter.isActive())
            self.draw_invoice_for_pdf(painter)
            painter.end()
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





