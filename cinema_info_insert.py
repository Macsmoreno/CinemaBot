from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Movies, Places, Movies_schedule, Base
from cinema_list_request import movies_request, result, movies_places_id, places

engine = create_engine('sqlite:///movies.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

for movie in movies_request['results']: 
    movie_id = movie['id']
    movie_info = result(movie_id)
    instance_result = Movies(id = movie['id'], id_of_movie = movie_info[0], 
                    title = movie_info[1], description = movie_info[2], trailer_url = movie_info[3],
                    publication = movie_info[4] )
    session.add(instance_result)
    session.commit()

for movie in movies_request['results']: 
    movie_id = movie['id']
    movie_places_info = movies_places_id(movie_id)
    instance_places_id = Movies_schedule(id_movie_in_schedule = movie_places_info['movie']['id'] , 
                                            datetime_of_movie = movie_places_info['datetime'],
                                            place_id_in_schedule = movie_places_info['place']['id'], 
                                            price = movie_places_info['price'] )
    session.add(instance_places_id)
    session.commit()

for new_place in places['results']:
    instance_places = Places(cinema_title = new_place['title'],
                            address = new_place['address'],
                            url = new_place['foreign_url'],
                            place_id = new_place['id'])
    session.add(instance_places)
    session.commit()
