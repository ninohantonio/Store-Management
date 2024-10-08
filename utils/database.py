import os

from sqlalchemy import create_engine, String, SmallInteger, BigInteger
from sqlalchemy.orm import declarative_base, mapped_column
from typing_extensions import Annotated
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv('DATABASE_URL')


engine = create_engine(db_url)

Base = declarative_base()

Base.metadata.create_all(engine)

# Type of data
str_50 = Annotated[str, mapped_column(String(50))]
str_10 = Annotated[str, mapped_column(String(10))]
str_30 = Annotated[str, mapped_column(String(30))]
str_20 = Annotated[str, mapped_column(String(20))]
str_13 = Annotated[str, mapped_column(String(13))]
str_30_optional = Annotated[Optional[str], mapped_column(String(30))]
str_date_time = Annotated[str, mapped_column(String(19))]
str_date = Annotated[str, mapped_column(String(10))]
int_small = Annotated[SmallInteger, mapped_column(SmallInteger)]
int_big = Annotated[BigInteger, mapped_column(BigInteger)]