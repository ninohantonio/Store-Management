from controllers.article_controller import get_date_to_string
from models.model_class import Article
from services.auth_service import create_user, verify_password

create_user("ninohantonio@gmail.com", "ninokely123")
# verify = verify_password("ninohantonio@gmail.com", "ninokely123")
# print(verify)
article = Article(
            libelle="cahier laureat",
            prixUnitaire= ,
            typeConteneur=,
            pieceParPaquet=,
            pieceParBoite=,
            pieceEnStock=,
            packetEnStock=,
            boiteEnStock=,
            description=,
            dateEntrer=get_date_to_string(),
            numeroArticle=
        )
#nettoyer la carte
#afficher la facture avec options pdf
#gerer le screen facture (affichage et recherche)
#gerer le screen journal (affichage et recherche)