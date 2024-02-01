#!/usr/bin/python3
"""DBStorage"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv


class DBStorage:
    """class for mysqldb"""
    __engine = None
    __session = None

    def __init__(self):
        """The consructor: create the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """uery on the current database session depending of the class name"""
        classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        all_objts = {}
        if cls:
            return {
                    cls.__name__ + '.' + str(
                        obj.id): obj for obj in self.__session.query(
                            cls).all()}
        else:
            for cls_ in classes:
                all_objts.update(
                        {cls_ + '.' + str(
                            _id): obj for _id, obj in self.__session.query(
                                eval(cls_).id, eval(cls_)).all()})

            return all_objts

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """save all the changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """To delete an obj"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables"""
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
            Close: Close the local session
        """
        self.__session.close()
