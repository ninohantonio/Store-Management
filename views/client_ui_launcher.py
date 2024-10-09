from PySide6.QtWidgets import QDialog, QTableWidgetItem

from models.model_class import Client
from services.client_service import get_all_client, get_client_by_id
from views.client_list_dialog import Ui_liste_client


class ClientList(QDialog):
    def __init__(self):
        super(ClientList, self).__init__()
        self.ui = Ui_liste_client()
        self.ui.setupUi(self)

        self.temporary_client_selected = False

        self.selected_client = Client()

        clients = get_all_client()
        self.load_table_data(clients)

        self.ui.pushButton_2.clicked.connect(self.handle_temporary_client)
        self.ui.tableWidget.setColumnHidden(2, True)


    def load_table_data(self, data: list[Client]):
        self.ui.tableWidget.setRowCount(0)

        for i, row in enumerate(data):
            self.ui.tableWidget.insertRow(i)
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(row.nom)))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(row.telephone)))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(row.numeroClient)))


    def handle_temporary_client(self):
        self.temporary_client_selected = True
        self.accept()

    def get_selected_client(self):
        selected_row = self.ui.tableWidget.currentRow()
        print(f"selected row = {selected_row}")
        if selected_row != -1:
            # Récupérer les informations du client sélectionné
            numero = self.ui.tableWidget.item(selected_row, 2).text()
            return get_client_by_id(numero)

        return None
