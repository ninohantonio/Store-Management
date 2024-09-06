from sqlalchemy.orm import sessionmaker

from models.model_class import Client
from utils.database import engine

Session = sessionmaker(bind=engine)
session = Session()

def insert_new_client(client: Client):
    session.add(client)
    session.commit()

def get_all_client():
    clients = session.query(Client).all()
    return clients

def get_client_by_id(client_id: int):
    client = session.query(Client).where(Client.numeroClient == client_id).first()
    return client

def get_client_by_name(client_name: str):
    clients = session.query(Client).where(Client.nom.contains(client_name)).all()
    return clients

def update_client(client_id: int, new_client: Client):
    client = get_client_by_id(client_id)
    client.nom = new_client.nom
    client.adresse = new_client.adresse
    client.telephone = new_client.telephone
    session.commit()

def delete_client_by_id(client_id: int):
    client = get_client_by_id(client_id)
    session.delete(client)
    session.commit()
