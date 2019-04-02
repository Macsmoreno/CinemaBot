from telegram import ReplyKeyboardMarkup
import settings

def get_keyboard():
    my_keyboard = ReplyKeyboardMarkup([
                                       ['Сейчас в кино'],
                                       ['Кинотеатры', 'Избранное']
                                     ], resize_keyboard=True)
    return my_keyboard


def greet_user(bot, update, user_data):
    text = 'Привет, {}!'.format(update.message.chat.first_name)
    
    update.message.reply_text(text, reply_markup=get_keyboard())
    