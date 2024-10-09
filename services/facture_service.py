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
    facture.numeroFacture = get_next_facture_number()
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


def get_next_facture_number():
    # Récupérer la dernière facture enregistrée
    last_facture = session.query(Facture).order_by(Facture.numeroFacture.desc()).first()

    if last_facture:
        # Incrémenter le numéro de facture
        next_number = str(int(last_facture.numeroFacture) + 1).zfill(10)
    else:
        # Si aucune facture n'existe encore, commencer à 00000001
        next_number = '0000000001'

    return next_number