from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Date, JSON
from sqlalchemy.orm import Mapped, relationship, mapped_column

from utils.database import Base, engine, str_50, str_10, str_date, str_date_time, int_small, str_20, str_30_optional, \
    str_13


class Client(Base):
    __tablename__: str = "client"

    numeroClient = Column(Integer, primary_key=True, autoincrement=True)
    nom : Mapped[str_50]
    adresse : Mapped[str_50]
    telephone : Mapped[str_10]
    commandes: Mapped[list["Commande"]] = relationship()
    factures: Mapped[list["Facture"]] = relationship()


class Approvisionnement(Base):
    __tablename__: str = "approvisionnement"

    numeroApprovisionnement = Column(Integer, primary_key=True, autoincrement=True)
    quantiteLimite: Mapped[int_small]
    typeQuantite: Mapped[str_10]
    numeroArticle: Mapped[str_13] = mapped_column(ForeignKey("article.numeroArticle"))


class Article(Base):
    __tablename__: str = "article"

    numeroArticle = Column(String(13), primary_key=True)
    libelle: Mapped[str_20]
    typeConteneur: Mapped[str_10]
    pieceParPaquet: Mapped[int_small]
    pieceParBoite: Mapped[int_small]
    pieceEnStock: Mapped[int_small]
    packetEnStock: Mapped[int_small]
    boiteEnStock: Mapped[int_small]
    prixUnitaire: Mapped[int_small]
    dateEntrer = Column(Date)
    description: Mapped[str_30_optional]
    commandes: Mapped[list["Commande"]] = relationship()
    approvisionnement: Mapped["Approvisionnement"] = relationship()


class Commande(Base):
    __tablename__: str = "commande"

    numeroCommande = Column(Integer, primary_key=True, autoincrement=True)
    dateCommande = Column(DateTime)
    dateLivraison = Column(Date)
    quantiteCommande: Mapped[int_small]
    type = Column(String(10))
    numeroClient: Mapped[int] = mapped_column(ForeignKey("client.numeroClient"))
    numeroArticle: Mapped[str_13] = mapped_column(ForeignKey("article.numeroArticle"))

class Facture(Base):
    __tablename__ = "facture"

    numeroFacture = Column(String(10), primary_key=True, unique=True)
    dateEnregistrement = Column(DateTime)
    listeArticle = Column(JSON)
    statutPayement: Mapped[bool] = mapped_column()
    avancement: Mapped[int_small] = mapped_column()
    numeroClient = Column(ForeignKey("client.numeroClient"))

class Journal(Base):
    __tablename__ = "journal"

    numeroJournal = Column(Integer, primary_key=True, autoincrement=True)
    dateEnregistrement = Column(DateTime)
    listeArticle = Column(JSON)
    description = Column(String(150))
    typeAction = Column(String(50))

class Notification(Base):
    __tablename__ = "notification"

    numeroNotification = Column(Integer, primary_key=True, autoincrement=True)
    titre: Mapped[str_50]
    dateEmmission = Column(DateTime)
    contenu = Column(String(100))
    numeroArticle: Mapped[str_13]

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(60), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

class Articlerapide(Base):
    __tablename__ = 'articlerapide'

    id = Column(Integer, primary_key=True, autoincrement=True)
    numeroArticle: Mapped[str_13] = mapped_column(ForeignKey("article.numeroArticle"))



Base.metadata.create_all(engine)