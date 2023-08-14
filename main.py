import os

import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


def obtener_claves_secretas():
    """
    Obtiene las claves secretas de Spotify desde un archivo .env.

    Returns:
        client_id (str): ID de la aplicación de Spotify.
        client_secret (str): Clave secreta de la aplicación de Spotify.
    """
    load_dotenv()

    client_id = os.environ.get('SPOTIFY_CLIENT_ID')
    client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

    return client_id, client_secret


def iniciar_sesion_spotif(client_id, client_secret):
    """
    Inicia sesión en Spotify.

    Args:
        client_id (str): ID de la aplicación de Spotify.
        client_secret (str): Clave secreta de la aplicación de Spotify.
    
    Returns:
        sp (spotipy.client.Spotify): Objeto de sesión de Spotify.
    """
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return sp


# Dame el listado de episodios del podcast con ID 768GVwxeh1o6kD5bD0qJeJ:
podcast_id = '768GVwxeh1o6kD5bD0qJeJ'

token_info = client_credentials_manager.get_access_token(as_dict=False)
access_token = token_info

id = '768GVwxeh1o6kD5bD0qJeJ'       #<------------------------------------ INSERT SHOW ID MANUALLY
type = 'episodes'
market  = 'US'
limit = 50
offset = 0

id_list = []
dur_list = []
date_list = []
name_list = []
desc_list = []

counter = 0
more_runs = 1

search = 'Filosofía de bolsillo'

while(counter <= more_runs):


    endpoint_url = f"https://api.spotify.com/v1/shows/{id}/episodes?"


    query = f'{endpoint_url}'
    query += f'&q={search}'
    query += f'&type={type}'
    query += f'&offset={offset}'
    query += f'&market={market}'
    query += f'&limit={limit}'


    response = requests.get(query, 
                   headers={"Content-Type":"application/json", 
                            "Authorization":f"Bearer {access_token}"})
    json_response = response.json()



    for i in range(len(json_response['items'])):

        id_list.append(json_response['items'][i]['id'])
        dur_list.append(json_response['items'][i]['duration_ms'])
        date_list.append(json_response['items'][i]['release_date'])    
        name_list.append(json_response['items'][i]['name'])
        desc_list.append(json_response['items'][i]['description'])
        
        
    more_runs = (json_response['total'] // 50 )         
        
    counter += 1
    
    offset = offset + 50 

for n in name_list:
    print(n)
    print()
