import datetime
import json
import pprint

import requests

TODAY = datetime.datetime.today()


movies = requests.get(f'https://kudago.com/public-api/v1.4/movies/?fields=id,title&page_size=20&actual_since={TODAY}&location=kzn')

movies_request = movies.json()

#for names in movies_request['results']:
#    with open ('List_of_cinema.txt', 'a', encoding='utf-8') as new_file:
#       new_file.write("{}, id = /{} \n".format(names['title'], str(names['id'])))


pp = pprint.PrettyPrinter(indent=4)

for movie in movies_request['results']:
        movie_id = movie['id']
        movies_id_info = requests.get(f'https://kudago.com/public-api/v1.4/movies/{movie_id}/?fields=&expand=')
        movie_id_request = movies_id_info.json()
        movie_description_raw = movie_id_request['body_text'].replace('<p>', '')
        movie_description = movie_description_raw.replace('</p>', '')
        movie_trailer = movie_id_request['trailer']
        #pp.pprint(movie_description)
        #pp.pprint(movie_trailer)
