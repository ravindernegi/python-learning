from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, Float

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"
    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String)
    price = Column(String)
    quantity = Column(INTEGER)
