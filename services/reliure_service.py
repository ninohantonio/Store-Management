from datetime import datetime, timedelta, date

from sqlalchemy.orm import sessionmaker

from models.model_class import Reliure, Typelivre
from utils.database import engine

Session = sessionmaker(bind=engine)
session = Session()


def get_all_reliure_commande():
    return session.query(Reliure).all()

def get_all_type_livre():
    return session.query(Typelivre).all()

def get_type_livre_by_id(livre_id: int):
    return session.query(Typelivre).filter_by(numeroType=livre_id).first()

def get_reliure_by_date(search_date: date):
    # Obtenir la date de début et de fin de la journée
    start_of_day = search_date
    end_of_day = start_of_day + timedelta(days=1)

    # Filtrer les factures enregistrées ce jour-là
    result = session.query(Reliure).filter(
        Reliure.dateCommande >= start_of_day,
        Reliure.dateEnregistrement < end_of_day
    ).all()

    return result

def get_reliure_by_id(reliure_id: int):
    return session.query(Reliure).filter_by(numeroReliure=reliure_id).first()

def insert_new_type_livre(typelivre: Typelivre):
    session.add(typelivre)
    session.commit()
    return
