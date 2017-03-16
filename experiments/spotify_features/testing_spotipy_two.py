# -*- coding: utf-8 -*-
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy

print 'testetetetete'

CLIENT_ID = '1a6f2ba5f65645729c3f1f035d745c77'
CLIENT_SECRET = '75d10aafa6d142a9a888085f1a29ab32'

print 'opaaaaaaaaaa'

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID,CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q='não existe amor em sp', type='track')

track_id = results["tracks"]["items"][0]["id"]

print track_id

x = sp.audio_features([track_id])

print type(x[0]['tempo'])