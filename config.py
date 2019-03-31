import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'bot.db')