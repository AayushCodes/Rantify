import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
cid = 'f1b3bf6e85204114b5f0e4aaffc4ae2a'
secret = '69c292ce3c774ca6abd3932c3483bc5d'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
artist_name = []
track_name = []
popularity = []
track_id = []
for i in range(0,10000,50):
    track_results = sp.search(q='thank u,next', type='track')
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

print(artist_name,track_name,popularity,track_id)