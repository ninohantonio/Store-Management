from sqlalchemy.orm import sessionmaker

from models.model_class import Articlerapide
from utils.database import engine

Session = sessionmaker(bind=engine)
session = Session()

def get_all_articlerapide():
    return session.query(Articlerapide).all()


def insert_new_article_rapide(article_rpd: Articlerapide):
    session.add(Articlerapide)
    session.commit()

