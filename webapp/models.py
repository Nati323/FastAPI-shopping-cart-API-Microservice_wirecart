import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    id            = Column(Integer, primary_key=True, auto_increment=True)
    user_id       = Column(Integer)
    username      = Column(String)

    product_id    = Column(Integer)
    product_title = Column(String)
    product_desc  = Column(String)
    product_price = Column(Integer)

    quantity      = Column(Integer)
    auto_date     = Column(DateTime, default=datetime.datetime.now)
