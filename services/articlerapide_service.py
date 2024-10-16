from sqlalchemy.orm import sessionmaker

from utils.database import engine

Session = sessionmaker(bind=engine)
session = Session()

