# -*- coding: utf-8 -*-
#from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import string
import re


try:
	x = 12/0
except:
	y = 10
	pass
print y


CLIENT_ID = '1a6f2ba5f65645729c3f1f035d745c77'
CLIENT_SECRET = '75d10aafa6d142a9a888085f1a29ab32'

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID,CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

string_search = '1979'
string_search = re.sub('/', ' ', string_search)
print string_search
string_search = " ".join(string_search.split())
print

try:
	results = sp.search(q=string_search, type='track')
except:
	pass

print

track_id = results["tracks"]["items"][0]["id"]

print sp.audio_features([track_id])