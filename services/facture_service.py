from sqlalchemy.orm import sessionmaker

from models.model_class import Facture, Client
from utils.database import engine

Session = sessionmaker(bind=engine)
session = Session()

def get_all_facture():
    return session.query(Facture).all()

def get_facture_for_client(client_id: int):
    return session.query(Facture).where(Facture.numeroClient == client_id).all()

def get_facture_by_id(facture_id: int):
    return session.query(Facture).filter(Facture.numeroFacture == facture_id).first()

def get_facture_by_date_enregistrement(date: str):
    return session.query(Facture).filter(Facture.dateEnregistrement == date).all()

def get_facture_by_state(statut: bool):
    return session.query(Facture).filter(Facture.statutPayement == statut).all()

def get_client_by_facture(facture_id: int):
    return session.query(Client).join(Facture, Facture.numeroFacture == facture_id, full=True).first()

def insert_new_facture(facture: Facture):
    session.add(facture)
    session.commit()

def update_facture_by_id(facture_id: int, new_facture: Facture):
    facture = get_facture_by_id(facture_id)
    facture.statutPayement = new_facture.statutPayement
    facture.listeArticle = new_facture.listeArticle
    session.commit()

def delete_facture_by_id(facture_id: int):
    session.delete(get_facture_by_id(facture_id))
    session.commit()