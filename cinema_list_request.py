import requests
import json
import datetime


TODAY = datetime.datetime.today()


raw_data = requests.get(f'https://kudago.com/public-api/v1.4/movies/?fields=id,title&page_size=20&actual_since={TODAY}&location=kzn')


result_of_request = raw_data.json()


for names in result_of_request['results']:
    with open ('List_of_cinema.txt', 'a', encoding='utf-8') as new_file:
        new_file.write("{}, id = /{} \n".format(names['title'], str(names['id'])))


def cinema_info(bot, update, user_data):
        cinema_id = update.message.text.split('/')
        if cinema_id in 'List_of_cinema.txt':
                try:
                        raw_id_info = requests.get(f'https://kudago.com/public-api/v1.4/movies/{cinema_id}/?fields=&expand=')
                        result_of_info_request = raw_id_info.json()
                        raw_id_cinema_info = result_of_info_request['body_text'].replace('<p>', '' ) 
                        id_cinema_info = raw_id_cinema_info.replace('</p>', '' )
                        trailer = result_of_info_request['trailer']
                        update.message.reply_text(id_cinema_info, trailer)
                except:
                        update.message.reply_text('Что-то не так!')