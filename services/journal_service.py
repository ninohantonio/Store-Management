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