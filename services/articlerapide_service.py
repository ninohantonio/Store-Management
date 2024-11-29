from sqlalchemy.orm import sessionmaker

from models.model_class import Articlerapide, Article
from utils.database import engine

Session = sessionmaker(bind=engine)
session = Session()

def get_all_articlerapide():
    return session.query(Articlerapide).join(Article, Article.numeroArticle == Articlerapide.numeroArticle).order_by(Article.libelle.asc()).all()


def insert_new_article_rapide(article_rpd: Articlerapide):
    session.add(article_rpd)
    session.commit()

