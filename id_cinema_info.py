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


id_of_cinema = session.query(Movies).all()
a = id_of_cinema.cinema_id

for i in a:
    movies_id_info = requests.get(f'https://kudago.com/public-api/v1.4/movies/{i}/?fields=&expand=')
    movies_info_request = movies_id_info.json()
    raw_id_cinema_info = movies_info_request['body_text'].replace('<p>', '' ) 

    id_cinema_description = raw_id_cinema_info.replace('</p>', '' )
    trailer = movies_info_request['trailer']

    instance = Movies(description = id_cinema_description , trailer_url = trailer)
    session.add(instance)
    session.commit()


#import pprint
#print(id_cinema_description)
#print(trailer)
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(movies_of_info_request)