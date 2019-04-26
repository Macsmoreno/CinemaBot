from telegram import MessageEntity, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, error
from utils import get_keyboard, list_keyboard

from cinema_list_request import movies_places_id

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

def inline_button_info(bot, update):
    query = update.callback_query
    cinema_id = int(query.data)
    row = session.query(Movies).filter(Movies.id == cinema_id).first()
    logging.info(cinema_id)
    text = f"""
        ***Название***: {row.title}
        ***Описание***:
        {row.description}
            [Трейлер]:({row.trailer_url})
            """
    inline_list_kbd = [[InlineKeyboardButton("Посмотерть сеансы", callback_data = cinema_id)]]
    logging.info(cinema_id)
    kbd_list_markup = InlineKeyboardMarkup(inline_list_kbd)
    query.edit_message_text(text, reply_markup = kbd_list_markup)

def need_more_movies():
    pass

def back_to_movies():
    pass

def inline_button_list(bot, update):
    query = update.callback_query
    print(query)
    callback_id = int(query.data)
    cinema_list =f'''
    {movies_places_id(callback_id)}'''
    query.edit_message_text(cinema_list)
    

def cinema_location(bot, update, user_data):
    pass


