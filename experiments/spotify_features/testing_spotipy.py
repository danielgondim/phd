# -*- coding: utf-8 -*-
#from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import string
import re

CLIENT_ID = '1a6f2ba5f65645729c3f1f035d745c77'
CLIENT_SECRET = '75d10aafa6d142a9a888085f1a29ab32'

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID,CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

string_search = 'Mascarada'
string_search = re.sub('/', ' ', string_search)
string_search = " ".join(string_search.split())

print string_search

artista = 'Joyce'

try:
	results = sp.search(q=string_search, limit=50, type='track')
	#print results
	music_count = 0
	if len(results["tracks"]["items"]) > 0:
		for item in results["tracks"]["items"]:
			music_count += 1
			if item["name"] == string_search:
				for artist in item["artists"]:
					#print artist["name"]
					if artist["name"] == artista:
						print 'Musica numero: ' + str(music_count)
	print str(music_count)
except:
	print "deu merda"
	pass
					