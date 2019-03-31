import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class About_cinema(Base):
    __tablename__ = 'Information'
    title = Column(Text, nullable = False)
    cinema_id = Column(Integer, primary_key = True)


class Id_info(Base):
    __tablename__ = 'Id_info'
    description = Column(Text, nullable = False)
    trailer_url = Column(String, nullable = False)
    cinema = relationship(About_cinema)


engine = create_engine('sqlite:///cinema_information.db')


Base.metadata.create_all(engine)
