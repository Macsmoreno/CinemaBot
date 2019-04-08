from sqlalchemy_declarative import Movies, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///movies.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def cinema_list(bot, update, user_data):
        for instance in session.query(Movies).order_by(Movies.id):
                list_of_movies = []
                title = instance.title
                id_of_movies = instance.id_of_movie
                list_of_movies.extend(f"{title}, /id = {id_of_movies}")
        update.message.reply_text(list_of_movies)        

def cinema_location(bot, update, user_data):
    pass


def chosen_cinema(bot, update, user_data):
    pass
