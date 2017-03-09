import requests

class TestApi(object):
    '''
    Class to test our API

    '''

    def __init__(self):
        self.api = 'http://localhost:5000/v1/api'

    def test_favorites_get(self):
        result = requests.get(self.api_url + '/favorites').json()
        assert {'message': 'Poll was created succesfully'} == result