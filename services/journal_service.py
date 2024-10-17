from datetime import datetime, timedelta

from sqlalchemy.orm import sessionmaker

from models.model_class import Journal
from utils.database import engine

Session = sessionmaker(bind=engine)
session = Session()

def get_journal_by_type_action(action: str):
    return session.query(Journal).filter(Journal.typeAction.contains(action)).all()

def insert_new_journal(journal: Journal):
    session.add(journal)
    session.commit()

def get_all_journal():
    return session.query(Journal).all()

def search_journals_by_date(search_date: datetime):
    # Obtenir la date de début et de fin de la journée
    start_of_day = datetime(search_date.year, search_date.month, search_date.day)
    end_of_day = start_of_day + timedelta(days=1)

    # Filtrer les factures enregistrées ce jour-là
    result = session.query(Journal).filter(
        Journal.dateEnregistrement >= start_of_day,
        Journal.dateEnregistrement < end_of_day
    ).all()

    return result