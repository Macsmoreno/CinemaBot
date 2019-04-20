from telegram import MessageEntity, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, error
from utils import get_keyboard

import logging


from sqlalchemy_declarative import Movies, Base
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///movies.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def greet_user(bot, update, user_data):
    text = 'Привет, {}!'.format(update.message.chat.first_name)
    logging.info(text)
    update.message.reply_text(text, reply_markup = get_keyboard())


def cinema_list(bot, update, user_data):
    for instance in session.query(Movies).order_by(Movies.publication).limit(10):
        title = instance.title
        inlinekbd = [[InlineKeyboardButton("Подробнее", callback_data=f'{instance.id}')]]
        kbd_markup = InlineKeyboardMarkup(inlinekbd)
        update.message.reply_text(title, reply_markup = kbd_markup)

def inline_button_pressed(bot, update):
    print(update.callback_query)
    query = update.callback_query
    print(query)
    cinema_id = int(query.data)
    print(cinema_id)
    row = session.query(Movies).filter(Movies.id == cinema_id).first()
    logging.info("cinema_id")
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
