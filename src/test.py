import os

import sqlalchemy as sa
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

metadata = sa.MetaData()
Base = declarative_base(metadata=metadata)

local_env = "../.env"
load_dotenv(local_env)


def get_sql_alchemy_url():
    server = os.environ["SERVER"]
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    database = os.environ["POSTGRES_DB"]
    port = os.environ["PORT"]
    url = f"postgresql://{user}:{password}@{server}:{port}/{database}"
    # print(f'sqlalchemy url: {url}')
    return url


db_url = get_sql_alchemy_url()
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()


class Test(Base):
    __tablename__ = "test"
    __table_args__ = {"schema": "dbo"}

    col1 = sa.Column(sa.String, primary_key=True)
    col2 = sa.Column(sa.Integer)


query = session.query(Test.col1)
query.all()
