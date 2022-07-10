import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'Usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    name = Column(String(250))
    LastName = Column(String(250))
    email =Column(String)
    password =Column(String)
    address=Column(String)

class Person(Base):
    __tablename__ = 'Person'
    ID = Column(Integer, primary_key=True)
    Name=Column(String(250))
class Planet(Base):
    __tablename__ = 'Planet'
    ID = Column(Integer, primary_key=True)
    Name=Column(String(250))
class FavPerson(Base):
    __tablename__ = 'FavPerson'
    ID = Column(Integer, primary_key=True)
    Usuarios_ID = Column(Integer,ForeignKey('Usuarios.ID'))
    Person_ID = Column(Integer,ForeignKey('Person.ID'))
class FavPlanet(Base):
    __tablename__ = 'FavPlanet'
    ID = Column(Integer, primary_key=True)
    Usuarios_ID = Column(Integer,ForeignKey('Usuarios.ID'))
    Planet_ID = Column(Integer,ForeignKey('Planet.ID'))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')