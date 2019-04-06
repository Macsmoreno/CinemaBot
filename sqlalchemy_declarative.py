import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Movies(Base):
    __tablename__ = 'Movies'
    title = Column(Text, nullable = False)
    id = Column(Integer, primary_key = True)
    id_of_movie = Column(Integer, primary_key = True)
    description = Column(String, nullable = False)
    trailer_url = Column(String, nullable = False)


engine = create_engine('sqlite:///movies.db')


Base.metadata.create_all(engine)
