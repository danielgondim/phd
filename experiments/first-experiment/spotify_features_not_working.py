#chamada python testingAcousticBrainz.py 5eb8bc10d65cbdda3cd096f50081ae3c 2017-01-02 2017-01-31
# -*- coding: utf-8 -*-
import requests, sys, acoustic_brainz, music_brainz, time, datetime, calendar
from unidecode import unidecode
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import string
import re

API_KEY = sys.argv[1]
LASTFM_USERS_DETAILS = {"ourixilva":[21,50400,36000], "dcmaia":[21,50400,36000], "amaurymedeiros":[10,4,10800,20], "felipevf":[12,6,10800,18]} 
LIMIT_OF_MUSICS = "10"
TIMESTAMP_DIFFERENCE = 14400 #4 horas
INITIAL_TIME = str(int(time.time()) - 3600)
FINAL_TIME = str(int(time.time()))
#API_REST_LASTFM = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + \
#	LASTFM_USERNAME + "&api_key=" + API_KEY + "&format=json&limit=" + LIMIT_OF_MUSICS
#API_REST_LASTFM_TIME = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + \
#	LASTFM_USERNAME + "&api_key=" + API_KEY + "&format=json&from=" + INITIAL_TIME + "&to=" + FINAL_TIME
CLIENT_ID = '1a6f2ba5f65645729c3f1f035d745c77'
CLIENT_SECRET = '75d10aafa6d142a9a888085f1a29ab32'

def is_weekend(date):
	return date.weekday() >= 5 

def convert_to_datetime(date):
	return datetime.datetime.strptime(date + " 00:00:00", "%Y-%m-%d %H:%M:%S")

def api_rest_with_timestamp(date_time, lastfm_user, timestamp):
	current_time = calendar.timegm(date_time.utctimetuple())
	return "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + \
	lastfm_user + "&api_key=" + API_KEY + "&format=json&from=" + str(current_time) + "&to=" + \
	str(current_time + timestamp)

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID,CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

json_file_data = {}

musics_with_spotifyid = 0
musics_without_spotifyid = 0
number_musics = 0
music_with_spotify_analysis = 0
music_without_spotify_analysis = 0

for current_user in LASTFM_USERS_DETAILS:
	current_date = convert_to_datetime(sys.argv[2])
	current_date += datetime.timedelta(hours=LASTFM_USERS_DETAILS[current_user][0])
	final_date = convert_to_datetime(sys.argv[3])
	final_date += datetime.timedelta(hours=LASTFM_USERS_DETAILS[current_user][0])
	#print "NOVO USUARIO: " + current_user
	features = {'energy':{},'instrumentalness':{},'valence':{},'tempo':{}}
	print "Retrieving features of the musics from the user " + current_user
	print "..."
	while (current_date <= final_date):
		if (current_date.weekday() < 5):
			#pegar musicas pela manha
			#print "Musicas da manha do dia: " + str(current_date)
			response = requests.get(api_rest_with_timestamp(current_date, current_user, LASTFM_USERS_DETAILS[current_user][1]))
			data = response.json()
			for track in data['recenttracks']['track']:
				music_found = False
				track_id = ""
				number_musics += 1
				#print "Musica: " + track['name']
				#print "Artista: " + track['artist']['#text']
				string_search = track['name']
				string_search = re.sub('/', ' ', string_search)
				string_search = " ".join(string_search.split())
				#print string_search

				try:
					results = sp.search(q=string_search, limit=50, type='track')
					if len(results["tracks"]["items"]) > 0:
						for item in results["tracks"]["items"]:
							if music_found:
								break
							if item["name"] == string_search:
								for artist in item["artists"]:
									if artist["name"].lower() == track["artist"]["#text"].lower():
										track_id = item["id"]
										#print "Spotify ID: " + track_id
										musics_with_spotifyid += 1
										music_found = True
										music_features = sp.audio_features([track_id])
										#music_analysis = sp.audio_analysis(track_id)
										if music_features != {}:
											music_with_spotify_analysis += 1
											for feature in features:
												features[feature][track_id] = music_features[0][feature]
										else:
											music_without_spotify_analysis += 1
										break
					if track_id == "":
						#print "Spotify ID:"
						musics_without_spotifyid += 1
				except:
					#print "Deu erro mas continuei. Sem Spotify ID!"
					musics_without_spotifyid += 1
					#print
					continue
				#print
			#print "################################"

			#passando para o inicio do expediente do outro dia
			current_date += datetime.timedelta(hours=LASTFM_USERS_DETAILS[current_user][2])
		else:
			response = requests.get(api_rest_with_timestamp(current_date, current_user, LASTFM_USERS_DETAILS[current_user][1]))
			data = response.json()
			#se for fds passa o dia
			#print "Hoje eh fim de semana, nao teve trabalho!!!!"
			#print "################################"
			current_date += datetime.timedelta(days=1)
	json_file_data[current_user] = features
	print "Features of the musics from the user " + current_user + " retrieved\n"
print "Features from all the users retrieved"
print
print "Total de musicas com analise acustica do Spotify: " + str(music_with_spotify_analysis)
print "Total de musicas sem analise acustica do Spotify: " + str(music_without_spotify_analysis)
print "Total de musicas com ID do Spotify: " + str(musics_with_spotifyid)
print "Total de musicas sem ID do Spotify: " + str(musics_without_spotifyid)
print "Total de musicas: " + str(number_musics)

with open('spotify_features_data_not_working.json', 'w') as outfile:
    json.dump(json_file_data, outfile)

file = open("finished.txt","w") 
file.write("Job done!") 
file.close() 