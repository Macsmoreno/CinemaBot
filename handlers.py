from telegram import MessageEntity, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, error
from utils import get_keyboard, list_keyboard

from cinema_list_request import movies_places_id

import datetime, logging


from sqlalchemy_declarative import Base, Movies, Movies_schedule, Places 
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///movies.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def greet_user(bot, update, user_data):
    text = """
    Здравствуйте! Говорит ***что*** смотреть и показывает ***где*** бот - *КиноБезЗаБот*.
Чтобы посмотреть список фильмов нажмите кнопку 
            ***Сейчас в кино***.
Чтобы посмтреть список кинотеатров нажмите кнопку 
            ***Кинотеатры***.
Приятного пользования ботом.)
    """
    logging.info(text)
    update.message.reply_text(text, reply_markup = get_keyboard(), parse_mode = ParseMode.MARKDOWN)


def cinema_list(bot, update, user_data):
    for instance in session.query(Movies).order_by(Movies.publication).limit(10):
        title = instance.title
        inlinekbd = [[InlineKeyboardButton("Подробнее", callback_data=f'{instance.id_of_movie}')]]
        kbd_markup = InlineKeyboardMarkup(inlinekbd)
        update.message.reply_text(title, reply_markup = kbd_markup)

def inline_button_info(bot, update):
    query = update.callback_query
    cinema_id = query.data
    cinema_id_int = int(query.data)
    row = session.query(Movies).filter(Movies.id_of_movie == cinema_id_int).first()
    logging.info(cinema_id)
    text = f"""
    Название: {row.title}

Описание: {row.description}

Трейлер: {row.trailer_url}
            """
    inline_list_kbd = [[InlineKeyboardButton("Посмотерть сеансы", callback_data = 'cinema_id')]]
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
    print(callback_id)
    for instance in session.query(Movies_schedule).filter(Movies_schedule.id_movie_in_schedule == callback_id).\
                                                    order_by(Movies_schedule.price).limit(10):
        cinema_list = f""" 
        Начало сеанса: {instance.datetime_of_movie}
        Стоимость билета: {instance.price}
        """
        update.message.text(cinema_list)
    

def cinema_location(bot, update, user_data):
    for instance in session.query(Places):
        text = f"""
        *Название*: {instance.cinema_title}
        *Адрес*: {instance.address}
        [Сайт]({instance.url})
        """
        inlinekbd = [[InlineKeyboardButton("Посмотереть сеансы", callback_data=f'{instance.place_id}')]]
        kbd_markup = InlineKeyboardMarkup(inlinekbd)
        update.message.reply_text(text, reply_markup = kbd_markup, parse_mode = ParseMode.MARKDOWN)

def inline_button_schedule(bot, update):
    query = update.callback_query
    place_id = int(query.data)
    row = session.query(Places).filter(Places.place_id == place_id).limit(10)
    logging.info(place_id)
    for instance in session.query(Movies).filter(Movies.id_of_movie == row.id_movie_in_schedule):
        try:
            text = f"""
                Название: {instance.title}
                Начало: {row.datetime_of_movie}
                Трейлер: {instance.trailer_url}
                    """
            query.edit_message_text(text)
        except:
            update.message.reply_text("Сеансов не найдено")


