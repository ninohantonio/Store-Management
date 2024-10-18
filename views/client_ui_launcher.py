from PySide6.QtWidgets import QDialog, QTableWidgetItem

from models.model_class import Client
from services.client_service import get_all_client, get_client_by_id, get_client_by_name
from views.client_list_dialog import Ui_liste_client
from views.states.client_form_launcher import ClientFormDialog


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

        self.ui.search_client.textChanged.connect(self.get_client_by_search)
        self.ui.search_client.returnPressed.connect(self.get_client_by_search)

        self.ui.pushButton.clicked.connect(self.show_add_new_client_form)


    def load_table_data(self, data: list[Client]):
        self.ui.tableWidget.setRowCount(0)

        for i, row in enumerate(data):
            self.ui.tableWidget.insertRow(i)
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(row.nom)))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(row.telephone)))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(row.numeroClient)))

    def refresh_table_client(self):
        clients = get_all_client()
        self.load_table_data(clients)
        return


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

    def show_add_new_client_form(self):
        self.client_form = ClientFormDialog()

        self.client_form.finished.connect(self.refresh_table_client)

        self.client_form.exec()

    def get_client_by_search(self):
        search = self.ui.search_client.text()
        if search.strip() == "":
            self.refresh_table_client()
            return
        else:
            clients = get_client_by_name(search)
            self.load_table_data(clients)
            return


