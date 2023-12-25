#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        """Getter attribute cities that returns the list of City instances 
            with state_id equals to the current State.id
        """
        from models import storage
        return [obj for obj in storage.all(City) if self.id == obj.state_id]
