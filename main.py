import sys

from PySide6.QtWidgets import QApplication

from models.model_class import Client
from views.main_ui_launcher import MainWindow


def print_article(client):
    # for article in articles:
    print(f"""
                id = {client.numeroClient}
                nom = {client.nom}
                adresse = {client.adresse}
                telephone = {client.telephone}
           """)

client1 = Client(nom = "RAKOTO be", adresse = "lot 1234 uidfadsidaf tanambao", telephone="0341234567")
client2 = Client(nom = "RANDRIA kely", adresse = "lot 1234 uidfadsidaf tanambao", telephone="0343214561")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
