import logging
from handlers import cinema_list, cinema_location, chosen_cinema, cinema_get_id
from utils import greet_user


from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler, ConversationHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[logging.FileHandler('bot.log', 'a', 'utf-8')]
                    )

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Бот запускается')
    
    cinema_now = ConversationHandler(
        entry_points = [RegexHandler('^(Сейчас в кино)$', cinema_list, pass_user_data=True)],
        states = {
            "id":[CommandHandler("id", cinema_get_id, pass_user_data=True)],
        },
        fallbacks = []
    )

    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(cinema_now)
    dp.add_handler(RegexHandler('^(Кинотеатры)$', cinema_location, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Избранное)$', chosen_cinema, pass_user_data=True))
    
    
    

    mybot.start_polling()
    mybot.idle()
    
if __name__=="__main__":
    main()