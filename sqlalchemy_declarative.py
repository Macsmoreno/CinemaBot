import os
import sys
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table, Text 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('movies_id', Integer, ForeignKey('Movies.id_of_movie')),
    Column('places_id', Integer, ForeignKey('Places.place_id')),
    Column('movies_schedule_id', Integer, ForeignKey('Movies_schedule.place_id_in_schedule'))    

)

class Movies(Base):
    '''таблица с данными о фильмах'''
    __tablename__ = 'Movies'
    title = Column(Text, nullable = False)
    id_of_movie = Column(Integer, primary_key = True)
    movies = relationship('Places', secondary = association_table, back_populates= "places")
    movies1 = relationship('Movies_schedule', secondary = association_table, back_populates= "id_in_schedule")
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
    places = relationship('Movies', secondary = association_table, back_populates = "movies")
    places1 = relationship("Movies_schedule", secondary = association_table, back_populates= "place_in_schedule")

class Movies_schedule(Base):
    '''таблица с данными о расписании'''
    __tablename__ = 'Movies_schedule'
    id_movie_in_schedule = Column(Integer, primary_key = True)
    id_in_schedule = relationship('Movies', secondary = association_table, back_populates = "movies1")
    datetime_of_movie = Column(Integer, primary_key = True)
    place_id_in_schedule = Column(Integer, primary_key = True)
    place_in_schedule = relationship('Places', secondary = association_table, back_populates = "places1") 
    price = Column(String, nullable = True,)


engine = create_engine('sqlite:///movies.db')

Base.metadata.create_all(engine)
