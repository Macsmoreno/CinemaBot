from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import About_cinema, Base

from cinema_list_request import result_of_request


engine = create_engine('sqlite:///cinema_information.db')


Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)


session = DBSession()


for j in result_of_request['results']:   
    instance = About_cinema(title = j['title'], cinema_id = j['id'])
    session.add(instance)
    session.commit()