from PySide6.QtWidgets import QTableWidgetItem

from models.model_class import Article, Facture, Journal, Reliure, Client
from services.client_service import get_client_by_id
from services.reliure_service import get_type_livre_by_id, get_total_for_reliure


def refresh_stock_table_data(table_widget, data: list[Article]):
    table_widget.setRowCount(0)

    # Remplir le QTableWidget avec les données
    for i, row in enumerate(data):
        table_widget.insertRow(i)
        table_widget.setItem(i, 0, QTableWidgetItem(str(row.libelle)))
        table_widget.setItem(i, 1, QTableWidgetItem(str(row.prixUnitaire)))
        table_widget.setItem(i, 2, QTableWidgetItem(str(row.pieceEnStock)))
        table_widget.setItem(i, 3, QTableWidgetItem(str(row.description)))
        table_widget.setItem(i, 4, QTableWidgetItem(str(row.pieceParPaquet)))
        table_widget.setItem(i, 5, QTableWidgetItem(str(row.pieceParBoite)))
        table_widget.setItem(i, 6, QTableWidgetItem(str(row.packetEnStock)))
        table_widget.setItem(i, 7, QTableWidgetItem(str(row.boiteEnStock)))
        table_widget.setItem(i, 8, QTableWidgetItem(str(row.dateEntrer)))


def refresh_facture_table_data(table_widget, data: list[Facture]):
    table_widget.setRowCount(0)

    for i, row in enumerate(data):
        table_widget.insertRow(i)
        statut = "Tout payer" if row.statutPayement else "Non payer"
        table_widget.setItem(i, 0, QTableWidgetItem(str(row.numeroFacture)))
        table_widget.setItem(i, 1, QTableWidgetItem(str(row.dateEnregistrement)))
        table_widget.setItem(i, 2, QTableWidgetItem(statut))
        table_widget.setItem(i, 3, QTableWidgetItem(str(row.avancement)))
        table_widget.setItem(i, 4, QTableWidgetItem(str(row.numeroClient)))


def refresh_reliure_table_data(table_widget, data: list[Reliure]):
    table_widget.setRowCount(0)

    for i, row in enumerate(data):
        client = get_client_by_id(row.numeroClient)
        type = get_type_livre_by_id(row.numeroType)
        etat = "Oui" if row.statutLivrer else "Non"
        total_payer = get_total_for_reliure(row.numeroReliure)

        table_widget.insertRow(i)
        table_widget.setItem(i, 0, QTableWidgetItem(str(row.numeroReliure)))
        table_widget.setItem(i, 1, QTableWidgetItem(str(client.nom)))
        table_widget.setItem(i, 2, QTableWidgetItem(str(type.typeLivre)))
        table_widget.setItem(i, 3, QTableWidgetItem(str(row.nombrePageNoir)))
        table_widget.setItem(i, 4, QTableWidgetItem(str(row.nombrePageCouleur)))
        table_widget.setItem(i, 5, QTableWidgetItem(str(row.nombreExemplaire)))
        table_widget.setItem(i, 6, QTableWidgetItem(str(total_payer)))
        table_widget.setItem(i, 7, QTableWidgetItem(etat))




def refresh_journal_table_data(table_widget, data: list[Journal]):
    table_widget.setRowCount(0)

    for i, row in enumerate(data):
        table_widget.insertRow(i)
        table_widget.setItem(i, 0, QTableWidgetItem(str(row.typeAction)))
        table_widget.setItem(i, 1, QTableWidgetItem(str(row.description)))
        table_widget.setItem(i, 2, QTableWidgetItem(str(row.dateEnregistrement)))


def refresh_search_view_value(table_widtget, data: list[Article]):
    table_widtget.setRowCount(0)

    for i, row in enumerate(data):
        table_widtget.insertRow(i)
        table_widtget.setItem(i, 0, QTableWidgetItem(str(row.libelle)))
        table_widtget.setItem(i, 1, QTableWidgetItem(str(row.numeroArticle)))


def refresh_client_list(tableWidget, data: list[Client]):
    tableWidget.setRowCount(0)

    for i, row in enumerate(data):
        tableWidget.insertRow(i)
        tableWidget.setItem(i, 0, QTableWidgetItem(str(row.nom)))
        tableWidget.setItem(i, 1, QTableWidgetItem(str(row.telephone)))
        tableWidget.setItem(i, 2, QTableWidgetItem(str(row.numeroClient)))