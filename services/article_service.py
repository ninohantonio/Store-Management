from datetime import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.model_class import Article
from utils.database import engine

Session = sessionmaker(bind=engine)
session = Session()

def get_all_article():
    articles = session.query(Article).order_by(Article.pieceEnStock.asc()).all()
    return articles

def get_article_by_id(article_id):
    article = session.query(Article).where(Article.numeroArticle == article_id).one_or_none()
    return article

def filter_article_by_date(date: datetime.date):
    articles = session.query(Article).where(dateEntrer = date).all()
    return articles

def insert_new_article(article: Article):
    session.add(article)
    session.commit()

def update_article(article_id: str, new_article: Article):
    article = get_article_by_id(article_id)
    article.description = new_article.description
    article.libelle = new_article.libelle
    article.dateEntrer = new_article.dateEntrer
    article.prixUnitaire = new_article.prixUnitaire
    article.pieceEnStock = new_article.pieceEnStock
    article.pieceParPaquet = new_article.pieceParPaquet
    article.pieceParBoite = new_article.pieceParBoite

    session.commit()

def delete_article_by_id(article_id: str) -> bool:
    article = session.query(Article).filter_by(Article.numeroArticle==article_id).one_or_none()
    if article:
        session.delete(article)
        session.commit()
        return True
    else:
        return False

# def delete_article_by_id(article_id) -> bool:
#     article = session.query(Article).where(Article.numeroArticle == article_id).delete()
#     session.commit()
#     return True

def get_article_by_name(article_name):
    articles = session.query(Article).filter(Article.libelle.contains(article_name)).all()
    return articles

def get_article_by_price(article_price):
    articles = session.query(Article).where(Article.prixUnitaire == article_price).order_by(Article.pieceEnStock.asc()).all()
    return articles

def verify_article_by_id(article_id):
    return session.query(Article).filter_by(numeroArticle=article_id).first() is not None


