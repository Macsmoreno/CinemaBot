import requests
import json
import datetime
import pprint



raw_id_info = requests.get(f'https://kudago.com/public-api/v1.4/movies/1323/?fields=&expand=')

result_of_info_request = raw_id_info.json()

pp = pprint.PrettyPrinter(indent=4)

#pp.pprint(result_of_info_request)

raw_id_cinema_info = result_of_info_request['body_text'].replace('<p>', '' ) 
id_cinema_info = raw_id_cinema_info.replace('</p>', '' )

trailer = result_of_info_request['trailer']

print(id_cinema_info)
print(trailer)