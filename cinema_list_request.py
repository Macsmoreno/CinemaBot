import datetime
import json
import requests

TODAY = datetime.datetime.today()


movies = requests.get(f'https://kudago.com/public-api/v1.4/movies/?fields=id&page_size=100&actual_since={TODAY}&location=kzn')

movies_request = movies.json()


def result(movie_id):
        movies_id_info = requests.get(f'https://kudago.com/public-api/v1.4/movies/{movie_id}/?fields=id,title,body_text,running_time,trailer&text_format=text')
        movie_id_request = movies_id_info.json()
        movie_list = [movie_id_request['id'], movie_id_request['title'], movie_id_request['body_text'], movie_id_request['trailer']]
        return movie_list

for movie in movies_request['results']:
        movie_id = movie['id']
        movie_info = result(movie_id)