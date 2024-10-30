from datetime import datetime, timedelta, date

from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from models.model_class import Reliure, Typelivre, Client
from utils.database import engine

Session = sessionmaker(bind=engine)
session = Session()


def get_all_reliure_commande():
    return session.query(Reliure).order_by(Reliure.dateCommande.desc()).all()

def get_all_type_livre():
    return session.query(Typelivre).all()

def get_type_livre_by_id(livre_id: int):
    return session.query(Typelivre).filter_by(numeroType=livre_id).first()

def get_reliure_by_date(search_date: date):
    # Obtenir la date de début et de fin de la journée
    start_of_day = search_date
    end_of_day = start_of_day + timedelta(days=1)

    # Filtrer les factures enregistrées ce jour-là
    result = session.query(Reliure).order_by(Reliure.dateCommande.desc()).filter(
        Reliure.dateCommande >= start_of_day,
        Reliure.dateCommande < end_of_day
    ).all()

    return result

def get_reliure_by_id(reliure_id: int):
    return session.query(Reliure).filter_by(numeroReliure=reliure_id).first()

def insert_new_type_livre(typelivre: Typelivre):
    session.add(typelivre)
    session.commit()
    return

def get_reliure_by_state(state: bool):
    return session.query(Reliure).filter(Reliure.statutLivrer == state).all()

def insert_new_reliure_commande(reliure: Reliure):
    session.add(reliure)
    session.commit()
    return

def get_total_for_reliure(reliure_id: int):
    reliure = get_reliure_by_id(reliure_id)
    type = get_type_livre_by_id(reliure.numeroType)
    return (reliure.nombrePageNoir * type.prixPageNoir + reliure.nombrePageCouleur * type.prixPageCouleur + type.prixReliure) * reliure.nombreExemplaire

def get_reliure_by_date_and_state(date: date, state: bool):
    return session.query(Reliure).order_by(Reliure.dateCommande.desc()).filter(
        Reliure.dateCommande == date, Reliure.statutLivrer == state
    ).all()

def get_reliure_by_client_name(clientname: str):
    return session.query(Reliure).join(Client).filter(Client.nom.contains(clientname)).all()


def get_total_reliure_group_by_date():
    # Calcul du premier jour du mois actuel
    debut_mois = date(datetime.today().year, datetime.today().month, 1)

    # Récupérer les factures depuis la base
    reliures = session.query(
        Reliure.dateCommande,
        Reliure.numeroReliure
    ).filter(
        Reliure.dateCommande >= debut_mois, Reliure.statutLivrer == True
    ).all()

    # Grouper par jour et calculer les totaux
    ventes_par_jour = {}
    for jour, numero in reliures:
        total = get_total_for_reliure(numero)
        if jour in ventes_par_jour:
            ventes_par_jour[jour] += total
        else:
            ventes_par_jour[jour] = total

    return ventes_par_jour

