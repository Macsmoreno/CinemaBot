from telegram import ReplyKeyboardMarkup
import settings

def get_keyboard():
    my_keyboard = ReplyKeyboardMarkup([
                                       ['Сейчас в кино'],
                                       ['Кинотеатры', 'Избранное']
                                     ], resize_keyboard=True)
    return my_keyboard