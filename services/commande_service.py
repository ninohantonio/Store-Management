from sqlalchemy.orm import sessionmaker

from models.model_class import Commande
from utils.database import engine

Session = sessionmaker(bind=engine)
session = Session()

def get_all_commande():
    commandes = session.query(Commande).all()
    return commandes

def get_all_commande_for_client(client_id: int):
    commandes = session.query(Commande).where(Commande.numeroClient == client_id).all()
    return commandes

def get_commande_by_article(article_id: int):
    commades = session.query(Commande).where(Commande.numeroArticle == article_id).all()
    return commades

def get_client_by_commande(article_id: int):
    pass