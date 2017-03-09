import requests
import uuid

from models import Favorite, User
from flask import Blueprint, request, session, jsonify

api = Blueprint('api', 'api', url_prefix='/api/v1.0')


@api.route('/favorites', methods=['GET', 'POST'])
def favorites():
    '''
    GET:  Returns the users favorites
    POST: Allows a user to favorite a photo
    :return:
    '''
    if request.method == 'GET':
        return jsonify([favorite.to_json() for favorite in Favorite.query.all()])
    else:
        favorite = Favorite(user_id=request.form['user_id'],
                            title=request.form['title'],
                            date_taken=request.form['date_taken'],
                            link=request.form['link'],
                            published=request.form['published'],
                            author=request.form['author'],
                            author_id=request.form['author_id'],
                            tags=request.form['tags'])

        return jsonify({"message": "POST not implemented"})

def _get_tags(photo):
    return ', '.join(photo['tags'].split(' '))

@api.route('/latest', methods=['GET'])
def latest():
    '''
    GET: returns the latest photos from Flickr
    :return:
    '''
    # The end point was not valid JSON.  There docs
    # recommend adding the nojsoncallback=1 parameter.
    url = ''.join(["https://api.flickr.com/services/feeds/photos_public.gne?format=json",
                          "&nojsoncallback=1"])
    r = requests.get(url=url)
    photos = r.json()
    latest = []
    flickr_url = 'https://www.flickr.com/photos/'

    for photo in photos['items']:
        latest.append({
            'id': uuid.uuid4(),
            'title': photo['title'],
            'link': photo['link'],
            'tags': _get_tags(photo),
            'media': photo['media']['m'],
            'date_taken': photo['date_taken'].split('T')[0],
            'author': photo['author'].split(' ')[1].replace('"', '').replace('(', '').replace(')', ''),
            'author_id': ''.join([flickr_url, photo['author_id']])
        })
    return jsonify(latest)