from models.model_class import Article

from services.article_service import insert_new_article, get_all_article, update_article, get_article_by_id


def print_article(articles):
    # for article in articles:
    print(f"""
                   numero article = {article.numeroArticle}
                   libelle = {article.libelle}
                   prix Unitaire = {article.prixUnitaire}
                   quantite en Stock = {article.quantiteStock}
                   date d'Entrer en stock = {article.dateEntrer}
                   article description = {article.description}
           """)

new_article = Article(libelle = "Stylo schneider", quantiteStock = 100, prixUnitaire=800, dateEntrer="2024-09-06", description="miampy description")
old_article = Article(libelle = "Stylo schneider", quantiteStock = 100, prixUnitaire=800, dateEntrer="2024-09-06", description="")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    article = get_article_by_id(1)
    print_article(article)
    update_article(1, new_article)
    print("separation")
    article = get_article_by_id(1)
    print_article(article)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
