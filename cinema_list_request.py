import requests
import json
import datetime


TODAY = datetime.datetime.today()


raw_data = requests.get(f'https://kudago.com/public-api/v1.4/movies/?fields=id,title&page_size=20&actual_since={TODAY}&location=kzn')


result_of_request = raw_data.json()


for names in result_of_request['results']:
    with open ('List_of_cinema.txt', 'a', encoding='utf-8') as new_file:
        new_file.write("{}, id = /{} \n".format(names['title'], str(names['id'])))

