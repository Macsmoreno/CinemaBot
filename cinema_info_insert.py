from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Movies, Base
from cinema_list_request import movies_request, result

engine = create_engine('sqlite:///movies.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

for movie in movies_request['results']: 
    movie_id = movie['id']
    movie_info = result(movie_id)
    instance = Movies(id = movie['id'], id_of_movie = movie_info[0], 
                    title = movie_info[1], description = movie_info[2], trailer_url = movie_info[3],
                    publication = movie_info[4] )
    session.add(instance)
    session.commit()

