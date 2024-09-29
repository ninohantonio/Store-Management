from PySide6.QtWidgets import QTableWidgetItem

from models.model_class import Article


def refresh_stock_table_data(table_widget, data: list[Article]):
    table_widget.setRowCount(0)

    # Remplir le QTableWidget avec les données
    for i, row in enumerate(data):
        table_widget.insertRow(i)
        table_widget.setItem(i, 0, QTableWidgetItem(str(row.libelle)))
        table_widget.setItem(i, 1, QTableWidgetItem(str(row.prixUnitaire)))
        table_widget.setItem(i, 2, QTableWidgetItem(str(row.description)))
        table_widget.setItem(i, 3, QTableWidgetItem(str(row.pieceEnStock)))
        table_widget.setItem(i, 4, QTableWidgetItem(str(row.pieceParPaquet)))
        table_widget.setItem(i, 5, QTableWidgetItem(str(row.pieceParBoite)))
        table_widget.setItem(i, 6, QTableWidgetItem(str(row.packetEnStock)))
        table_widget.setItem(i, 7, QTableWidgetItem(str(row.boiteEnStock)))
        table_widget.setItem(i, 8, QTableWidgetItem(str(row.dateEntrer)))


def refresh_search_view_value(table_widtget, data: list[Article]):
    table_widtget.setRowCount(0)

    for i, row in enumerate(data):
        table_widtget.insertRow(i)
        table_widtget.setItem(i, 0, QTableWidgetItem(str(row.libelle)))