from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.model_class import Article

engine = create_engine("sqlite:///database.db")

Session = sessionmaker(bind=engine)
session = Session()

def get_all_article():
    articles = session.query(Article).order_by(Article.quantiteStock.asc()).all()
    return articles

def get_article_by_id(article_id):
    article = session.query(Article).where(Article.numeroArticle == article_id).one_or_none()
    return article

def insert_new_article(article: Article):
    session.add(article)
    session.commit()

def update_article(article_id: int, new_article: Article):
    article = get_article_by_id(article_id)
    article.description = new_article.description
    article.libelle = new_article.libelle
    article.dateEntrer = new_article.dateEntrer
    article.prixUnitaire = new_article.prixUnitaire
    article.quantiteStock = new_article.quantiteStock
    session.commit()

def delete_article(article_id) -> bool:
    article = session.query(Article).filter_by(Article.numeroArticle==article_id).one_or_none()
    if article:
        session.delete(article)
        session.commit()
        return True
    else:
        return False

def delete_article_by_id(article_id) -> bool:
    session.query(Article).filter_by(numeroArticle=article_id).delete()
    session.commit()
    return True

def get_article_by_name(article_name):
    articles = session.query(Article).filter(Article.libelle.contains(article_name)).all()
    return articles


