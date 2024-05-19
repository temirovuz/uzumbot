from sqlalchemy import create_engine, Column, Integer, String, Float, BigInteger, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
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


class Shops(Base):  # dokonlar
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class FoodsCategory(Base):
    __tablename__ = 'foods_category'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Foods(Base):  # Ovqatlar
    __tablename__ = 'foods'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    image = Column(String)
    category_id = Column(Integer, ForeignKey('foods_category.id'))
    shops_id = Column(Integer, ForeignKey('shops.id'))


class Drinks(Base):  # ichimliklar
    __tablename__ = 'drinks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    shops_id = Column(Integer, ForeignKey('shops.id'))
    shops = relationship("Shops", back_populates="drinks")


class Images(Base):  # Images
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    shops_id = Column(Integer, ForeignKey('shops.id'))
    category_id = Column(Integer, ForeignKey('foods_category.id'))
    image = Column(String)


class Basket(Base):
    __tablename__ = 'basket'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    foods_id = Column(Integer, ForeignKey('foods.id'))
