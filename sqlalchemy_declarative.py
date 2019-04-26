import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Movies(Base):
    '''таблица с данными о фильмах'''
    __tablename__ = 'Movies'
    title = Column(Text, nullable = False)
    id = Column(Integer, primary_key = True)
    id_of_movie = Column(Integer, primary_key = True)
    description = Column(String, nullable = False)
    trailer_url = Column(String, nullable = False)
    publication = Column(Integer, primary_key = True)

class Places(Base):
    '''таблица с данными о кинотеатрах'''
    __tablename__ = 'Places'
    cinema_title = Column(Text, nullable = False)
    address = Column(Text, nullable = False)
    url = Column(Text, nullable = False)
    place_id = Column(Integer, primary_key = True)

class Movies_schedule(Base):
    '''таблица с данными о расписании'''
    __tablename__ = 'Movies_schedule'
    id_movie_in_schedule = Column(Integer, ForeignKey('Movies.id_of_movie'))
    id_movie = relationship(Movies)
    datetime_of_movie = Column(Integer, primary_key = True)
    place_id_in_schedule = Column(Integer, ForeignKey('Places.place_id'))
    place = relationship(Places)
    price = Column(String, nullable = False)


engine = create_engine('sqlite:///movies.db')

Base.metadata.create_all(engine)
