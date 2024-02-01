#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', backref='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        """
        Getter attribute cities that returns
                the list of City instances
                with state_id equals to the current State.id
        """
        from models import storage
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            return [obj for obj in storage.all(
                City).values() if self.id == obj.state_id]
