from datetime import datetime

from models.model_class import Article


def insert_article_controller(article: Article) -> str:
    if article.prixUnitaire < 0 :
        return "prix"
    elif article.quantiteStock < 0:
        return "quantite"
    else:
        return ""

def get_date_to_string() -> str:
    date = datetime.now()
    date = str(date)
    date = date.split(' ')
    return date[0]

