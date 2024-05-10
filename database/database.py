from sqlalchemy import create_engine, Column, Integer, String, Float, BigInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///uzumbaza.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, unique=True)
    full_name = Column(String)
    phone_number = Column(String, unique=True)
    latitude = Column(Float)
    longitude = Column(Float)
    lang = Column(String(2))

