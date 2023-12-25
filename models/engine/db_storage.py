#!/usr/bin/python3
"""DBStorage"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv

var_env = getenv('HBNB_ENV')
user = getenv('HBNB_MYSQL_USER')
psw = getenv('HBNB_MYSQL_PWD')
sqlhost = getenv('HBNB_MYSQL_HOST')
dbname = getenv('HBNB_MYSQL_DB')

class DBStorage:
    """class for mysqldb"""
    __engine = None
    __session = None

    def __init__(self):
        """The consructor: create the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user,
            psw, sqlhost, dbname), pool_pre_ping=True)
        if var_env == 'test':
            Base.metadata.drop_all(bind=self.__engine)
        else:
            Base.metadata.create_all(bind=self.__engine)

    def all(self, cls=None):
        """uery on the current database session depending of the class name"""
        classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        all_objts = {}
        if cls:
            return {str(cls) + '.' + str(_id):  obj for _id, obj in self.__session.\
                    query(cls.id, cls).all()}
        else:
            for cls_ in classes:
                all_objts.update(
                        {cls_ + '.' + str(_id):  obj for _id, obj in self.__session.\
                            query(eval(cls_).id, eval(cls_)).all()})

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
            self.save()

    def reload(self):
        """Create all tables"""
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=engine, expire_on_commit = False)
        Session = scoped_session(session_factory)
        self.__session = Session()
