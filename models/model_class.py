from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Date
from sqlalchemy.orm import Mapped, relationship, mapped_column

from utils.database import Base, engine, str_50, str_10, str_date, str_date_time, int_small, str_20, str_30_optional


class Client(Base):
    __tablename__: str = "client"

    numeroClient = Column(Integer, primary_key=True, autoincrement=True)
    nom : Mapped[str_50]
    adresse : Mapped[str_50]
    telephone : Mapped[str_10]
    commandes: Mapped[list["Commande"]] = relationship()
    factures: Mapped[list["Facture"]] = relationship()

class Article(Base):
    __tablename__: str = "article"

    numeroArticle = Column(String(13), primary_key=True)
    libelle: Mapped[str_20]
    pieceParPaquet: Mapped[int_small]
    quantiteStock: Mapped[int_small]
    margeApprovisionnement: Mapped[int_small]
    prixUnitaire: Mapped[int_small]
    dateEntrer = Column(Date)
    description: Mapped[str_30_optional]
    commandes: Mapped[list["Commande"]] = relationship()

class Commande(Base):
    __tablename__: str = "commande"

    numeroCommande = Column(Integer, primary_key=True, autoincrement=True)
    dateCommande = Column(DateTime)
    dateLivraison = Column(Date)
    quantiteCommande: Mapped[int_small]
    numeroClient: Mapped[int] = mapped_column(ForeignKey("client.numeroClient"))
    numeroArticle: Mapped[int] = mapped_column(ForeignKey("article.numeroArticle"))

class Facture(Base):
    __tablename__ = "facture"

    numeroFacture = Column(String(10), primary_key=True, unique=True)
    dateEnregistrement = Column(DateTime)
    listeArticle = Column(String(255))
    statutPayement: Mapped[bool] = mapped_column()
    numeroClient = Column(ForeignKey("client.numeroClient"))

class Journal(Base):
    __tablename__ = "journal"

    numeroJournal = Column(Integer, primary_key=True, autoincrement=True)
    dateEnregistrement = Column(DateTime)
    listeArticle = Column(String(255))
    typeAction = Column(String(50))


Base.metadata.create_all(engine)