from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Movies, Base
from cinema_list_request import movies_request, movie_id_request, movie_trailer

engine = create_engine('sqlite:///movies.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

for j in movies_request['results']:   
    instance = Movies(title = j['title'], id = j['id'])
    session.add(instance)
    session.commit()

for i in movie_id_request:
    instance = Movies(description = i['body_text'] )
    session.add(instance)
    session.commit()

for x in movie_id_request:
    instance = Movies(trailer_url = x['trailer'])
    session.add(instance)
    session.commit()

