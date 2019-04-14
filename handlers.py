from telegram import ReplyKeyboardRemove, ParseMode


from query_example import movie_list

from sqlalchemy_declarative import Movies, Base
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///movies.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def cinema_list(bot, update, user_data):
    update.message.reply_text(f"{movie_list[0:9]}")
    return "id" 

def cinema_get_id(bot, update, user_data):
    cinema_id = int(update.message.text.split('id'))
    row = session.query(Movies).filter(Movies.id == cinema_id).first()
    text = f"""
<b>Название</b>: {row.title}
<b>Описание</b>:
{row.description}
    <b>Трейлер</b>:{row.trailer_url}
    """
    update.message.reply_text(text, parse_mode = ParseMode.HTML)







def cinema_location(bot, update, user_data):
    pass


def chosen_cinema(bot, update, user_data):
    pass
