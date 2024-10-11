from datetime import datetime, timedelta

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


def search_factures_by_date_range(session: Session, start_date: datetime, end_date: datetime):
    # Ajuster la date de fin pour inclure toute la journée
    end_date_adjusted = end_date + timedelta(days=1)

    # Filtrer les factures entre deux dates
    result = session.query(Facture).filter(
        Facture.dateEnregistrement >= start_date,
        Facture.dateEnregistrement < end_date_adjusted
    ).all()

    return result


def search_factures_by_date(session: Session, search_date: datetime):
    # Obtenir la date de début et de fin de la journée
    start_of_day = datetime(search_date.year, search_date.month, search_date.day)
    end_of_day = start_of_day + timedelta(days=1)

    # Filtrer les factures enregistrées ce jour-là
    result = session.query(Facture).filter(
        Facture.dateEnregistrement >= start_of_day,
        Facture.dateEnregistrement < end_of_day
    ).all()

    return result

