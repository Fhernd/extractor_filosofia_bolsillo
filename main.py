import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Configurar credenciales
client_id = '1a3a71a5b9ad46a08c9ec452c037a747'
client_secret = 'abc'

# Autenticación
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Haz una solicitud a la API, por ejemplo, buscar un álbum
results = sp.search(q='album:Abbey Road artist:The Beatles', type='album')
albums = results['albums']['items']

for album in albums:
    print(album['name'], album['release_date'])
