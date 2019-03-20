import logging
from handlers import *

from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler,  Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename = 'bot.log'
                    )

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Бот запускается')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Сейчас в кино)$', cinema_list, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Кинотеатры)$', cinema_location, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Избранное)$', chosen_cinema, pass_user_data=True))
    


    mybot.start_polling()
    mybot.idle()
    
if __name__=="__main__":
    main()