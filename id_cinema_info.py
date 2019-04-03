import requests
import json
from sqlalchemy_declarative import Movies, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///movies.db')
Base.metadata.bind = engine
DBsession = sessionmaker()
DBsession.bind = engine
session = DBsession()


id_of_cinema = Movies.query().filter(Movies.id == id)


for i in range(id_of_cinema):
    def movies_details(i):
        movies_id_info = requests.get(f'https://kudago.com/public-api/v1.4/movies/{i}/?fields=&expand=')
        movies_info_request = movies_id_info.json()
        raw_id_cinema_info = movies_info_request['body_text'].replace('<p>', '' ) 
        id_cinema_description = raw_id_cinema_info.replace('</p>', '' )
        trailer = movies_info_request['trailer']
        return movies_details

print(movies_details(3833))