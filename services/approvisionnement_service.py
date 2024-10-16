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
    appros = get_all_approvisionnement()
    for appro in appros:
        if verify_if_approvisionnement_low(appro):
            articles.append(appro.numeroArticle)

    return articles

def get_appro_by_article_id(article_id):
    return session.query(Approvisionnement).filter_by(numeroArticle=article_id).first()

def update_appro(appro_id, new_appro: Approvisionnement):
    appro = session.query(Approvisionnement).filter_by(numeroApprovisionnement=appro_id).first()
    if appro:
        appro.quantiteLimite = new_appro.quantiteLimite
        appro.typeQuantite = new_appro.typeQuantite
    session.commit()
