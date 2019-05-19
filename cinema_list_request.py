import datetime
import json
import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

''' дата начала '''
start_date = datetime.datetime.today()


movies = requests.get(f'https://kudago.com/public-api/v1.4/movies/?fields=id&page_size=100&actual_since={start_date}&location=kzn&imdb_rating')

movies_request = movies.json()

def result(movie_id):
        ''' собирает инфу про кино по id'''
        movies_id_info = requests.get(f'https://kudago.com/public-api/v1.4/movies/{movie_id}/?fields=id,publication_date,title,body_text,running_time,trailer&text_format=text&imdb_rating')
        movie_id_request = movies_id_info.json()
        movie_list = [movie_id_request['id'], 
                movie_id_request['title'], 
                movie_id_request['body_text'], 
                movie_id_request['trailer'],
                movie_id_request['publication_date']]
        return movie_list

for movie in movies_request['results']:
        movie_id = movie['id']
        movie_info = result(movie_id)

def movies_places_id(movie_id):
        '''показывает где идет кино по id'''
        movies_places_request = requests.get(f'https://kudago.com/public-api/v1.4/movies/{movie_id}/showings/?fields=id,title,movie,place,datetime,price&location=kzn&actual_since={start_date}')
        movies_places = movies_places_request.json()
        info_list = []
        for info in movies_places['results']: 
               info_list.append([
                info['datetime'],
                info['movie']['id'],
                info['place']['id'],
                info['price']
                ])
        return info_list

''' список кинотеатров '''
places_request = requests.get("https://kudago.com/public-api/v1.4/places/?fields=id,title,address,foreign_url&order_by=address&text_format=text&location=kzn&categories=cinema")

places = places_request.json()


