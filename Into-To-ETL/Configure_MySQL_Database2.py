# [ETL-Project:2] Configure MySQL Database
from sqlalchemy import create_engine, Float, Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class = mlb_players(Base):
    __tablename = 'mlb_players_2019'
    pid = Column(Integer, primary_key=True)
    fname = Column(String, nullable=False)
    lname = Column(String, nullable=False)
    age = Column(Integer)
    height = Column(String)
    weight = Column(String)
    birthday = Column(DateTime)
    city = Column(String)
    number = Column(String)
    position = Column(String)
    exp = Column(String)
    team = Column(String)
    throw = Column(String)
    bat = Column(String)
    college = Column(String)


Base.metadata.tables

MySQL_DB_Connection = f'{user}:{password}@localhost/moneyball_db'

try:
    engine = create_engine(f'mysql://{MySQL_DB_Connection}', echo=False)
    connection = engine.connect()
    print(f'\n<Connected> MySQL Datbase: moneyball_db')

except exc.OperationalError:
    MySQL_Base_Connection = f'{user}:{password}@localhost'
    engine = create_engine(f'mysql://{MySQL_Base_Connection}', echo=False)
    connection = engine.connect()
    engine.execute('CREATE DATABASE IF NOT EXISTS moneyball_db;')
    print(f'\n<Created> MySQL Database: moneyball_db [Connection:Successful]')
