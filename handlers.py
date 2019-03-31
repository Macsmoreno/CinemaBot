def cinema_list(bot, update, user_data):
    with open ('List_of_cinema.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        update.message.reply_text(content)



def cinema_location(bot, update, user_data):
    pass


def chosen_cinema(bot, update, user_data):
    pass
