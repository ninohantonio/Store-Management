from PySide6.QtWidgets import QDialog, QTableWidgetItem

from models.model_class import Facture, Client
from services.client_service import get_client_by_id
from services.facture_service import session
from views.states.facture_dialog_ui import Ui_Dialog


class FactureDialog(QDialog):
    def __init__(self, facture: Facture=None, can_change_state=False):
        super(FactureDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.facture = facture

        self.total_a_payer = 0

        self.statut_payement = True

        if can_change_state :
            self.ui.change_state_btn.setHidden(False)
        else:
            self.ui.change_state_btn.setHidden(True)

        client = get_client_by_id(facture.numeroClient)

        self.display_header_information(facture, client)
        self.display_facture_detail(facture)


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

        liste_article = facture.listeArticle
        for i, row in enumerate(liste_article):
            self.ui.tableWidget.insertRow(i)
            row_data = row.split(':')
            self.total_a_payer += int(row_data[2])

            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(row_data[1]))
            self.ui.tableWidget.setItem(i, 1,  QTableWidgetItem(row_data[4]))
            self.ui.tableWidget.setItem(i, 2,  QTableWidgetItem(row_data[3]))
            self.ui.tableWidget.setItem(i, 3,  QTableWidgetItem(row_data[2]))

        reste_payer = "0 Ar" if facture.statutPayement else f"{self.total_a_payer - facture.avancement} Ar"
        self.ui.reste_payer.setText(reste_payer)
        self.ui.avance.setText(f"{facture.avancement} Ar")
        self.ui.total.setText(f"{self.total_a_payer} Ar")

    def change_facture_state(self):
        if self.statut_payement:
            self.facture.statutPayement = False
            self.ui.statut_facture.setText("Non payer")
        else:
            self.facture.statutPayement = True
            self.ui.statut_facture.setText("Tout payer")
        session.commit()
        session.close()
        self.display_facture_detail(self.facture)
        return





