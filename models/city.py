#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import string, Column, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    
    name = olumn(String(128), nullable=False)
    state_id = Column(String(60), nullable=False ,ForeignKey('states.id'))

    state = relationship('State', back_populates='cities')
