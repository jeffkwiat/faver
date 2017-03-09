import datetime

from app import db, app
from models import Favorite

db.app = app
db.init_app(app)

favorite1 = Favorite(user_id=1,
                    title='Favorite 1',
                    link='http://localhost.com',
                    date_taken=datetime.datetime.now(),
                    published=datetime.datetime.now(),
                    author='Jeff Kwiat',
                    author_id='123012399291',
                    tags='bob dylan neil young etc')

favorite2 = Favorite(user_id=2,
                    title='Favorite 2',
                    link='http://localhost.com:5000',
                    date_taken=datetime.datetime.now(),
                    published=datetime.datetime.now(),
                    author='Jeff Kwiat',
                    author_id='12301239asdffasdfa9291',
                    tags='june july august november')

db.session.add(favorite1)
db.session.add(favorite2)
db.session.commit()
