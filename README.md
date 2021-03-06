# Кино без забот

Бот предназначен для поиска сеансов кино и выбора кинотеатра.
Написан на языке Python с использованием библиотеки [Python telegram bot](https://github.com/python-telegram-bot).
Для корректно функционирования бота необходимо установить Python 3.6.8 и все необходимые основные компоненты.

Основные функции бота:
1. Функция **Сейчас в кино** показывает актуальный список сеансов.
2. Функция **Кинотеатры** показывает кинотеатры города.

## Установка и запуск бота.

Для установки и запуска бота не обходимо:
1. [Клонировать репозиторий](https://github.com/Macsmoreno/CinemaBot.git);
2. Запустить комнадную строку и перейти в каталог с репозиторием;
3. Запустить интерпретатор в командной строке: 'python';
4. Выполнить в интерепретаторе: 'pip install -r requirements.txt' для установки необходимых зависимостей;
5. В файл *settings.py* добавить свой токен в соответствующие поле. При отсутствии токена запросить его у [BotFather](@BotFather);
6. Выйти из интерпретатора командой: 'exit()';
7. Выполнить в командной строке: 'python bot.py' для запуска бота;
8. Активировать бота командой **/start**. 
