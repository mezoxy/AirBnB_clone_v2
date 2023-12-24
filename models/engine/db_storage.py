#!/usr/bin/python3
"""DBStorage"""


from sqlachemy import create_engine
from sqlachemy.orm import sessionmaker, scoped_session
from models.BaseModel import Base
import os

var_env = os.environ.get('HBNB_ENV')
user = os.environ.get('HBNB_MYSQL_USER')
psw = os.environ.get('HBNB_MYSQL_PWD')
sqlhost = os.environ.get('HBNB_MYSQL_HOST')
dbname = os.environ.get('HBNB_MYSQL_DB')

class DBStorage:
    """class for mysqldb"""
    __engine = None
    __session = None

    def __init__(self):
        """The consructor: create the engine"""
        self.__engine = create_engine('mysql+mysqlb://{}:{}@{}/{}'.format(user,
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
            return {str(cls) + '.' + str(_id):  obj for _id, obj self.__session.\
                    query(cls.id, cls).all()}
        else:
            for cls_ in classes:
                all_objts.update(
                        {cls_ + '.' + str(_id):  obj for _id, obj self.__session.\
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
        self.__session = scoped_session(session_factory)
