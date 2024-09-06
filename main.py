from models.model_class import Article, Client, Base, engine, Commande
from services.client_service import insert_new_client, get_all_client, get_client_by_id, update_client, \
    get_client_by_name, delete_client_by_id


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
    # delete_client_by_id(1)
    # clients = get_all_client()
    # for client in clients:
    #     print_article(client)
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
