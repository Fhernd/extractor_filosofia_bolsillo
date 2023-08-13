import os

import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

# Autenticación
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

token_info = client_credentials_manager.get_access_token(as_dict=False)

TOKEN = token_info + 'aaaa'
SHOW_ID = '6xpiit8aJmwDHk1rKdxmri'

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(f"https://api.spotify.com/v1/shows/6xpiit8aJmwDHk1rKdxmri/episodes", headers=headers)

print(response.status_code)

if response.status_code == 200:
    episodes = response.json().get('items', [])
    for episode in episodes:
        print(episode['name'])
