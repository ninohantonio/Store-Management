from sqlalchemy.orm import sessionmaker

from models.model_class import Commande, Client, Article
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
    clients = (session.query(Client)
               .where(Client.numeroClient == Commande.numeroClient and Article.numeroArticle == Commande.numeroArticle and Article.numeroArticle == article_id).all())
    return clients

def get_article_by_commande(client_id: int):
    articles = session.query(Article).where(Article.numeroArticle == Commande.numeroArticle and Client.numeroClient == Commande.numeroClient and Client.numeroClient == client_id).all()
    return articles

def insert_new_commande(commande: Commande):
    session.add(commande)
    session.commit()

def delete_commande_by_id(commande_id: int):
    commande = session.query(Commande).where(Commande.numeroCommande == commande_id).first()
    session.delete(commande)
    session.commit()
