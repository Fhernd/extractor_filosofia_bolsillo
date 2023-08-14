import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

# Autenticación
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Dame el listado de episodios del podcast con ID 768GVwxeh1o6kD5bD0qJeJ:
podcast_id = '768GVwxeh1o6kD5bD0qJeJ'

episodios = sp.show_episodes(podcast_id)

for episodio in episodios['items']:
    print(episodio['name'])


def get_podcast_episodes(podcast_id):
    episodes = []
    results = sp.show_episodes(podcast_id)
    episodes.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        episodes.extend(results['items'])
    return episodes
