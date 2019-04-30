import requests
from decouple import config

if config('MAIN', cast=bool):
    BASE_URL = config('SLAVE_URL')
else:
    BASE_URL = config('MAIN_URL')


def search(word):
    url = BASE_URL + '/rdf'
    json = {'word': word}
    r = requests.post(url, json=json)
    if r.status_code == 200:
        response = r.json()
        return response
