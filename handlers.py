from utils import get_keyboard


def greet_user(bot, update, user_data):
    text = 'Привет, {}!'.format(update.message.chat.first_name)
    
    update.message.reply_text(text, reply_markup=get_keyboard())
    
    
def cinema_list(bot, update, user_data):
    pass


def cinema_location(bot, update, user_data):
    pass


def chosen_cinema(bot, update, user_data):
    pass

