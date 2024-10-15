from sqlalchemy.orm import sessionmaker

from models.model_class import Approvisionnement
from services.article_service import get_article_by_id
from utils.database import engine

Session = sessionmaker(bind=engine)
session = Session()

def insert_new_approvisionnement(appro: Approvisionnement):
    session.add(appro)
    session.commit()

def get_all_approvisionnement():
    return session.query(Approvisionnement).all()

def verify_if_approvisionnement_low(appro: Approvisionnement):
    article = get_article_by_id(appro.numeroArticle)
    if appro.typeQuantite == "Paquet":
        return appro.quantiteLimite >= article.packetEnStock
    elif appro.typeQuantite == "Boite":
        return appro.quantiteLimite >= article.boiteEnStock
    else:
        return appro.quantiteLimite >= article.pieceEnStock

def get_article_in_limite() -> list[str]:
    articles = []
    for appro in get_all_approvisionnement():
        if verify_if_approvisionnement_low(appro):
            articles.append(appro.numeroArticle)

    return articles
