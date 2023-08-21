import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class Character(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth_year = Column(Date, nullable=False)
    eye_color = Column(String(10))
    homeworld = Column(String(50), ForeignKey('planets.id'))
    created = Column(String(50))
    edited = Column(String(50))
    gender = Column(String(20))
    hair_color = Column(String(20))
    height = Column(Integer)
    mass = Column(Integer)
    skin_color = Column(String(20))
    url = Column(String(100))

    def to_dict(self):
        return {}



class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50))
    created = Column(String(50))
    edited = Column(String(50))
    diameter = Column(Integer)
    gravity = Column(String(50))
    orbital_period = Column(Integer)
    population = Column(Integer)
    residents = Column(String) 
    rotation_period = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String(50))
    url = Column(String(100))

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phoneNumber = Column(String, unique=True, nullable=False)

    def to_dict(self):
        return {}

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(50))
    
    
    def to_dict(self):
        return {}
        
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
