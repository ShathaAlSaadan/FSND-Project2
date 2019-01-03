import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(200), nullable=False)
    picture = Column(String(250))

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    User_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'id': self.id,
        }

class Item(Base):
    __tablename__ = 'item'

    title = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    User_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    Category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        return{
        'title' : self.title,
        'id' : self.id
        }

engine = create_engine('sqlite:///categoryitmes.db')
Base.metadata.create_all(engine)
