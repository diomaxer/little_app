from sqlalchemy.orm import relationship

from database.alchemy_db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Store(Base):
    __tablename__ = "store"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    location = Column(String)

    product = relationship("Product", back_populates="owner")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    store_id = Column(Integer, ForeignKey('store.id'))
    name = Column(String)
    price = Column(Integer)

    owner = relationship("Store", back_populates="product")
